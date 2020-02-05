# 標題 (# + text)

## 次標題 (## + text)

...依此類推(Atx形式)

標題還可以這樣使用

    This is an H1
    =============

    This is an H2
    -------------

(Setext形式)

* * *

段落以空白行分隔。

"行末" 兩個空格 産生斷行(正統如此,各自編輯器有其他語法) "\_" x 2
&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt; 下一行 >>>>>>>>>>>>

* * *

### 文本屬性：

_斜體_
_斜體_
**粗體**
**粗體**
==螢光筆==
~~刪除線~~
`等寬字型`
Proportional
`Monospaced`

## ![](https://i.imgur.com/X8k8Myc.png)

### 列表：( \*, +, - 皆可 )

-   王二
-   張三
    -   張三伍(多階層,前面兩個空格)
    -   張三柒
        -   張三柒伍減租(Q_Q)
-   李四

* * *

### 編號列表：( 數字 + . )

1.  不論
2.  三七
3.  二十一

* * *

### Cherk Box：( \*, +, - 皆可 & [space or x] )

-   [x] `male`
-   [ ] `female`
-   [ ] `?????`

* * *

### 表格：(只能簡單的表格)

| 預設值  | 靠右對齊 | 靠左對齊 | 置中對齊 |
| ---- | ---: | :--- | :--: |
| 1234 | 1234 | 1234 | 1234 |
| 123  |  123 | 123  |  123 |
| 12   |   12 | 12   |  12  |
| 1    |    1 | 1    |   1  |

* * *

### 區塊：三個反引號( \` )

    name = 'pool'
    print('Hello', name)

#### 點亮不同程式語法：

python:

```python
name = 'pool'
print('Hello', name)
```

c:

```c
void main()
{
  int num = 5;
  printf("%d\n", num);
}
```

* * *

### 階層式區塊：

> POOL
>
> > Qoo!!
> >
> > > ## Good~
> > >
> > > ### 連結使用
> > >
> > > [連結名稱] + ( 網址)
> > > [Google](https://www.google.com.tw/)

* * *

### 圖片使用

! + [圖片名稱] + (圖片網址資料夾位置)
![台灣黑熊](https://attach.setn.com/newsimages/2014/09/22/145441-XXL.jpg)

* * *

### html：(可以直接讀取html標籤語法)

<p>
  <center>
    <img width="500" src="https://mdn.mozillademos.org/files/9347/grumpy-cat-small.png" alt="">
  </center>
</p>
<b>
  <center>support 'html'</center>
</b>
<hr>

### 數學公式：(支援 $LaTax$ 格式, 用"錢($)"包起來)

#### 範例：

### $m = \\frac{m_0}{\\sqrt{1-\\frac{v^2}{c^2}}}$

#### 上標：

$X^{n+1}$

#### 下標：

$X\_{m+1}$

#### 開根號：

$\\sqrt{x^2 + y^2}$

#### 分數：

$9.8\\frac{m^2}{s}$

* * *

### 分割線： ^

    ---
    ***
    ___
    -----
    * * *
    很多種都可以,當然也可以用<hr>(html)

* * *

### 列出所有標題 `[TOC]`

[TOC]
