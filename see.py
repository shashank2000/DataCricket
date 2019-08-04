import yaml
import os

dataMap = []
i = 0
for filename in os.listdir('ipl'):
    i += 1
    if (i % 100 == 0):
        print(i)
    if filename.endswith(".yaml"): 
         with open('ipl/' + filename) as f:
                dataMap.append(yaml.safe_load(f))
    else:
        continue

print(dataMap)
