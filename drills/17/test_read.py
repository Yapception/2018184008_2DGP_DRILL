# f = open('data.txt', 'r')
# data_str = f.read()
# f.close()
#
# print(data_str)
# # data_str 은 str이기때문에 내부 데이터로의 변환을 해야하는 작업이 필요. parsing 이 필요함.

import json

with open('data.json', 'r') as f:
    data = json.load(f)

print(type(data))
print(data)
