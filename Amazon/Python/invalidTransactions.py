class Transaction(object):
    def __init__(self, trans):
        name, time, amount, city = trans.split(',')
        self.name = name
        self.time = int(time)
        self.amount = int(amount)
        self.city = city
    
    def invalidAmount(self):
        return self.amount > 1000
    
    def diffCity(self, city, time):
        return city != self.city and abs(time - self.time) <= 60
    
    def invalid(self, city, time):
        return self.invalidAmount() or self.diffCity(city, time)
    
class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        mp = collections.defaultdict(list)
        for trans in transactions:
            transObj = Transaction(trans)
            mp[transObj.name].append(transObj)
        
        res = []
        for trans in transactions:
            transObj = Transaction(trans)
            for compareObj in mp[transObj.name]:
                if transObj.invalid(compareObj.city, compareObj.time):
                    res.append(trans)
                    break
        return res
        
        
        