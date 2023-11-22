import csv
import json
import demjson3

# with open('/Users/dm.osipenko/Полезное/py114_Dmitry/lesson_14/new.txt', 'r') as file:
#     text = file.readlines()
#     for item in text:
#         result = len(item.strip().replace('_',''))
#         print(f'Count {len(text)}, {result}')


# a = 20
# b = 10
#
# res = a if a > b else b
# print(f'Большее значение {res}')

# my_f = open('example.csv')
# my_reader = csv.reader(my_f, delimiter=' ')
# data = list(my_reader)
# print(data)

# f = open('data.csv','w', newline='')
# data_writer = csv.writer(f,delimiter=';')
# my_data = [['20.11', 'python', '15'], ['21.11', 'swift', '10'], ['22.11', 'C++', '14']]
#
# for item in my_data:
#     data_writer.writerow(item)
# f.close()

# my_str = '{"id": 1, "name": "Dima", "age": 31}'
# data = json.loads(my_str)
# print(type(data))
# print(data['age'])

with open('data.json','r') as file:
    data = json.load(file)
    print(data)
print('*********')
# my_dict = {"id":11, "phone":123, "addr":'Минск'}
# my_s = json.dumps(my_dict)
# print(my_s,type(my_s))
# my_s = json.dumps(my_dict, ensure_ascii=False)
# print(my_s)
#
# my_dict1 = {"id":11, "phone":123, "addr":'Минск'}
# with open('data_dick_1.json', 'w') as f:
#     json.dump(my_dict1,f)
#
#     with open('data_dick_1_true.json', 'w') as f:
#         json.dump(my_dict1, f, ensure_ascii=False)




# ss = {'id':1}
# print(demjson3.encode(ss))

