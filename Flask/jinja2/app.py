#! /usr/bin/env python3
from flask import Flask, request, url_for, redirect, render_template, flash

app = Flask(__name__)  # __name__ 代表目前執行的模組
@app.route('/')  # route()裝飾器將函式綁定URL
def home():  # 基本上是回傳文本當然也可以是html!
    var = 'variable'
    lst = ['Zoo', 'Qoo']
    dic = {'key1': 100, 'key2': 'pool'}
    users = ['pool', 'alan', 'joe']
    safe = '<i><b> Hello </b></i>'

    def func(string):
        return '~~' + string + '~~'
    return render_template('jinja.html', var=var, lst=lst, func=func, dic=dic, safe=safe, **dic)


@app.route('/child')
def child_template():
    return render_template('child.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
