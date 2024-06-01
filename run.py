from gera_grade import GeraGrade
from gera_imagem import GeraImagem
from size import Size
from dificuldade import Dificuldade


palavras = ["MATEUS", "GENESIS", "SALMOS", "ROMANOS", "JOAO", 'CONRINTIOS', 'PROVERBIOS', 'RUTE', 'AGEU', 'DANIEL', 'TITO', 'TIMOTIO']
gerador = GeraGrade(tamanho=Size.LG.value, dificuldade=Dificuldade.MEDIO)
grade, palavras_adicionadas, palavras_nao_adicionadas = gerador.cria_caca_palavras(palavras)


imagem = GeraImagem(grade, palavras_adicionadas, 'Livros da Biíblia')
imagem.gerar_imagem()
print(palavras_nao_adicionadas)