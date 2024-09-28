import os
os.system("clear")
from OptionAndTarget import *

import random, time

while True:
    random_element = random.choice(Option)+' '+random.choice(Option)+' '+random.choice(Option)+'.'
    log = random.choice(Target)
    if random_element == log:
        print(random_element)
        time.sleep(1)