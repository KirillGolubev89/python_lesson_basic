# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruit_list1 = ['яблоко', 'груша', 'апельсин', 'банан']
fruit_list2 = ['яблоко', 'груша', 'банан']

new_list = [fruit for fruit in fruit_list1 if fruit in fruit_list2]

print(new_list)
