from decimal import Decimal, getcontext
import math
import time
import os
import sys
import colorama
from colorama import Fore
colorama.init()
os.system('clear')
print("Let's Calculate Pi!")

numberofdigits = int(input("Please enter the number of decimal place to calculate Pi to: "))
getcontext().prec = numberofdigits

def fn_os():
    curr_os=sys.platform
    print ("Your PC is running:", curr_os)

start_time = time.time()
def calc(n):
    t = Decimal(0)
    pi = Decimal(0)
    deno = Decimal(0)
    k = 0
    for k in range(n):
     t=(Decimal(-1)**k)*(math.factorial (Decimal(6)*k))*(13591409 +545140134*k)
     deno = math.factorial(3*k)*(math.factorial(k)**Decimal(3))*(640320**(3*k))
     pi += Decimal(t)/Decimal(deno)
    pi = pi * Decimal(12)/Decimal(640320**Decimal(1.5))
    pi = 1/pi
    return str(pi)

print(Fore.GREEN + calc(1))
print(Fore.RED + "\nTime taken to calculate:", time.time() - start_time)
print(Fore.BLACK + "")
print("System Info:")
print("------------------------------")
print ("Your PC has", os.cpu_count(), "CPU's")
fn_os()
print ("Your Python Version is:",sys.version[0:5])
