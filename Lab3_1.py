import http.client
import json


# Определение операции
def operation_definition(res, old_res):
    if resp_json['operation'] == "sum":
        return old_res + res
    if resp_json['operation'] == "div":
        return old_res / res
    if resp_json['operation'] == "sub":
        return old_res - res
    if resp_json['operation'] == "mul":
        return old_res * res


# Подключаюсь к серверу
conn = http.client.HTTPConnection("167.172.172.227:8000")
# Задание 1
conn.request('GET', '/number/11', )
r1 = conn.getresponse().read().decode()
resp1_json = json.loads(r1)
print(r1)
print(resp1_json['number'])
# Задание 2
conn.request('GET', '/number/?option=11', )
r2 = conn.getresponse().read().decode()
resp_json = json.loads(r2)
print(r2)
print(resp_json['number'])
res1 = operation_definition(int(resp_json['number']), int(resp1_json['number']))
print("Результат выполнения операции:", int(res1))
# Задание 3
headers = {'Content-type': 'application/x-www-form-urlencoded'}
conn.request('POST', '/number/', 'option=11', headers)
r3 = conn.getresponse().read().decode()
resp_json = json.loads(r3)
print(r3)
print(resp_json['number'])
res2 = operation_definition(resp_json['number'], int(res1))
print("Результат выполнения операции:", int(res2))
# Задание 4
headers = {'Content-type': 'application/json'}
body = json.dumps({'option': 11})
conn.request('PUT', '/number/', body, headers)
r4 = conn.getresponse().read().decode()
resp_json = json.loads(r4)
print(r4)
print(resp_json['number'])
res3 = operation_definition(resp_json['number'], int(res2))
print("результат выполнения операции: ", int(res3))
# Задание 5
body = json.dumps({'option': 11})
conn.request('DELETE', '/number/', body)
r5 = conn.getresponse().read().decode()
resp_json = json.loads(r5)
print(r5)
print(resp_json['number'])
res4 = operation_definition(resp_json['number'], int(res3))
print("результат выполнения операции: ", int(res4))
conn.close()
