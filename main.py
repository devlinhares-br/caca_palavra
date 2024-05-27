import random
import string
from PIL import Image, ImageDraw, ImageFont

SM = 10
MD = 15
LG = 20

HORIZONTAL = 'h'
VERTICAL = 'v'
DIAGONAL = 'd'

FACIL = 'facil'
MEDIO = 'medio'


def criar_grade(tamanho:int):
    return [[' ' for _ in range(tamanho)] for _ in range(tamanho)]

def pode_colocar_palavra(grade:list, palavra:str, linha:int, coluna:int, direcao:str, tamanho:int):
    if direcao == HORIZONTAL:
        if coluna + len(palavra) > tamanho:
            return False
        for i in range(len(palavra)):
            if grade[linha][coluna + i] != ' ' and grade[linha][coluna + i] != palavra[i]:
                return False
            
    elif direcao == VERTICAL:
        if linha + len(palavra) > tamanho:
            return False
        for i in range(len(palavra)):
            if grade[linha + i][coluna] != ' ' and grade[linha + i][coluna] != palavra[i]:
                return False
            
    elif direcao == DIAGONAL:
        if coluna + len(palavra) > tamanho or linha + len(palavra) > tamanho:
            return False
        for i in range(len(palavra)):
            if grade[linha + i][coluna + i] != ' ' and grade[linha + i][coluna + i] != palavra[i]:
                return False

    return True

def coloca_palavra(grade, palavra, linha, coluna, direcao):
    if direcao == HORIZONTAL:
        for i in range(len(palavra)):
            grade[linha][coluna + i] = palavra[i]

    elif direcao == VERTICAL:
        for i in range(len(palavra)):
            grade[linha + i][coluna] = palavra[i]

    elif direcao == DIAGONAL:
        for i in range(len(palavra)):
            grade[linha + i][coluna + i] = palavra[i]
    
    return grade
    

def preencher_espacos_vazios(grade, tamanho):
    letras = string.ascii_uppercase

    for i in range(tamanho):
        for j in range(tamanho):
            if grade[i][j] == ' ':
                grade[i][j] = random.choice(letras)

def cria_caca_palavras(palavras:list, tamanho:int=SM, dificuldade='facil'):
    grade = criar_grade(tamanho)
    if dificuldade == 'facil':
        direcoes = [HORIZONTAL, VERTICAL]
    elif dificuldade == 'medio':
        direcoes = [HORIZONTAL, VERTICAL, DIAGONAL]
    else:
        raise ValueError('Dificuldade inválida!\nDisponível dificuldades: [facil, medio]')
    palavras_adicionadas = []
    palavras_nao_colocadas = []

    for palavra in palavras:
        colocada = False
        tentativas = 0
        max_tentativas = 1000 * tamanho
        while not colocada and tentativas < max_tentativas:
            tentativas += 1
            direcao = random.choice(direcoes)
            linha = random.randint(0, tamanho - 1)
            coluna = random.randint(0, tamanho - 1)
            
            if pode_colocar_palavra(grade, palavra, linha, coluna, direcao, tamanho):
                grade = coloca_palavra(grade, palavra.upper(), linha, coluna, direcao)
                colocada = True
                palavras_adicionadas.append(palavra)
                tentativas = 0
        if not colocada:
            palavras_nao_colocadas.append(palavra)
    preencher_espacos_vazios(grade, tamanho)
    return grade, palavras_adicionadas, palavras_nao_colocadas

def gerar_imagem(grade, palavras_adicionadas, nome_arquivo='caca_palavras.png', title='Caça-Palavras'):
    tamanho = len(grade)
    cell_size = 30
    margin = 80

    img_width = tamanho * cell_size + 2 * margin
    img_height = tamanho * cell_size + 2 * margin + 100
    img = Image.new('RGB', (img_width, img_height), color='white')
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 24)
        title_font = ImageFont.truetype("arial.ttf", 36)  # Fonte maior para o título
    except IOError:
        font = ImageFont.load_default()
        title_font = ImageFont.load_default()

    x0 = margin
    y0 = margin + 100  # Ajuste para posicionar abaixo do título
    x1 = x0 + tamanho * cell_size
    y1 = y0 + tamanho * cell_size
    draw.rectangle([x0, y0, x1, y1], outline='black')

    for i in range(tamanho):
        for j in range(tamanho):
            x = margin + j * cell_size
            y = margin + 100 + i * cell_size  # Ajuste para posicionar abaixo do título
            if grade[i][j] != ' ':
                draw.text((x + 7, y + 5), grade[i][j], fill='black', font=font)

    # Escrever o título
    title_bbox = draw.textbbox(xy=(0, 0), text=title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text(((img_width - title_width) // 2, 10), title, fill='black', font=title_font)

    # Escrever as palavras para procurar na parte superior da imagem
    max_width = img_width - 2 * margin
    current_line = ""
    y_offset = 100  # Posição inicial do texto acima do caça-palavras

    for palavra in palavras_adicionadas:
        new_line = current_line + (palavra + " - ")
        text_bbox = draw.textbbox(xy=(0, 0), text=new_line, font=font)
        text_width = text_bbox[2] - text_bbox[0]

        if text_width > max_width:
            draw.text((margin, y_offset), current_line, fill='black', font=font)
            y_offset += 30
            current_line = palavra + " "
        else:
            current_line = new_line

    if current_line:
        draw.text((margin, y_offset), current_line, fill='black', font=font)

    img.save(nome_arquivo)

# Exemplo de uso:
palavras = ["PYTHON", "PROGRAMAÇÃO", "OBJETOS", "FUNCOES", "DADOS", "ALGORITIMOS", "ESTUDOS", "BOSS"]

grade, palavras_adicionadas, palavras_nao_adicionadas = cria_caca_palavras(palavras, LG, MEDIO)
gerar_imagem(grade, palavras_adicionadas)
