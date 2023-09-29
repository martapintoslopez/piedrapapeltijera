import random

print("¿Quieres jugar a piedra, papel o tijera? (y/n)")
play = input(">")
while play == 'y':
    cards = ['piedra','papel','tijera']

    print("""Escribe que quieres: 
          piedra, papel o tijera.""")
    yourword = input(">")
    if yourword in cards:
        print(f"""\t\tHas elegido:
        \t\t {yourword}""")
        yourwordvalue = cards.index(yourword)
        
        #Función para que devuelva la palabra que elige la computadora
        def whatisit(election):
            print(f"\t\t\t {cards[election]}")
            if yourwordvalue < election:
                print(f"""A ver... {cards[election]} gana a {yourword}
                        ¡TE HE GANADO!""")
            elif yourwordvalue > election:
                print(f"""A ver... {yourword} gana a {cards[election]}
                      ¡ME HAS GANADO!""")
            else:
                print("\t\t\t\tIguales, empatamos")

        def computerelection():
            new_election = int(random.randint(0,2))
            print("\t\tMi elección es:")
            print(new_election)
            whatisit(new_election)

        computerelection()
    
    else:
        print("No te he entendido")

    print("¿Quieres jugar de nuevo? (y/n)")
    play = input(">")

print("Bye!")