import pickle
import random
from collections import defaultdict
from Board import Board


class Qlearning:
    def __init__(self):
        self.states = []
        self.lr = 0.2
        self.exp_rate = 0.3
        self.decay_gamma = 0.9
        self.Q_values = {}
        self.board = Board('X','O')
    
    def chooseAction(self,board):
        my_nxt_reward = 0
        actions = board.getValidMoves()
        action = None
        if random.random() <= self.exp_rate:
            action = actions[random.randint(0,len(actions)-1)]
        else:
            for a in actions:
                cur_pos = board.getBoard()
                
                try:
                    nxt_reward = self.Q_values[cur_pos][a]
                except:
                    if cur_pos not in self.Q_values:
                            self.Q_values[cur_pos] = {}
                    if a not in self.Q_values[cur_pos]:
                        self.Q_values[cur_pos][a] = 0
                    nxt_reward = 0.0
                
                if nxt_reward >= my_nxt_reward:
                    action = a
                    my_nxt_reward = nxt_reward
        
        return action


    def reset(self):
        self.states = []
        if random.randint(1,2) == 1:
            self.board = Board('X','O')
        else:
            self.board = Board('O','X')


    def QUpdate(self,rounds=100):
        i=0
        while i < rounds:
            if self.board.isWin():
                if self.board.getWinner()=='X':
                    reward = 15
                elif self.board.getWinner()=='O':
                    reward = -5
                else:
                    reward = 5
                for s in reversed(self.states):
                    try:
                        cur_q_value = self.Q_values[s[0]][s[1]]
                    except :
                        if s[0] not in self.Q_values:
                            self.Q_values[s[0]] = {}
                        if s[1] not in self.Q_values[s[0]]:
                            self.Q_values[s[0]][s[1]] = 0
                        cur_q_value = 0.0
                    reward = cur_q_value + self.lr * (self.decay_gamma * reward - cur_q_value)
                    self.Q_values[s[0]][s[1]] = round(reward, 3)
                self.reset()
                i += 1
            else:
                action = self.chooseAction(self.board)
                self.states.append([self.board,action])
                self.board.makeMove(action[0],action[1])
        print(self.Q_values)

    def getMove(self,b):
        return self.chooseAction(b)


                


