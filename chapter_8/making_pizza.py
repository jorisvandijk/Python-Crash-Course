 # 1. Imports enrire pizza.py module
#import pizza

# 2. Imports only one function from pizza.py, make_pizza
#from pizza import make_pizza

# 3. Import a function and give it an alias:
#from pizza import make_pizza as mp

#4. Import module as an alias:
import pizza as p

# 1. Functipon calls for importing the entire pizza file:
#pizza.make_pizza("large", 'olive')
#pizza.make_pizza("medium", 'extra cheese', 'green peppers')

# 2. Function calls when only importing the single function:
#make_pizza("large", 'olive')
#make_pizza("medium", 'extra cheese', 'green peppers')

# 3. Function calls when only importing the single function with alias:
#mp("large", 'olive')
#mp("medium", 'extra cheese', 'green peppers')

# 4. Function calls when importing module as an alias:
p.make_pizza("large", 'olive')
p.make_pizza("medium", 'extra cheese', 'green peppers')
