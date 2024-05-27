from enum import Enum

class Direcoes(Enum):
    HORIZONTAL = 'h'
    VERTICAL = 'v'
    DIAGONAL = 'd'
    DIAGONAL_INVERTIDA = 'di'
    HORIZONTAL_OPOSTA = 'h_o'
    VERTICAL_OPOSTA = 'v_o'
    DIAGONAL_OPOSTA = 'd_o'
    DIAGONAL_INVERTIDA_OPOSTA = 'di_o'