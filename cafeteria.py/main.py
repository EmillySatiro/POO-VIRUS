from Balcao import Cafeteria
from Cardapio import Itemcardapio

def main(): 
    cafeteria = Cafeteria()
    cafeteria.adicionar_item_cardapio(Itemcardapio("Café Expresso", 5.00))
    cafeteria.adicionar_item_cardapio(Itemcardapio("Café com leite ", 7.00))
    cafeteria.adicionar_item_cardapio(Itemcardapio("Café puro", 3.00))
    cafeteria.adicionar_item_cardapio(Itemcardapio("Café gelado", 8.00))

    while True: 
        print("\n Menu: ")
        print("1. Mostrar cardápio")
        print("2. Fazer pedido(Área do Cliente)")
        print("3. Mostrar pedidos(Area do cliente)")
        print("4. Login Adm")
        print("5. Login Funcinário")
        print("6. Sair")
        
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == '1': 
            cafeteria.mostrar_cardapio()
        elif escolha =='2':
            cafeteria.fazer_pedido()
        elif escolha =='3':
            cafeteria.mostrar_pedidos()
        elif escolha == '4': 
            if cafeteria.autenticar_usuario("administrador"):
                while True: 
                    print("\n Área Administrativa: ")
                    print("1. Mostrar relátorio administartivo")
                    print("2. Sair")
                    
                    adm_escolha = input("Escolha opção: ").strip()
                    
                    if adm_escolha == '1':
                        cafeteria.mostrar_relatorio()
                    elif adm_escolha ==' 2':
                        break
                    else: 
                        print("Opção invalida, Tente novamente.")
            else:  
                print("Senha de administrador incorreta")
        elif escolha == '5': 
            if cafeteria.autenticar_usuario("funcionario"):
                while True: 
                    print("\n Área do funcionário: ")
                    print("1. Atualizar status do pedido")
                    print("2. sair")
                    
                    fun_escolha = input("Escolha uma opção:")
                    
                    if fun_escolha == '1': 
                        try: 
                            index = int(input("Digite o número do pedido para atualizar: ")) -1
                            status = input("Digite o novo status(Entregue/Pago)").strip()
                            cafeteria.atualizar_status_pedido(index, status)
                        except ValueError:
                            print("Valor invalido, Digite um número para o pedido.")
                    elif fun_escolha =='2': 
                        break
                    else : 
                        print("Opção invalida. Tente novamente.")
            else: 
                print("Senha de funcionário incorreta.")
        elif escolha == '6':
            break
        else: 
            print("Opção invalida. tente novamente")

if __name__=="__main__": 
    main()