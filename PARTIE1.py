from typing import List,Tuple
import re



def init_board(n:int)->List[List[int]]:
    board = [[0 for m in  range(n)] for d in range(n)]
    for d in range(n):
        for m in range(n):
            if d < 2:
                board[d][m]=1
            elif n-d<= 2 :
                board[d][m]=2
    return board

#print(init_board(7))

def print_board(board : List[List[int]])-> None:
    n = len(board)
    Dash = ['-' for d in range(n)]
    Ch = [chr(d) for d in range(97,97+n)]
    WidthOfLine_number = len(str(n))
    FirstSpace = "    "    #il ajoute de l'espace
    SecondSpace = "    "
    if WidthOfLine_number != 1:
        print(SecondSpace+" ".join(Dash))
    else :
        print(FirstSpace+" ".join(Dash))
    for d in range(n):
        if len(str(n-d)) != 1 :
            line = str(n-d) +" |"
        else:
            line = str(n-d).rjust(WidthOfLine_number," ")+" |"
        for m in range(n):           # add values of row
            if board[d][m] == 1:
                line+=" "+"B"
            elif board[d][m] == 2:
                line+=" "+"W"
            else :
                line+=" "+"."
        line+=" |"
        print(line)
    if WidthOfLine_number == 1:         # ajoute des tirets
        print(FirstSpace+" ".join(Dash))
        print(FirstSpace+" ".join(Ch))
    else:
        print(SecondSpace+" ".join(Dash))
        print(FirstSpace+" ".join(Ch))
        
        
#print_board(init_board(7))
            
def winner(board: List[List[int]]) -> int or None:
    n = len(board)
    for d in range(n):
        if board[0][d] == 2:
            return 1
        elif board[n-1][d] == 1:
            return 2
        return None
            
#print(winner(init_board(7)))

def is_in_board(n : int, pos : Tuple[int, int]) -> bool:
    d,m = pos
    if d >= 0  and d <= n-1 and m >= 0 and m <= n-1 :    
        return True
    return False

#print(is_in_board(7,(0,7)))

def input_move() -> str:
    while 1:
        coup = input("Saisir votre coup : ")
        a = r"[a-z][0-9]{1,2}>[a-z][0-9]{1,2}"
        if re.match(a, coup):
            return coup
        else:
            print("Saisir un coup au format valide (exemple : a7>a6)")
    print("")

#input_move()

def extract_pos(n : int, str_pos : str): 
    if len(str_pos) >= 2 and str_pos[0].islower() and str_pos[1].isdigit():
        row = int(str_pos[1])
        col = ord(str_pos[0]) - ord('a') + 1
        if row <= n and col <= n:
            return (n- row, col - 1)
    return None

#print(extract_pos(7,'e2'))          



def check_move(board: List[List[int]], player: int, str_move: str) -> bool:
    start_pos, end_pos = extract_pos(len(board), str_move[:2]), extract_pos(len(board), str_move[3:])
    if start_pos is None or end_pos is None:
        return False
    start_row, start_col = start_pos
    end_row, end_col = end_pos
    if board[start_row][start_col] != player:
        return False
    
    if board[end_row][end_col] == player:
        return False
    
    if start_col == end_col:
        if abs(end_row - start_row)==1:
            if board[end_row][end_col] != 0:
                return False
            return True
        elif abs(start_col - end_col)== 1:
            if abs(start_row - end_row)==1:
                return True
    return False
    
def main(n) -> None:
    board = init_board(n)
    print_board(board)
    game = None
    player = 1
    while game is None:
        move = input_move()
        if check_move(board, player, move):
            start, end = extract_pos(n, move[:2]), extract_pos(n, move[3:])
            play_move(board, (start, end), player)
            player = 3 - player
        print_board(board)
        winner = game(board)
    print("Player", winner, "wins !")

def play_move(board : List[List[int]], move : Tuple[Tuple[int, int], Tuple[int,int]], player : int) -> None : 
    start, end = move
    start_a, start_b = start
    end_a, end_b = end
    board[end_a][end_b] = player
    board[start_a][start_b] = 0



"""
move = ((6,2),(5,4))
play_move(list,move,2)
print_board(list)"""

     


 

    
    
        
        
    


            
    