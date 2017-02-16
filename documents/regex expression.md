**正则匹配**

**一，正则表达式简介**

**第一节：正则表达式概述**

正则表达式（Regular
Expression）是强大、便捷、高校的文本处理工具。它是一些用来匹配和处理文本的字符串。正则表达式是由
“普通字符”和具有特殊含义的“元字符”组成，正则表达式具有丰富的语法和表达能力，可以精确的描述匹配字符的范围（如“.”、“[
]”、“[\^
]”）和数量（如“？”、“+”、“{n}”）,还可以匹配出现位置（如“\^”、“\$”）以及子表达式嵌套等等。正则表达式能够添加、删除、分离、叠加、插入和休整各种类型的文本和数据。从根本上讲，最常用的两种基本用途是搜索和替换。

正则表达式与其他程序设计语言一样，拥有自己的特殊语法和指令，但其本身并不是一种完备的程序设计语言，甚至算不上是一种能够直接安装并运行的程序。准确来说，正则表达式语言是内置于其他语言或软件产品里的“迷你”语言。

**第二节：常用应用软件和编程语言中的正则表达式**

不同的正则表达式实现在基本的语法方面大都是一致的，但在正则表达式的使用方法和具体功能，在不同的应用程序/语言中各有不同。支持正则表达式的编程语言和应用软件各用各的调用方法。应用程序大多使用菜单选项和对话框来访问正则表达式，而程序设计语言大都在函数或对象类中使用正则表达式。此外，在不同的应用程序/语言中，正则表达式的实现也不一样，它们的语法和功能有明显的差异。

一般来说，程序设计语言有3种处理正则表达式的方式：集成式、程序式和面向对象式。在第一种方式中，正则表达式是直接内建在语言之中的，Perl就是如此。但其他两种方式中，正则表达式不属于语言的低级语法。相反，普通的函数接收普通的字符串，把它们作为正则表达式进行处理。由不同的函数进行不同的，关系到一个或多个正则表达式操作。大多数语言（不包括Perl）采用的都是这两种方式之一，包括Java，.NET，Tcl，Python，PHP，Emacs，lisp和Ruby。

**grep**是一种用来对文件或标准输入文本进行文字搜索的Unix工具。根据具体的命令选项，grep支持基本、扩展和perl正则表达式。

**JavaScrip** 通过在string和regex对象的几个方法里实现正则表达式处理。

**Macromedia ColdFusion** 通过4个函数提供正则表达式的支持。

**Macromedia Dreamweaver**支持在“搜索和替换”（菜单选项）操作中使用正则表达式

**Macromedia HomeSite**（包括ColdFusion
Studio）支持在“搜索和替换”（菜单选项）操作中使用正则表达式

**Microsoft ASP**
所有的ASP脚本都支持正则表达式。正则表达式支持是通过一个名为regexp的对象提供的。

**Microsoft ASP.NET**里的正则表达式支持由.NET Framework提供。

**Microsoft C\#** 里的正则表达式支持由.NET Framework提供。

**Microsoft.NET**通过它的基本类库提供了强大灵活的正则表达式支持，这些支持在所有.NET语言和工具里都可以使用。

**Microsoft Visual Studio.NET**里的正则表达式支持由.NET Framework提供。

**MySQL**是一个流行的开放源代码数据库软件，提供了正则表达式支持作为一种数据库搜索手段。

**Perl**是一门功能强大的脚本语言，是目前最流行最重要的正则表达式编程语言，可以说是各种正则表达式实现的“始祖”，其他各种实现几乎都与Perl兼容。正则表达式支持是Perl的核心组件之一。如果要在Perl脚本里使用正则表达式，只要给出给出一些操作和相应的模式即可。

例如，检查变量中的文本能否由某个正则表达式匹配。下面的代码检查\$reply中所含的字符串，报告这个字符串是否全部由数字构成：

**If ( \$reply =\~ /\^[0-9]+\$/) {**

**Print “only digits”;**

**} else {**

**Printf “ not only digits\\n ”;**

**}**

**PHP**通过它的PCRE组件提供与Perl相兼容的正则表达式支持。从PHP
4.2.0版本开始，PCRE（Perl Compatibel Regular
Expressions，Perl兼容的正则表达式）组件将自动安装。

**Sun
Java**对正则表达式的支持是从1.4版本开始的。Java语言中正则表达式匹配功能主要是通过java.util.regex.matcher类和一些方法实现的。

输入为摄氏或华氏温度（单位为C或F），识别用户输入的温度类型，并进行相应的转换。

![](regex_expression/42c0e346eca24e1ff0bdbbb8b2b74279.png)

图 5 温度转换流程图

![](regex_expression/135139c5beddbe83c437d7710cb5e61c.png)

图 6 温度正则表达式

**第三节：正则表达式的标准**

现行的正则表达式主要有三套标准，包括perl（PCRE）和POSIX的两套标准。

**1 POSIX标准**

POSIX把正则表达式分为两种（favor）：BRE（Basic Regular
Expressions）与ERE（Extended Regular Expressions
）。所有的POSIX程序可以选择支持其中的一种。具体规范如下表：

![](regex_expression/444e3937189bc3fb2c4a198ef41b918a.png)

从上图可以看出，有三个空白栏，那么是不是就意味这无法使用该功能了呢？答案是否定的，因为我们现在使用的linux发行版，都是集成GNU套件的，GNU是Gnu’s
Not
Unix的缩写，GNU在实现了POXIS标准的同时，做了一定的扩展，所以上面空白栏中的功能也能使用。下面一一讲解：

1.  BRE如何使用+、?呢？需要用\\+、\\?

2.  BRE如何使用\|呢？需要用\\\|

3.  ERE如何使用\\1、\\2…\\9这样的反引用？和BRE一样，就是\\1、\\2…\\9

