import random
lower = "abcdefghijklmnñopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
NUMBER = "0123456789"
Symbol = "[]{+}#()*;.<>@'_~!?/^¿¡$%¨!·€"
all = lower + upper + NUMBER + Symbol
length = 16
password = "".join(random.sample(all, length))
print ("The password you generate is:", password)