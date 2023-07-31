'''
Crie uma função chamada encontra_primos que receba dois números inteiros positivos como parâmetros e retorne uma lista de todos os números primos entre os dois números, 
incluindo os próprios números fornecidos.
Por exemplo, se a função for chamada com encontra_primos(10, 20), ela deve retornar [11, 13, 17, 19], 
já que esses são os únicos números primos entre 10 e 20.

Dicas:

- Você pode usar a função is_prime da biblioteca sympy para verificar se um número é primo ou não. Para usá-lo, 
você precisa instalá-lo com o comando pip install sympy e, em seguida, importá-lo com from sympy import isprime.

- Você pode criar uma lista vazia e adicionar cada número primo encontrado à lista usando o método append.

- Lembre-se de incluir os próprios números fornecidos na lista se eles forem primos.
'''

from sympy import isprime

def encontra_primos(x, y):
    intervalo = list(range(x, (y+1)))
    primos = []
    for i in intervalo:
        if isprime(i):
            primos.append(i)
    return primos

print(encontra_primos(11,58))