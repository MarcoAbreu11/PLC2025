
def verificar_stock(stock):
    produtos_da_maquina_vazios = ''
    
    for produto in stock:
        if produto['quant'] == 0:
            if produtos_da_maquina_vazios:
                produtos_da_maquina_vazios += ", "
            produtos_da_maquina_vazios += str(produto['cod'])
    
    if not produtos_da_maquina_vazios:
        return 'Stock carregado'
    else:
        return f"Produtos com códigos {produtos_da_maquina_vazios} não têm stock"