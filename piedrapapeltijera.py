import random

print("¿Quieres jugar a piedra, papel o tijera? (y/n)")
play = input(">")
while play == 'y':
    cards = ['piedra','papel','tijera']

    print("""Escribe que quieres: 
          piedra, papel o tijera.""")
    yourword = input(">")
    if yourword in cards:
        print(f"Has elegido:{yourword}")
            
        #yourcard = card[]
        #print(card[1])

        #Función para que devuelva la palabra (cambiar para usar la lista)
        def whatisit(election):
            if election == 0:
                print("Piedra")
            elif election == 1:
                print("Papel")
            elif election == 2:
                print("Tijera")

        def computerelection():
            new_election = int(random.randint(0,2))
            print("Mi elección es:")
            whatisit(new_election)

        computerelection()

    #FALTA LA PARTE DE COMPARAR Y VER QUIÉN GANA
    
    else:
        print("No te he entendido")

    print("¿Quieres jugar de nuevo? (y/n)")
    play = input(">")