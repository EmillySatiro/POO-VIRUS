from Balcao import Cafeteria
from Cardapio import Itemcardapio

def main(): 
    cafeteria = Cafeteria()
   
    cafeteria.adicionar_item_cardapio(Itemcardapio("Cappuccino", 6.00))
    cafeteria.adicionar_item_cardapio(Itemcardapio("Mocha", 7.50))
    cafeteria.adicionar_item_cardapio(Itemcardapio("Chá Preto", 4.00))
    cafeteria.adicionar_item_cardapio(Itemcardapio("Chá Verde", 4.50))
    cafeteria.adicionar_item_cardapio(Itemcardapio("Croissant", 3.50))
    cafeteria.adicionar_item_cardapio(Itemcardapio("Bolo de Chocolate", 5.50))
    cafeteria.adicionar_item_cardapio(Itemcardapio("Biscoito Amanteigado", 2.50))
    cafeteria.adicionar_item_cardapio(Itemcardapio("Sanduíche Natural", 6.50))
    cafeteria.adicionar_item_cardapio(Itemcardapio("Panqueca com Mel", 5.00))
    cafeteria.adicionar_item_cardapio(Itemcardapio("Smoothie de Frutas", 6.00))
    cafeteria.adicionar_item_cardapio(Itemcardapio("Milkshake de Baunilha", 6.50))
    cafeteria.adicionar_item_cardapio(Itemcardapio("Espresso Duplo", 4.50))
    cafeteria.adicionar_item_cardapio(Itemcardapio("Latte Macchiato", 5.50))
    cafeteria.adicionar_item_cardapio(Itemcardapio("Affogato", 6.00))


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
            cafeteria.mostrar_pedidos_cliente()
        elif escolha == '4': 
           
            if cafeteria.autenticar_usuario("administrador"):
                while True: 
                    print("\nÁrea Administrativa: ")
                    print("1. Mostrar relatório administrativo")
                    print("2. Alterar senha do administrador")
                    print("3. Alterar senha de funcionário")
                    print("4. Mostrar todos os pedidos")
                    print("5. Sair")

                    adm_escolha = input("Escolha uma opção: ").strip()

                    if adm_escolha == '1':
                        cafeteria.mostrar_relatorio()
                    elif adm_escolha == '2':
                        cafeteria.alterar_senha_admin()
                    elif adm_escolha == '3':
                        cafeteria.alterar_senha_funcionario()
                    elif adm_escolha == '4':
                        cafeteria.mostrar_pedidos()
                    elif adm_escolha == '5':
                        break
                    else:
                        print("Opção inválida, tente novamente.")
            else:
                print("Senha de administrador incorreta")
        elif escolha == '5': 
            if cafeteria.autenticar_usuario("funcionario"):
                while True: 
                    print("\n Área do funcionário: ")
                    print("1. Atualizar status do pedido")
                    print("2. Mostrar todo os pedidos feitos: ")
                    print("3. Procurar dados de um pedido: ")
                    print("4. Editar cardapio")
                    print("5. sair")
                    
                    fun_escolha = input("Escolha uma opção:")
                    
                    if fun_escolha == '1': 
                        try: 
                            index = int(input("Digite o número do pedido para atualizar: ")) -1
                            status = input("Digite o novo status(Entregue/Pago)").strip()
                            cafeteria.atualizar_status_pedido(index, status)
                        except ValueError:
                            print("Valor invalido, Digite um número para o pedido.")
                    elif fun_escolha =='2':
                        cafeteria.mostrar_pedidos()
                    elif fun_escolha =='3':
                        cafeteria.mostrar_pedidos_cliente()
                    elif fun_escolha == '4': 
                        
                        while True: 
                            print("\n Edição de cardapio: ")
                            print("1. Editar item")
                            print("2. adicionar item ao cardapio")
                            print("3. Excluir item do cardapio")
                            print("4. sair")
                            
                            escolhaa = input("Escolha opção: ").strip()
                            
                            if escolhaa == '1':
                                cafeteria.editar_item_cardapio()
                            elif escolhaa ==' 2':
                                cafeteria.adicionar_iten_cardapio_funcionari()
                            elif escolhaa == '3':
                                cafeteria.excluir_item_cardapio()
                            elif escolhaa == '4': 
                                break
                            else: 
                                print("Opção invalida, Tente novamente.")
         
                    elif fun_escolha =='5': 
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