import random
import time

name = ''
i = 0

mood = 12
health = 5
eat_sat = 5
drink_sat = 5

class Animal:
     profit = 0
     name = ''

bear = Animal()
bear.name = 'Медведь'
bear.profit = 4

wolf = Animal()
wolf.name = 'Волк'
wolf.profit = 0

hare = Animal()
hare.name = 'Заяц'
wolf.profit = 1

boar = Animal()
boar.name = 'Кабан'
boar.profit = 2

elk = Animal()
elk.name = 'Лось'
elk.profit =  3

a_name = [bear.name,   wolf.name,   hare.name,   boar.name,   elk.name]
a_prof = [bear.profit, wolf.profit, hare.profit, boar.profit, elk.profit]

class Weapon:
     amount = 0
     value = 0
     hardness = 0
     name = ''

axe = Weapon()
axe.value = 15
axe.name = 'Топор'
axe.amount = 1

knife = Weapon()
knife.value = 6
knife.name = 'Нож'

bow = Weapon()
bow.value = 10
bow.name = 'Лук'

fist = Weapon()
fist.value = 3
fist.name = 'Кулак'
fist.amount = 2

w_name =   [axe.name,   knife.name,   bow.name,   fist.name]
w_amount = [axe.amount, knife.amount, bow.amount, fist.amount]
w_value =  [axe.value,  knife.value,  bow.value,  fist.value]

def Hunting(name, i,  mood, health, eat_sat, drink_sat):
     print(' ')
     print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
     print(' ')
     print('Вы вышли на охоту...')
     time.sleep(2)

     hunt_r = random.randint(1,100)                                             #Рандомное нахождение животных
     if hunt_r >= 0 and hunt_r <=60 :
          anim_r = random.randint(1,100)
          if anim_r >= 0 and anim_r <=10 :
               name = a_name[0]                                                 #Необходимые присваивания
               prof = a_prof[0]
               print('Вы нашли животное "'+name+'"')
               Hunting_dop(name, prof, i,  mood, health, eat_sat, drink_sat)
          elif anim_r > 10 and anim_r <=30 :
               name = a_name[1]
               prof = a_prof[1]
               print('Вы нашли животное "'+name+'"')
               Hunting_dop(name, prof, i,  mood, health, eat_sat, drink_sat)
          elif anim_r > 30 and anim_r <=50 :
               name = a_name[2]
               prof = a_prof[2]
               print('Вы нашли животное "'+name+'"')
               Hunting_dop(name, prof, i,  mood, health, eat_sat, drink_sat)
          elif anim_r > 50 and anim_r <=80 :
               name = a_name[3]
               prof = a_prof[3]
               print('Вы нашли животное "'+name+'"')
               Hunting_dop(name, prof, i,  mood, health, eat_sat, drink_sat)
          elif anim_r > 80 and anim_r <=100 :
               name = a_name[4]
               prof = a_prof[4]
               print('Вы нашли животное "'+name+'"')
               Hunting_dop(name, prof, i,  mood, health, eat_sat, drink_sat)
     else:
          print('Вы ничего не нашли...')
          #time.sleep(2)
          #Menu(date_g, time_g)
     
