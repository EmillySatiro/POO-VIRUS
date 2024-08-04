from Cardapio import Itemcardapio
from Cardapio import Pedido

def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    
    def calcular_digito(cpf, peso):
        soma = sum(int(cpf[i]) * (peso - i) for i in range(len(cpf) - 2))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    digito1 = calcular_digito(cpf, 10)
    digito2 = calcular_digito(cpf, 11)
    
    return cpf[-2:] == f"{digito1}{digito2}"


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
    
    def adicionar_iten_cardapio_funcionari(self): 
        descricao = input("Digite a decrição do item: ").strip()
        preco = float(input("Digite o preço do item: "))
        item = Itemcardapio(descricao, preco)
        self.adicionar_item_cardapio(item)
        print("Item adicionado com sucesso!")
    
    def editar_item_cardapio_funcionario(self):
        if self.autenticar_usuario("funcionario"):
            descricao_atual = input("Digite a descrição do item que deseja editar: ").strip()
            item = self._cardapio.get(descricao_atual)
            
            if item:
                print(f"Item atual: {item.get_descricao()}, Preço: R${item.get_preco():.2f}")
                
                nova_descricao = input("Digite a nova descrição do item (ou pressione Enter para manter a atual): ").strip()
                novo_preco_input = input("Digite o novo preço do item (ou pressione Enter para manter o atual): ").strip()
                
                if nova_descricao:
                    item.set_descricao(nova_descricao)
                    
                if novo_preco_input:
                    try:
                        novo_preco = float(novo_preco_input.replace(',', '.'))  # Substitui vírgula por ponto
                        item.set_preco(novo_preco)
                    except ValueError:
                        print("Preço inválido. O preço não foi alterado.")
                        
                self._cardapio[item.get_descricao()] = item
                if nova_descricao and nova_descricao != descricao_atual:
                    del self._cardapio[descricao_atual]
                
                print("Item atualizado com sucesso!")
            else:
                print("Item não encontrado no cardápio.")
        else:
            print("Autenticação de funcionário falhou. Não é possível editar itens.")


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
        while True:
            cpf_cliente = input("Digite seu CPF: ").strip()
            if validar_cpf(cpf_cliente):
                break
            else:
                print("CPF inválido. Tente novamente.")
                
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
        
    def mostrar_pedidos_cliente(self):
        nome_cliente = input("Digite seu nome: ").strip()
        cpf_cliente = input("Digite seu CPF: ").strip()

        encontrado = False
        for pedido in self._pedido:
            if pedido.get_nome_cliente() == nome_cliente and pedido.get_cpf_cliente() == cpf_cliente:
                print("\t\n=================================")
                print(f"Pedido para {nome_cliente}:")
                print(f"Total: R${pedido.calcular_total():.2f}")
                print(f"Status: {pedido.get_status()}")
                print("\nItens do Pedido:")
                for item in pedido.get_itens():
                    print(f"- {item.get_descricao()}: R${item.get_preco():.2f}")
                print("\n=================================")
                encontrado = True
                break

        if not encontrado:
            print("Pedido não encontrado para o cliente fornecido.")

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
        senha = input(f"Digite a senha para {tipo}: ").strip()
        if tipo == "administrador":
            return senha == self._senha_admin
        elif tipo == "funcionario":
            return senha == self._senha_funcionario
        return False
    def excluir_item_cardapio(self):
        self.mostrar_cardapio()
        descricao = input("Digite a descrição do item que deseja excluir: ").strip()

        if descricao in self._cardapio:
            del self._cardapio[descricao]
            print(f"Item '{descricao}' foi excluído com sucesso do cardápio.")
        else:
            print(f"Item '{descricao}' não encontrado no cardápio.")
            
    def alterar_senha_admin(self):
        senha_atual = input("Digite a senha atual do administrador: ").strip()
        if senha_atual == self._senha_admin:
            nova_senha = input("Digite a nova senha para o administrador: ").strip()
            confirmar_senha = input("Confirme a nova senha: ").strip()
            if nova_senha == confirmar_senha:
                self._senha_admin = nova_senha
                print("Senha do administrador alterada com sucesso!")
            else:
                print("As senhas não coincidem. Tente novamente.")
        else:
            print("Senha atual incorreta.")
    
    def alterar_senha_funcionario(self):
        nome_funcionario = input("Digite o nome do funcionário: ").strip()
        if nome_funcionario in self._usuarios_funcionario:
            senha_atual = input("Digite a senha atual do funcionário: ").strip()
            if senha_atual == self._usuarios_funcionario[nome_funcionario]:
                nova_senha = input("Digite a nova senha para o funcionário: ").strip()
                confirmar_senha = input("Confirme a nova senha: ").strip()
                if nova_senha == confirmar_senha:
                    self._usuarios_funcionario[nome_funcionario] = nova_senha
                    print("Senha do funcionário alterada com sucesso!")
                else:
                    print("As senhas não coincidem. Tente novamente.")
            else:
                print("Senha atual incorreta.")
        else:
            print("Funcionário não encontrado.")
        

    
            
        
        
        