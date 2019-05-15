import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#-----------------1-------------
mpg= pd.read_csv('c:/Users/User/Desktop/Python/ClassAct11/mpg.csv')

#-------------2------------
mpg["force"]= mpg["weight"]*mpg["acceleration"]
mpg

#--------------3-----------
origin=mpg[(mpg.origin=='japan') & (mpg.cylinders==4)] 
origin

#-------------4-------------
mpg["weight"].corr(mpg["acceleration"])

#---------------------------5---------------
model_year=mpg[(mpg.model_year<80) & (mpg.horsepower>=200)]  
#model_year=mpg[mpg.model_year==82]  
model_year


plt.plot(model_year.horsepower,model_year.mpg,'o',color="green")
plt.xlabel('Horsepower greater than 200')
plt.ylabel('Miles per gallon')
plt.title('Miles per gallon for cars before the year 1980 with a horsepower greater than 200')
plt.show()
