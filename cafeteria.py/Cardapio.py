from abc import ABC, abstractmethod

class Produto (ABC):
    
    @abstractmethod
    def get_preco(self):
        pass
    
    @abstractmethod
    def get_descricao(self):
        pass
    
class Itemcardapio(Produto):
    
    def __init__(self, descricao, preco):
        self._descricao= descricao
        self._preco = preco
        
    def get_descricao(self):
        return self._descricao
    
    def get_preco(self):
        return self._preco

    def set_descricao(self, descricao):
        self._descricao = descricao

    def set_preco(self, preco):
        self._preco = preco


class Pedido:
    STATUS_EM_PROCESSAMENTO = "Em pocessamento "
    STATUS_ENTREGUE = "Entregue"
    STATUS_PAGO = "Pago"
    
    def __init__(self, nome_cliente = None, cpf_cliente = None):
        self._itens = []
        self._status = Pedido.STATUS_EM_PROCESSAMENTO
        self._valor_pago = 0.0
        self._nome_cliente = nome_cliente
        self._cpf_cliente = cpf_cliente
    
    def adicionar_item(self,  item):
        if isinstance(item, Itemcardapio): 
            self._itens.append(item)
        else:
            raise ValueError("O item seve existir!!")
        
    def Remover_item(self, item: Itemcardapio):
        if item in self._itens:
            self._itens.remove(item)
        else:
            print("\t\n Item não encontrado no pedido!!")
            
    def calcular_total(self):
        return sum(item.get_preco() for item in self._itens)
    
    def marcar_entregue(self):
        if self._status == Pedido.STATUS_EM_PROCESSAMENTO:
            self._status = Pedido.STATUS_ENTREGUE
            print("\t\n O pedidofoi entregue !!")
        else: 
            print("\t\n O pedido já foi entregue e pago!!")
            
    def marcar_pago(self):
        if self._status == Pedido.STATUS_ENTREGUE:
            self._status = Pedido.STATUS_PAGO
            self._valor_pago = self.calcular_total()
            self.gerar_nota_fiscal()
            print("\t\n O pedidofoi Pago !!")
           
           
        else: 
            print("\t\n O pedido deve estar entregue para ser marcado como pago..")
            
    def get_status(self):
        return self._status
    
    def get_valor_pago(self):
        return self._valor_pago
    
    def gerar_nota_fiscal(self):
        nota= (f"============================\n"
                f"Nota Fiscal\n"
                f"Cliente: {self._nome_cliente}\n"
                f"CPF: {self._cpf_cliente}\n"
                f"Total: {self.calcular_total():.2f}\n"
                f"Status : {self._status}\n"
                f"============================")
        print(nota)
        
    def get_nome_cliente(self):
        return self._nome_cliente 
    
    def get_cpf_cliente(self):
        return self._cpf_cliente
    
    def get_itens(self):
        return self._itens
    
    