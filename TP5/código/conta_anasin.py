from conta_analex import lexer

prox_simb = ('Erro', 0, 0)

def parserError(simb):
    print("Erro sintático, token inesperado: ", simb)

def rec_term(simb):
    global prox_simb
    if prox_simb and prox_simb.type == simb:
        prox_simb = lexer.token()
    else:
        parserError(prox_simb)

'''
p1: Exp    -> Term OpExp
p2: OpExp  -> Op Exp | ε
p3: Term   -> INT | PARENTESES_ABRIR Exp PARENTESES_FECHAR
p4: Op     -> SOMA | DIFERENCA | MULTIPLICACAO | DIVISAO
'''

def rec_Op():
    if prox_simb.type in ['SOMA','DIFERENCA','MULTIPLICACAO','DIVISAO']:
        operador_atual = prox_simb.type
        print(f'p4: Op -> {operador_atual}')
        rec_term(prox_simb.type)
        print(f'Reconheci p4: Op -> {operador_atual}')
    else:
        parserError(prox_simb)

def rec_OpExp():
    global prox_simb
    if prox_simb and prox_simb.type in ['SOMA','DIFERENCA','MULTIPLICACAO','DIVISAO']:
        print('p2: OpExp -> Op Exp')
        rec_Op()
        rec_Exp()
        print('Reconheci p2: OpExp -> Op Exp')
    else:
        print('p2: OpExp -> ε')
        return

def rec_Term():
    global prox_simb
    if prox_simb.type == 'INT':
        print('p3: Term -> INT')
        rec_term('INT')
        print('Reconheci p3: Term -> INT')
    elif prox_simb.type == 'PARENTESES_ABRIR':
        print('p3: Term -> PARENTESES_ABRIR Exp PARENTESES_FECHAR')
        rec_term('PARENTESES_ABRIR')
        rec_Exp()
        rec_term('PARENTESES_FECHAR')
        print('Reconheci p3: Term -> PARENTESES_ABRIR Exp PARENTESES_FECHAR')
    else:
        parserError(prox_simb)

def rec_Exp():
    global prox_simb
    print('p1: Exp -> Term OpExp')
    rec_Term()
    rec_OpExp()
    print('Reconheci p1: Exp -> Term OpExp')

def rec_Parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    if prox_simb == None:
        return
    rec_Exp()
    print("That's all forks")