import time

eat_sat = 10
mood = 0
health = 0

class Food() :
     value = 0
     amount = 0
     name = ' '

fry_meat = Food()
fry_meat.value = 5
fry_meat.name = 'Жареное мясо'

row_meat = Food()
row_meat.value = 4
row_meat.name = 'Сырое мясо'

canned_food = Food()
canned_food.value = 4
canned_food.name = 'Консервы'
canned_food.amount = 1

berries = Food()
berries.value = 3
berries.name = 'Ягоды'
berries.amount = 2

f_amount = [fry_meat.amount, row_meat.amount, canned_food.amount, berries.amount]
f_name   = [fry_meat.name,   row_meat.name,   canned_food.name,   berries.name]
f_value  = [fry_meat.value,  row_meat.value,  canned_food.value,  berries.value]

fn_list = []
fv_list = []
fa_list = []

f_sum = 0
out_f = 0

def Eating(eat_sat, f_sum, out_f, mood, health):
     eat_need =(25 - eat_sat) / 5
     
     print(' ')
     print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
     print(' ')
     print('Чтобы наесться, вы должны съесть: '+str(eat_need)+'(кг)')
     print(' ')

     for x in range(4):
          f_sum += f_amount[x]                                   #общее кол-во пищи

     if f_sum > 0 :                
          print('У вас есть:')                                   #проверка на пустоту склада
          print(' ')
     else :
          print('У вас нет еды!')
          time.sleep(2)
          #Menu(date_g, time_g)

     for y in range(4):                                          #основной список
          if f_amount[y] > 0 :
               out_f += 1
               print(str(out_f)+'. '+str(f_name[y]))
               print('Питательность: '+str(f_value[y]))
               print('Кол-во: '+str(f_amount[y])+'кг')
               print(' ')
               fn_list.append(f_name[y])
               fv_list.append(f_value[y])
               fa_list.append(f_amount[y])

     ch_n1 = input('Введите номер выбранного продукта: ')
     if int(ch_n1) < 0 or int(ch_n1) > 4 :                       #проверка на правильность ввода
          print('Вы ввели неправильное значение!')
          time.sleep(2)
          #Menu(date_g, time_g)
          
     ch_n2 = input('Введите кол-во выбранного продукта(кг): ')   #защита от обманщика
     if int(ch_n2) < 0 or int(ch_n2) > fa_list[int(ch_n1)-1]:
          print('Вы ввели неправильное значение!')
          time.sleep(2)
          #Menu(date_g, time_g)

     fn = fn_list[int(ch_n1)-1]
     
     print(' ')
     print('Вы съели '+ch_n2+'кг продукта "'+fn+'"')

     fv = fv_list[int(ch_n1)-1] * int(ch_n2)
     eat_sat = eat_sat + fv                                      #необходимые изменения
     mood = mood + 4
     health = health + 3
     time_m = 30
     '''if i >= 1 :
          tl = Time(tl[0], tl[1], tl[2], tl[3], tl[4], tl[5], tl[6], tl[7])
          time.sleep(2)
     else:
          tl = Time(hour, mint, day, mon, time_m, time_h, time_gl, date_gl)
          time.sleep(2)
     i += 1'''
          
     time.sleep(2)
     #Menu(date_g, time_g)                                       #выход
     
Eating(eat_sat, f_sum, out_f, mood, health)
