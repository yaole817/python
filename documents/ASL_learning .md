# ASL learning summary


1 ASL准则
=======

1.  变量命名不超过4个字符，且不能以数字开头；

2.  变量名和函数名不区分大小写；

3.  Scope和Device都会形成自己的作用域，类似于C++中的namespace和class；

4.  所有以”\_”开头的函数都是Reserved的，给系统使用，不能给自己的函数起这样的名字；

5.  ASL中的路径有相对路径和绝对路径之分。其结构有点像文件目录；

6.  对于函数，最多只能传递8个参数（Arg0\~Arg7），只能用这8个名字，不能自己起名字；

7.  对于局部变量，最多能使用8个变量（Local0\~Local7），和函数参数一样，不能自己起名字，而且在使用之前必须手动赋初值；

8.  声明变量时不需要显示声明其类型，这一点不同于C和C++

9.  根作用域下有\\\_GPE，\\\_PR，\\\_SB，\\\_SI，\\\_TZ五个作用域。

    ```asl
        \_GPE就是ACPI的事件处理；
    ```

    ```asl
        \_PR处理器；
    ```

    ```asl
        \_SB所有的设备和总线；
    ```

    ```asl
        \_SI系统指示灯；
    ```

    ```asl
        \_TZ温度，用于读取某些温度；
    ```

不同属性的东西放在对应的作用域下。

10. 符号“\\”引用根作用域，“\^”引用上级作用域
11. ASL中没有运算符，+-\*/=是不会出现了，但是有等价的函数。



2 赋值方法
========

ASL 的赋值方法有且仅有一个

```asl
Store（Source, Destination） // Destination = Source
```


3 变量定义
========

正如前面提到的，声明变量时不需要显式地声明其类型。

```asl
Name(MYIN,1)                //定义了一个整数
Name(MSTR, “Hello,world”)   //定义了一个字符串
```


4 ASL运算函数
===========
| 名字         | 描述    | 例子                                       |
| ---------- | ----- | ---------------------------------------- |
| Add        | 整数相加  | Add(1, 2, Local0) //Local0 = 1 + 2       |
| And        | 按位与   | And(0x11, 0x22, Local0) //Local0 = 0x11 & 0x22 |
| Decrement  | 整数自减1 | Decrement(Local0) // Local0--            |
| Divide     | 整数除法  | Divide(10, 9, Local1, Local0) //Local0 = 10 / 9, Local1 = 10 % 9 |
| Increment  | 整数自增1 | Increment(Local0) //Loacal0++            |
| Mod        | 整数求余  | Mod (10, 9, Local0) //Local0 = 10 % 9    |
| Multiply   | 整数相乘  | Multiply(1, 2, Local0) //Local0 = 1* 2   |
| ShiftLeft  | 左移    | ShiftLeft(1, 20, Local0) // Local0 = 1 << 20 |
| ShiftRight | 右移    | ShiftRight(0x10000, 4, Local0) // Local0 = 0x10000 >> 4 |
| Subtract   | 整数减法  | Subtract(2, 1, Local0) //Local0 = 2 - 1  |
| Or         | 或     | Or(0x01, 0x02, Local0) //Local0 = 0x01   |
| Not        | 取反    | Not(0x00,Local0) //Local0 = ~(0x00)      |
| Nor        | 异或    | Nor(0x11, 0x22, Local0) //Local0 = ~(0x11) & ~(0x22) |


5 ASL逻辑运算
===========
| 名字            | 描述     | 例子                               |
| ------------- | ------ | -------------------------------- |
| LAnd          | 逻辑与    | LAnd(1, 1) // (1 && 1)           |
| LEqual        | 逻辑相等   | LEqual(1, 1) // (1 == 1)         |
| LGreater      | 逻辑大于   | LGreater(1, 2) // (1 \> 2)       |
| LGreaterEqual | 逻辑大于等于 | LGreaterEqual(1, 2) // (1 \>= 2) |
| LLess         | 逻辑小于   | LLess(1, 2) //(1 \< 2)           |
| LLessEqual    | 逻辑小于等于 | LLessEqual(1, 2) // (1 \<= 2)    |
| LNot          | 逻辑反    | LNot(0) //( !0)                  |
| LNotEqual     | 逻辑不等于  | LNotEqual(0, 1) // (0 != 1)      |
| LOr           | 逻辑或    | LOR(0, 1) // (0 \|\| 1)          |




6 函数定义
========


6.1 一般函数定义
------------

```asl
Method(TEST){}
```

定义一个名为TEST的函数，没有形参


6.2 带有形参的函数定义
------------------

定义有两个输入参数的函数，以及使用局部变量Local0\~Local7

```asl
Method(MADD,2)
{
  Store(Arg0, Local0)
  Store(Arg1, Local1)
  Add(Local0, Local1, Local0)
}
```

函数使用方法 

```asl
MADD(A,B)
```


6.3 带有返回值的参数
----------------

```asl
Method(MADD,2)
{
    Store(Arg0, Local0)
    Store(Arg1, Local1)
    Add(Local0, Local1, Local0)
    Return (Local0)
}
```

函数调用

```asl
Store(MADD(1,2), Local0) //Local0 = 1 + 2
```


6.4 定义可序列化的函数
------------------

这个有点类似于多线程同步的概念，也就是说，当函数声明为Serialized，内存中仅能存在一个实例。一般应用在函数中创建一个对象。

例如 Method(TEST, Serialized)

或者Method(TEST, NotSerialized)


7 流程控制
========

在ASL中，常见的流程控制列表如下：

```asl
Break, BreakPoint, Case, Continue, Default, Else, ElseIf, Fatal, If, NoOp, Return, Sleep, Stall, Switch, While
```


7.1 If用法介绍
----------

例如下面的语句判断一下当前系统的接口是不是Darwin，如果是把OSYS = 0x2710

```asl
If (_OSI ("Darwin"))
{
	Store (0x2710, OSYS)
}
```



另外如果系统不是Linux，那么OSYS = 0x07D0

```asl
If (_OSI ("Darwin"))
{
    Store (0x2710, OSYS)
}
ElseIf (_OSI ("Linux"))
{
    Store (0x03E8, OSYS)
}
Else
{
    Store(0x07D0, OSYS)
}
```




7.2 Switch, Case, Defaule, BreakPoint
---------------------------------

Switch可以看做是一系列If....Else的集合。BreakPoint相当于断点，意味着退出当前Swtich

```asl
Switch(Arg2)
{
    Case(1)
    {
      If(LEqual(1, Arg1)
      {
          Return (1)
      }
	  BreakPoint
    }
    Case(2)
    {
        ....
        Return (2)
    }
    Default
    {
        BreakPoint
    }
}

```




7.3 循环控制While以及暂停Stall
--------------------------

```ASL
Store(10, Local0)
While (LAnd (0x00, Local0))
{
    Decrement (Local0)
    Stall (32)
}

```

