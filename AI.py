import random
import copy
from Qlearning import Qlearning

class AI:
    def __init__(self,mark='X',type='random'):
        self.type = type
        self.plyr = mark
        if type=='q':
            self.qLearner = Qlearning()
            self.qLearner.QUpdate(rounds=500)
            print('Q training Over') 
    
    def getMark(self):
        return self.plyr

    def getMove(self,board=None):
        if self.type == 'dfs' and board !=None:
            print(board.getValidMoves())
            a,b = self.dfsMove(board)
            if a!=-1 and b != -1:
                return a,b
        if self.type == 'q':
            a,b = self.qMove(board)
            return a,b
        return [random.randint(0,2),random.randint(0,2)]
    
    def dfsMove(self,board):
        queue = board.getValidMoves()
        print(len(queue),queue)
        if len(queue) == 0:
            return -1,-1
        
        for i in queue:
            _ = board.makeMove(i[0],i[1])
            if board.isWin() and board.getWinner() == self.plyr:
                board.unMove(i[0],i[1])
                return i[0],i[1]
            
            a,b = self.dfsMove(board)
            board.unMove(i[0],i[1])
            if a != -1 and b != -1:
                return i[0],i[1]
        
        return -1,-1

    def qMove(self,board):
        return self.qLearner.getMove(board)



