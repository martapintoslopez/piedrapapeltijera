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
        
        #Función que devuelve la palabra que elige la computadora y compara con la nuestra
        def whatisit(election):
            print(f"\t\t\t {cards[election]}")
            if yourwordvalue == 0 and election == 2:
                print(f"""A ver... {yourword} gana a {cards[election]}
                  ¡ME HAS GANADO!""")      
            elif yourwordvalue == 2 and election == 0:
                print(f"""A ver... {cards[election]} gana a {yourword}
                    ¡TE HE GANADO!""")          
            else:
                if yourwordvalue < election:
                    print(f"""A ver... {cards[election]} gana a {yourword}
                        ¡TE HE GANADO!""")
                elif yourwordvalue > election:
                    print(f"""A ver... {yourword} gana a {cards[election]}
                      ¡ME HAS GANADO!""")
                else:
                    print("\t\tIguales, empatamos")

        def computerelection():
            new_election = int(random.randint(0,2))
            print("\t\tMi elección es:")
            whatisit(new_election)

        computerelection()
    
    else:
        print("No te he entendido")

    print("¿Quieres jugar de nuevo? (y/n)")
    play = input(">")

print("Bye, bye!")