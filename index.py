#--------------------------------------------------------- FUNÇÕES ---------------------------------------------------------#

#FUNÇÃO 01 SOMAR:
def somar(a, b, c): 
    soma = a + b + c
    print(f"{soma}")
somar(1,8,9)


#FUNÇÃO 02 DISPONIVEL:
lista_espera = ['Daniel', 'Marcos', 'Maria']
def disponivel():
    for x in lista_espera:
        print('Ola', x, 'O seu produto esta disponivel em estoque.')
disponivel()


#FUNÇÃO 03 CONTADOR:
#o "*" tem a função de desempacotar, é o mesmo que dizer para o python que não sabemos quantos números irão vir.
def contador(* numero):
    tamanho = len(numero)
    print(f"O valores de entrada foram: {numero} e sua quantidade é: {tamanho}")
contador(9,8,2,3,4,2)


#FUNÇÃO 04 EQUAÇÃO DO SEGUNDO GRAU:
def equacao2grau(a, b, c):
    D = (b**2 - 4*a*c)
    x1 = (-b + D**(1/2)) / (2*a)
    x2 = (-b - D**(1/2)) / (2*a)
    print(f"{x1} e {x2}")
equacao2grau(1 , 2 , -15)














