#class
#Systaxe

#propriedades de uma pc: Marca, Memoria Ram, Placa de Video
class Computador:
    #_init_(self) inicializa as propriedades, parar podermos acessar no futuro
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    
    def Ligar(self):
        print('Ligando')
    
    def Desligar(self):
        print('Desligando')

    def ExibirInformacoesdoPC(self):
        print(self.marca +" "+ self.memoria_ram +" "+ self.placa_de_video)

computador1 = Computador('Lenovo', '4GB', 'Nvidia')
computador1.Ligar()
computador1.Desligar()
print(computador1.ExibirInformacoesdoPC())

