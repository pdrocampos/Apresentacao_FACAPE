class Estacionamento:
    veiculos = []

    #Construtor
    @classmethod
    def __init__(self, precoInicial, precoPorHora):
        self.precoInicial = precoInicial
        self.precoPorHora = precoPorHora

    @classmethod
    def adicionarVeiculo(self):
        print("")
        print("Digite a placa do veículo para estacionar:")
        self.veiculos.append(input())
    
    @classmethod
    def removerVeiculo(self):
        print("")
        print("Digite a placa do veículo para remover:")
        placa = ""
        placa = input()

        if any(x == placa for x in self.veiculos):
            print("")
            print("Digite a quantidade de horas que o veículo permaneceu estacionado:")
            horas = 0
            valorTotal = 0
            horas = float(input())
            valorTotal = self.precoInicial + (self.precoPorHora * horas)
            self.veiculos.remove(placa)
            print("")
            print(f"O veículo {placa} foi removido e o preço total foi de: R$ {valorTotal}")
        else:
            print("")
            print("Desculpe, esse veículo não está estacionado aqui. Confira se digitou a placa corretamente")
    
    @classmethod
    def listarVeiculos(self):
        if any(self.veiculos):
            print("")
            print("Os veículos estacionados são:")
            contadorFor = 1
            for item in self.veiculos:
                print(f"Posição Nº{contadorFor} - {item}")
                contadorFor+=1
        else:
            print("")
            print("Não há veículos estacionados.")


print("")
print("Seja bem vindo ao sistema de estacionamento! Digite o preço inicial:")
precoInicial = float(input())
print("")
print("Agora digite o preço por hora:")
precoPorHora = float(input())

es = Estacionamento(precoInicial, precoPorHora)

exibirMenu = True

while exibirMenu:
    print("")
    print("Digite a sua opção: ")
    print("1 - Cadastrar veículo")
    print("2 - Remover veículo")
    print("3 - Listar veículos")
    print("4 - Encerrar")

    match (input()):

        case "1":
            es.adicionarVeiculo()
            
        case "2":
            es.removerVeiculo()
            
        case "3":
            es.listarVeiculos()
            
        case "4":
            exibirMenu = False
            break
        case _:
            print("Opção inválida")
            
    print("")        
    print("Pressione uma tecla para continuar")
    input()

print("")
print("O programa se encerrou!")