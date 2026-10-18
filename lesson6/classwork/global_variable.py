pet = 'cat'

def show_pet():
   print ("the pet is a ", pet)

show_pet()

# def adopt_dog():
#   print ("the old pet is a ", adopt_dog)
# pet = 'dog'

# adopt_dog()

def adopt_parrot(): 
   global pet 
   pet = 'parrot'

adopt_parrot()
show_pet()


