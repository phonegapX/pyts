"""
测试环境中可以直接采用HTTP协议进行测试,但是在实际部署中为了安全性需要建议采用HTTPS协议,
HTTPS是由SSL+HTTP协议构建的可进行加密传输、身份认证的网络协议,要比HTTP协议更加安全,
可防止数据在传输过程中不被窃取、改变,确保数据的完整性.
使用HTTPS需要证书,本程序用于生成测试证书,它会在当前目录生成相应证书,用于测试HTTPS协议使用
"""

import os

from werkzeug.serving import make_ssl_devcert


def create_crt(path, host):
    make_ssl_devcert(path, host=host) #生成证书


if __name__ == "__main__":
    path = os.path.dirname(os.path.realpath(__file__)) #当前路径
    if not os.path.exists(os.path.join(path, 'ssl.key')):
        filepath = os.path.join(path, 'ssl')
        create_crt(filepath, 'localhost')