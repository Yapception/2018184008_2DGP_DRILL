import json

data = {'x': 10, 'y': 20, 'size': 1.5}
# f = open('data.txt', 'w')
# f.write(str(data))
# f.close()
with open('data.json', 'w') as f:
    json.dump(data, f)
