from genereTreeGraphviz2 import printTreeGraph

reserved = {
    'if' : 'IF',
    'print' : 'PRINT',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'for' : 'FOR',
    'to' : 'TO',
    'from' : 'FROM',
    'def' : 'DEF',
    'return' : 'RETURN',
    'pop' : 'POP',
    'append' : 'APPEND',
    'length' : 'LENGTH',
    'count' : 'COUNT',
    'sort' : 'SORT',
    'reverse' : 'REVERSE'
   }

tokens = [
    'NAME','NUMBER','BRACERIGHT','BRACELEFT',
    'PLUS','MINUS','TIMES','DIVIDE',
    'LPAREN','RPAREN', 'COLON', 'AND', 'OR', 'EQUAL', 'EQUALS', 'LOWER','HIGHER',
    'HIGHEROREQUAL','LOWEROREQUAL','DIFFERENT','PLUSEQUAL','MINUSEQUAL','INCREMENT',
    'COMMA','LBRACKET', 'RBRACKET','DOT',
    ]+list(reserved.values())

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'NAME')
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
t_PLUSEQUAL = r'\+='
t_MINUSEQUAL = r'\-='
t_INCREMENT = r'\§§'
t_COMMA = r'\,'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_DOT = r'\.'

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_RETURN(t):
    r'return'
    return t

import ply.lex as lex
lexer = lex.lex()

def p_start(t):
    ''' start : bloc'''
    t[0] = ('start',t[1])
    #print(t[0])
    printTreeGraph(t[0])
    #eval(t[1])
    evalInst(t[1])

names={}
functions = {}

def evalInst(t):
    if t[0] == 'print':
        if isinstance(t[1], list):
            values_to_print = [evalExpr(expr) for expr in t[1]]
            print('CALC >', ' '.join(str(v) for v in values_to_print))
        else:
            print('CALC >', evalExpr(t[1]))
    if t[0]=='assign' :
        names[t[1]]=evalExpr(t[2])
    if t[0] == 'assign_plus_equal':
        var_name, additional_value = t[1], evalExpr(t[2])
        if var_name in names:
            names[var_name] += additional_value
    if t[0] == 'assign_minus_equal':
        var_name, additional_value = t[1], evalExpr(t[2])
        if var_name in names:
            names[var_name] -= additional_value
    if t[0] == 'assign_increment':
        var_name = t[1]
        if var_name in names:
            names[var_name] += 1
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
    if t[0] == 'def':
        function_name = t[1]
        function_body = t[2]
        functions[function_name] = function_body
    if t[0] == 'def_with_args':
        function_name = t[1]
        param_name = t[2]
        function_body = t[3]
        functions[function_name] = (param_name, function_body)
    if t[0] == 'def_with_args':
        function_name = t[1]
        param_names = t[2]
        function_body = t[3]
        functions[function_name] = (param_names, function_body)
    if t[0] == 'call_function_with_args':
        function_name = t[1]
        arg_values = [evalExpr(arg) for arg in t[2]]
        if function_name in functions:
            param_names, function_body = functions[function_name]
            for pname, pvalue in zip(param_names, arg_values):
                names[pname] = pvalue
            evalInst(function_body)
    if t[0] == 'call_function':
        function_name = t[1]
        if function_name in functions:
            function_body = functions[function_name]
            evalInst(function_body)
    if t[0] == 'def_with_return':
        function_name = t[1]
        function_body = t[2]
        functions[function_name] = function_body
    elif t[0] == 'assign':
        var_name = t[1]
        if isinstance(t[2], tuple) and t[2][0] == 'call_function_with_return':
            function_name = t[2][1]
            if function_name in functions:
                function_body = functions[function_name]
                return_value = evalInst(function_body)
                names[var_name] = return_value
        else:
            names[var_name] = evalExpr(t[2])
    elif t[0] == 'return':
        return evalExpr(t[1])
    if t[0] == 'array_pop':
        array_name = t[1]
        index = evalExpr(t[2])
        try:
            array_value = names[array_name]
            del array_value[index]
        except IndexError:
            print(f"Erreur: Index {index} hors limites pour le tableau {array_name}.")
        except KeyError:
            print(f"Erreur: Tableau {array_name} non défini.")
    if t[0] == 'append':
        array_name = t[1]
        value_to_append = evalExpr(t[2])
        if array_name in names and isinstance(names[array_name], list):
            names[array_name].append(value_to_append)
        else:
            print(f"Erreur : {array_name} n'est pas un tableau ou n'est pas défini.")
    if t[0] == 'array_count':
        array_name = t[1]
        value_to_count = evalExpr(t[2])
        if array_name in names and isinstance(names[array_name], list):
            count_result = names[array_name].count(value_to_count)
            print(count_result)
        else:
            print(f"Erreur : {array_name} n'est pas un tableau ou n'est pas défini.")
    if t[0] == 'array_length':
        array_name = t[1]
        if array_name in names and isinstance(names[array_name], list):
            print(len(names[array_name]))
    if t[0] == 'array_sort':
        array_name = t[1]
        if array_name in names and isinstance(names[array_name], list):
            names[array_name].sort()
        else:
            print(f"Erreur : {array_name} n'est pas un tableau ou n'est pas défini.")
    if t[0] == 'array_reverse':
        array_name = t[1]
        if array_name in names and isinstance(names[array_name], list):
            names[array_name].reverse()
        else:
            print(f"Erreur : {array_name} n'est pas un tableau ou n'est pas défini.")
    elif t[0] == 'def_with_return_params':
        function_name = t[1]
        param_names = t[2]
        function_body = t[3]
        functions[function_name] = (param_names, function_body)
    elif t[0] == 'recursive_with_return_params':
        function_name = t[1]
        param_names = t[2]
        function_body = t[3]
        functions[function_name] = (param_names, function_body)
    elif t[0] == 'assign_with_call_return':
        var_name = t[1]
        function_name = t[2]
        arg_values = [evalExpr(arg) for arg in t[3]]
        if function_name in functions:
            param_names, function_body = functions[function_name]
            local_context = dict(zip(param_names, arg_values))
            return_value = evalInstWithLocalContext(function_body, local_context)
            names[var_name] = return_value

