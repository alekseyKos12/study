id_employee = {"Anton": 333,"Denis": 334, "Andrey": 434} # словарь
print(id_employee)
print(id_employee["Denis"])
print(id_employee.get("Sergey", 'Сотрудник не найден'))# get возвращает значение по указанному ключу
id_employee.update({'Slava': 545,
                    'alex': 656})# update принимает другой словарь , обновить или добавить несколько ключей
dismissed = id_employee.pop('Andrey')# pop удаляет ключ , но оставляет его значение , работает со списком
print(dismissed, 'свободный ID')
print(id_employee)
print(id_employee.keys())# отоброжение только ключей
print(id_employee.values())# отображение значение ключей
print(id_employee.items())# отоброжает ключ и значение

my_set = {10, 12, 13.4, 14, True, 10, 12, 13.4, 14, True,}
print(my_set)
list = (1, 2, 3, 4)
my_set.add(list)
my_set.add('number')
my_set.remove(10)
print(my_set)
