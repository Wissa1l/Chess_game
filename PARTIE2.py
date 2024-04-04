from typing import List,Tuple
import PARTIE1 as partie
import random
import time
import sys


def init_board(file_path: str or None) -> List[List[int]]:
    board = []
    if file_path is not None:
        with open(file_path, "r") as f:
            first_line = f.readline()
            n = int(first_line[0])
            board = [[0 for m in  range(n)] for d in range(n)]
            second_line = f.readline()  #2ème line du fichier
            
            #the string "third_line" into a list of strings, separated by the comma (',') character.
            list2 = second_line.split(',') 
            for x in list2:
                indice = partie.extract_pos(n,x)
                i,j = indice[0],indice[1]
                board[i][j] = 2
            third_line = f.readline()  #3ème line du fichier
            list3 = third_line.split(',')
            #On a emporté la fonction extract_pos(n,x)
            for x in list3:
                indice = partie.extract_pos(n,x)
                i,j = indice[0],indice[1]
                board[i][j] = 1
            
                #row = [str(x) for x in line.strip().split()]
                #board.append(row)
    else:
        board = [[0 for d in range(7)] for m in range(7)]
        for d in range(7):
            for m in range(7):
                if d < 2:
                    board[d][m]=1
                elif 7-d<= 2 :
                    board[d][m]=2
        
    return board

for row in init_board('board.txt'):
    print(row)



def ai_select_peg(board: List[List[int]], player: int) -> tuple:
    pionDevant = []
    desti = 0        # une destination pour le pion
    if player == 1:
        desti = 1
    else:
        desti = -1
    for x in range(len(board) - desti, -1, -desti):
        if player in board[x]:
            for z in range(len(board)):
                pionDevant.append((x, z))
    return random.choice(pionDevant)       # triée par ordre croissant de position

#print(ai_select_peg(init_board('board.txt'),1))

