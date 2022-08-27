 import random
 upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 lower="abcdefghijklmnopqrstuvwxyz"
 numbers="0123456789"
 symbols="[]{}()*;/,._-"
 all=lower+upper+symbols
 length=16  //length of the password
 password="".join(random.sample(all,length))
 print(password)