def evalExpr(t):
    if type(t) is not tuple:
        if type(t) is str:
            if t in names:
                return names[t]
            else:
                print(f"Variable non initialisée : '{t}'")
                return
        return t
    if t[0] == '==': return evalExpr(t[1]) == evalExpr(t[2])
    if t[0] == '+': return evalExpr(t[1]) + evalExpr(t[2])
    if t[0] == '-': return evalExpr(t[1]) - evalExpr(t[2])
    if t[0] == '*': return evalExpr(t[1]) * evalExpr(t[2])
    if t[0] == '/':
        if t[2] == 0: return 0
        return evalExpr(t[1]) / evalExpr(t[2])
    if(t[0]) == ">": return evalExpr(t[1]) > evalExpr(t[2])
    if (t[0]) == "<": return evalExpr(t[1]) < evalExpr(t[2])
    if (t[0]) == ">=": return evalExpr(t[1]) >= evalExpr(t[2])
    if (t[0]) == "<=": return evalExpr(t[1]) <= evalExpr(t[2])
    if (t[0]) == "!=": return evalExpr(t[1]) != evalExpr(t[2])
    if (t[0]) == '|': return evalExpr(t[1]) or evalExpr(t[3])
    if t[0] == '&': return evalExpr(t[1]) and evalExpr(t[3])
    if isinstance(t, str):
        if t in names:
            return names[t]
        else:
            raise NameError(f"Variable non initialisée : '{t}'")
    if t[0] == 'array_index':
        array = evalExpr(t[1])
        index = evalExpr(t[2])
        try:
            return array[index]
        except IndexError:
            print(f"Erreur: Index {index} hors limites pour le tableau.")
            return None
    if t[0] == 'array_append':
        array_name = t[1]
        value_to_append = evalExpr(t[3])
        if array_name in names and isinstance(names[array_name], list):
            names[array_name].append(value_to_append)
        else:
            print(f"Erreur : {array_name} n'est pas un tableau ou n'est pas défini.")

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
    'statement : PRINT LPAREN expr_list RPAREN COLON'
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

def p_expression(t):
    '''expression : array'''
    t[0] = t[1]

