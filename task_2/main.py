#Ввод данных 
n = int(input("Введите количество школьников: "))
k = int(input("Введите количество яблок: "))
№Расчет кол-ва яблок на каждого школьника 
apples_per_student = k // n 
#Расчет остатка яблок в корзине
apples_left = k % n 
#Вывод результата
print(apples_per_student)
print(apples_left)
