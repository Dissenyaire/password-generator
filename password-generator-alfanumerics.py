"""
Code with less symbols
"""
import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER = "0123456789"
Symbol = "+#*;.<>@_~!?/¿¡$%!€"
all = lower + upper + NUMBER + Symbol
length = 16
password = "".join(random.sample(all, length))
print ("The password you generate is:", password)