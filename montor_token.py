"""
在使用TradeStation API进行交易之前,必须要进行授权认证的操作,授权后将会获取访问令牌(token),
凭token才能进行各种操作,比如进行交易,但是token默认有效期是1200秒,超过1200秒就会失效,失效后就
需要重新刷新token才行,所以本程序运行后将会每秒检测一次token是否将超时,如需要就重新刷新token

建议:实盘部署中此程序应该按守护进程方式运行
"""

import time
import param #接口配置参数
from ts.ts_lib import TradeStationClient #自定义封装库


while True:

    tradestation_client = TradeStationClient(
        username=param.username,
        client_id=param.client_id,
        client_secret=param.client_secret,
        redirect_uri=param.redirect_uri,
        paper_trading=param.paper_trading)

    #内部会检测访问令牌(token)是否过期,如果要过期的话就重新刷新token
    tradestation_client.silent_sso()

    time.sleep(1) #一秒检测一次
