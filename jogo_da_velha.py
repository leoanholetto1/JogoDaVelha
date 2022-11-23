branco =" "
token = ["X" , "O"]

def criarBoard():
    board =[
        [branco,branco,branco],
        [branco,branco,branco],
        [branco,branco,branco],
    ]
    return board


def InputValido(mensagem):
    try:
        n = int(input(mensagem))
        if(n >= 1 and n<=3):
            return n-1
        else: 
            print("Numero precisa estar entre 1 e 3")
            return InputValido(mensagem)
    except:
        print("Número Invalido")
        InputValido(mensagem)

def verificaMovimento(board,i,j):
    if(board[i][j] == branco):
        return True 
    else:
        return False

def fazMovimento(board,i,j,jogador):
    board[i][j]=token[jogador]

def verificaGanhador(board):
    for i in range (3):
        if(board[i][0] == board[i][1] and board[i][2] == board[i][1] and board[i][0] != branco):
            return board[i][0]

    for i in range (3):
        if(board[0][i] == board[1][i] and board[2][i] == board[1][i] and board[0][i] != branco):
            return board[0][i]
    
    if(board[0][0]!=branco and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        return board[0][0]
    
    if(board[0][2]!=branco and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return board[0][2]
    
    for i in range(3):
        for j in range(3):
            if(board[i][j] == branco):
                return False
    
    return "EMPATE" 


