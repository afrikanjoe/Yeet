import heapq

class StockPrice:

    def __init__(self):
        self.stock_prices = {}
        self.time_stamps = []
        self.max = -2**32
        self.min = 2**32 

    def update(self, timestamp: int, price: int) -> None:
        
        
        
        
        prev = self.stock_prices.get(timestamp,None)
        self.stock_prices[timestamp] = price
        if(prev==self.max):
            self.max = max(self.stock_prices.values())
        if(prev==self.min):
            self.min = min(self.stock_prices.values())
        
        if(self.stock_prices[timestamp]>self.max):
            self.max = self.stock_prices[timestamp]
                
        if(self.stock_prices[timestamp]<self.min):
            self.min = self.stock_prices[timestamp]
        
        
        heapq.heappush(self.time_stamps,-timestamp)

    def current(self) -> int:
        
        time = -self.time_stamps[0]
        return self.stock_prices[time]
        
        

    def maximum(self) -> int:
        return self.max
        

    def minimum(self) -> int:
        return self.min



import heapq

class StockPriceOptimal:

    def __init__(self):
        self.stock_prices = {}
        self.time_stamps = []
        self.max = []
        self.min =[] 

    def update(self, timestamp: int, price: int) -> None:
        
    
        heapq.heappush(self.max,(-price,timestamp))
        heapq.heappush(self.min,(price,timestamp))
        heapq.heappush(self.time_stamps,-timestamp)
        self.stock_prices[timestamp] = price

    def current(self) -> int:
        time = -self.time_stamps[0]
        return self.stock_prices[time]
        
        

    def maximum(self) -> int:
        v = self.max[0]
        while -v[0] != self.stock_prices[v[1]]:
            heapq.heappop(self.max)
            v = self.max[0]
        return -v[0]
    def minimum(self) -> int:
        v = self.min[0]
        while v[0] != self.stock_prices[v[1]]:
            heapq.heappop(self.min)
            v = self.min[0]
        return v[0]
        