def Hunting_dop(name, prof, i,  mood, health, eat_sat, drink_sat):              #Основная функция
     print(' ')
     print('1. Атаковать')
     if i < 2 :
          print('2. Преследовать') 
          print('3. Ждать')                                                     #    Ловушка для обмащика  
          print('')                                                             #Нельзя "Ждать" и "Преследовать" больше 2 раз 
     i +=1                                                                                
     ch_n = input('Введите номер желаемого действия: ')                         #Обработка ввода
     if ch_n == '1' :
          print('Вы атаковали животное "'+name+'"')
          Fighting(name, prof,  mood, health, eat_sat, drink_sat)
     elif ch_n == '2' :
          attack_r1 = random.randint(1,100)
          if attack_r1 > 80 and attack_r1 <= 100:                               #С вероятностью 20% животное
               print('Вы были атакованы животным "'+name+'"')                   #    может вас атаковать
               Fighting(name, prof,  mood, health, eat_sat, drink_sat)
          else:
               wait = random.randint(5,10)
               print('')
               print('Вы преследовали животное '+str(wait)+' минут')
               print('За это время ничего не произошло.')
               Hunting_dop(name, prof, i,  mood, health, eat_sat, drink_sat)
     elif ch_n == '3' :
          attack_r2 = random.randint(1,100)
          if attack_r2 > 70 and attack_r2 <= 95:                               #С вероятностью 20% животное 
               print('Вы были атакованы животным "'+name+'"')                  #    может вас атаковать
               Fighting(name, prof,  mood, health, eat_sat, drink_sat)
          elif attack_r2 > 95 and attack_r2 <= 100:
               print('Животное ушло')
          else:
               wait = random.randint(5,10)
               print('')
               print('Вы выждали '+str(wait)+' минут')
               print('За это время ничего не произошло.')
               Hunting_dop(name, prof, i,  mood, health, eat_sat, drink_sat)

def Fighting(name, prof,  mood, health, eat_sat, drink_sat) :                   #Собственно сам файтинг
     print(' ')
     print('Выберите оружие: ')
     print(' ')

     out_f = 0
     
     for y in range(4):                                                         #Основной список
          if w_amount[y] > 0 :
               out_f += 1
               print(str(out_f)+'. '+str(w_name[y]))
               print('Мощность: '+str(w_value[y]))
               print('Кол-во: '+str(w_amount[y])+'шт.')
               print(' ')

     ch_n = input('Введите номер выбранного оружия: ')
     if ch_n == '' or int(ch_n) < 0 or int(ch_n) > 4:                           #Проверка на правильность ввода
          print('Вы ввели неправильное значение!')
          time.sleep(2)
          Fighting(name, prof,  mood, health, eat_sat, drink_sat)
          
     wep = w_name[int(ch_n)-1]

     print('  ')
     print('Бой начинается!..')
     print('  ')
     time.sleep(2)
     vic_rand = random.randint(0,100)                                           #Определение вероятности выигрыша
     if wep == 'Топор':                                                         #   c разными типами оружия
          wep_fact = 10
     elif wep == 'Лук':
          wep_fact = 5
     elif wep == 'Нож':
          wep_fact = 20
     elif wep == 'Кулак':
          wep_fact = 40
          
     if vic_rand < wep_fact:                                                    #Исход битвы
          end_h = random.randint(1, 10)
          if end_h >= 1 and end_h <= 5 :
               print('Вы были повержены и бежали...')
               
               eat_sat += 5                                                     #Необходимые изменения
               drink_sat += 5
               mood -= 5
               
          elif end_h > 5 and end_h <= 10:
               print('Игра окончена.')
               print('Вы проиграли!')
               #Final()
               
     if vic_rand >= wep_fact:
          end_a = random.randint(1, 10)
          if end_a >= 1 and end_a <= 3 :
               print('Ваш противник "'+name+'" был повержен и бежал...')
          elif end_a > 3 and end_a <= 10:
               print('Вы победили!')
               print('Вы получили '+str(prof)+'(кг) мяса.')

          eat_sat += 3                                                          #Необходимые изменения X2
          drink_sat += 3
          mood += 4
     
     time_h = 2 + random.randint(0,3)
     time_m = random.randint(14,31)
          
     '''if i >= 1 :
          tl = Time(tl[0], tl[1], tl[2], tl[3], tl[4], tl[5], tl[6], tl[7])
          time.sleep(2)
     else:
          tl = Time(hour, mint, day, mon, time_m, time_h, time_gl, date_gl)
          time.sleep(2)
     i += 1'''
     
     time.sleep(2)
     #Menu(date_g, time_g)                                                      #Выход
     
          
Hunting(name, i,  mood, health, eat_sat, drink_sat)   