通过上面总结，可以发现：GNU中的ERE与BRE的功能相同，只是语法不同（BRE需要用\\进行转义，才能表示特殊含义）。例如a{1,2}，在ERE表示的是a或aa，在BRE中表示的是a{1,2}这个字符串。为了能够在Linux下熟练使用文本处理工具，我们必须知道这些命令支持那种正则表达式。现对常见的命令总结如下：

－ 使用BRE语法的命令有：grep、ed、sed、vim

－ 使用ERE语法的命令有：egrep、awk、emacs

当然，这也不是绝对的，比如 sed
通过-r选项就可以使用ERE了，大家到时自己man一下就可以了。

One thing that sets this flavor apart is that most metacharacters require a
backslash to give the metacharacter its flavor

还值得一提的是POSIX还定义了一些shorthand，具体如下：

-   [:alnum:]

-   [:alpha:]

-   [:cntrl:]

-   [:digit:]

-   [:graph:]

-   [:lower:]

-   [:print:]

-   [:punct:]

-   [:space:]

-   [:upper:]

-   [:xdigit:]

在使用这些shorthand时有一个约束：必须在[]中使用，也就是说如果像匹配0-9的数字，需要这么写[[:alnum:]]，取反就是[\^[:alnum:]]。shorhand
在BRE与EBE中的用法相同。

如果你对sed、awk比较熟悉，你会发现我们平常在变成语言中用的\\d、\\w在这些命令中不能用，原因很简单，因为POSIX规范根本没有定义这些shorthand，这些是由下面将要说的PCRE中定义的。

