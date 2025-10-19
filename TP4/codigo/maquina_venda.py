from carregar_guardar_stock import carregar_stock, guardar_stock
from verificar_stock import verificar_stock
from data_atual import data_atual
from tarefas_da_maquina import *

def main():
    stock = carregar_stock()
    
    if stock is None:
        print('maq: Não foi possível carregar o stock')
        return

    saldo = 0.0
    
    # Mensagem inicial conforme enunciado
    status_stock = verificar_stock(stock)
    print(f'maq: {data_atual}, {status_stock}, Estado atualizado.')
    print('maq: Bom dia. Estou disponível para atender o seu pedido.')

    while True:
        try:
            comando = input(">> ").strip()
            
            if comando.upper() == 'LISTAR':
                listar_produtos(stock)
                
            elif comando.upper().startswith('MOEDA'):
                partes = comando.split(' ', 1)
                if len(partes) > 1:
                    moedas_input = partes[1].rstrip(' .')
                    moedas_inseridas = inserir_moedas(moedas_input)
                    saldo_adicional = calcular_saldo(moedas_inseridas)
                    saldo = round(saldo + saldo_adicional, 2)
                    print(f"maq: Saldo = {formatar_saldo(saldo)}")
                else:
                    print("maq: Formato inválido. Use: MOEDA 1e, 50c, 20c, ...")
                    
            elif comando.upper().startswith('SELECIONAR'):
                resultado, saldo, stock = selecionar_produto(comando.upper(), saldo, stock)
                print(resultado)
                
            elif comando.upper() == 'SAIR':
                resultado_sair = sair(saldo)
                guardar_stock(stock)
                print(resultado_sair)
                break
                
            else:
                print("maq: Comando não reconhecido. Comandos disponíveis: LISTAR, MOEDA, SELECIONAR, SAIR")
                
        except KeyboardInterrupt:
            print("\nmaq: Programa interrompido pelo utilizador")
            guardar_stock(stock)
            break
        except Exception as e:
            print(f"maq: Ocorreu um erro - {e}")

if __name__ == "__main__":
    main()