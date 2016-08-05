import time

sleep_sat = 5
mood = 5
health = 5

def Sleeping(sleep_sat, mood, health):
     sleep_need = round((20 - sleep_sat) / 2,5)
     
     print(' ')
     print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
     print(' ')
     
     if sleep_sat == 20 :
          print('Вы не хотите спать!')
     else:
          print('Вы решили лечь спать...')
          print('Чтобы выспаться, вы должны проспать '+str(sleep_need)+' часов')
          print(' ')
          time.sleep(2)

     time_h = sleep_need
     print('Вы проспали '+str(time_h)+' часов')

     sleep_sat += 20 - sleep_sat
     mood += 4
     health += 3

     '''if i >= 1 :
          tl = Time(tl[0], tl[1], tl[2], tl[3], tl[4], tl[5], tl[6], tl[7])
          time.sleep(2)
     else:
          tl = Time(hour, mint, day, mon, time_m, time_h, time_gl, date_gl)
          time.sleep(2)
     i += 1'''
     
     time.sleep(2)
     #Menu()
     
Sleeping(sleep_sat, mood, health) 
