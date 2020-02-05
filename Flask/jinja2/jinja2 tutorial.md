# [Jinja2](https://jinja.palletsprojects.com/en/2.10.x/)

* * *

[TOC]

* * *

## expressions 表達式

-   (變量)  {{ ... }}
-   (聲明)  {% ... %}
-   (註解)  {# ... #}

* * *

### variables 變量

-   使用雙大括號: {{ variable }}


-   variable 可以是python中的任何變量, (list)
    -   (變量) - {{ variable }}
    -   (串列) - {{ lst[3] }}
    -   (字典) - {{ dic['key'] }} (={{ dic.key }})
    -   (屬性) - {{ class.attribute }} (={{ class[attribute] }})
    -   (函數) - {{ func() }}

#### [Filter (變量過濾器)](https://jinja.palletsprojects.com/en/2.10.x/templates/#list-of-builtin-filters)

-   \+|Filter(): {{ `items`|Filter() }}
-   {{ `items`|Filter1()|Filter }} (可以使用多個過濾器)

| Filter     | -                                    |
| ---------- | ------------------------------------ |
| safe       | 轉義(當變量本身是html code, 轉程html編碼, 而非純字串) |
| capitalize | 字首大寫                                 |
| lower      | 小寫                                   |
| upper      | 大寫                                   |
| title      | 每個單詞字首都大寫                            |
| trim       | 刪除首尾空格                               |
| striptags  | 去掉變量中的HTML標籤                         |
| default    | 設定一個預設值, 當變量沒有定義時呼叫                  |

-   也可以當作語法使用: {% `filter` upper %} This text becomes uppercase {% endfilter %}

* * *

#### [Test (檢查器)](https://jinja.palletsprojects.com/en/2.10.x/templates/#list-of-builtin-tests)

-   判斷一個變量是否滿足某種類型 {% if variable is escaped %}

```html
{% if variable is defined %}
    value of variable: {{ variable }}
{% else %}
    variable is not defined
{% endif %}
```

| Test        | -            |
| ----------- | ------------ |
| callable( ) | 是否可調用(是不是函式) |
| defined( )  | 是否已定義        |
| escaped( )  | 是否是          |
| upper( )    | 是否都大寫        |
| lower( )    | 是否都小寫        |
| string( )   | 是否是一個字串      |
| sequence( ) | 是否是一個列表      |
| number( )   | 是否是一個數字      |
| odd( )      | 是否是一個奇數      |
| even( )     | 是否是一個偶數      |

* * *

## 繼承模板:

-   block定義: {% block name %} 內容 {% endblock %} ({% endblock name %} 也可以)
-   繼承定義: {% extends "base.html" %} (放在第一行繼承模板)
-   子模板 就是繼承定義後, 放入一個個block 即可！
-   若是子模板有相同名稱的 block, 則會取代父模板中的 block (若是父模板沒有同樣block 則會不見)
-   在子模板 block中放入 {{ super() }}, 可以保留父模板的內容 (在多層block+中 最上層需要+super(), 裡面內容才會保留)

#### Base Template

base.html:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    {% block head %}
    <link rel="stylesheet" href="style.css" />
    <title>{% block title %}{% endblock %} - My Webpage</title>
    {% endblock %}
</head>
<body>
    <div id="content">{% block content %}{% endblock %}</div>
    <div id="footer">
        {% block footer %}
        &copy; Copyright 2008 by <a href="http://domain.invalid/">you</a>.
        {% endblock %}
    </div>
</body>
</html>
```

#### Child Template

child.html:

```html
{% extends "base.html" %}
{% block title %}Index{% endblock %}
{% block head %}
    {{ super() }}
    <style type="text/css">
        .important { color: #336699; }
    </style>
{% endblock %}
{% block content %}
    <h1>Index</h1>
    <p class="important">
      Welcome to my awesome homepage.
    </p>
{% endblock %}
```

* * *

### `for`

-   跟python 使用方式雷同

```html
{% for val in list %}
  {{ val }}
{% endfor %}
```

* * *

### `if`, `elif`, `else`

-   可以組合for一起使用

```html
{% `if` bool %}
  內容
{% `elif` bool%}
  內容
{% `else` %}
  內容
{% endif %}
```

* * *

### `Set` & `with` 賦值(定義變量, 可以是 python 中的資料型態)

-   {% `set` lst = [0, 1, 2]  %}
-   {% `with` x = 99 %} 只有在定義空間內有效 {% endwith %}

* * *

### Math & Comparisons & Logic

-   {{ 1 + 1 }}
-   {{ 1 == 1 }}
-   {{ True or False }}
-   支援 `+`, `-`, `*`, `**`, `/`, `//`, `%`, `==`, `>`, `<`, `>=`, `<=`, `or`, `and`, `not`, `in`

* * *

### Macro 巨集

```html
{% macro input(name, value='', type='text') -%}
    <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}">
{%- endmacro %}
```

-   使用呼叫: `{{ input('password', type='password') }}`