def ai_move(board: List[List[int]], pos: Tuple[int, int], player: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    movement = []
    x , z = pos
    desti = 0      #une destination pour le pion choisi par l’IA
    if player == 1:
        desti = 1
    else:
        desti = -1
    line = desti + x
    if 0 <= line < len(board):
        if z < len(board) - 1:
            movement.append((line, z + 1))
        elif z > 0:
            movement.append((line, z - 1))
        movement.append((line, z))
        # triée par ordre croissant de position
    return pos, random.choice([M for M in movement if board[M[0]][M[1]] == 0])

#print(ai_move(init_board('board.txt'),(1,2),1))


    

def input_select_peg(board: List[List[int]], player: int) -> tuple:
    t = len(board)
    Pos_actuelle = []
    desti = 0
    if player == 1 :
        desti = 1
    else :
        desti = -1
    for s in range(t):
        PegIndice = []      #les indices de pion
        for e in range(t):
            if board[s][e] == player:
                if board[s + desti][e] == 0 and 0 <= s + desti < t:
                    PegIndice.append((s, e))
                elif board[s + desti][e - 1] != player and 0 <= e - 1 < t:
                    PegIndice.append((s, e))
                elif  0 <= e + 1 < t and  board[s + desti][e + 1] != player :
                    PegIndice.append((s, e))
        if PegIndice:
            Pos_actuelle.append(PegIndice)
    
    d=0
    m=0
    Move = Pos_actuelle[d][m]  #la position actuelle du pion
    board[Move[0]][Move[1]] = 50
    
    while True:
        print_board(board)
        #pour demander à l'utilisateur de sélectionner son pion à jouer à l'aide des touches i, k, j et l. 
        choice = input("Entrer i (haut), j (gauche), l (droite), k (bas) ou y ,SVP:")
        if choice == 'j':
            if m == 0:
                board[Move[0]][Move[1]] = player
                m = len(Pos_actuelle[d])-1
                Move = Pos_actuelle[d][m]
                board[Move[0]][Move[1]] = 50
            else:
                board[Move[0]][Move[1]] = player
                m -= 1
                Move = Pos_actuelle[d][m]
                board[Move[0]][Move[1]] = 50
                
        elif choice == 'i':
            if d == 0:
                board[Move[0]][Move[1]] = player
                d = len(Pos_actuelle)-1
                row = Pos_actuelle[d]
                m = find_closest_peg(Move, row)
                Move = Pos_actuelle[d][m]
                board[Move[0]][Move[1]] = 50
            else:
                board[Move[0]][Move[1]] = player
                d -=1
                row = Pos_actuelle[d]
                m = find_closest_peg(Move, row)
                Move = Pos_actuelle[d][m]
                board[Move[0]][Move[1]] = 50
                
        elif choice == 'l':
            if m == len(Pos_actuelle[d])-1:
                board[Move[0]][Move[1]] = player
                m = 0
                Move = Pos_actuelle[d][m]
                board[Move[0]][Move[1]] = 50
            else:
                board[Move[0]][Move[1]] = player
                m += 1
                Move = Pos_actuelle[d][m]
                board[Move[0]][Move[1]] = 50 
    
        elif choice == 'k':
            if d == len(Pos_actuelle)-1:
                board[Move[0]][Move[1]] = player
                d = 0
                row = Pos_actuelle[d]
                m = find_closest_peg(Move, row)
                Move = Pos_actuelle[d][m]
                board[Move[0]][Move[1]] = 50
            else:
                board[Move[0]][Move[1]] = player
                d +=1
                row = Pos_actuelle[d]
                m = find_closest_peg(Move, row)
                Move = Pos_actuelle[d][m]
                board[Move[0]][Move[1]] = 50
                
        elif choice == 'y':  #Le choix est validé avec la touche y 
            board[Move[0]][Move[1]] = player
            return Move
        
        else:
            print("Invalide")


#print(input_select_peg(init_board('board.txt'),2))


def input_move(board: List[List[int]], pos: Tuple[int, int], player: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    x, z = pos
    validPositions = []
    # on sélectionne la destination du pion en position pos
    desti = 0
    if player == 1 :
        desti = 1
    else :
        desti = -1
    if board[x+desti][z] == 0:
        validPositions.append((x+desti, z))
        
    if z == len(board)-1:
        if board[x+desti][z-1] != player:
            validPositions.append((x+desti, z-1))
            
    elif z == 0:
        if board[x+desti][z+1] != player:
            validPositions.append((x+desti, z+1))
    
    else:
        if board[x+desti][z-1] != player:
            validPositions.append((x+desti, z-1))
        if board[x+desti][z+1] != player:
            validPositions.append((x+desti, z+1))

    c = 0  
    PositionAc = validPositions[c]   #la position actuelle du pion
    old_peg = board[PositionAc[0]][PositionAc[1]] #c'est pour eviter la repitition de '#'
    board[PositionAc[0]][PositionAc[1]] = 50
    t = len(validPositions)
    
    
    while True:
        print_board(board)
        choice = input("Entrer l (droite) ou j (gauche) ou y , SVP :")
        
        if choice == 'l':   # l (droite)
            board[PositionAc[0]][PositionAc[1]] = old_peg
            c = (c + 1) % t
            PositionAc = validPositions[c]
            old_peg = board[PositionAc[0]][PositionAc[1]]
            board[PositionAc[0]][PositionAc[1]] = 50
            
        elif choice == 'j':   #  j(gauche)
            board[PositionAc[0]][PositionAc[1]] = old_peg
            c = (c - 1 + t) % t
            PositionAc = validPositions[c]
            old_peg = board[PositionAc[0]][PositionAc[1]]
            board[PositionAc[0]][PositionAc[1]] = 50
        
        elif choice == 'y':
            board[PositionAc[0]][PositionAc[1]] = old_peg
            return pos,PositionAc             
    
#print(input_move(init_board('board.txt'),(1,4),2))


def find_closest_peg(current_peg: Tuple[int, int], next_line: List[Tuple[int, int]]) -> List[int] :
    H = []
    for e in next_line:
        # Calcul La distance d'après cette formule '𝑑 = |𝑥1 −𝑥2| + |𝑦1 −𝑦2|'
        d = abs(current_peg[1]-e[1]) + abs(current_peg[0]-e[0]) 
        H.append((e,d))
    return H.index(min(H, key=lambda n: n[1]))



def print_board(board : List[List[int]])-> None:
    n = len(board)
    Dash = ['-' for d in range(n)]
    Ch = [chr(d) for d in range(97,97+n)]
    WidthOfLine_number = len(str(n))
    FirstSpace = "    "             #il ajoute de l'espace
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
        for m in range(n):             # add values of row
            if board[d][m] == 1:
                line+=" "+"B"
            elif board[d][m] == 50: # elle represente '#'
                line+=" "+"#" 
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
        
        
print_board(init_board('board.txt'))
print(input_select_peg(init_board('board.txt'),2))
print(input_move(init_board('board.txt'),(1,4),2))

def main() -> None:
    ai_play = False
    fichier = None #le chemin du fichier
    if len(sys.argv) >= 2:
        fichier = sys.argv[1]
    # python3 partie2.py board.txt –ai
    if  len(sys.argv) >= 3 and sys.argv[2] == '-ai'  :
        ai_play = True

    board = init_board(fichier)
    print_board(board)
    Player = 1
    while True:
        if Player == 1:
            print("Joueur : ",Player)  
            Peg = None
            if ai_play:
                time.sleep(4)
                Peg = ai_select_peg(board, Player)
                print(Peg,900)
            else:
                Peg = input_select_peg(board, Player)
                
            Move = ai_move(board, Peg, Player) if ai_play else input_move(board, Peg, Player)
    
            partie.play_move(board, Move, Player)
            print_board(board)
          
            winner_result = partie.winner(board)
            if winner_result is not None:
                print(f"Player {winner_result} a gagné le jeu!")
                break
    
        else:
            print("Joueur : ",Player)    
            Peg = None 
            Peg = input_select_peg(board, Player) 
            Move = input_move(board, Peg, Player)
          
            partie.play_move(board, Move, Player)
            print_board(board)
          
            winner_result = partie.winner(board)
            if winner_result is not None:
                print(f"Player {winner_result} a gagné le jeu!")
                break
   
        if Player == 1:
            Player = 2
        else :
            Player = 1
            

"""if __name__ == '__main__':
    main()"""   
            
main()
