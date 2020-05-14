class Player:

    def __init__(self,mark='O'):
        self.mark = mark
    
    def getMark(self):
        return self.mark

    def getMove(self,board=None):
        assert board != None, "Must pass board to play !"
        board.printBoard()
        print("Enter (space seprated) row and col for put ",self.mark)
        x,y = [int(i)-1 for i in input().split(' ')]
        return x,y