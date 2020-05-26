# [0-9]{1,2}[\/]{1}[0-9]{1,2}[,\/]{1}[0-9]{4}

import os
import re

regex = re.compile(r'[0-9]{1,2}[\/]{1}[0-9]{1,2}[,\/]{1}[0-9]{4}')
os.listdir(".")
sciezka_folder=os.listdir("../Python_Bootcamp/Daty")
print(sciezka_folder)

tescik_sciezka=sciezka_folder[0]

file=str(sciezka_folder[0])
file=os.path.join("../Python_Bootcamp/Daty", file)
print(file)
with open(file, "r") as f:
    for line in f:
        pattern = regex.findall(line)
        for word in pattern:
            print(word)
