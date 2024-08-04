from Cardapio import Itemcardapio
from Cardapio import Pedido

class Cafeteria:
    def __init__(self):
        self._cardapio = {}
        self._pedido = []
        self._total_vendas = 0.0
        self._senha_admin = "123"
        self._senha_funcionario = "321"
        self._usuarios_funcionario = {"funcionario": self._senha_funcionario}
        
    def adicionar_item_cardapio(self, item :Itemcardapio): 
        self._cardapio[item.get_descricao()] = item
        
    def mostrar_cardapio(self): 
        print("\t\n =================================")
        print(f'\t\n Cardápio: ')
        for descricao, item in self._cardapio.items():
            print(f"\t\n {descricao}: R${item.get_preco():.2f}")
        print("\t\n =================================")
        
    def fazer_pedido(self):
        if not self._cardapio:
            print("O cardápio está vazio!")  
            return

        nome_cliente = input("Digite seu nome: ").strip()
        cpf_cliente = input("Digite seu CPF: ").strip()
        pedido = Pedido(nome_cliente, cpf_cliente)
        itens_adicionados = False  

        while True:
            descricao = input("Digite o item que deseja adicionar ao pedido (ou 'sair' para finalizar): ").strip()
            if descricao.lower() == 'sair':
                if not itens_adicionados:  
                    print("Nenhum item válido foi adicionado ao pedido. Pedido não realizado.")
                    return
                break

            item = self._cardapio.get(descricao)
            if item:
                pedido.adicionar_item(item)
                itens_adicionados = True  
            else:
                print("Item não encontrado no cardápio. Por favor, tente novamente.")  # MUDANÇA

        
        print(f"Pedido finalizado. Total: R${pedido.calcular_total():.2f}")
        pedido.gerar_nota_fiscal()
        self._pedido.append(pedido) 
            
    def mostrar_pedidos(self): 
        print("\t\n =================================")
        print(f'\t\n Pedidos: ')
        for i, pedido in enumerate(self._pedido):
            status = pedido.get_status()
            valor_pago = pedido.get_valor_pago()
            print(f"\t\n Pedido {i +1}: Total: R${pedido.calcular_total():.2f}, Status: {status}, Valor pago: R${valor_pago:.2f}")
        print("\t\n =================================")
    
    def atualizar_status_pedido(self, index, status):
        try: 
            pedido = self._pedido[index]
            if status == 'Entregue':
                pedido.marcar_entregue()
            elif status == 'Pago':
                pedido.marcar_pago()
                self._total_vendas += pedido.get_valor_pago()
            else: 
                print("Status invalido!!")
        except IndexError: 
            print("Pedido não encontrado!!")
    
    def mostrar_relatorio(self):
        print("\t\n =================================")
        print(f"\t\n Relatório Administrativo: ")
        print(f"Total de vendas: R${self._total_vendas:.2f}")
        print(F"Total de Pedidos: {len(self._pedido)}")
        print("\t\n =================================")
        
    def autenticar_usuario(self, tipo): 
        senha = input(f"Digite a senha para {tipo}").strip()
        if tipo == "administrador":
            return senha == self._senha_admin
        elif tipo == "funcionario":
            return senha == self._senha_funcionario
        return False
        
                
            
    
            
        
        
        