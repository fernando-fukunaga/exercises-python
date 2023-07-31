'''
Exercícios:

4.1 - Escreva o código para a função soma, vista anteriormente:
'''
from typing import List


def soma(lista: List[int]) -> int:
    if lista == []:
        return 0
    
    return lista[0] + soma(lista[1:])


'''
4.2 - Escreva uma função recursiva que conte o número de itens em uma lista:
'''
def contador_lista(lista: List) -> int:
    if lista == []:
        return 0
    
    return 1 + contador_lista(lista[1:])


'''
4.3 - Encontre o valor mais alto em uma lista:
'''
def valor_mais_alto(lista: List[int]) -> int:
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    
    mais_alto_tirando_indice = valor_mais_alto(lista[1:])
    return lista[0] if lista[0] > mais_alto_tirando_indice else mais_alto_tirando_indice