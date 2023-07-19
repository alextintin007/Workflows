import random
from recid_list import RECID_INFO

unique_values = list(set(RECID_INFO.values()))
random_value = random.choice(list(RECID_INFO.values()))

print(random_value)