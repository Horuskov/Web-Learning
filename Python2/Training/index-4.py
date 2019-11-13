# Module: organize section in a Python file
import converter  # converter is a file into the folder
from converter import lbs_to_kg  # import a specific function from the selected file

print(lbs_to_kg(100))

print(converter.kg_to_lbs(70))

# Package: a bunch of modules
import ecommerce.shipping
# from ecommerce.shipping import calculate_shipping, calc_tax
# from ecommerce import shipping

ecommerce.shipping.calculate_shipping()

# Random
import random

for i in range(3):
    print(random.randint(10, 20))

members = ["Joe", "Avrel", "William"]
leader = random.choice(members)
print(leader)


# Working with directories
import path from Path

# Absolute path: from the hard drive comme :c\Program Files...
# Relative path: from a closer location

path = Path("ecommerce")
print(path.exists())