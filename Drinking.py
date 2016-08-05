import time

drink_sat = 10
drink_amount = 10
mood = 0
health = 0

def Drinking(drink_sat, drink_amount, mood, health) :
     drink_need = (25 - drink_sat) / 5

     print(' ')
     print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
     print(' ')
     print('Чтобы напиться, вы должны выпить: '+str(drink_need)+'(кг)')

     if  drink_amount > 0 :                
          print('У вас есть '+str(drink_amount)+'(л) воды')                    #проверка на пустоту склада
          print(' ')
     else :
          print('У вас нет воды!')
          time.sleep(2)
          #Menu(date_g, time_g)

     ch_n = input('Введите кол-во воды, которое вы хотите выпить: ')
     if int(ch_n) < 0 or int(ch_n) > drink_amount :                             #проверка на правильность ввода
          print('Вы ввели неправильное значение!')
          time.sleep(2)
          #Menu(date_g, time_g)

     print(' ')
     print('Вы выпили '+ch_n+'(л) воды.')

     dv = ch_n
     drink_sat += dv                                                            #необходимые изменения
     mood += 4
     health += 3
     time_m = 30
     
     """if i >= 1 :
          tl = Time(tl[0], tl[1], tl[2], tl[3], tl[4], tl[5], tl[6], tl[7])
          time.sleep(2)
     else:
          tl = Time(hour, mint, day, mon, time_m, time_h, time_gl, date_gl)
          time.sleep(2)
     i += 1"""

     time.sleep(2)                                                              #выход         
     #Menu(date_g, time_g)

Drinking(drink_sat, drink_amount, mood, health)
