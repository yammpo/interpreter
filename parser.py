#from __future__ import annotations
import ply.yacc as yacc
from lexer import Lexer
from ply.lex import LexError
import sys
from typing import List, Dict, Tuple


class SyntaxTreeNode:
	def __init__(self, _type='const', value=None, children=None, lineno=None, lexpos=None):
		self.type = _type
		self.value = value
		self.children = children or []
		self.lineno = lineno
		self.lexpos = lexpos
        
	def __repr__(self):
		return f"""{self.type} {self.value or ''} {self.lineno or ''}:{self.lexpos or ''}"""

	def print_(self, level: int = 0):
		print(' ' * level, self)

	def print(self, level: int = 0):
		if self is None:
			return
		print(' ' * level, self)
		if isinstance(self.children, list):
			for child in self.children:
				if child:
					child.print(level + 1)
		elif isinstance(self.children, SyntaxTreeNode):
			self.children.print(level + 1)
		elif isinstance(self.children, dict):
			for key, value in self.children.items():
				print(' ' * (level + 1), key)
				if value:
					value.print(level + 2)

class Parser():
	tokens = Lexer.tokens

	def __init__(self):
		self._lexer = Lexer()
		self.parser = yacc.yacc(module=self, debug=False)
		self.functions: Dict[str, SyntaxTreeNode] = dict()
		self.ok=True

	def parse(self, s):
		try:
			res = self.parser.parse(s)
			return res, self.functions, self.ok
		except LexError:
			sys.stderr.write(f'Illegal token {s}\n')

	def p_program(self, p):
		'program : PROGRAM_START blocks PROGRAM_END'
		p[0] = SyntaxTreeNode('program', children=p[2], lineno=p.lineno(1), lexpos=p.lexpos(1))

	def p_blocks(self, p):
		'''blocks : blocks block
		| block'''
		if len(p) == 2:
			p[0] = SyntaxTreeNode('block', children=p[1])
		else:
			p[0] = SyntaxTreeNode('blocks', children=[p[1], p[2]])

	def p_block(self, p):
		'''block : vardeclaration
		| function
		| empty'''
		p[0] = p[1]

	def p_function(self, p):
		'function : FUNC_START NAME EQUALSIGN funcname RBRACKET statements FUNC_END'
		p[0] = SyntaxTreeNode('function', value=p[4], children={'body': p[6]}, lineno=p.lineno(1))
		
	def p_statements(self, p):
		'''statements : statements statement
		| statement'''
		if len(p) == 2:
			p[0] = SyntaxTreeNode('statement', children=p[1])
		else:
			p[0] = SyntaxTreeNode('statements', children=[p[1], p[2]])

	def p_statement(self, p):
		'''statement : vardeclaration
		| assignment 
		| while
		| switch
		| call
		| operator
		| empty'''
		p[0] = p[1]
		# в assignment'е будут все выражения (результатом которых является временная переменная)

	def p_assignment(self, p):
		'assignment : ASSIGN_START VALUE_START expression VALUE_END TO_START variables TO_END ASSIGN_END'
		p[0] = SyntaxTreeNode('assignment', children=[p[3], p[6]])

	def p_while(self, p):
		'while : WHILE_START CHECK_START expression CHECK_END DO_START statements DO_END WHILE_END'
		p[0] = SyntaxTreeNode('while', children={'condition': p[3], 'body': p[6]}, lineno=p.lineno(1), lexpos=p.lexpos(1))

	#можно чек ду сделать отдельным правилом, но надо ли?

	def p_switch(self, p):
		'switch : SWITCH_START conditions SWITCH_END'
		p[0] = SyntaxTreeNode('switch', children=p[2], lineno=p.lineno(1), lexpos=p.lexpos(1))

	def p_conditions(self, p):
		'''conditions : conditions condition
		| condition'''
		if len(p) == 2:
			p[0] = SyntaxTreeNode('condition', children=p[1])
		else:
			p[0] = SyntaxTreeNode('conditions', children=[p[1], p[2]])

	def p_condition(self, p):
		'''condition : CONDITION_START CHECK_START expression CHECK_END DO_START statements DO_END CONDITION_END
		| empty'''
		if len(p) == 2:
			p[0] = p[1]
		else:
			p[0] = SyntaxTreeNode('condition', children={'condition': p[3], 'body': p[6]}, lineno=p.lineno(1), lexpos=p.lexpos(1))

	def p_call(self, p):
		'call : CALL_START funcname CALL_END'
		p[0] = SyntaxTreeNode('function_call', value=p[2], lineno=p.lineno(1), lexpos=p.lexpos(1))

	def p_funcname(self, p):
		'''funcname : MAIN
		| ID'''
		p[0] = SyntaxTreeNode('funcname', value=p[1], lineno=p.lineno(1))

	def p_vardeclaration(self, p): #пока без массивов и без СONST и без инициализации ))) про const кстати спросить
		'vardeclaration : VARDECLARATION_START declarations VARDECLARATION_END'
		p[0] = SyntaxTreeNode('vardeclaration', children=p[2], lineno=p.lineno(1), lexpos=p.lexpos(1))
		
	def p_declarations(self, p):
		'''declarations : declarations declaration
		| declaration'''
		if len(p) == 2:
			p[0] = SyntaxTreeNode('declaration', children=p[1])
		else:
			p[0] = SyntaxTreeNode('declarations', children=[p[1], p[2]])

	def p_declaration(self, p):
		'''declaration : VAR_START EQUALSIGN ID RBRACKET TYPE_START type TYPE_END LBRACKET VAR_END
		| empty'''
		if len(p) == 2:
			p[0] = p[1]
		else:
			p[0] = SyntaxTreeNode('declaration', value=p[6], children=p[3], lineno=p.lineno(1), lexpos=p.lexpos(1))

	def p_type(self, p):
		'''type : INT
		| CELL
		| BOOL'''
		p[0] = SyntaxTreeNode('type', value=p[1], children=[], lineno=p.lineno(1), lexpos=p.lexpos(1))

	def p_variables(self, p):
		'''variables : variables variable
		| variable'''
		if len(p) == 2:
			p[0] = SyntaxTreeNode('variable', children=p[1]) #может еще что-то
		else:
			p[0] = SyntaxTreeNode('variables', children=[p[1], p[2]])

	def p_variable(self, p):  #обращение к переменной, пока без массивов
		'''variable : VAR_START NAME EQUALSIGN ID VAR_END
		| empty'''
		if len(p) == 2:
			p[0] = p[1]
		else:
			p[0] = SyntaxTreeNode('variable', value=p[4], children=[], lineno=p.lineno(1), lexpos=p.lexpos(1))

	def p_expressions(self, p):
		'''expressions : expressions expression
		| expression'''
		if len(p) == 2:
			p[0] = SyntaxTreeNode('expression', children=p[1]) #может еще что-то
		else:
			p[0] = SyntaxTreeNode('expressions', children=[p[1], p[2]])

	def p_expression(self, p):
		'''expression : variable
		| const
		| math
		| empty'''
		p[0] = p[1]

	def p_const(self, p): #клетки?
		'''const : TRUE
		| FALSE
		| NUMBER'''
		p[0] = SyntaxTreeNode('const', value=p[1], lineno=p.lineno(1), lexpos=p.lexpos(1))

	def p_math(self, p): #нот без вызова процедуры
		'''math : ADD_START expression expressions ADD_END
		| MUL_START expression expressions MUL_END
		| SUB_START expression expression SUB_END
		| DIV_START expression expression DIV_END
		| OR_START expression expressions OR_END
		| AND_START expression expressions AND_END
		| MAX_START expression expressions MAX_END
		| MIN_START expression expressions MIN_END
		| EQ_START expression expressions EQ_END
		| NOT_START expression NOT_END'''
		if len(p) == 9:
			p[0] = SyntaxTreeNode('unar', value=p[1], children=p[2], lineno=p.lineno(1), lexpos=p.lexpos(1))
		else:
			p[0] = SyntaxTreeNode('plural', value=p[1], children=[p[2], p[3]], lineno=p.lineno(1), lexpos=p.lexpos(1))
        
	#ДОБАВИТЬ МАССИВЫ В VARDECLARATION И VARIABLE!! и оператор узнать что за выражение

	def p_operator(self, p): # в getdronscount обращение к переменной или все-таки имя? какие тут выражения?
		'''operator : LEFT_START expression LEFT_END
		| RIGHT_START expression RIGHT_END
		| UP_START expression UP_END
		| DOWN_START expression DOWN_END
		| SENDDRONS_START expression SENDDRONS_END
		| GETDRONSCOUNT_START variable GETDRONSCOUNT_END'''
		p[0] = SyntaxTreeNode('operator', value=p[1], children=p[2], lineno=p.lineno(1), lexpos=p.lexpos(1))

	def p_error(self,p):
		print(f'Syntax error at {p.lineno} line\n')
		#print(p.lexpos)

	def p_empty(self, p):
		'empty : '
		p[0] = SyntaxTreeNode('empty')
	#с empty и рекурсиями что-то подумать и убрать нафиг

parser = Parser()
f=open('test','r')
tree, functions,ok = parser.parse(f.read())
f.close()

if tree is not None and ok is True:
	tree.print()
	print(functions)
else:
	print('error tree built')


