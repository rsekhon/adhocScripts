#!/usr/bin/python3

#import this
import numpy as np

def meanExample() :
   costs = np.column_stack(([2, 1, 2, 1],
                            [4, 6, 5, 5]))

   mean_costs = np.mean(costs[:,1])

   print(mean_costs)

def sortExample() :
  p = [0, 5, 15, 5, 10, 8]
  print(sorted(p, reverse=False))


def deleteExample() :
  p = ['j', 'x', 'n', 'k', 'e', 'x']
  del(p[3:5])
  print(p)

def listPlusExample() :
  print([1, 0 , 1] + [2, 4, 6])

def numpyExample() :
  import numpy as np

  store = np.array([0,9,0,1])
  cost  = np.array([82, 82, 73, 73])
  np_cols = np.column_stack((store, cost))
  print(np_cols)

def featherExample() :
  import feather
  import pandas as pd 
  import numpy as np
  arr = np.random.randn(10000000) # 10% nulls
  arr[::10] = np.nan
  df = pd.DataFrame({'column_{0}'.format(i): arr for i in range(10)})
  feather.write_dataframe(df, 'test.feather')


#meanExample()
#sortExample()
#deleteExample()
#listPlusExample()
#numpyExample()
featherExample()