| 流派        | 说明                                                                   | 工具                                            |                         |
|-------------|------------------------------------------------------------------------|-------------------------------------------------|-------------------------|
| BRE         | (、)、{、}都必须转义使用，不支持+、?、\|                               | grep、sed、vi（但vi支持这些多选结构和反向引用） |                         |
| GNU BRE     | (、)、{、}、+、?、\|都必须转义使用                                     | GNU grep、GNU sed                               |                         |
| ERE         | 元字符不必转义，+、?、(、)、{、}、\|可以直接使用，\\1、\\2的支持不确定 | egrep、awk                                      |                         |
| GNU ERE     | 元字符不必转义，+、?、(、)、{、}、\|可以直接使用，支持\\1、\\2         | grep –E、GNU awk                                |                         |
| POSIX字符组 | 说明                                                                   | ASCII语言环境                                   | Unicode语言环境         |
| [:alnum:]\* | 字母字符和数字字符                                                     | [a-zA-Z0-9]                                     | [\\p{L&}\\p{Nd}]        |
| [:alpha:]   | 字母                                                                   | [a-zA-Z]                                        | \\p{L&}                 |
| [:ascii:]   | ASCII字符                                                              | [\\x00-\\x7F]                                   | \\p{InBasicLatin}       |
| [:blank:]   | 空格字符和制表符                                                       | [ \\t]                                          | [\\p{Zs}\\t]            |
| [:cntrl:]   | 控制字符                                                               | [\\x00-\\x1F\\x7F]                              | \\p{Cc}                 |
| [:digit:]   | 数字字符                                                               | [0-9]                                           | \\p{Nd}                 |
| [:graph:]   | 空白字符之外的字符                                                     | [\\x21-\\x7E]                                   | [\^\\p{Z}\\p{C}]        |
| [:lower:]   | 小写字母字符                                                           | [a-z]                                           | \\p{Ll}                 |
| [:print:]   | 类似[:graph:]，但包括空白字符                                          | [\\x20-\\x7E]                                   | \\P{C}                  |
| [:punct:]   | 标点符号                                                               | [][!"\#\$%\&'()\*+,./:;\<=\>?\@\\\^\_\`{\|}\~-] | [\\p{P}\\p{S}]          |
| [:space:]   | 空白字符                                                               | [ \\t\\r\\n\\v\\f]                              | [\\p{Z}\\t\\r\\n\\v\\f] |
| [:upper:]   | 大写字母字符                                                           | [A-Z]                                           | \\p{Lu}                 |
| [:word:]\*  | 字母字符                                                               | [A-Za-z0-9\_]                                   | [\\p{L}\\p{N}\\p{Pc}]   |
| [:xdigit:]  | 十六进制字符                                                           | [A-Fa-f0-9]                                     | [A-Fa-f0-9]             |

**2 Globbing（wildcard patterns）**

Bash本身是不能处理正则表达式的。脚本中，也是类似于sed,awk等命令来处理正则表达式。

The command interpreters of the early versions of
[Unix](https://en.wikipedia.org/wiki/Unix) (1st through 6th Editions, 1969–75)
relied on a separate program to expand [wildcard
characters](https://en.wikipedia.org/wiki/Wildcard_character) in unquoted
arguments to a command:
/etc/glob.[[1]](https://en.wikipedia.org/wiki/Glob_(programming)#cite_note-1)
That program performed the expansion and supplied the expanded list of file
paths to the command for execution. Its name is an abbreviation for "global
command". Later, this functionality was provided as a library function, glob(),
used by programs such as the
[shell](https://en.wikipedia.org/wiki/Bourne_shell).

Bash是不能执行文件名扩展，而是利用globbing进程，但是globbing并不是利用标准RE
set。Globbing只是认识并展开wildcards。Globbing可以翻译标准wildcard
characters：“\*，？，[]以及一些特殊字符，例如\^在[]中取反”。Wildcardss在globbing中有一些重要的限制，例如\*不能匹配“.”开头的文件名。“？”在和globbing和regex有不同的含义。

![](regex_expression/12d888940e7def1c0072d6b52fe426f5.png)

In all cases the path separator character (/ on unix or \\ on windows) will
never be matched.

![](regex_expression/81f4df1307e720c40c7d8d77c677c0a5.png)

Some shells (such as the [C shell](https://en.wikipedia.org/wiki/C_shell) and
[Bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell))) support additional
syntax known as
[alternation](https://en.wikipedia.org/wiki/Alternation_(string_expansion)) or
[brace expansion](https://en.wikipedia.org/wiki/Brace_expansion).

-   Brace expansion

Brace expansion, also called alternation, is a feature copied from the [C
shell](https://en.wikipedia.org/wiki/C_shell). It generates a set of alternative
combinations. Generated results need not exist as files. The results of each
expanded string are not sorted and left to right order is preserved:

**\$** echo a{p,c,d,b}e

ape ace ade abe

**\$** echo {a,b,c}{d,e,f}

ad ae af bd be bf cd ce cf

这个不是可移植的，例如在Bourne shell（/bin/sh）就不行，他只能按原样输出。

可以迭代使用

ls \*.{jpg,jpeg,png} \# expands to \*.jpg \*.jpeg \*.png - after which,

\# the wildcards are processed

echo \*.{png,jp{e,}g} \# echo just show the expansions -

\# and braces in braces are possible.

In addition to alternation, brace expansion can be used for sequential ranges
between two integers or characters separated by double dots. Newer versions of
Bash allow a third integer to specify the increment.

**\$** echo {1..10}

1 2 3 4 5 6 7 8 9 10

**\$** echo file{1..4}.txt

file1.txt file2.txt file3.txt file4.txt

**\$** echo {a..e}

a b c d e

**\$** echo {1..10..3}

1 4 7 10

**\$** echo {a..j..3}

a d g j

When brace expansion is combined with variable expansion the variable expansion
is performed after the brace expansion, which in some cases may necessitate the
use of the built-in eval, thus:

**\$** start=1; end=10

**\$** echo {\$start..\$end} *\# fails to expand due to the evaluation order*

{1..10}

**\$** eval echo {\$start..\$end} *\# variable expansion occurs then resulting
string is evaluated*

1 2 3 4 5 6 7 8 9 10

-   Bash Extended Globbing

these are not the only forms of *wildcards* supported by bash. The other forms
are referred to as extended globbing and you must enable them before you can use
them:

\$ shopt -s extglob

Extended globbing as described by the bash man page:

-   ?(pattern-list) Matches zero or one occurrence of the given patterns

-   \*(pattern-list) Matches zero or more occurrences of the given patterns

-   \+(pattern-list) Matches one or more occurrences of the given patterns

-   \@(pattern-list) Matches one of the given patterns

-   !(pattern-list) Matches anything except one of the given patterns

注：wildcards in bash are referred to as pathname expansion.

**3 perl标准**

Perl语言第一版是由[Larry
Wall](http://en.wikipedia.org/wiki/Larry_Wall)发布于1987年12月，Perl在发布之初，就因其强大的功能而一票走红，Perl的定位目标就是“天天要使用的工具”。Perl比较显诸特征之一是与sed与awk兼容，这造就了Perl成为第一个通用性脚本语言。

随着Perl的不断发展，其支持的正则表达式的功能也越来越强大。其中影响较大的是于1994年10月发布的Perl
5，其增加了很多特性，比如non-capturing parentheses、lazy
quantifiers、look-ahead、元符号\\G等等。

正好这时也是WWW兴起的时候，而Perl就是为了文本处理而发明的，所有Perl基本上成了web开发的首选语言。Perl语言应用是如此广泛，以至于其他语言开始移植Perl，最终Perl
compatible（兼容）的PCRE诞生了，这其中包括了Tcl, Python, Microsoft’s .NET ,
Ruby, PHP, C/C++, Java等等。

前面说了shorthand在POSIX与PCRE是不同的，PCRE中我们常用的有如下这些：

-   \\w 表示[a-zA-Z]

-   \\W 表示[\^a-zA-Z]

-   \\s 表示[ \\t\\r\\n\\f]

-   \\S 表示[\^ \\t\\r\\n\\f]

-   \\d 表示[1-9]

-   \\D 表示[\^1-9]

-   \\\< 表示一个单词的起始

-   \\\> 表示一个单词的结尾

    **二，正则匹配原理（perl）**

正则表达式是由普通字符（例如字符 a 到
z）以及特殊字符（称为"元字符"）组成的文字模式，模式描述在搜索文本时要匹配的一个或多个字符串，正则表达式作为一个模板，将某个字符模式与所搜索的字符串进行匹配。

**1，字符说明**

-   特殊字符

| 特别字符 | 描述                                                                                                                                                          |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \$       | 匹配输入字符串的结尾位置。如果设置了 RegExp 对象的 Multiline 属性，则 \$ 也匹配 '\\n' 或 '\\r'。要匹配 \$ 字符本身，请使用 \\\$。                             |
| ( )      | 标记一个子表达式的开始和结束位置。子表达式可以获取供以后使用。要匹配这些字符，请使用 \\( 和 \\)。                                                             |
| \*       | 匹配前面的子表达式零次或多次。要匹配 \* 字符，请使用 \\\*。                                                                                                   |
| \+       | 匹配前面的子表达式一次或多次。要匹配 + 字符，请使用 \\+。                                                                                                     |
| .        | 匹配除换行符 \\n之外的任何单字符。要匹配 .，请使用 \\。                                                                                                       |
| [        | 标记一个中括号表达式的开始。要匹配 [，请使用 \\[。                                                                                                            |
| ?        | 匹配前面的子表达式零次或一次，或指明一个非贪婪限定符。要匹配 ? 字符，请使用 \\?。                                                                             |
| \\       | 将下一个字符标记为或特殊字符、或原义字符、或向后引用、或八进制转义符。例如， 'n' 匹配字符 'n'。'\\n' 匹配换行符。序列 '\\\\' 匹配 "\\"，而 '\\(' 则匹配 "("。 |
| \^       | 匹配输入字符串的开始位置，除非在方括号表达式中使用，此时它表示不接受该字符集合。要匹配 \^ 字符本身，请使用 \\\^。                                             |
| {        | 标记限定符表达式的开始。要匹配 {，请使用 \\{。                                                                                                                |
| \|       | 指明两项之间的一个选择。要匹配 \|，请使用 \\\|。                                                                                                              |

-   限定符

限定符用来指定正则表达式的一个给定组件必须要出现多少次才能满足匹配。有\*或+或?或{n}或{n,}或{n,m}共6种

| **字符** | **描述**                                                                                                                                                                  |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \*       | 匹配前面的子表达式零次或多次。例如，zo\* 能匹配 "z" 以及 "zoo"。\* 等价于{0,}。                                                                                           |
| \+       | 匹配前面的子表达式一次或多次。例如，'zo+' 能匹配 "zo" 以及 "zoo"，但不能匹配 "z"。+ 等价于 {1,}。                                                                         |
| ?        | 匹配前面的子表达式零次或一次。例如，"do(es)?" 可以匹配 "do" 或 "does" 中的"do" 。? 等价于 {0,1}。                                                                         |
| {n}      | n 是一个非负整数。匹配确定的 n 次。例如，'o{2}' 不能匹配 "Bob" 中的 'o'，但是能匹配 "food" 中的两个 o。                                                                   |
| {n,}     | n 是一个非负整数。至少匹配n 次。例如，'o{2,}' 不能匹配 "Bob" 中的 'o'，但能匹配 "foooood" 中的所有 o。'o{1,}' 等价于 'o+'。'o{0,}' 则等价于 'o\*'。                       |
| {n,m}    | m 和 n 均为非负整数，其中n \<= m。最少匹配 n 次且最多匹配 m 次。例如，"o{1,3}" 将匹配 "fooooood" 中的前三个 o。'o{0,1}' 等价于 'o?'。请注意在逗号和两个数之间不能有空格。 |

-   定位符

定位符使您能够将正则表达式固定到行首或行尾
它们还使您能够创建这样的正则表达式，这些正则表达式出现在一个单词内、在一个单词的开头或者一个单词的结尾

定位符用来描述字符串或单词的边界，\^和\$分别指字符串的开始与结束，\\b描述单词的前或后边界，\\B表示非单词边界。

| **字符** | **描述**                                                                                              |
|----------|-------------------------------------------------------------------------------------------------------|
| \^       | 匹配输入字符串开始的位置 如果设置了 RegExp 对象的 Multiline 属性，\^ 还会与 \\n 或 \\r 之后的位置匹配 |
| \$       | 匹配输入字符串结尾的位置 如果设置了 RegExp 对象的 Multiline 属性，\$ 还会与 \\n 或 \\r 之前的位置匹配 |
| \\b      | 匹配一个字边界，即字与空格间的位置                                                                    |
| \\B      | 非字边界匹配                                                                                          |

-   元字符

| **字符**    | **描述**                                                                                                                                                                                                                                                                                                                                                      |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \\          | 将下一个字符标记为一个特殊字符、或一个原义字符、或一个 向后引用、或一个八进制转义符 例如，'n' 匹配字符 "n" '\\n' 匹配一个换行符 序列 '\\\\' 匹配 "\\" 而 "\\(" 则匹配 "("                                                                                                                                                                                     |
|             | 匹配输入字符串的开始位置 如果设置了 RegExp 对象的 Multiline 属性，\^ 也匹配 '\\n' 或 '\\r' 之后的位置                                                                                                                                                                                                                                                         |
| \$          | 匹配输入字符串的结束位置 如果设置了RegExp 对象的 Multiline 属性，\$ 也匹配 '\\n' 或 '\\r' 之前的位置                                                                                                                                                                                                                                                          |
| \*          | 匹配前面的子表达式零次或多次 例如，zo\* 能匹配 "z" 以及 "zoo" \* 等价于{0,}                                                                                                                                                                                                                                                                                   |
| \+          | 匹配前面的子表达式一次或多次 例如，'zo+' 能匹配 "zo" 以及 "zoo"，但不能匹配 "z" + 等价于 {1,}                                                                                                                                                                                                                                                                 |
| ?           | 匹配前面的子表达式零次或一次 例如，"do(es)?" 可以匹配 "do" 或 "does" 中的"do" ? 等价于 {0,1}                                                                                                                                                                                                                                                                  |
| {n}         | n 是一个非负整数 匹配确定的 n 次 例如，'o{2}' 不能匹配 "Bob" 中的 'o'，但是能匹配 "food" 中的两个 o                                                                                                                                                                                                                                                           |
| {n,}        | n 是一个非负整数 至少匹配n 次 例如，'o{2,}' 不能匹配 "Bob" 中的 'o'，但能匹配 "foooood" 中的所有 o 'o{1,}' 等价于 'o+' 'o{0,}' 则等价于 'o\*'                                                                                                                                                                                                                 |
| {n,m}       | m 和 n 均为非负整数，其中n \<= m 最少匹配 n 次且最多匹配 m 次 例如，"o{1,3}" 将匹配 "fooooood" 中的前三个 o 'o{0,1}' 等价于 'o?' 请注意在逗号和两个数之间不能有空格                                                                                                                                                                                           |
| ?           | 当该字符紧跟在任何一个其他限制符 (\*, +, ?, {n}, {n,}, {n,m}) 后面时，匹配模式是非贪婪的 非贪婪模式尽可能少的匹配所搜索的字符串，而默认的贪婪模式则尽可能多的匹配所搜索的字符串 例如，对于字符串 "oooo"，'o+?' 将匹配单个 "o"，而 'o+' 将匹配所有 'o'                                                                                                         |
| .           | 匹配除 "\\n" 之外的任何单个字符 要匹配包括 '\\n' 在内的任何字符，请使用象 '[.\\n]' 的模式                                                                                                                                                                                                                                                                     |
| (pattern)   | 匹配 pattern 并获取这一匹配 所获取的匹配可以从产生的 Matches 集合得到，在VBScript 中使用 SubMatches 集合，在JScript 中则使用 \$0…\$9 属性 要匹配圆括号字符，请使用 '\\(' 或 '\\)'                                                                                                                                                                             |
| (?:pattern) | 匹配 pattern 但不获取匹配结果，也就是说这是一个非获取匹配，不进行存储供以后使用 这在使用 "或" 字符 (\|) 来组合一个模式的各个部分是很有用 例如， 'industr(?:y\|ies) 就是一个比 'industry\|industries' 更简略的表达式                                                                                                                                           |
| (?=pattern) | 正向预查，在任何匹配 pattern 的字符串开始处匹配查找字符串 这是一个非获取匹配，也就是说，该匹配不需要获取供以后使用 例如，'Windows (?=95\|98\|NT\|2000)' 能匹配 "Windows 2000" 中的 "Windows" ，但不能匹配 "Windows 3.1" 中的 "Windows" 预查不消耗字符，也就是说，在一个匹配发生后，在最后一次匹配之后立即开始下一次匹配的搜索，而不是从包含预查的字符之后开始 |
| (?!pattern) | 负向预查，在任何不匹配 pattern 的字符串开始处匹配查找字符串 这是一个非获取匹配，也就是说，该匹配不需要获取供以后使用 例如'Windows (?!95\|98\|NT\|2000)' 能匹配 "Windows 3.1" 中的 "Windows"，但不能匹配 "Windows 2000" 中的 "Windows" 预查不消耗字符，也就是说，在一个匹配发生后，在最后一次匹配之后立即开始下一次匹配的搜索，而不是从包含预查的字符之后开始  |
| x\|y        | 匹配 x 或 y 例如，'z\|food' 能匹配 "z" 或 "food" '(z\|f)ood' 则匹配 "zood" 或 "food"                                                                                                                                                                                                                                                                          |
| [xyz]       | 字符集合 匹配所包含的任意一个字符 例如， '[abc]' 可以匹配 "plain" 中的 'a'                                                                                                                                                                                                                                                                                    |
| [\^xyz]     | 负值字符集合 匹配未包含的任意字符 例如， '[\^abc]' 可以匹配 "plain" 中的'p'、'l'、'i'、'n'                                                                                                                                                                                                                                                                    |
| [a-z]       | 字符范围 匹配指定范围内的任意字符 例如，'[a-z]' 可以匹配 'a' 到 'z' 范围内的任意小写字母字符                                                                                                                                                                                                                                                                  |
| [\^a-z]     | 负值字符范围 匹配任何不在指定范围内的任意字符 例如，'[\^a-z]' 可以匹配任何不在 'a' 到 'z' 范围内的任意字符                                                                                                                                                                                                                                                    |
| \\b         | 匹配一个单词边界，也就是指单词和空格间的位置 例如， 'er\\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'                                                                                                                                                                                                                                            |
| \\B         | 匹配非单词边界 'er\\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'                                                                                                                                                                                                                                                                                  |
| \\cx        | 匹配由 x 指明的控制字符 例如， \\cM 匹配一个 Control-M 或回车符 x 的值必须为 A-Z 或 a-z 之一 否则，将 c 视为一个原义的 'c' 字符                                                                                                                                                                                                                               |
| \\d         | 匹配一个数字字符 等价于 [0-9]                                                                                                                                                                                                                                                                                                                                 |
| \\D         | 匹配一个非数字字符 等价于 [\^0-9]                                                                                                                                                                                                                                                                                                                             |
| \\f         | 匹配一个换页符 等价于 \\x0c 和 \\cL                                                                                                                                                                                                                                                                                                                           |
| \\n         | 匹配一个换行符 等价于 \\x0a 和 \\cJ                                                                                                                                                                                                                                                                                                                           |
| \\r         | 匹配一个回车符 等价于 \\x0d 和 \\cM                                                                                                                                                                                                                                                                                                                           |
| \\s         | 匹配任何空白字符，包括空格、制表符、换页符等等 等价于 [ \\f\\n\\r\\t\\v]                                                                                                                                                                                                                                                                                      |
| \\S         | 匹配任何非空白字符 等价于 [\^ \\f\\n\\r\\t\\v]                                                                                                                                                                                                                                                                                                                |
| \\t         | 匹配一个制表符 等价于 \\x09 和 \\cI                                                                                                                                                                                                                                                                                                                           |
| \\v         | 匹配一个垂直制表符 等价于 \\x0b 和 \\cK                                                                                                                                                                                                                                                                                                                       |
| \\w         | 匹配包括下划线的任何单词字符 等价于'[A-Za-z0-9\_]'                                                                                                                                                                                                                                                                                                            |
| \\W         | 匹配任何非单词字符 等价于 '[\^A-Za-z0-9\_]'                                                                                                                                                                                                                                                                                                                   |
| \\xn        | 匹配 n，其中 n 为十六进制转义值 十六进制转义值必须为确定的两个数字长 例如，'\\x41' 匹配 "A" '\\x041' 则等价于 '\\x04' & "1" 正则表达式中可以使用 ASCII 编码                                                                                                                                                                                                   |
| \\num       | 匹配 num，其中 num 是一个正整数 对所获取的匹配的引用 例如，'(.)\\1' 匹配两个连续的相同字符                                                                                                                                                                                                                                                                    |
| \\n         | 标识一个八进制转义值或一个向后引用 如果 \\n 之前至少 n 个获取的子表达式，则 n 为向后引用 否则，如果 n 为八进制数字 (0-7)，则 n 为一个八进制转义值                                                                                                                                                                                                             |
| \\nm        | 标识一个八进制转义值或一个向后引用 如果 \\nm 之前至少有 nm 个获得子表达式，则 nm 为向后引用 如果 \\nm 之前至少有 n 个获取，则 n 为一个后跟文字 m 的向后引用 如果前面的条件都不满足，若 n 和 m 均为八进制数字 (0-7)，则 \\nm 将匹配八进制转义值 nm                                                                                                             |
| \\nml       | 如果 n 为八进制数字 (0-3)，且 m 和 l 均为八进制数字 (0-7)，则匹配八进制转义值 nml                                                                                                                                                                                                                                                                             |
| \\un        | 匹配 n，其中 n 是一个用四个十六进制数字表示的 Unicode 字符 例如， \\u00A9 匹配版权符号 (?)                                                                                                                                                                                                                                                                    |

-   运算符的优先级

正则表达式从左到右进行计算，并遵循优先级顺序，这与算术表达式非常类似

相同优先级的从左到右进行运算，不同优先级的运算先高后低
下表从最高到最低说明了各种正则表达式运算符的优先级顺序：

| **运算符**                     | **描述**                                                                                                                         |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| \\                             | 转义符                                                                                                                           |
| (), (?:), (?=), []             | 圆括号和方括号                                                                                                                   |
| \*, +, ?, {n}, {n,}, {n,m}     | 限定符                                                                                                                           |
| \^, \$, \\任何元字符、任何字符 | 定位点和序列（即：位置和顺序）                                                                                                   |
| \|                             | 替换，"或"操作                                                                                                                   |
|                                | 字符具有高于替换运算符的优先级，使得"m\|food"匹配"m"或"food" 若要匹配"mood"或"food"，请使用括号创建子表达式，从而产生"(m\|f)ood" |

**2，匹配示例**

1.  **匹配单个字符**

**. 可以匹配任何一个单个的字符、数字、字母甚至是.字符本身**

**文本**

scales1.xls

orders3.xls

sales2.xls

na1.xls

sa1.xls

**正则表达式**

sales.

**匹配结果**

scales1.xls

orders3.xls

sales2.xls

na1.xls

sa1.xls

1.  **\\ 转义字符：匹配元字符本身而不是它在正则表达式里的特殊含义**

**文本**

scales1.xls

orders3.xls

sales2.xls

na1.xls

sa1.xls

**正则表达式**

.a.\\.xls

**匹配结果**

scales1.xls

orders3.xls

sales2.xls

na1.xls

sa1.xls

1.  **匹配一组字符**

**[ ] 字符集合：匹配该集合里的任意一个成员**

**文本**

The phrase “regular expression” is often abbreviated as RegEx or regex.

**正则表达式**

[Rr]eg[Ee]x

**匹配结果**

The phrase “regular expression” is often abbreviated as RegEx or regex.

1.  **字符区间（在[ ]之间为元字符，字符集和外只是普通字符）**

**文本**

scales1.xls

orders3.xls

sales2.xls

na1.xls

sa1.xls

sa2.xls

**正则表达式**

[ns]a[0-9]\\.xls

**匹配结果**

scales1.xls

orders3.xls

sales2.xls

na1.xls

sa1.xls

sa2.xls

1.  **\^ 对一个字符集合取非运算（只有放在[]间，紧跟左方括号后面）**

**文本**

scales1.xls

orders3.xls

sales2.xls

na1.xls

sa1.xls

sam.xls

**正则表达式**

[ns]a[\^0-9]\\.xls

**匹配结果**

scales1.xls

orders3.xls

sales2.xls

na1.xls

sa1.xls

sam.xls

1.  **数字元字符**

>   **\\d 任何一个数字字符（等价于[0-9]）**

>   **\\D 任何一个非数字字符（等价于[\^0-9]）**

**文本**

var myArray = new Array();

\`\`\`

If (myArray[0] == 0)

\`\`\`

}

**正则表达式**

myArray\\[\\d\\]

**匹配结果**

var myArray = new Array();

\`\`\`

If (myArray[0] == 0)

\`\`\`

}

1.  **字母数字元字符**

>   **\\w 任何一个字母数字字符或下划线字符（等价于[a-zA-Z0-9]）**

>   **\\W 任何一个非字母数字字符或下划线字符（等价于[\^a-zA-Z0-9]）**

**文本**

11214

A1C2E3

48075

M1B4F2

90046

H1H2H2

**正则表达式**

\\w\\d\\w\\d\\w\\d

**匹配结果**

11214

A1C2E3

48075

M1B4F2

90046

H1H2H2

1.  **空白字符元字符**

>   **\\s 任何一个空白字符（等价于[\\f\\n\\r\\t\\v]]）**

>   **\\S 任何一个非空白字符（等价于[\^\\f\\n\\r\\t\\v]]）**

**表 POSIX字符类**

| 字符类     | 说明                                                    |
|------------|---------------------------------------------------------|
| [:alnum:]  | 任何一个字母或数字（等价于[a-zA-Z0-9]）                 |
| [:alpha:]  | 任何一个字母（等价于[a-zA-Z]）                          |
| [:blank:]  | 空格或制表符（等价于[\\t]）                             |
| [:cntrl:]  | ASCII控制字符（ASCII 0到31，再加上ASCII 127）           |
| [:digit:]  | 任何一个数字（等价于[0-9]）                             |
| [:graph:]  | 和[:print:]一样，但不包括空格                           |
| [:lower:]  | 任何一个小写字母（等价于[a-z]）                         |
| [:print:]  | 任何一个可打印字符                                      |
| [:punct:]  | 既不属于[:alnum:]也不属于[:cntrl:]的任何一个字符        |
| [:space:]  | 任何一个空白字符，包括空格（等价于[\^\\f\\n\\r\\t\\v]） |
| [:upper:]  | 任何一个大写字母（等价于[A-Z]）                         |
| [:xdigit:] | 任何一个十六进制数字（等价于[a-fA-F0-9]）               |

1.  **重复匹配**

**+ 匹配一个或多个字符集合**

**文本**

Send personal email to <ben@forta.com>. For questions about a book use
<support@forta.com>. Feel free to send unsolicited email to <apam@forta.com>
(wouldn’t it be nice if it were that simple, huh?).

**正则表达式**

\\w+\@\\w+\\.\\w+

**匹配结果**

Send personal email to <ben@forta.com>. For questions about a book use
<support@forta.com>. Feel free to send unsolicited email to <apam@forta.com>
(wouldn’t it be nice if it were that simple, huh?).

1.  **？ 匹配一个字符的零次或一次出现**

**文本**

The URL is <http://www.forta.com/>, to connct securely use
<https://www.forta.com/> instead.

**正则表达式**

https?://[\\w./]+

**匹配结果**

The URL is <http://www.forta.com/> to connct securely use
<https://www.forta.com/> instead.

1.  **匹配零个或任意多个字符**

**文本**

Hello <ben@forta.com> is my email address.

**正则表达式**

\\w+[\\w.]\*\@[\\w.]+\\.\\w+

**匹配结果**

Hello <ben@forta.com> is my email address.

1.  **{m,n} 重复匹配次数，最少m次最多n次**

**文本**

4/8/03

10-6-2004

2/2/2

01-01-01

**正则表达式**

\\d{1,2}[-\\/]\\d{1,2}[-\\/]\\d{2,4}

**匹配结果**

4/8/03

10-6-2004

2/2/2

01-01-01

**{n}重复匹配n次**

**{n, }至少重复匹配n次**

1.  **+、\*和 {n,
    }属于贪婪型元字符，它们会尽可能地从一段文本的开头一直匹配到这段文本的结尾，而不是从这段文本的开头匹配到碰到第一个匹配时为止，+？、\*？和{n,
    }?属于懒惰型元字符，它会匹配尽可能少的字符**

**文本**

This offer is not available to customers living in \<B\>AK\</B\> and
\<B\>HI\</B\>.

**正则表达式**

\<[bB]\>.\*\</[Bb]\>

\<[bB]\>.\*?\</[Bb]\>

**匹配结果**

This offer is not available to customers living in \<B\>AK\</B\> and
\<B\>HI\</B\>.

This offer is not available to customers living in \<B\>AK\</B\> and
\<B\>HI\</B\>.

1.  **位置匹配（解决在什么地方进行字符串匹配)**

**\\b 匹配一个单词的开始或结尾**

**文本**

The cat scattered his food all over the room.

**正则表达式**

\\bcat\\b

**匹配结果**

The cat scattered his food all over the room.

**\^ 定义字符串开头**

**文本**

\<?xml version=”1.0” encoding=”UTF-8” ?\>

\<wsdl:definitions targetnamespace=<http://tips.cf>

xmlns:impl=<http://tips.cf> xmlns:intf=<http://tips.cf>

xmlns:apachesoap=”http://xml.apache.org/xml-soap”

**正则表达式**

\^\\s\*\<\\?xml.\*\\?\>

**匹配结果**

\<?xml version=”1.0” encoding=”UTF-8” ?\>

\<wsdl:definitions targetnamespace=<http://tips.cf>

xmlns:impl=<http://tips.cf> xmlns:intf=<http://tips.cf>

xmlns:apachesoap=”http://xml.apache.org/xml-soap”

**\$ 定义字符串结尾**

1.  **(?m)分行匹配模式(能够改变其他元字符行为的元字符序列)**

分行匹配模式将使得正则表达式引擎把行分隔符当做一个字符串分隔符来对待。在分行匹配模式下，\^不仅匹配正常的字符串开头，还将匹配行分割符（换行符）后面的开始位置（这个位置是不可见的）；\$不仅匹配正常的字符串结尾，还将匹配行分割符（换行符）后面的结束位置。

**文本**

\<SCRIPT\>

Function dospellcheck(form, field) {

// Make sure not empty

If (field.value == ‘ ‘) {

Return false;

}

// Init

Var windowname=’spellwindow’;

Var

spellcheckURL=’spell.cfm?formname=comment&fieldname=’+field.

Name;

\`\`\`

// Done

Return flase;

}

\</SCRIPT\>

**正则表达式**

(?m)\^\\s\*//.\*\$

**匹配结果**

\<SCRIPT\>

Function dospellcheck(form, field) {

// Make sure not empty

If (field.value == ‘ ‘) {

Return false;

}

// Init

Var windowname=’spellwindow’;

Var

spellcheckURL=’spell.cfm?formname=comment&fieldname=’+field Name;

\`\`\`

// Done

Return flase;

}

\</SCRIPT\>

1.  **子表达式的嵌套（**子表达式指的是整个正则表达式中的一部分，通常是括号内的表达式，或者是由\|（相当于或）分隔的多选分支。（a\|b\|c）等价于[abc]**）**

**文本**

Pinging hog.forta.com [12.159.46.200]

With 32 bytes of data:

**正则表达式**

(((\\d{1,2})\|(1\\d{2})\|(2[0-4]\\d)\|(25[0-5]))\\.){3}((\\d{1,2})\|(1\\d{2})\|(2[0-4]\\d)\|(25[0-5]))

**匹配结果**

Pinging hog.forta.com [12.159.46.200]

With 32 bytes of data:

分析各个子表达式的时候，应该按照先内后外的原则俩进行而不是从第一个字符开始一个字符一个字符地区尝试。

1.  **回溯引用：前后一致引用（回溯引用允许正则表达式引用前面的匹配结果）**

\\n表示回溯引用，匹配与之相同的内容，n代表模式里的第几个子表达式

**文本**

\<BODY\>

\<H1\>Welcome to my Homepage\</H1\>

Content is divided into two Sections：\<BR\>

\<H2\>ColdFusion\</H2\>

Information about Macromedia ColdFusion

\<H2\>Wireless\</H2\>

Information about Bluetooth, 802.11, and more

\<H2\>This is not valid HTML\</H3\>

\</BODY\>

**正则表达式**

\<[Hh]([1-6])\>.\*?\</[Hh]\\1\>

**匹配结果**

\<BODY\>

\<H1\>Welcome to my Homepage\</H1\>

Content is divided into two Sections：\<BR\>

\<H2\>ColdFusion\</H2\>

Information about Macromedia ColdFusion

\<H2\>Wireless\</H2\>

Information about Bluetooth, 802.11, and more

\<H2\>This is not valid HTML\</H3\>

\</BODY\>

1.  **前后查找**

**？=
正向前查找，需要匹配的文本跟在=后面，被匹配的文本不包含在最终的匹配结果里**

**文本**

<http://www.forta.com/>

<https://mail.forta.com/>

<ftp://forta.com/>

**正则表达式**

.+(?=:)

**匹配结果**

<http://www.forta.com/>

<https://mail.forta.com/>

<ftp://forta.com/>

1.  **？\<= 正向后查找
    需要匹配的文本跟在=后面，被匹配的文本不包含在最终的匹配结果里**

**文本**

ABC01: \$23.45

HGG42: \$5.31

CFMX1: \$899.00

XTC99: \$69.96

Total items found: 4

**正则表达式**

(?\<=\\\$)[0-9.]+

**匹配结果**

ABC01: \$23.45

HGG42: \$5.31

CFMX1: \$899.00

XTC99: \$69.96

Total items found: 4

1.  **提取Web页面标题**

HTML页面标题是出现在\<TITLE\>和\</TITLE\>标题之间的文字，而这对标签又必须嵌在HTML代码的\<HEAD\>

部分里。

**文本**

\<HEAD\>

\<TITLE\>Ben Forta’s Homepage\</TITLE\>

\</HEAD\>

**正则表达式**

(?\<=\<[tT][iI][tT][lL][eE]\>).\* (?=\</[tT][iI][tT][lL][eE]\>)

**匹配结果**

\<HEAD\>

\<TITLE\>Ben Forta’s Homepage\</TITLE\>

\</HEAD\>

1.  **？！ 负向前查找 将向前查找不与给定模式相匹配的文本**

**？\<! 负向后查找 将向后查找不与给定模式相匹配的文本**

**文本**

I paid \$30 for 100 apples,

50 oranges, and 60 preas.

I saved \$5 on this order.

**正则表达式**

(?\<!\\\$)\\d+

**匹配结果**

I paid \$30 for 100 apples,

50 oranges, and 60 preas.

I saved \$5 on this order.

Total items found: 4

1.  **嵌套条件**

**（？(backerference)true-regex\|false-regex)
backerference存在时执行true-regex，否则执行false-regex**

电话号码匹配

**文本**

123-456-7890

(123)456-7890

(123)-456-7890

(123-456-7890

1234567890

123 456 7890

**正则表达式**

(\\( )?\\d{3}(?(1)\\)\|-)\\d{3}-\\d{4}

**匹配结果**

123-456-7890

(123)456-7890

(123)-456-7890

(123-456-7890

1234567890

123 456 7890

**常见问题的正则表达式的解决方案**

北美电话号码

北美地区的电话号码由一个3位数的区号和一个7位数的号码组成（着7位数字又分成一个3位数的局号和一个4位数的线路号，局号和线路号之间用连字符分隔）。每位电话号码可以是任意数字，但区号和局号的第一个数字不能是0或1。**（555）
555-5555**（右括号的后面有一个空格）或**（555）555-5555**或**555-555-5555**。

**文本**

J. Doe: 248-555-1234

B. Smith: （313） 555-123

A. Lee:（810）555-1234

**正则表达式**

\\(？[2-9]\\d\\d)?[ -]?[2-9]\\d\\d-\\d{4}

**匹配结果**

J. Doe: 248-555-1234

B. Smith: （313） 555-123

A. Lee:（810）555-1234

**URL地址**

URL匹配内容为：协议名（http或https）、一个主机名、一个可选的端口号、一个文件路径。

**文本**

<http://www.forta.com/blog>

<https://www.forta.com:80/blog/index.cfmg>

<http://www.forta.com>

<http://ben:password@www.forta.com/>

<http://localhost/index.php?ab=1&c=2>

<http://localhost:8500/>

**正则表达式**

https?://(\\w\*:\\w\*\@)?[-\\w.]+(:\\d+)?(/([\\w/\_.]\*(\\?\\S+)？)？)?

**匹配结果**

<http://www.forta.com/blog>

<https://www.forta.com:80/blog/index.cfmg>

<http://www.forta.com>

<http://ben:password@www.forta.com/>

<http://localhost/index.php?ab=1&c=2>

<http://localhost:8500/>

注意：在字符组内部，元字符定义规则是不一样的，例如，在字符组外部，.号是元字符，但在内部则不是如此，相反，连字符只有在字符组内部才是元字符，否则就不是。脱字符在字符组外部表示一个意思，在字符组内部紧接着[表示另一个意思，其他情况下又表示别的意思。

量词（\*,+,?）作用的对象是它们之间紧邻的子表达式。例如my？，?作用的是y而不是my，如果量词之前紧邻的是一个括号包围的子表达式，则整个子表达式视为一个单元（my）?。
