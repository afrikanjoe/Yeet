class UndergroundSystem:

    def __init__(self):
        
        self.checkins = {}
        self.averages = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = [stationName,t]
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        checkin = self.checkins[id]
        del self.checkins[id]
        
        time = t- checkin[1]
        val = self.averages.get(checkin[0]+','+stationName,[])
        val.append(time)
        self.averages[checkin[0]+','+stationName] = val
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.averages[startStation+','+endStation])/len(self.averages[startStation+','+endStation])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)