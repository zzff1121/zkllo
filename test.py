# num = [0, 1, 2, 3, 4, 5, 6, 7]
# num_1 = 0
# str_1 = 'zff'
# zff(num_1)

# num_list = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
#
# # for i in range(5):
# #     for j in range(5):
# #         num_list[i][j] = i*j
# for num in num_list:
#     for i in range(len(num)):
#         print(num[i])
# print(num_list)

# str_1 = ' zhe shi yi ge zi fu c'
# print(len(str_1))
# num = str_1.index('h')
# print(num)
# str_2 = str_1.replace('yi', 'liang')
# print(f'{str_2}')
# list_1 = str_1.split(' ')
# print(list_1)
# print(type(list_1[0]))
# str_3 = str_1.strip()
# print(str_3)
# num = str_1.count(' ')
# print(num)
# print(str_1)

# set_1 = {5, 4, 1, 3, 4, 5}
# num = set_1.pop()
# print(num)
# print(type(set_1))

# def zff(**kwargs):
#     print(f"{kwargs}")
#
#
# zff(name='zhangfeifan', age=24)


# f = open('D:/Python/ProjectCollection/a.txt', 'w', encoding='UTF-8')
#
# f.close()

# import pyecharts
#
# line = pyecharts.charts.Line()
#
# line.add_xaxis(['x', 'y', 'z', 'w'])
#
# line.add_yaxis('age', [24, 22, 21, 20])
#
# line.render()


# 连接数据库
from pymysql import Connection


conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456'
)

print(conn.get_server_info())

conn.close()


