class UndergroundSystem:

    def __init__(self):

        self.customer = {}
        self.station = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:

        self.customer[id] = [t, stationName]

    def checkOut(self, id: int, stationName: str, t: int) -> None:

        checkin_time, start = self.customer[id]
        end = stationName
        total_time = t - checkin_time

        if (start, end) not in self.station:
            self.station[(start, end)] = (total_time, 1)

        else:
            time_so_far, trips = self.station[(start, end)]
            self.station[(start, end)] = (time_so_far + total_time, trips + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:

        return self.station[(startStation, endStation)][0] / self.station[(startStation, endStation)][1]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)