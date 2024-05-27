from gera_grade import GeraGrade
from gera_imagem import GeraImagem
from size import Size
from dificuldade import Dificuldade


palavras = ["python", "algoritimo", "grade", "caça", "palavras", 'banana']
gerador = GeraGrade(tamanho=Size.MD.value, dificuldade=Dificuldade.MEDIO)
grade, palavras_adicionadas, palavras_nao_adicionadas = gerador.cria_caca_palavras(palavras)


imagem = GeraImagem(grade, palavras_adicionadas)
imagem.gerar_imagem()
print(palavras_nao_adicionadas)