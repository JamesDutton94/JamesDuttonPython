#James Dutton
#ECE492 Final Project Driver
import numpy as num
import ystockquote as ys
import urllib

#get list of stocks
F = open("stocks.txt","r")
#create lists used throughout program
stocks = []
stockOpen = []
stockClose = []
stockDChange = []

#create list from stock document, use rstrip to remove \n
#for i in F:
 #   stocks.append(i.rstrip())
    
  #  stockDChange.append((ys.get_change(i.rstrip())))
#for i in 30:
 #   stockOpen[i] = stockDchange[i] + ys.get_price()
print ys.get_today_open('GOOG')

  



