import DataPlot

# noinspection PyTypeChecker
class Graph:
    def __init__(self, graph = None, currentPoint):
        self.graphwdt = graph
        self.CurrentSignal = None
        self.Y_Coordinates += currentPoint
        self.count = 0
        
        
    def browse(self, currentPoint):
        self.signal = DataPlot(col = "r" , graph = self.graphwdt, y_point=self.Y_Coordinates)
        self.signal.Y_Coordinates += currentPoint
 


