import json
print(dir(json))

json_file1 = open("jswannie1.json", "r", encoding="UTF-8")
data = json.load(json_file1)
json_file1.close()

print(type(data), data)
print(data["quiz"]["sport"]["q1"]["question"])
print(data["quiz"]["sport"]["q1"]["answer"])
print(data["quiz"]["sport"]["q1"]["options"])
print(data["quiz"]["maths"]["q1"]["question"])
print(data["quiz"]["maths"]["q1"]["answer"])

dumpy = json.dumps(data)

print(dumpy)

file2 = """{"car_type": "BMW", "country": "Germany", "question1": true, "max_speed": 328}"""

data2 = json.loads(file2)

print(data2)
