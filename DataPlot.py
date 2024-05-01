from PyQt5 import QtCore
import time
import numpy as np
from scipy.signal import lfilter, butter

class DataPlot:
    def __init__(self, graph = None, current = 0):
        self.Y_Coordinates = []
        self.X_Coordinates = []
        self.currentpoint = current
        self.X_Points_Plotted = 0
        self.speed = 5
        self.FVC = 0
        self.FEF = 0
        self.PEFR = 0
        self.graphwidget = graph
        self.filteredYaxis= None
        self.Plot_Signal()
       
    def Plot_Signal(self):
        self.Y_Coordinates.append(self.currentpoint)
        self.X_Coordinates =  list(np.arange(len(self.Y_Coordinates)))
        numerator, denominator = butter(2, 0.5, 'high', analog=False) #(Highpass Filter testing)
        self.filteredYaxis = lfilter(numerator, denominator, self.Y_Coordinates)
        self.data_line = self.graphwidget.plot(self.X_Coordinates[:1], self.filteredYaxis[:1], pen="green")
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.Update_Plot_Data)
        self.timer.start()

    def Update_Plot_Data(self):
        self.Y_Coordinates.append(self.currentpoint)
        self.X_Coordinates =  list(np.arange(len(self.Y_Coordinates)))
        self.X_Points_Plotted += self.speed
            
        self.graphwidget.setLimits(xMin=0, xMax=float('inf'))
            
        self.data_line.setData(self.X_Coordinates[0 : self.X_Points_Plotted + 1], self.filteredYaxis[0 : self.X_Points_Plotted + 1])  # Update the data.
            
        self.graphwidget.getViewBox().setXRange(max(self.X_Coordinates[0 : self.X_Points_Plotted + 1]) - 1000, max(self.X_Coordinates[0 : self.X_Points_Plotted + 1]))
            
       
