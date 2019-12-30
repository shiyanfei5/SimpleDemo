from model.bridge.TradeRecord import TradeRecord


def main():
    raw_list_buy = []   # 有买有卖者的情况
    raw_list_sell = []  # 对卖方向分组
    result = {
        "investorid":{
            "B":[ ],
            "S":[ ]
        }



    }
    # 需要保证读入的数据是按照价格排序 降序排序
    # 以买方向
    for i in raw_list_buy:
        trade_record =  TradeRecord()
        if trade_record.investorid not in result.keys():
            result[trade_record.investorid] = {
                "B":[],
                "S":[]
            }




