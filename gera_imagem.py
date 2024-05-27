from PIL import Image, ImageDraw, ImageFont

class GeraImagem:
    def __init__(self, grade, palavras_adicionadas, titulo="Caça Palavras", fonte_titulo="fonts/Roboto-Black.ttf", fonte_caca_palavras="fonts/Roboto-Black.ttf", fonte_palavras='fonts/Roboto-Light.ttf'):
        self.grade = grade
        self.palavras_adicionadas = palavras_adicionadas
        self.titulo = titulo
        self.fonte_titulo = fonte_titulo
        self.fonte_caca_palavras = fonte_caca_palavras
        self.fonte_palavras = fonte_palavras

    def gerar_imagem(self, nome_arquivo='caca_palavras.png'):
        tamanho = len(self.grade)
        cell_size = 30
        margin = 80

        img_width = tamanho * cell_size + 2 * margin
        img_height = tamanho * cell_size + 2 * margin + 100
        img = Image.new('RGB', (img_width, img_height), color='white')
        draw = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype(self.fonte_caca_palavras, 24)
            title_font = ImageFont.truetype(self.fonte_titulo, 36)  # Fonte maior para o título
            fonte_palavras = ImageFont.truetype(self.fonte_palavras, 24)  # Fonte maior para o título

        except IOError:
            font = ImageFont.load_default()
            title_font = ImageFont.load_default()
            fonte_palavras = ImageFont.load_default()

        x0 = margin
        y0 = margin + 100  # Ajuste para posicionar abaixo do título
        x1 = x0 + tamanho * cell_size
        y1 = y0 + tamanho * cell_size
        draw.rectangle([x0, y0, x1, y1], outline='black')

        for i in range(tamanho):
            for j in range(tamanho):
                x = margin + j * cell_size
                y = margin + 100 + i * cell_size  # Ajuste para posicionar abaixo do título
                if self.grade[i][j] != ' ':
                    draw.text((x + 7, y + 5), self.grade[i][j], fill='black', font=font)

        # Escrever o título
        title_bbox = draw.textbbox(xy=(0, 0), text=self.titulo, font=title_font)
        title_width = title_bbox[2] - title_bbox[0]
        draw.text(((img_width - title_width) // 2, 10), self.titulo, fill='black', font=title_font)

        # Escrever as palavras para procurar na parte superior da imagem
        max_width = img_width - 2 * margin
        current_line = ""
        y_offset = 100  # Posição inicial do texto acima do caça-palavras

        for palavra in self.palavras_adicionadas:
            new_line = current_line + (palavra + " - ")
            text_bbox = draw.textbbox(xy=(0, 0), text=new_line, font=fonte_palavras)
            text_width = text_bbox[2] - text_bbox[0]

            if text_width > max_width:
                draw.text((margin, y_offset), current_line, fill='black', font=fonte_palavras)
                y_offset += 30
                current_line = palavra + " - "
            else:
                current_line = new_line
        current_line = current_line[:-2]
        if current_line:
            draw.text((margin, y_offset), current_line, fill='black', font=fonte_palavras)

        img.save(nome_arquivo)

