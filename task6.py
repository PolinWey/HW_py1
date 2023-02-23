"""Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за 
проезд и получали билет с номером. Счастливым билетом называют такой билет с 
шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. 
билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать 
программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no"""

num_ticket_i = int(input('Введите номер вашего билета: '))
num_ticket = str(num_ticket_i)
sum1 = int(num_ticket[0]) + int(num_ticket[1]) + int(num_ticket[2])
sum2 = int(num_ticket[3]) + int(num_ticket[4]) + int(num_ticket[5])
if sum1 == sum2:
    print('YES!')
elif sum1 != sum2:
    print('NO.')