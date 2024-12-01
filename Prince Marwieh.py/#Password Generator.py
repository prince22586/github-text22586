# final project INFO 301 section 2 PRINCE MARWIEH ID 7908 - Password Gerenator

# Importing the relevant modules
from random import randint

# All uppercase password
password = ""
for i in range(5):
    i = chr(randint(65, 70))
    password = str(password) + i
print(password) 

# Upper and lowercase password
password = ""
for i in range(5):
    i = chr(randint(65, 70))
    for j in range(5):
        j = chr(randint(65, 70)).lower()
    password = str(password) + i + j
print(password)  