def p_statement_assign_plus_equal(t):
    'statement : NAME PLUSEQUAL expression COLON'
    t[0] = ('assign_plus_equal', t[1], t[3])

def p_statement_assign_minus_equal(t):
    'statement : NAME MINUSEQUAL expression COLON'
    t[0] = ('assign_minus_equal', t[1], t[3])

def p_statement_assign_increment(t):
    'statement : NAME INCREMENT COLON'
    t[0] = ('assign_increment', t[1], t[3])


def p_statement_if(t):
    'statement : IF LPAREN expression RPAREN BRACELEFT bloc BRACERIGHT'
    t[0] = ('if', t[3], t[6])

def p_statement_if_else(t):
    'statement : IF LPAREN expression RPAREN BRACELEFT bloc BRACERIGHT ELSE BRACELEFT bloc BRACERIGHT'
    t[0] = ('if-else', t[3], t[6], t[10])

def p_statement_while(t):
    'statement : WHILE LPAREN expression RPAREN BRACELEFT bloc BRACERIGHT'
    t[0] = ('while', t[3], t[6])

def p_statement_for(t):
    'statement : FOR LPAREN NAME FROM expression TO expression RPAREN BRACELEFT bloc BRACERIGHT'
    t[0] = ('for', t[3], t[5], t[7], t[10])

def p_statement_def_no_args(t):
    'statement : DEF NAME LPAREN RPAREN BRACELEFT bloc BRACERIGHT'
    t[0] = ('def', t[2], t[6])

def p_call_function(t):
    'statement : NAME LPAREN RPAREN COLON'
    t[0] = ('call_function', t[1])

def p_statement_def_args(t):
    'statement : DEF NAME LPAREN param_list RPAREN BRACELEFT bloc BRACERIGHT'
    t[0] = ('def_with_args', t[2], t[4], t[7])

def p_param_list_more(t):
    'param_list : param_list COMMA NAME'
    t[0] = t[1] + [t[3]]

def p_param_list_single(t):
    'param_list : NAME'
    t[0] = [t[1]]

def p_arg_list_more(t):
    'arg_list : arg_list COMMA expression'
    t[0] = t[1] + [t[3]]

def p_arg_list_single(t):
    'arg_list : expression'
    t[0] = [t[1]]

def p_call_function_with_args(t):
    'statement : NAME LPAREN arg_list RPAREN COLON'
    t[0] = ('call_function_with_args', t[1], t[3])

def p_expr_list_single(t):
    'expr_list : expression'
    t[0] = [t[1]]

def p_statement_def_return(t):
    'statement : DEF NAME LPAREN RPAREN BRACELEFT return_statement BRACERIGHT'
    t[0] = ('def_with_return', t[2], t[6])

def p_return_statement(t):
    'return_statement : RETURN expression COLON'
    t[0] = ('return', t[2])

def p_call_function_and_assign(t):
    'statement : NAME EQUAL NAME LPAREN RPAREN COLON'
    t[0] = ('assign', t[1], ('call_function_with_return', t[3]))

def p_array_empty(t):
    'array : LBRACKET RBRACKET'
    t[0] = []

def p_array_nonempty(t):
    'array : LBRACKET expr_list RBRACKET'
    t[0] = t[2]

def p_expr_list_multiple(t):
    'expr_list : expr_list COMMA expression'
    t[1].append(t[3])
    t[0] = t[1]

def p_expression_array_index(t):
    'expression : expression LBRACKET expression RBRACKET'
    t[0] = ('array_index', t[1], t[3])

def p_statement_array_pop(t):
    'statement : expression DOT POP LPAREN expression RPAREN COLON'
    t[0] = ('array_pop', t[1], t[5])

def p_statement_array_append(t):
    'statement : expression DOT APPEND LPAREN expression RPAREN COLON'
    t[0] = ('append', t[1], t[5])

def p_statement_array_count(t):
    'statement : expression DOT COUNT LPAREN expression RPAREN COLON'
    t[0] = ('array_count', t[1], t[5])

def p_statement_array_length(t):
    'statement : expression DOT LENGTH LPAREN RPAREN COLON'
    t[0] = ('array_length', t[1])

