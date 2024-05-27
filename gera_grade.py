from dificuldade import Dificuldade
from direcoes import Direcoes
from size import Size
from string import ascii_uppercase
import random

class GeraGrade():
    def __init__(self, tamanho:Size = Size.MD, dificuldade:Dificuldade = Dificuldade.MEDIO) -> None:
        self.tamanho = tamanho
        self.dificuldade = dificuldade
        self.grade = self.criar_grade(tamanho)
        self.direcoes = self.definir_direcoes(dificuldade)

    
    def criar_grade(self, tamanho: int):
        return [[' ' for _ in range(tamanho)] for _ in range(tamanho)]
    
    def definir_direcoes(self, dificuldade: Dificuldade):
        if dificuldade == Dificuldade.FACIL:
            return [Direcoes.HORIZONTAL, Direcoes.VERTICAL]
        elif dificuldade == Dificuldade.MEDIO:
            return [Direcoes.HORIZONTAL, Direcoes.VERTICAL, Direcoes.DIAGONAL]
        
    
    def pode_colocar_palavra(self, palavra, linha, coluna, direcao):
        len_palavra = len(palavra)
        if direcao == Direcoes.HORIZONTAL:
            if coluna + len_palavra > self.tamanho:
                return False
            for i in range(len_palavra):
                if self.grade[linha][coluna + i] != ' ' and self.grade[linha][coluna + i] != palavra[i]:
                    return False
                
        elif direcao == Direcoes.VERTICAL:
            if linha + len_palavra > self.tamanho:
                return False
            for i in range(len_palavra):
                if self.grade[linha + i][coluna] != ' ' and self.grade[linha + i][coluna] != palavra[i]:
                    return False
                
        elif direcao == Direcoes.DIAGONAL:
            if coluna + len_palavra > self.tamanho or linha + len_palavra > self.tamanho:
                return False
            for i in range(len_palavra):
                if self.grade[linha + i][coluna + i] != ' ' and self.grade[linha + i][coluna + i] != palavra[i]:
                    return False

        elif direcao == Direcoes.DIAGONAL_OPOSTA:
            if coluna - len_palavra < 0 or linha + len_palavra > self.tamanho:
                return False
            for i in range(len_palavra):
                if self.grade[linha + i][coluna - i] != ' ' and self.grade[linha + i][coluna - i] != palavra[i]:
                    return False
            
        elif direcao == Direcoes.HORIZONTAL_OPOSTA:
            if coluna - len_palavra < 0:
                return False
            for i in range(len_palavra):
                if self.grade[linha][coluna - i] != ' ' and self.grade[linha][coluna - i] != palavra[i]:
                    return False

        elif direcao == Direcoes.VERTICAL_OPOSTA:
            if linha - len_palavra < 0:
                return False
            for i in range(len_palavra):
                if self.grade[linha - i][coluna] != ' ' and self.grade[linha - i][coluna] != palavra[i]:
                    return False

        elif direcao == Direcoes.DIAGONAL_INVERTIDA:
            if coluna + len_palavra > self.tamanho or linha - len_palavra < 0:
                return False
            for i in range(len_palavra):
                if self.grade[linha - i][coluna + i] != ' ' and self.grade[linha - i][coluna + i] != palavra[i]:
                    return False

        elif direcao == Direcoes.DIAGONAL_INVERTIDA_OPOSTA:
            if coluna - len_palavra < 0 or linha - len_palavra < 0:
                return False
            for i in range(len_palavra):
                if self.grade[linha - i][coluna - i] != ' ' and self.grade[linha - i][coluna - i] != palavra[i]:
                    return False

        return True
    

    def coloca_palavra(self, palavra, linha, coluna, direcao):
        if direcao == Direcoes.HORIZONTAL:
            for i in range(len(palavra)):
                self.grade[linha][coluna + i] = palavra[i]

        elif direcao == Direcoes.VERTICAL:
            for i in range(len(palavra)):
                self.grade[linha + i][coluna] = palavra[i]

        elif direcao == Direcoes.DIAGONAL:
            for i in range(len(palavra)):
                self.grade[linha + i][coluna + i] = palavra[i]

        elif direcao == Direcoes.DIAGONAL_OPOSTA:
            for i in range(len(palavra)):
                self.grade[linha + i][coluna - i] = palavra[i]

        elif direcao == Direcoes.HORIZONTAL_OPOSTA:
            for i in range(len(palavra)):
                self.grade[linha][coluna - i] = palavra[i]

        elif direcao == Direcoes.VERTICAL_OPOSTA:
            for i in range(len(palavra)):
                self.grade[linha - i][coluna] = palavra[i]

        elif direcao == Direcoes.DIAGONAL_INVERTIDA:
            for i in range(len(palavra)):
                self.grade[linha - i][coluna + i] = palavra[i]

        elif direcao == Direcoes.DIAGONAL_INVERTIDA_OPOSTA:
            for i in range(len(palavra)):
                self.grade[linha - i][coluna - i] = palavra[i]
    
    def preencher_espacos_vazios(self):
        letras = ascii_uppercase
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                if self.grade[i][j] == ' ':
                    self.grade[i][j] = random.choice(letras)
    
    def cria_caca_palavras(self, palavras):
        if self.dificuldade == Dificuldade.FACIL:
            direcoes = [Direcoes.HORIZONTAL, Direcoes.VERTICAL]
        elif self.dificuldade == Dificuldade.MEDIO:
            direcoes = [Direcoes.HORIZONTAL, Direcoes.VERTICAL, Direcoes.DIAGONAL, Direcoes.DIAGONAL_INVERTIDA]
        elif self.dificuldade == Dificuldade.DIFICIL:
            direcoes = [Direcoes.HORIZONTAL, Direcoes.VERTICAL, Direcoes.DIAGONAL, Direcoes.DIAGONAL_INVERTIDA, Direcoes.VERTICAL_OPOSTA, Direcoes.HORIZONTAL_OPOSTA]
        elif self.dificuldade == Dificuldade.SUPER_DIFICIL:
            direcoes = list(Direcoes)

        palavras_adicionadas = []
        palavras_nao_colocadas = []

        for palavra in palavras:
            colocada = False
            tentativas = 0
            max_tentativas = 1000 * self.tamanho
            while not colocada and tentativas < max_tentativas:
                tentativas += 1
                direcao = random.choice(direcoes)
                linha = random.randint(0, self.tamanho - 1)
                coluna = random.randint(0, self.tamanho - 1)
                
                if self.pode_colocar_palavra(palavra, linha, coluna, direcao):
                    self.coloca_palavra(palavra.upper(), linha, coluna, direcao)
                    colocada = True
                    palavras_adicionadas.append(palavra)
                    tentativas = 0

            if not colocada:
                palavras_nao_colocadas.append(palavra)

        self.preencher_espacos_vazios()
        return self.grade, palavras_adicionadas, palavras_nao_colocadas
