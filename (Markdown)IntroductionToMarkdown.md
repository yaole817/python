# MarkDown

## 内容
[TOC]

## 1 简介
Markdown是一种转换工具，将**纯文本**转换成HTML，后续，各家应用都增加导出pdf。  
Markdown是由JOHN GRUBER开发：[Markdown主页](https://daringfireball.net/projects/markdown/)。  

Markdown主要部分：  
1. 纯文本的格式化语法
2. 转换软件（最初以perl实现）

Markdown实际上就是HTML的极端简化版。  
Markdwon的语法非常简单明了，也因此基本语法并不强大，无法满足使用者的需求，所以对Markdown的扩展层出不穷，现在应用最多的就是Github的Markdown语法。  

## 2 基本语法
[Markdown基本语法](https://daringfireball.net/projects/markdown/syntax)。  
Markdown是将纯文本转换成HTML，因此它本身也支持一些HTML的元素。（这里说的HTML不是HTML5）  

### 2.1 标题
以前缀`#`来表示标题。  
`#`表示一级标题；  
`##`表示二级标题；  
...  
`######`表示六级标题（最大级数）；  

### 2.2 引用
段落开头，以前缀`>`表示引用。  

> 我是引用  
> > 我是二级引用
> > > 我是三级引用

### 2.3 行
以`<br>`或者行尾两个空格`  `表示换行；  
Markdown不支持4个空格的首行缩进，如果要实现，需要使用全角的两个空格。  

我是第一行  
我是第二行<br>
我是第三行  

### 2.4 强调字体
以前后缀`*`或`_`来表示斜体；  
以前后缀`**`或`__`来表示粗体；  
允许粗体、斜体嵌套。  

**我是粗体**    
*我是斜体*  
***我是粗斜体***  

### 2.5 列表
以前缀`* `或 `- `或`+ `表示无序列表；  
以数字前缀`1. `表示有序列表。  
一个列表元素下多个行需要使用4个空格或1个制表符。  

* 我是无序列表1  
- 我是无序列表2  
  我是无序列表2第二行  

1. 我是有序列表1  

### 2.6 代码块
以前缀4个空格或1个制表符表示代码块；  

    #include "studio.h"
    struct A {
        int a;
        int b;
    }

以字前前缀<code>`</code>表示行内代码；  

我是一个行内代码：`studio.h`  

以段落前后缀<code>```</code>表示代码块，还可以指定代码块语言；

```c 
#include "studio.h"
struct A {
    int a;
    int b;
}
```

### 2.7 链接
以`[]()`来定义一个跳转链接，`[]`中是显示名称，`()`中是跳转链接地址。  
跳转链接既可以跳转向网页，也可以跳转本地链接。  
链接本地路径时，可以使用相对路径，也可以使用绝对路径。  
 
[an example](http://example.com/ "Title")  

以`[][]`来定义一个引用链接  
[an example][id]  
[id]: http://example.com/  "Optional Title Here"  

### 2.8 图片引用
以`![]()`来定义一个图片引用；除比链接多一个`!`之外，使用方式相同  


## 3 扩展语法

### 3.0 目录
使用`[TOC]`以自动生成目录。  

### 3.1 表格

目前不论哪家的应用，表格都不支持嵌套，而且只支持横向表格。  

| AAAAA | BBBBB | CCCCC |
|:-:|--:|:--|
| A | B | C |


### 3.2 UML图

#### 3.2.1 [流程图](https://github.com/adrai/flowchart.js) 
元素：`start`，`end`，`operation`，`subroutine`，`condition`，`inputoutput`  
书写格式：  
```
tag=>type: content:>url
```

```flow
st=>start: Start:>https://www.zybuluo.com
io=>inputoutput: verification
op=>operation: Your Operation
cond=>condition: Yes or No?
sub=>subroutine: Your Subroutine
e=>end

st->io->op->cond
cond(yes)->e
cond(no)->sub->io
```

### 3.2.2 序列图
```sequence
Alice->John: Hello John, how are you?
loop every minute
    John-->Alice: Great!
end
```

### 3.2.3 甘特图
```gantt
title 项目开发流程
section 项目确定
    需求分析       :a1, 2016-06-22, 3d
    可行性报告     :after a1, 5d
    概念验证       : 5d
section 项目实施
    概要设计      :2016-07-05  , 5d
    详细设计      :2016-07-08, 10d
    编码          :2016-07-15, 10d
    测试          :2016-07-22, 5d
section 发布验收
    发布: 2d
    验收: 3d
```

### 3.2.4 
```graphLR
    A[Hard edge] -->|Link text| B(Round edge)
    B --> C{Decision}
    C -->|One| D[Result one]
    C -->|Two| E[Result two]
```

### 3.3 数学公式LaTex
以前后缀`$`表示行内公式；  
以段落前后缀`$$`表示正行公式；  


$$\sum_{i=1}^n a_i=0$$

$$f(x_1,x_x,\ldots,x_n) = x_1^2 + x_2^2 + \cdots + x_n^2 $$

$$\sum^{j-1}_{k=0}{\widehat{\gamma}_{kj} z_k}$$