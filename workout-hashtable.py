
from lib2to3.pgen2 import token


weather_dic={}
with open("sample.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day=tokens[0]
        try:
            temperature = int(tokens[1])
            weather_dic.__setitem__(day,temperature)
            
        except:
            print("Invalid temperature.Ignore the row")


print(weather_dic['Jan 4'])