import sys, getopt, io
import requests
import json, csv
import urllib.request
import plotext as ptt
import uniplot as uni
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
"%matplotlib"

class My_DcTracker_Class():
    """NAME
        My_DcTracker_Class - A Class to display a current figure of dc prices by using a requests function.

        """


    def __init__(self, argu):
        self.argu = argu
        self.url = argu['url']
        self.currency = argu['currency']
        self.comission = argu['comission']
        self.coinvalue = argu['coinvalue']
        self.coinamount = argu['coinamount']
        

    def __str__(self):
        pass

    def __eq__(self, other):
        pass

    def get_request(self):
        """ Requests the data and exports it as a json file. """
        req_data = requests.get(self.argu['url'])
        return req_data.json()

    def get_tempK(self, data):
        test_dict = [] 
        for i in range(40):
            test_dict.append(float(data['list'][i]['main']['feels_like']))
        return test_dict

    def set_tempC(self, data):
        celcius = []
        for kelvin in range(0, 40):
            celcius_v = float(data[kelvin])-273.15
            data[kelvin] = celcius_v
        return(data)

    def set_time(self, data):
        time = []
        for i in range(40):
            time.append(data['list'][i]['dt_txt'])
        print(time)
        return time

    def set_plot(self, earnings, times):
        y = earnings
        x = times
        listofzeros = [0] * len(earnings)
        ptt.plot(y,line_color='red')
        ptt.plot(listofzeros,line_color='green')
        ptt.ylim(-500, -250)
        ptt.grid(True)
        ptt.canvas_color("black")
        ptt.axes_color("black")
        ptt.ticks_color("cloud")
        ptt.show()

    def set_uni(self, data, time):
        y = data
        yo = time
        uni.plot(
                [y,yo], 
                lines=1, 
                x_gridlines=[10,20,30], 
                y_gridlines=[0,2,4,6,8,10]
                ) 

    def set_matplot(self, data, time):
        plt.plot(data)
        plt.ylabel('some numbers')
        plt.show()



