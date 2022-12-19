# -*- coding: utf-8 -*-

"""
web服务页面逻辑
"""

from flask import render_template, request, url_for, redirect, flash, render_template_string

from tsrv import app

import sys
sys.path.insert(0, '../')

import param
from ts.client import TradeStationClient


@app.route('/login', methods=['GET'])
def login():
    """
    生成授权登录页面给账号管理员进行登录授权
    """
    tradestation_client = TradeStationClient(
        username=param.username,
        client_id=param.client_id,
        client_secret=param.client_secret,
        redirect_uri=param.redirect_uri,
        paper_trading=param.paper_trading)
    url = tradestation_client.get_login_page()
    return redirect(url)


@app.route('/', methods=['GET', 'POST'])
#@app.route('/auth', methods=['GET', 'POST'])
def auth():
    """
    账号管理员授权成功后,本函数将会被调用
    本函数将会通过授权code去获取真正的访问令牌(token)
    """
    code = request.args.get('code') #获取授权code
    state = request.args.get('state')
    if not code or not state:
        return render_template_string('')

    if request.method == 'GET':
        tradestation_client = TradeStationClient(
            username=param.username,
            client_id=param.client_id,
            client_secret=param.client_secret,
            redirect_uri=param.redirect_uri,
            paper_trading=param.paper_trading)
        #下面函数内部会通过授权code去获取真正的访问令牌(token),并保存到文件,以便后续API接口使用
        if tradestation_client.grab_access_token(code):
            return render_template('success.html') #展现授权成功页面
        else:
            return render_template('error.html') #展现授权失败页面

    elif request.method == 'POST':
        pass
