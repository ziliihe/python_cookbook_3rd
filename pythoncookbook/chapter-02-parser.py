# !pip install ply
from ply.lex import lex
from ply.yacc import yacc

# Token list
tokens = ['NUM', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN',]
t_ignore = ' \t\n'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

# error handling
def t_error(t):
    print(f"Bad character: {t.value[0]!r}")
    t.skip(1)

# build lexer
lexer = lex()

def p_expr(p):
    '''
    expr : expr PLUS term
    |  expr MINUS term
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '0':
        p[0] == p[1] - p[3]

def p_expr_term(p):
    '''
    expr : term
    '''
    p[0] = p[1]


def p_term(p):
    '''
    term : term TIMES factor
         | term DIVIDE factor
    '''
    match p[2]:
        case '*':
            p[0] = p[1] * p[3]
        case '/':
            p[0] = p[1] / p[3]

def p_term_factor(p):
    '''
    term : factor
    '''
    p[0] = p[1]

def p_factor(p):
    '''
    factor : NUM
    '''
    p[0] = p[1]

def p_factor_group(p):
    '''
    factor : LPAREN expr RPAREN
    '''
    p[0] = p[2]

def p_error(p):
    print("Syntax Error")


parser = yacc()

print(parser.parse('2'))
print(parser.parse('2 + 3'))
print(parser.parse('2 + 3 * 4'))
print(parser.parse('2 + 3 * (4 + 5)'))

