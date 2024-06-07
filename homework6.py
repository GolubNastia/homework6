my_dict = {'Имя' : 'Саша', 'Год рождения' : 1987}
print(my_dict)
print(my_dict['Имя'])
print(my_dict.get('Фамилия', 'Такого значения нет'))
my_dict.update({'Фамилия': 'Петров', 'Страна рождения' : 'Россия'})
print(my_dict)
a = my_dict.pop('Фамилия')
print(a)

my_set = {1, 2, 'Non', 1, 2, 'Non', True, (5, 8, 3)}
print(my_set)
my_set.update({'666', 'New'})
print(my_set)
my_set.discard('New')
print(my_set)