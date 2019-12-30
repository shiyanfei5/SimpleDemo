# -*- coding: utf-8 -*-





class BridgeQueue(object):

    def __init__(self, ):
        self.Queue = []



    def addTradeRecord(self,trade_record):

        for group in self.Queue:
            if trade_record.price == group.price:
                group.add(trade_record)
                return
        new_group = BridgeGroup(trade_record)


    def addGroup(self,bridge_group):
        self.Queue.append(bridge_group)








