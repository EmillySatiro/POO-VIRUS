from abc import ABC, abstractmethod

class Acao(ABC):
    @abstractmethod
    def executar(self, virus):
        pass

class InvadirSistema(Acao):
    def __init__(self, sistema):
        self.sistema = sistema
        
    def executar(self, virus):
        virus.invadir_sistema(self.sistema)
        
class Alimemtar(Acao):
    def __init__(self, informacoes):
        self.informacao = informacoes
    
    def executar(self, virus):
        virus.alimetar(self.informacao)
        
class Dormir(Acao):
    def executar(self, virus):
        virus.dormir()
        
class Evoluir(Acao):
    def executar(self, virus):
        virus.evoluir()
        
class Virus:
    def __init__(self, nome):
        self.nome = nome 
        self.forca = 50 
        self.fome = 50 
        self.energia = 100
        self.bitcondes = 0
        self.nivel = 1
        
    # metodos a implementar 
    def invadir_sistema(self, sistema):
        """
        Realiza a invasão em um sistema
        Aumenta a força do vírus e a fome
        Adiciona bitcondes como recompensa
        """
        pass
    
    def Alimentar(self,informaçaõ):
        """
        Consome uma quantidade de informações para reduzir a fome do vírus. 
        Reduzida de acordo com a quantidade de informações fornecidas. 
        Garantir que a fome não fique negativa.
        """
        pass
    
    def dormir(self):
        """
        Recupera a energia do vírus. 
        O vírus deve aumentar sua energia a um valor máximo (100).
        """
        pass
    
    def evoluir(self):
        """
        Aumenta o nível do vírus. 
        Aumentar também a força e desbloquear novas habilidades.
        """
        pass
    
    def status(self):
        """
        Retorna uma string formatada com o estado atual do vírus, 
        incluindo nome, força, fome, energia, bitcondes e nível.
        """
        pass
    
    # talvez farei uma de implementar uma habilidade 
    
    
class Sistema:
    def __init__(self, nome, complexidade, recompensa, tempo_parar_reparar):
        self.nome = nome 
        self.complexidade = complexidade
        self.recompensa = recompensa
        self.tempo_para_reparar = tempo_parar_reparar
        self.reparado = False
        
    def reparar(self):
        """
        Simula a recuperação do sistema após uma invasão. 
        Alterar o estado de 'reparado' para True após um certo tempo.
        """
        pass

    def complexidade_atual(self):
        """
        Retorna a complexidade atual do sistema, que pode ser alterada ao longo do tempo.
        """
        pass
    
class Jogo:
    def __init__(self, nome_virus) :
        self.virus = Virus(nome_virus)
        self.sistemas = [
            Sistema(" Sistema A", 30,20,5),
            Sistema(" Sistema B", 30,20,5),
            Sistema(" Sistema C", 30,20,5),
            Sistema(" Sistema D", 30,20,5),
            Sistema(" Sistema E", 30,20,5),
        ]
        self.tempo = 0
        
    def executar_acao(self, acao):
        acao.executar(self.virus)
        
    def avancar_tempo(self):
        self.tempo += 1
        self.virus.fome += 5
        self.virus.energia -= 5
        print(f'Tempo avançado . Fome: {self.virus.fome}, Energia: {self.virus.energia}')
    
    def status(self):
        print(self.virus.status())
        for sistema in self.sistemas:
            print(f'Sistema: {sistema.nome}, Complexidade: {sistema.complexidade}')
            
    def verificar_virus(self):
        '''
        verificar se o bichinho ta bem de saude 
        '''
        pass
    
    def verificar_desempenho(self):
        ''' gerar um relatorio de como virus se saiu // talvez '''
    pass