"""
Piedra Papel tijeras
¡Vamos a jugar! ¡Tienes que devolver qué jugador ganó! En caso de empate devolución Draw!.

Ejemplos:

rps('scissors','paper') // Player 1 won!
rps('scissors','rock') // Player 2 won!
rps('paper','paper') // Draw!
"""

def rps(p1, p2):
    game = { 
        p1 : "Player 1",
        p2 : "Player 2"
        }

    if 'rock' in game and "scissors" in game:
        return f'{game["rock"]} won!'
   
    elif 'scissors' in game and "paper" in game:
        return f'{game["scissors"]} won!'

    elif 'paper' in game and "rock" in game:
        return f'{game["paper"]} won!'

    elif p1 == p2:
        return f'Draw!' 
    
    else:
        return "Recuerde ingresar simbolo valido"
            
       
 #Otra forma
#  def rps(p1, p2):
#     beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
#     if beats[p1] == p2:
#         return "Player 1 won!"
#     if beats[p2] == p1:
#         return "Player 2 won!"
#     return "Draw!"

# S, P, R = 'scissors', 'paper', 'rock'
# P1, P2, D = "Player 1 won!", "Player 2 won!", 'Draw!'
# MAPPING = {
#     (S, P): P1, (S, S): D, (S, R): P2,
#     (P, P): D, (P, S): P2, (P, R): P1,
#     (R, P): P2, (R, S): P1, (R, R): D,
# }

# rps = lambda *p: MAPPING[p]


print(rps( 'paper', 'scissors'))