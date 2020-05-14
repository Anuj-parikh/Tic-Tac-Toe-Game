# Game Playing with AI algorithms
In this Project, You can compare AI algorithm by their ability to play Tic-Tac-Toe.

## Run Comparision
to run project type below command:
```bash
python main.py
```

## Settings and Variable to run different analysis
In main file, type of comparision can be changed by varying parameter called type
type has 3 values:
dfs := dfs algorithm
q := q learning
random := randomly initialization 
```python
#player1 play with q learning algorithm 
player1 = AI(mark=mark_player1,type='q')

#player2 play with dfs algorithm
player2 = AI(mark=mark_player2,type='dfs')

```


Analysis can be done by varying number of rounds play by AI by changing times parameter in following line:

```python
analysis = g.play(player1,player2,times=10000)
```

## Q learning In AI.py
We can set number of times qUpdate can be done before Q learner can actually play game.

```python
self.qLearner.QUpdate(rounds=5000)
```

## variation in QLearning
We can set Q learning parameters in contructor of QLearning Class

```python
class Qlearning:
    def __init__(self):
        self.states = []
        self.lr = 0.4
        self.exp_rate = 0.3
        self.decay_gamma = 0.9
        self.Q_values = {}
        self.board = Board('X','O')
```