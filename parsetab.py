
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BRACELEFT BRACERIGHT COLON DIFFERENT DIVIDE ELSE EQUAL EQUALS FOR FROM HIGHER HIGHEROREQUAL IF LOWER LOWEROREQUAL LPAREN MINUS NAME NUMBER OR PLUS PLUSEQUAL PRINT RPAREN THEN TIMES TO WHILE start : blocbloc : bloc statement\n            | statement statement : NAME EQUAL expression COLONstatement : PRINT LPAREN expression RPAREN COLONexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression OR expression\n                  | expression AND expression\n                  | expression EQUALS expression\n                  | expression LOWER expression\n                  | expression HIGHER expression\n                  | expression HIGHEROREQUAL expression\n                  | expression LOWEROREQUAL expression\n                  | expression DIFFERENT expression\n                  | expression DIVIDE expressionexpression : LPAREN expression RPARENexpression : NUMBERexpression : NAMEstatement : NAME PLUSEQUAL expression COLONstatement : IF LPAREN expression RPAREN BRACELEFT statement BRACERIGHTstatement : IF LPAREN expression RPAREN BRACELEFT statement BRACERIGHT ELSE BRACELEFT statement BRACERIGHTstatement : WHILE LPAREN expression RPAREN BRACELEFT statement BRACERIGHTstatement : FOR NAME FROM expression TO expression BRACELEFT statement BRACERIGHT'
    
