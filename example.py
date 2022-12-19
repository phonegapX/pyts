"""
TradeStation API 使用的一些简单示例

详细的使用方法可以参考API官方文档:
https://tradestation.github.io/api-docs/

须知:
在使用API进行各种操作之前,需要先进行授权登录,获取访问令牌(token),才能进行各种操作
而这个授权登录过程已经完整封装成web方式,自动化进行,请先配置好授权认证web服务进行授权认证,
具体的细节请参考README文件
"""

import param #接口配置参数
from ts.ts_lib import TradeStationClient #自定义封装库


if __name__ == '__main__':

    """
    操作前,请先配置好授权认证web服务进行授权认证,具体的细节请参考README文件
    """

    tradestation_client = TradeStationClient(
        username=param.username,
        client_id=param.client_id,
        client_secret=param.client_secret,
        redirect_uri=param.redirect_uri,
        paper_trading=param.paper_trading)

    #可用的交易所信息
    r = tradestation_client.available_exchanges()
    print(r)

    #----------------------------------------------
    # 交易符号相关操作
    r = tradestation_client.symbol_lists()
    print(r)

    r = tradestation_client.symbol_list('NSDOTHE')
    print(r)

    r = tradestation_client.symbols_from_symbol_list('NSDOTHE')
    print(r)

    r = tradestation_client.symbol_info('GBTC')
    print(r)

    #----------------------------------------------
    # 报价相关
    r = tradestation_client.quotes(['GBTC'])
    print(r)

    #----------------------------------------------
    # 账户相关
    r = tradestation_client.user_accounts('test')
    print(r)

    r = tradestation_client.account_balances(['850000001','850000002','850000003'])
    print(r)

    r = tradestation_client.account_positions(['850000001','850000002','850000003'], ['GBTC'])
    print(r)

    r = tradestation_client.account_orders(['850000001','850000002','850000003'], 0, 10)
    print(r)
