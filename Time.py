import time
a = 1
i = 0
tlis = []

day = 10
mon = '06'
hour = 12
mint = 0
time_m = 20
time_h = 0
date_gl = ''
time_gl = ''

def Time(hour, mint, day, mon, time_m, time_h, time_gl, date_gl):
     mint = mint + time_m
     hour = hour + time_h

     if (mint > 59):
          mint = mint - 60
          hour += 1
     
     if (hour > 24):
          hour = hour - 24
          day += 1

     tlis = [hour, mint, day, mon, time_m, time_h, time_gl, date_gl]

     if tlis[1] < 9:
          mn_str = '0'+str(tlis[1])
          time_gl = str(tlis[0]) + ':' + mn_str
          date_gl = str(tlis[2]) + '.' + str(tlis[3])
     else:
          time_gl = str(tlis[0]) + ':' + str(tlis[1])
          date_gl = str(tlis[2]) + '.' + str(tlis[3])
          
     print(time_gl)
     print(date_gl)
     print('  ')

     return tlis


if i >= 1 :                                                 
     tl = Time(tl[0], tl[1], tl[2], tl[3], tl[4], tl[5], tl[6], tl[7])          #вставка
     time.sleep(2)
else:
     tl = Time(hour, mint, day, mon, time_m, time_h, time_gl, date_gl)
     time.sleep(2)
     i += 1
