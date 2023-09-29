import random

print("¿Quieres jugar a piedra, papel o tijera? (y/n)")
input(">")

card = ['Piedra','Papel','Tijera']

print("""Escribe que quieres: piedra, papel o tijera.
      Los dos sacaremos que hemos elegido.""")
print("¿List@? (y/n)")
input("¿Piedra, papel o tijera?>")

#mycard = card[]

def whatisit(election):
    if election == 0:
        print("Piedra")
    elif election == 1:
        print("Papel")
    elif election == 2:
        print("Tijera")

def computerelection():
    new_election = int(random.randint(0,2))
    print("My elección is:")
    whatisit(new_election)


computerelection()

