# 一个简单的字典
alien_0 = {
    'color':'green',
    'points':5,
    'x_positon':0,
    'y_positon':25,
    }
print(alien_0['color'])
#创建一个空字典
alien_1 = {}
#添加键值对
alien_1['color'] = 'yellow'
print(alien_1['color'])
#修改值
alien_1['color'] = 'red'
print(alien_1['color'])
#删除键值对
del alien_1['color']
print(alien_1)
#遍历键值对
for key,value in alien_0.items():
    print('\nkey:'+key)
    print('value:'+str(value))

# 遍历键
alien_3 = {
    'jen':'python',
    'sarah':'c',
    'edward':'rubi',
    'phil':'python',
    }
#for name in alien_3.keys():
for name in alien_3:
    print('\n'+name.title())
#遍历所有值 (无重复值)
for languages in set(alien_3.values()):
    print('\n' + languages.title())
# 遍历所有键（按顺序）
print('.......')
for name in sorted(alien_3.keys()):
    print('\n'+name.title())
