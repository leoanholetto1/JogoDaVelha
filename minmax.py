from jogo_da_velha import branco,token , verificaGanhador
import math 

def movimentoIA(board,jogador):
    possibilidades = getPosicoes(board)
    melhor_valor = None 
    melhor_movimento = None 
    for possibilidade in possibilidades:
        board[possibilidade[0]][possibilidade[1]] = token[jogador]
        valor=minmax(board, jogador)
        board[possibilidade[0]][possibilidade[1]] = branco
        if(melhor_valor is None):
            melhor_valor = valor
            melhor_movimento = possibilidade
        elif(jogador == 0):
            if(valor > melhor_valor):
                melhor_valor = valor
                melhor_movimento = possibilidade
        elif(jogador == 1):
            if(valor < melhor_valor):
                melhor_valor = valor
                melhor_movimento = possibilidade

    return melhor_movimento[0],melhor_movimento[1]


def getPosicoes(board):
    posi = []
    for i in range(3):
        for j in range(3):
            if(board[i][j] == branco):
                posi.append([i,j])
    return posi


score = {
    "EMPATE": 0,
    "X": 1,
    "O": -1
}


def minmax(board, jogador):
    ganhador = verificaGanhador(board)
    if(ganhador):
        return score[ganhador]
    jogador = (jogador + 1)%2
    
    possibilidades = getPosicoes(board)
    melhor_valor = None
    for possibilidade in possibilidades:
        board[possibilidade[0]][possibilidade[1]] = token[jogador]
        valor = minmax(board, jogador)
        board[possibilidade[0]][possibilidade[1]] = branco

        if(melhor_valor is None):
            melhor_valor = valor
        elif(jogador == 0):
            if(valor > melhor_valor):
                melhor_valor = valor
        elif(jogador == 1):
            if(valor < melhor_valor):
                melhor_valor = valor

    return melhor_valor
