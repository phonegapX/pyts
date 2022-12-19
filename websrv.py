"""
TradeStation API 授权认证web服务入口程序
实盘部署中此程序可以按守护进程方式运行
"""

from tsrv import app


if __name__ == "__main__":
    #HTTP方式运行,用于测试
    app.run(debug=True, port=80)
    #HTTPS方式运行,实盘部署中建议这种方式,测试证书由create_crt.py程序生成,实盘部署建议申请正式证书
    #app.run(debug=True, port=443, ssl_context=('ssl.crt', 'ssl.key'))