_lr_action_items = {'NAME':([0,2,3,8,9,10,11,12,13,14,18,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,57,58,59,60,64,65,66,69,70,72,],[4,4,-3,15,-2,16,16,16,16,16,16,16,-4,16,16,16,16,16,16,16,16,16,16,16,16,-21,-5,4,4,16,-22,-24,4,4,-25,-23,]),'PRINT':([0,2,3,9,25,39,57,58,59,64,65,66,69,70,72,],[5,5,-3,-2,-4,-21,-5,5,5,-22,-24,5,5,-25,-23,]),'IF':([0,2,3,9,25,39,57,58,59,64,65,66,69,70,72,],[6,6,-3,-2,-4,-21,-5,6,6,-22,-24,6,6,-25,-23,]),'WHILE':([0,2,3,9,25,39,57,58,59,64,65,66,69,70,72,],[7,7,-3,-2,-4,-21,-5,7,7,-22,-24,7,7,-25,-23,]),'FOR':([0,2,3,9,25,39,57,58,59,64,65,66,69,70,72,],[8,8,-3,-2,-4,-21,-5,8,8,-22,-24,8,8,-25,-23,]),'$end':([1,2,3,9,25,39,57,64,65,70,72,],[0,-1,-3,-2,-4,-21,-5,-22,-24,-25,-23,]),'EQUAL':([4,],[10,]),'PLUSEQUAL':([4,],[11,]),'LPAREN':([5,6,7,10,11,12,13,14,18,24,26,27,28,29,30,31,32,33,34,35,36,37,60,],[12,13,14,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'NUMBER':([10,11,12,13,14,18,24,26,27,28,29,30,31,32,33,34,35,36,37,60,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'FROM':([15,],[24,]),'COLON':([16,17,19,20,40,44,45,46,47,48,49,50,51,52,53,54,55,56,],[-20,25,-19,39,57,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,]),'PLUS':([16,17,19,20,21,22,23,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,63,],[-20,26,-19,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-18,26,]),'MINUS':([16,17,19,20,21,22,23,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,63,],[-20,27,-19,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-18,27,]),'TIMES':([16,17,19,20,21,22,23,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,63,],[-20,28,-19,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,-18,28,]),'OR':([16,17,19,20,21,22,23,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,63,],[-20,29,-19,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,-18,29,]),'AND':([16,17,19,20,21,22,23,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,63,],[-20,30,-19,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,-18,30,]),'EQUALS':([16,17,19,20,21,22,23,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,63,],[-20,31,-19,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,-18,31,]),'LOWER':([16,17,19,20,21,22,23,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,63,],[-20,32,-19,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-18,32,]),'HIGHER':([16,17,19,20,21,22,23,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,63,],[-20,33,-19,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-18,33,]),'HIGHEROREQUAL':([16,17,19,20,21,22,23,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,63,],[-20,34,-19,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-18,34,]),'LOWEROREQUAL':([16,17,19,20,21,22,23,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,63,],[-20,35,-19,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-18,35,]),'DIFFERENT':([16,17,19,20,21,22,23,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,63,],[-20,36,-19,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-18,36,]),'DIVIDE':([16,17,19,20,21,22,23,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,63,],[-20,37,-19,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-18,37,]),'RPAREN':([16,19,21,22,23,38,44,45,46,47,48,49,50,51,52,53,54,55,56,],[-20,-19,40,41,42,56,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,]),'TO':([16,19,43,44,45,46,47,48,49,50,51,52,53,54,55,56,],[-20,-19,60,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,]),'BRACELEFT':([16,19,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,63,67,],[-20,-19,58,59,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,66,69,]),'BRACERIGHT':([25,39,57,61,62,64,65,68,70,71,72,],[-4,-21,-5,64,65,-22,-24,70,-25,72,-23,]),'ELSE':([64,],[67,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'bloc':([0,],[2,]),'statement':([0,2,58,59,66,69,],[3,9,61,62,68,71,]),'expression':([10,11,12,13,14,18,24,26,27,28,29,30,31,32,33,34,35,36,37,60,],[17,20,21,22,23,38,43,44,45,46,47,48,49,50,51,52,53,54,55,63,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> bloc','start',1,'p_start','Esengo.py',79),
  ('bloc -> bloc statement','bloc',2,'p_line','Esengo.py',150),
  ('bloc -> statement','bloc',1,'p_line','Esengo.py',151),
  ('statement -> NAME EQUAL expression COLON','statement',4,'p_statement_assign','Esengo.py',160),
  ('statement -> PRINT LPAREN expression RPAREN COLON','statement',5,'p_statement_print','Esengo.py',165),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','Esengo.py',170),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','Esengo.py',171),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','Esengo.py',172),
  ('expression -> expression OR expression','expression',3,'p_expression_binop','Esengo.py',173),
  ('expression -> expression AND expression','expression',3,'p_expression_binop','Esengo.py',174),
  ('expression -> expression EQUALS expression','expression',3,'p_expression_binop','Esengo.py',175),
  ('expression -> expression LOWER expression','expression',3,'p_expression_binop','Esengo.py',176),
  ('expression -> expression HIGHER expression','expression',3,'p_expression_binop','Esengo.py',177),
  ('expression -> expression HIGHEROREQUAL expression','expression',3,'p_expression_binop','Esengo.py',178),
  ('expression -> expression LOWEROREQUAL expression','expression',3,'p_expression_binop','Esengo.py',179),
  ('expression -> expression DIFFERENT expression','expression',3,'p_expression_binop','Esengo.py',180),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','Esengo.py',181),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','Esengo.py',187),
  ('expression -> NUMBER','expression',1,'p_expression_number','Esengo.py',191),
  ('expression -> NAME','expression',1,'p_expression_name','Esengo.py',195),
  ('statement -> NAME PLUSEQUAL expression COLON','statement',4,'p_statement_assign_plus_equal','Esengo.py',199),
  ('statement -> IF LPAREN expression RPAREN BRACELEFT statement BRACERIGHT','statement',7,'p_statement_if','Esengo.py',203),
  ('statement -> IF LPAREN expression RPAREN BRACELEFT statement BRACERIGHT ELSE BRACELEFT statement BRACERIGHT','statement',11,'p_statement_if_else','Esengo.py',207),
  ('statement -> WHILE LPAREN expression RPAREN BRACELEFT statement BRACERIGHT','statement',7,'p_statement_while','Esengo.py',211),
  ('statement -> FOR NAME FROM expression TO expression BRACELEFT statement BRACERIGHT','statement',9,'p_statement_for','Esengo.py',215),
]
