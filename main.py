from AI import AI
from Player import Player
from Game import Game

mark_player1 = 'X'
mark_player2 = 'O'

player1 = AI(mark=mark_player1,type='q')
#player2 = Player(mark=mark_player2)
player2 = AI(mark=mark_player2,type='random')


g = Game(mark_player1,mark_player2)
analysis = g.play(player1,player2,times=500)

for i in analysis:
    if i!= 'WinStrikes':
        print(i," : ",analysis[i])
