import json

x = '{"name":"Praveen","Age":"37","City":"Trichy"}'

y = json.loads(x)

for b in y.values():
    print(b)


# open the file
with open(r"sample-json-file.csv") as js:
