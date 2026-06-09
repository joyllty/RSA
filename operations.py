
# gcd(a, b)  greatest common divisor
'''
saber se dois numeros são coprimos (mdc = 1)
'''
# extended_gcd(a, b) 
'''
além do mdc, retorna dois coeficientes x e y pra calcular o inverso modular
a*x + b*y = mdc(a, b)
'''
# modular_inverse(e, phi_n)
'''
usa o extended pra encontrar d tal que e*d congru 1 mod fi(n)
basicamente encontrar a chave privada
'''
def is_prime(n):
    '''
    verifica se um número é primo
    '''
    
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    divider = 3
    while divider * divisor <= n:
        if n % divider == 0:
            return False
        divider += 2
        
        return True


# mod_pow(base, exp, mod)
'''
calcula base^exp mod n, ver depois se vai ser eficiente pra cifrar mensagens com chaves com muuitos bits
'''


