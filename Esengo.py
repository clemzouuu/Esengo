from genereTreeGraphviz2 import printTreeGraph

reserved = {
   'if' : 'IF',
   'then' : 'THEN',
   'print' : 'PRINT',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'for' : 'FOR',
    'to' : 'TO',
    'from' : 'FROM'
   }

tokens = [
    'NAME','NUMBER','BRACERIGHT','BRACELEFT',
    'PLUS','MINUS','TIMES','DIVIDE',
    'LPAREN','RPAREN', 'COLON', 'AND', 'OR', 'EQUAL', 'EQUALS', 'LOWER','HIGHER',
    'HIGHEROREQUAL','LOWEROREQUAL','DIFFERENT'
    ]+list(reserved.values())

# Tokens
def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'NAME')    # Check for reserved words
    return t

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUAL  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_COLON = r';'
t_AND  = r'\&'
t_OR  = r'\|'
t_EQUALS  = r'=='
t_LOWER  = r'\<'
t_HIGHER  = r'\>'
t_BRACELEFT = r'\{'
t_BRACERIGHT = r'\}'
t_HIGHEROREQUAL = r'\>='
t_LOWEROREQUAL = r'\<='
t_DIFFERENT =  r'\!='

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()


# Parsing rules




def p_start(t):
    ''' start : bloc'''
    t[0] = ('start',t[1])
    print(t[0])
    printTreeGraph(t[0])
    #eval(t[1])
    evalInst(t[1])
names={}

def evalInst(t):
    print('evalInst', t)
    if type(t)!=tuple :
        print('warning')
        return
    if t[0]=='print' :
        print('CALC>', evalExpr(t[1]))
    if t[0]=='assign' :
        names[t[1]]=evalExpr(t[2])
    if t[0]=='bloc' :
        evalInst(t[1])
        evalInst(t[2])
    if t[0] == 'if':
        condition = evalExpr(t[1])
        if condition:
            evalInst(t[2])
    if t[0] == 'if-else':
        condition = evalExpr(t[1])
        if condition:
            evalInst(t[2])
        else:
            evalInst(t[3])
    if t[0] == 'while':
        condition = evalExpr(t[1])
        while condition:
            evalInst(t[2])
            condition = evalExpr(t[1])
    if t[0] == 'for':
        start = evalExpr(t[2])
        end = evalExpr(t[3])
        var_name = t[1]
        for value in range(start, end):
            names[var_name] = value
            evalInst(t[4])


def evalExpr(t):
    #print(t)
    if type(t) is not tuple:
        if type(t) is str:
            return names[t]
        return t
    if t[0] == '==': return evalExpr(t[1]) == evalExpr(t[2])
    if t[0] == '+': return evalExpr(t[1]) + evalExpr(t[2])
    if t[0] == '-': return evalExpr(t[1]) - evalExpr(t[2])
    if t[0] == '*': return evalExpr(t[1]) * evalExpr(t[2])
    if t[0] == '/':
        if t[2] == 0: return 0 ################### divide by 0
        return evalExpr(t[1]) / evalExpr(t[2])
    if(t[0]) == ">": return evalExpr(t[1]) > evalExpr(t[2])
    if (t[0]) == "<": return evalExpr(t[1]) < evalExpr(t[2])
    if (t[0]) == ">=": return evalExpr(t[1]) >= evalExpr(t[2])
    if (t[0]) == "<=": return evalExpr(t[1]) <= evalExpr(t[2])
    if (t[0]) == "!=": return evalExpr(t[1]) != evalExpr(t[2])





def p_line(t):
    '''bloc : bloc statement
            | statement '''
    if len(t)== 3 :
        t[0] = ('bloc',t[1], t[2])
    else:
        t[0] = ('bloc',t[1], 'empty')



def p_statement_assign(t):
    'statement : NAME EQUAL expression COLON'
    t[0] = ('assign',t[1], t[3])

def p_statement_print(t):
    'statement : PRINT LPAREN expression RPAREN COLON'
    t[0] = ('print',t[3])


def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression OR expression
                  | expression AND expression
                  | expression EQUALS expression
                  | expression LOWER expression
                  | expression HIGHER expression
                  | expression HIGHEROREQUAL expression
                  | expression LOWEROREQUAL expression
                  | expression DIFFERENT expression
                  | expression DIVIDE expression'''
    t[0] = (t[2],t[1], t[3])



def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]

def p_expression_name(t):
    'expression : NAME'
    t[0] = t[1]

def p_statement_if(t):
    'statement : IF expression BRACELEFT statement BRACERIGHT'
    t[0] = ('if', t[2], t[4])

def p_statement_if_else(t):
    'statement : IF expression BRACELEFT statement BRACERIGHT ELSE BRACELEFT statement BRACERIGHT'
    t[0] = ('if-else', t[2], t[4], t[8])

def p_statement_while(t):
    'statement : WHILE expression BRACELEFT statement BRACERIGHT'
    t[0] = ('while', t[2], t[4])

def p_statement_for(t):
    'statement : FOR NAME FROM expression TO expression BRACELEFT statement BRACERIGHT'
    t[0] = ('for', t[2], t[4], t[6], t[8])


def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

#s='1+2;x=4 if ;x=x+1;'
#s='print(1+2);x=4;x=x+1;'

# Ma partie

# 1 -> Votre interpréteur devra gérer les noms de variables à plusieurs caractères.
# 2 a -> affectation || b -> affichage d’expressions numériques
#s='maVariable = 12; print(maVariable);'


########### DOIT PRENDRE DES STRIG ? ##################


# 2 c -> instructions conditionnelles : implémenter le si-alors
#s='maVariable = 23041999; if maVariable < 1 {maVariable = 12;}print(maVariable);'

# 2 c -> instructions conditionnelles : implémenter si-alors-sinon
#s='maVariable = 23041999; if maVariable < 1 {maVariable = 12;} else {maVariable = 0;}print(maVariable);'


# 2 d -> structures itératives : implémenter le while
#s='maVariable = 10; while maVariable < 15 {maVariable = maVariable + 1;}print(maVariable);'


# 2 d -> structures itératives : implémenter le for
s='maVariable = 1; for i from 1 to 5 {maVariable = maVariable + 1;}print(maVariable);'



#2 e -> Affichage de l’arbre de syntaxe (sur la console ou avec graphViz)
parser.parse(s)




#with open("1.in") as file: # Use file to refer to the file object

#s = file.read()



#Afficher les valeurs
#print(names)
