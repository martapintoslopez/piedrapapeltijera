import random

print("¿Quieres jugar a piedra, papel o tijera? (y/n)")
input(">")

print("""Cuento hasta tres y escribes que quieres: piedra, papel o tijera.
      Los dos sacaremos a la vez que hemos elegido.""")
print("¿List@? (y/n)")
input(">")

Card = ['Piedra','Papel','Tijera']


def whatisit(election):
    if election == 0:
        print("Piedra")
    elif election == 1:
        print("Papel")
    elif election == 2:
        print("Tijera")

def computerelection():
    new_election = int(random.randint(1,3))
    print(new_election)



computerelection()

