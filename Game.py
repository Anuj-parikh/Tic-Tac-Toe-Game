from Board import Board
from collections import defaultdict

class Game:

    def __init__(self,plyr1,plyr2):
        self.plyr1 = plyr1
        self.plyr2 = plyr2

    def playOneRound(board,plyr1,plyr2):
        p_turn = True
        while board.isWin() == False:
            valid_turn = False
            while not valid_turn:
                if p_turn:
                    x,y = plyr1.getMove(board)
                else:
                    x,y = plyr2.getMove(board)
                valid_turn = board.makeMove(x,y)
            p_turn = not p_turn
        board.printBoard()
        print("---------------------------------------------")
        print(board.getWinningStrike())
        print(board.getWinner())
        print("---------------------------------------------")

        details = {}
        details['strike'] = board.getWinningStrike() 
        details['winner'] = board.getWinner()
        return details

    def play(self,plyr1,plyr2,times = 1):
        ans= defaultdict(int)
        ans['WinStrikes'] = defaultdict(int)
        for i in range(times):
            b = Board(self.plyr1,self.plyr2)
            d = Game.playOneRound(b,plyr1,plyr2)
            ans['WinStrikes'][str(d['strike'])] += 1 
            ans[d['winner']] += 1
        
        return ans