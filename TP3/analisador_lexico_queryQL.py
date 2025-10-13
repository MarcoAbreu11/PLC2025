import ply.lex as lex
import sys

def analizador_lexico_queryQL(entrada):
    tokens = (
        'SELECT', 'WHERE', 'FILTER', 'VARIABLE', 'PREFIXED_URI', 'DEFAULT_URI',
        'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN', 'DOT', 'STRING', 'INTEGER',
        'GREATER_THAN', 'LESS_THAN', 'EQUALS', 'NOT_EQUALS', 'LESS_EQUAL', 
        'GREATER_EQUAL', 'A_KEYWORD'
    )

    # tokens
    def t_NOT_EQUALS(t):
        r'!='
        return t

    def t_LESS_EQUAL(t):
        r'<='
        return t

    def t_GREATER_EQUAL(t):
        r'>='
        return t

    def t_SELECT(t):
        r'SELECT'
        return t

    def t_WHERE(t):
        r'WHERE'
        return t

    def t_FILTER(t):
        r'FILTER'
        return t

    def t_VARIABLE(t):
        r'\?[a-zA-Z_][a-zA-Z0-9_]*'
        return t

    def t_PREFIXED_URI(t):
        r'[a-zA-Z_@][a-zA-Z0-9_]*:[a-zA-Z_][a-zA-Z0-9_]*'
        return t

    def t_DEFAULT_URI(t):
        r':[a-zA-Z_][a-zA-Z0-9_]*'
        return t

    def t_LPAREN(t):
        r'\('
        return t

    def t_RPAREN(t):
        r'\)'
        return t

    def t_LBRACE(t):
        r'\{'
        return t

    def t_RBRACE(t):
        r'\}'
        return t

    def t_DOT(t):
        r'\.'
        return t

    def t_STRING(t):
        r'"[^"]*"'
        t.value = t.value[1:-1]
        return t

    def t_INTEGER(t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_GREATER_THAN(t):
        r'>'
        return t

    def t_LESS_THAN(t):
        r'<'
        return t

    def t_EQUALS(t):
        r'='
        return t

    def t_A_KEYWORD(t):
        r'\ba\b'
        return t

    # ignorar espaços e tabs
    t_ignore = ' \t'

    # trocar linha 
    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(t):
        print(f"Carácter ilegal '{t.value[0]}' na linha {t.lexer.lineno}")
        t.lexer.skip(1)

    lexer = lex.lex()
    lexer.input(entrada)

    print("Tokens encontrados:")
    for token in lexer:
        print(f'Line: {token.lineno}: {token.type} -> {token.value}')

entrada = sys.stdin.read()
output = analizador_lexico_queryQL(entrada)