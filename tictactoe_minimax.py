from math import inf
from random import choice as val
import itertools
import time

def analyze(pos):
    if success(pos, player1):
        score = +1
    elif success(pos, player2):
        score = -1
    else:
        score = 0
    return score

def success(pos, agent):
    win_pos = [
        [pos[0][0], pos[0][1], pos[0][2]],
        [pos[1][0], pos[1][1], pos[1][2]],
        [pos[2][0], pos[2][1], pos[2][2]],
        [pos[0][0], pos[1][0], pos[2][0]],
        [pos[0][1], pos[1][1], pos[2][1]],
        [pos[0][2], pos[1][2], pos[2][2]],
        [pos[0][0], pos[1][1], pos[2][2]],
        [pos[2][0], pos[1][1], pos[0][2]],
    ]
    if [agent, agent, agent] in win_pos:
        return True
    else:
        return False

def loss(pos):
    return success(pos, player2) or success(pos, player1)
def unmarked(pos):
    cell = []
    for i, r in enumerate(pos):
        for j, c in enumerate(r):
            if c == 0: cell.append([i, j])
    return cell

def feasible(i, j):
    if [i, j] in unmarked(set_board):
        return True
    else:
        return False

def set_pos(i, j, agent):
    if feasible(i, j):
        set_board[i][j] = agent
        return True
    else:
        return False
def algo_MiniMax(pos, depth, agent):
    if agent == player1:
        first = [-1, -1, -inf]
    else:
        first = [-1, -1, +inf]

    if depth == 0 or loss(pos):
        point = analyze(pos)
        return [-1, -1, point]

    for c in unmarked(pos):
        i, j = c[0], c[1]
        pos[i][j] = agent
        point = algo_MiniMax(pos, depth - 1, -agent)
        pos[i][j] = 0
        point[0], point[1] = i, j
        if agent == player1:
            if point[2] > first[2]:
                first = point
        else:
            if point[2] < first[2]:
                first = point
    return first

def agent_chance(X, O, choiceXO):
    depth = len(unmarked(set_board))
    if depth == 0 or loss(set_board):
        return
    print_board(set_board, X, O)
    if depth == 9:
        i = val([0, 1, 2])
        j = val([0, 1, 2])
    else:
        make = algo_MiniMax(set_board, depth, choiceXO)
        i, j = make[0], make[1]
    set_pos(i, j, choiceXO)

def game():
    agent_chance(X, O, player1)
    agent_chance(X, O, player2)

def result():
    print('')
    if success(set_board, player1):
        print_board(set_board, X, O)
        print('Result: X Wins!')
    elif success(set_board, player2):
        print_board(set_board, X, O)
        print('Result: O Wins!')
    else:
        print_board(set_board, X, O)
        print('Result: Draw Game')
        
def print_board(pos, X, O):
    for r in pos:
        print('\n')
        for c in r:
            if c == +1:
                print( X, end='')
            elif c == -1:
                print( O, end='')
            else:
                print('*', end='')
    print('\n')

def start():
    begin = time.time()
    for x in range (5):
        game()
    result()
    end = time.time()
    totalTime = end - begin
    print("Total searching period: %.3f seconds" % (totalTime))

player1 = +1
player2 = -1
X = 'X'
O = 'O'
set_board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

start()
