#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 SepineTam, Inc. All Rights Reserved 
#
# @Time    : 2024/3/7 15:19
# @Author  : Sepine Tam
# @File    : app.py.py
# @IDE     : PyCharm
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
