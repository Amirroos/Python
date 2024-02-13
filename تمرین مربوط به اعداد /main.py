# شعاع دایره را بگیرد  محیط و مساحت ان را حساب کند
# محیط:
from math import pi
x = int(input("Inter a number for circle :"))
x = x * 2 * pi
print(x)
#مساحت:
from math import pi 
x = int(input("Inter a number for circle :"))
x = pow(x,2)*pi
print(x)
# برنامه ای بنویسید ک از کاربر یه عدد را گرفته و مربع و مکعب ان را حساب کند
x = int(input("Inter number :"))
b = pow(x,2)
print("The square is :",b)
x = pow(x,3)
print("The cube is :",x)
# برنامه ای بنویسید ک دو عدد را از کاربر گرفته و اولی را به توان دومی برساند 
x = int(input("Inter first number :"))
b = int(input("Inter second number :"))
z = pow(x,b)
print(z)
# برنامه بنویسید ک سه عدد را از کاربر گرفته و میانگین ان هارا حساب کند
x = int(input("Inter first number :"))
x += int(input("Inter second number :"))
x += int(input("Inter third number :"))
x /= 3
print(x)