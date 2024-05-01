from PyQt5 import QtCore
import time
import numpy as np
from scipy.signal import lfilter, butter

class DataPlot:
    def __init__(self, ui = None, current = 0):
        self.Y_Coordinates = []
        self.X_Coordinates = []
        self.currentpoint = current
        self.X_Points_Plotted = 0
        self.speed = 5
        self.FVC = 0
        self.FEF = 0
        self.PEFR = 0
        self.GUI = ui
        self.filteredYaxis= None

       
    def Plot_Signal(self):
        self.Y_Coordinates.append(self.currentpoint)
        self.filteredYaxis = self.Y_Coordinates
        self.X_Coordinates =  list(np.arange(len(self.Y_Coordinates)))
        self.data_line = self.GUI.FlowGraph.plot(self.X_Coordinates[:1], self.Y_Coordinates[:1], pen="green")
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.Update_Plot_Data)
        self.timer.start()

    def Update_Plot_Data(self):
        self.Y_Coordinates.append(self.currentpoint)
        numerator, denominator = butter(2, 0.5, 'high', analog=False) #(Highpass Filter testing)
        self.filteredYaxis = lfilter(numerator, denominator, self.Y_Coordinates)
        self.X_Coordinates =  list(np.arange(len(self.Y_Coordinates)))
        self.X_Points_Plotted += self.speed
            
        self.GUI.FlowGraph.setLimits(xMin=0, xMax=float('inf'))
            
        self.data_line.setData(self.X_Coordinates[0 : self.X_Points_Plotted + 1], self.Y_Coordinates[0 : self.X_Points_Plotted + 1])  # Update the data.
            
        self.GUI.FlowGraph.getViewBox().setXRange(max(self.X_Coordinates[0 : self.X_Points_Plotted + 1]) - 1000, max(self.X_Coordinates[0 : self.X_Points_Plotted + 1]))
        peak = max(self.Y_Coordinates[0 : self.X_Points_Plotted + 1])
        avg = int(sum(self.Y_Coordinates) / len(self.Y_Coordinates))
        self.GUI.PEFR.setText(str(peak) + "mL/sec")
        self.GUI.FEF.setText(str(avg) + "mL/sec")

        
            
       
