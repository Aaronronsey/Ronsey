Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name = 'Ronsey'
print(name)
Ronsey
type(name)
<class 'str'>
name.lower()
'ronsey'
name.higher()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    name.higher()
AttributeError: 'str' object has no attribute 'higher'
name.upper()
'RONSEY'
friend = 'narong'
print('สวัสดีnarong สบายดีไหม')
สวัสดีnarong สบายดีไหม
print('สวัสดี,'friend',สบายดีไหม)
      
SyntaxError: unterminated string literal (detected at line 1)
print('สวัสดี,friend,สบายดีไหม)
      
SyntaxError: incomplete input
print('สวัสดี'+friend+'สบายดีไหม')
      
สวัสดีnarongสบายดีไหม













print('narong ยืมเงิน 10 บาท)
      
SyntaxError: incomplete input
print('narong ยืมเงิน 10 บาท')
      
narong ยืมเงิน 10 บาท
money = 10
      
print(friend + 'ยืมเงิน' + money + 'บาท')
      
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(friend + 'ยืมเงิน' + money + 'บาท')
TypeError: can only concatenate str (not "int") to str
type(money)
      
<class 'int'>
print(friend +'ยิมเงิน' + str(money) +'บาท')
      
narongยิมเงิน10บาท
print('{}ยืมเงิน {} บาท'.format(friend,money))
      
narongยืมเงิน 10 บาท
print(f' {friend} ยืมเงิน {money} บาท')
      
 narong ยืมเงิน 10 บาท
money = 168080293
      
print(f' {money:,}')
      
 168,080,293
print(f' {money:,.2f}')
      
 168,080,293.00
print('{:,.2f}'.formet(money))
      
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print('{:,.2f}'.formet(money))
AttributeError: 'str' object has no attribute 'formet'. Did you mean: 'format'?
print('{:,.2f}'.format(money))
      
168,080,293.00
import math
math.pi
3.141592653589793
math.pi * 20^2
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    math.pi * 20^2
TypeError: unsupported operand type(s) for ^: 'float' and 'int'
math.pi *(20**)
SyntaxError: incomplete input
math.pi(20** 2)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    math.pi(20** 2)
TypeError: 'float' object is not callable
math.pi * (20**2)
1256.6370614359173
>>> fron datetime import datetime
SyntaxError: invalid syntax
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2023, 3, 2, 9, 6, 41, 634719)
>>> datetime.now().strftime('%Y%M%D %H:%M:%S')
'20230703/02/23 09:07:55'
>>> import random
>>> random.randint (1,7)
1
>>> store = ['ป้าส้ม','ป้าเล็ก','ลุงหยอย']
>>> random.randint(store)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    random.randint(store)
TypeError: Random.randint() missing 1 required positional argument: 'b'
>>> random.choice(store)
'ป้าส้ม'
