

import fileinput

user_dict = {}
for f in fileinput.input('../contact.csv'):
    if fileinput.isfirstline():
        continue
    data = f.split(',')
    member_id = data[1]
    tel = data[3]
    member_data = user_dict.get(member_id)
    if not member_data:
        member_data = [0, 0]
    if len(tel) > 9:
        if tel[:3] == '639':
            member_data[0] += 1
        else:
            member_data[1] += 1

    user_dict.update({member_id: member_data})


with open('../conatct2.csv', 'a+') as ff:
    ff.seek(0) # 读取文件后，将游标重新指向起始位置
    ff.truncate()  # 清空游标之后的所有内容
    for k, v in user_dict.items():
        ff.write('{},{},{}\n'.format(k, v[0], v[1]))
