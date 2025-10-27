import ply.lex as lex

tokens = (
    'INT','PARENTESES_ABRIR','PARENTESES_FECHAR',
    'SOMA','DIFERENCA','MULTIPLICACAO','DIVISAO'
)

#tokens
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_PARENTESES_ABRIR(t):
    r'\('
    return t

def t_PARENTESES_FECHAR(t):
    r'\)'
    return t

def t_SOMA(t):
    r'\+'
    return t

def t_DIFERENCA(t):
    r'-'
    return t

def t_MULTIPLICACAO(t):
    r'\*'
    return t

def t_DIVISAO(t):
    r'/'
    return t

# ignorar espaços e tabs

t_ignore = ' \t'

# tocar de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}' na linha {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()
