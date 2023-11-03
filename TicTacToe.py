pl_name = 'O'
moves = [
[' ',' ',' '],
[' ',' ',' '],
[' ',' ',' '],
]

def play_again():
    print(f"\nPlayer {pl_name}\'s Turn ")
    move = input('Enter your move (X Y)(eg.: 01) : ')
    display(int(move[0]), int(move[1]), pl_name)

def display(x_,y_,dis):
    global pl_name
    if moves[x_][y_] != ' ':
        print("Already Occupied!! Try Again")
    else:
        moves[x_][y_] = dis
        y_dis = '''
        [0] [1] [2]'''
        a = '''    [0]-> _{}_|_{}_|_{}_'''.format(*moves[0])
        b = '''    [1]-> _{}_|_{}_|_{}_'''.format(*moves[1])
        c = '''    [2]->  {} | {} | {} '''.format(*moves[2]) 
        print(y_dis,a,b,c,sep='\n')
        if (pl_name == 'X'):
            pl_name = 'O'
        else:
            pl_name = 'X'
    check_Win()

def check_Win():
    win_cond = [
        ['00','01','02'],
        ['10','11','12'],
        ['20','21','22'],
        ['00','10','20'],
        ['01','11','21'],
        ['02','12','22'],
        ['00','11','22'],
        ['02','11','20']
    ]
    for j in win_cond:
        if moves[int(j[0][0])][int(j[0][1])] == moves[int(j[1][0])][int(j[1][1])] == moves[int(j[2][0])][int(j[2][1])]:
            print(f"{moves[int(j[0][0])][int(j[0][1])]}is the Winner")
            que = input('Want to play again: (Y/N)')
        else:  
            play_again()
    
play_again()