def p_statement_array_sort(t):
    'statement : expression DOT SORT LPAREN RPAREN COLON'
    t[0] = ('array_sort', t[1])

def p_statement_array_reverse(t):
    'statement : expression DOT REVERSE LPAREN RPAREN COLON'
    t[0] = ('array_reverse', t[1])

def p_statement_def_return_with_params(t):
    'statement : DEF NAME LPAREN param_list RPAREN BRACELEFT return_statement BRACERIGHT'
    t[0] = ('def_with_return_params', t[2], t[4], t[7])


def p_statement_call_with_args_and_assign_return(t):
    'statement : NAME EQUAL NAME LPAREN arg_list RPAREN COLON'
    t[0] = ('assign_with_call_return', t[1], t[3], t[5])

def evalInstWithLocalContext(t, local_context):
    global names
    old_context = names.copy()
    names.update(local_context)
    return_value = evalInst(t)
    names = old_context
    return return_value


def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

# 2 a -> affectation || b -> affichage d’expressions numériques
#s='maVariable = 12+2;maVariable§§; print(maVariable);'

# 2 c -> instructions conditionnelles : implémenter le si-alors
#s='maVariable = 118218; if (maVariable > 1) {maVariable = 12;print(maVariable);}'

# 2 c -> instructions conditionnelles : implémenter si-alors-sinon
#s='maVariable = 118218; if (maVariable == 1) {maVariable = 12;print(maVariable);} else {maVariable = 0;print(maVariable);}'

# 2 d -> structures itératives : implémenter le while
#s='maVariable = 10; while (maVariable < 15) {maVariable += 1;}print(maVariable);'

# 2 d -> structures itératives : implémenter le for
#s='maVariable = 1;for(i from 1 to 5){maVariable += 2;print(i);}print(maVariable);'

# Gros bonus : fonction void sans parametre
#s='def maFonction() {print(118218);print(1);} maFonction();'

# Gros bonus : fonction void avec parametre
#s='def maFonctionAvecParam(x) {print(x);print(1);} maFonctionAvecParam(118218);'

# Gros bonus : fonction void avec plusieurs parametres
#s='def maFonctionAvecParam(x,y,z) {print(x,y,z);} maFonctionAvecParam(10+1,5,2);'

# Gros bonus : Fonctions avec return
#s='def maFonctionAvecReturn() {return 3;}maVariable = maFonctionAvecReturn(); print(maVariable);'

# Gros bonus : Fonctions avec return et parametre
#s='def maFonctionAvecReturn(a,b,c) {return a+b-c;}maVariable = maFonctionAvecReturn(1,2,3); print(maVariable);'


#Gros bonus : Tableau vide
#s='monTableau = []; print(monTableau);'

#Gros bonus : Print index tableau
#s='monTableau = [1,2,3,4]; print(monTableau[3]);'

#Gros bonus : Fonction pop tableau
#s='monTableau = [1,2,3,4];monTableau.pop(0);print(monTableau);'

#Gros bonus : Fonction append tableau
#s='monTableau = [1,2,3];monTableau.append(4);print(monTableau);'

#Gros bonus : Fonction count tableau
#s='monTableau = [1,2,3,1,3,1];monTableau.count(1);'

#Gros bonus : Fonction length tableau
#s='monTableau = [1,2,3,1,3,1];monTableau.length();'

#Gros bonus : Fonction sort tableau
#s="monTableau = [1,19,5,3,4];monTableau.sort();print(monTableau);"

#Gros bonus : Fonction reverse tableau
#s="monTableau = [1,19,5,3,4];monTableau.reverse();print(monTableau);"

# Petits bonus : -> incrémentation et affectation élargie :
#s='x = 1; x-= 1;x+=3; print(x);'

# Petits bonus : -> print multiple :
# s='x = 1; y = 3;print(x,y);'

# Petits bonus : -> gestion des variables pas initialisées :
#s='def maFonctionAvecParam(x) {print(x);}maFonctionAvecParam(118218);print(y);'

#2 e -> Affichage de l’arbre de syntaxe (sur la console ou avec graphViz)
parser.parse(s)



#with open("1.in") as file: # Use file to refer to the file object

#s = file.read()

#Afficher les valeurs
#print(names)