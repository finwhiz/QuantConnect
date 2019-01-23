class BootCampTask(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2017, 6, 1)
        self.SetEndDate(2017, 6, 15)
        
        # Select the data you need here
        self.iwm = self.AddEquity("IWM",Resolution.Minute)
        self.iwm.SetDataNormalizationMode(DataNormalizationMode.Raw)
        
    def OnData(self, data):
        
        #Place an order and print the average fill price
        
        if not self.Portfolio.Invested:
            self.MarketOrder("IWM", 100)
            self.Debug("Purchased shares at " + str(self.Portfolio["IWM"].AveragePrice))
        
        pass
