#!/usr/bin/env python
#coding:utf-8
import numpy as np
import heapq

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""
import sys

ROW = "ABCDEFGHI"
COL = "123456789"

def initiate_domain(board):
    # intial domain setup
    # blocks constraints
    blocks = {}
    # rows constraints
    rows = {}
    # cols constraints
    cols = {}
    # domains
    domains = [[set(range(1,10)) for _ in range(9)] for _ in range(9)]
    # remaining values
    class PrioritizedItem:
        def __init__(self, priority, domain,pos):
            self.priority = priority
            self.domain = domain
            self.pos = pos

        def __lt__(self, other):
            return self.priority < other.priority
    RV = []


    for cor, value in board.items():
        r = int(ord(cor[0])-ord('A'))
        c = int(cor[1])-1
        if value != 0:
            # blocks
            block_key = ( r//3,c//3 )
            if block_key not in blocks:
                blocks[block_key] = set()
            blocks[block_key].add(value)
            # rows
            if r not in rows:
                rows[r] = set()
            rows[r].add(value)
            # cols
            if c not in cols:
                cols[c] = set()
            cols[c].add(value)
            
        


    for cor,value in board.items():
        r = int(ord(cor[0])-ord('A'))
        c = int(cor[1])-1
        if value == 0:
            block_key = ( r//3,c//3 )
            for i in range(1,10):
                if i in rows.get(r,set()) or i in cols.get(c,set()) or i in blocks.get(block_key,set()):
                    domains[r][c].discard(i)
    
    # num of remaining values
    for r in range(9):
        for c in range(9):
            heapq.heappush(RV, PrioritizedItem(len(domains[r][c]), domains[r][c], (r,c)))
    
    # print("Initial domains:")
    # print(np.array(domains))
    # print("\n")
    # print("Initial RV:")
    # for item in RV:
    #     print("pos:",item.pos,"domain:",item.domain)
    domains = np.array(domains)
    # print(len(RV))
    
    # def check_naked_pair(domain,visited,value):
    #     for i in range(3):
    #         for j in range(3):
    #             if domain[i,j] == value and visited[i][j] == 0:
    #                 return (i,j)
    #     return None

    # for n in range(3):
    #     for m in range(3):
    #         visited = [[0 for _ in range(3)] for _ in range(3)]
    #         for row in range(3):
    #             for col in range(3):
    #                 r = n*3 + row
    #                 c = m*3 + col
    #                 if len(domains[r][c]) == 2 and visited[row][col] == 0:
    #                     visited[row][col] = 1
    #                     naked_pair = check_naked_pair(domain=domains[n*3:n*3+3,m*3:m*3+3],visited = visited,value=domains[r,c])
    #                     if naked_pair:
    #                         for row in range(3):
    #                             for col in range(3):
    #                                 rr = n*3 + row
    #                                 cc = m*3 + col
    #                                 if (row,col) != (naked_pair[0],naked_pair[1]) and (row,col) != (row,col):
    #                                     for val in domains[r][c]:
    #                                         domains[rr][cc].discard(val)
    
    return blocks,rows,cols,domains, RV
                

def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)


def goalTest(board):
    if 0 not in set(board.values()):
        return True
    return False

def forward(RV,assigned_d,pos):
    for i in RV:
        if assigned_d in i.domain:
            if pos[0] == i.pos[0] or pos[1] == i.pos[1] or (pos[0]//3 == i.pos[0]//3 and pos[1]//3 == i.pos[1]//3):
                if len(i.domain) == 1 and assigned_d in i.domain:
                    # print("forward checking failed at",i.pos,"domain",i.domain)
                    # print("\n")
                    # for i in RV:
                        # print("pos:",i.pos,"domain:",i.domain)
                    return False
    return True

def backtracking(board):
    blocks,rows,cols,domains,RV = initiate_domain(board)
    res = backtrack(board,domains,RV)
    return res
def backtrack(board,domains,RV):
    """Takes a board and returns solved board."""
    # TODO: implement this
    mapping = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I'}
    if goalTest(board):
        # print("yes")
        return board
    
    if not RV:
        print(board)
    value = heapq.heappop(RV)
    domain, pos = value.domain, value.pos
    # print("\n")
    # print("pos",pos,"domain",domain)
    for d in domain:
        # update RV
        if forward(RV,d,pos):
            expr = mapping[pos[0]] + str(pos[1]+1)
            board[expr] = d
            changed = []
            for i in RV:
                if d in i.domain:
                    if pos[0] == i.pos[0] or pos[1] == i.pos[1] or (pos[0]//3 == i.pos[0]//3 and pos[1]//3 == i.pos[1]//3):
                        i.domain.discard(d)
                        i.priority = len(i.domain)
                        changed.append(i.pos)
                        # print("After assigning",d,"to",pos,"domains:")
                        # print("changed pos:",i.pos,"domain:",i.domain)
            heapq.heapify(RV)
            result = backtrack(board,domains,RV)
            if result:
                return result
            # print("Backtracking on pos",pos,"value",d)
            # print("\n")
            board[expr] = 0
            for i in RV:
                if i.pos in changed:
                    i.domain.add(d)
                    i.priority = len(i.domain)
            heapq.heapify(RV)
    heapq.heappush(RV, value)
    heapq.heapify(RV)
    # print("original value:",value.pos,"domain:",value.domain)
    return False


    # print("boatd",board)
    # solved_board = board
    return solved_board


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if len(sys.argv[1]) < 9:
            print("Input string too short")
            exit()

        print(sys.argv[1])
        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = { ROW[r] + COL[c]: int(sys.argv[1][9*r+c])
                  for r in range(9) for c in range(9)}    
        # print(board)
        blocks,rows,cols,domains,RV = initiate_domain(board)




          
        
        solved_board = backtracking(board)
        print("Solved board:")
        print(board)

        # Write board to file
        out_filename = 'output.txt'
        outfile = open(out_filename, "w")
        outfile.write(board_to_string(solved_board))
        outfile.write('\n')
    else:
        print("Usage: python3 sudoku.py <input string>")
    
    print("Finishing all boards in file.")