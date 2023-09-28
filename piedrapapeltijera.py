import random

print("¿Quieres jugar a piedra, papel o tijera? (y/n)")
input(">")

print("""Cuento hasta tres y escribes que quieres: piedra, papel o tijera.
      Los dos sacaremos a la vez que hemos elegido.""")
print("¿List@? (y/n)")
input(">")

def whatisit(election):
    if election == 1:
        print("Piedra")
    elif election == 2:
        print("Papel")
    elif election == 3:
        print("Tijera")

def computerelection():
    new_election = int(random.randint(1,3))
    print(new_election)



computerelection()

