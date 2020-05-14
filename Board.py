class Board:
    empty_cell = ' '

    def __init__(self,plyr1,plyr2):
        self.board = []
        self.winStrike = []
        #initialize empty board
        for i in range(3):
            self.board.append([])
        
        for i in range(3):
            for j in range(3):
                self.board[i].append(Board.empty_cell)
        
        self.plyr1 = plyr1
        self.plyr2 = plyr2
        assert plyr1 != plyr2 , "Both player must have different Symbol to play !"
        assert plyr1 != Board.empty_cell , "Player 1 cannot play with "+str(Board.empty_cell)+" As it is representation of Empty board"
        assert plyr2 != Board.empty_cell , "Player 2 cannot play with "+str(Board.empty_cell)+" As it is representation of Empty board"
        self.turn = True
        self.num_empty_cell = 9


    def isValid(self,x,y):
        if self.board[x][y] == Board.empty_cell:
            return True
        return False

    def getValidMoves(self):
        v_moves = []
        if self.num_empty_cell == 0:
            return v_moves
        
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == Board.empty_cell:
                    v_moves.append((i,j))
        return v_moves


    def unMove(self,x,y):
        if self.board[x][y] != Board.empty_cell:
            self.num_empty_cell = self.num_empty_cell + 1
            self.turn = not self.turn
        self.board[x][y] = Board.empty_cell
        

    def makeMove(self,x,y):
        if self.isValid(x,y):
            if self.turn:
                self.board[x][y] = self.plyr1
            else:
                self.board[x][y] = self.plyr2
            self.turn = not self.turn
            self.num_empty_cell = self.num_empty_cell - 1
            return True
        return False
      
    def isWin(self):
        for i in range(3):
            #check rows are equals
            if self.board[i][0] != Board.empty_cell :
                if self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                    self.winStrike = [(i,0),(i,1),(i,2)]
                    return True
            
            #check columns are equals
            if self.board[0][i] != Board.empty_cell :
                if self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                    self.winStrike = [(0,i),(1,i),(2,i)]
                    return True
        
        #cross line 1
        if self.board[0][0] != Board.empty_cell:
            if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
                self.winStrike = [(0,0),(1,1),(2,2)]
                return True
        
        #cross line 2
        if self.board[0][2] != Board.empty_cell:
            if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
                self.winStrike = [(0,2),(1,1),(2,0)]
                return True
        
        if self.num_empty_cell == 0:
            return True
        return False
    
    def getWinningStrike(self):
        return self.winStrike

    def getWinner(self):
        if len(self.winStrike) == 0:
            return Board.empty_cell
        return self.board[self.winStrike[0][0]][self.winStrike[0][1]]
    
    def printBoard(self):

        for i in range(3):
            for j in range(3):
                print(self.board[i][j],end='  |')
            print()
        print()
    
    def getBoard(self):
        b = tuple([tuple(b) for b in self.board])

        return b