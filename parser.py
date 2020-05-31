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
			p[0] = SyntaxTreeNode('blocks', children=[p[1]])
		else:
			p[0] = SyntaxTreeNode('blocks', children=[p[1], p[2]])

	def p_block(self, p):
		'''block : vardeclaration
		| function
		| empty'''
		p[0] = p[1]

	def p_block_error(self,p):
		'''block : error'''
		self.ok = False
		if isinstance(p[1], str):
			sys.stderr.write(f'Illegal symbol\n')
		else:
			sys.stderr.write(f'block error: "{p[1].value}" at {p[1].lineno}:{p[1].lexpos}\n')

	def p_function(self, p):
		'function : FUNC_START NAME EQUALSIGN funcname RBRACKET statements FUNC_END'
		p[0] = SyntaxTreeNode('function', value=p[4], children=p[6], lineno=p.lineno(1)) #исправить
		
	def p_statements(self, p):
		'''statements : statements statement
		| statement'''
		if len(p) == 2:
			p[0] = SyntaxTreeNode('statements', children=[p[1]])
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

	def p_statement_error(self, p):
		'''statement : error'''
		self.ok = False
		if isinstance(p[1], str):
			sys.stderr.write(f'Illegal symbol\n')
		else:
			sys.stderr.write(f'statement error: "{p[1].value}" at {p[1].lineno}:{p[1].lexpos}\n')

	def p_assignment(self, p):
		'assignment : ASSIGN_START VALUE_START expression VALUE_END TO_START variables TO_END ASSIGN_END'
		p[0] = SyntaxTreeNode('assignment', children=[p[3], p[6]])

	def p_while(self, p):
		'while : WHILE_START CHECK_START expression CHECK_END DO_START statements DO_END WHILE_END'
		p[0] = SyntaxTreeNode('while', children={'condition': p[3], 'body': p[6]}, lineno=p.lineno(1), lexpos=p.lexpos(1))

	def p_switch(self, p):
		'switch : SWITCH_START conditions SWITCH_END'
		p[0] = SyntaxTreeNode('switch', children=p[2], lineno=p.lineno(1), lexpos=p.lexpos(1))

	def p_conditions(self, p):
		'''conditions : conditions condition
		| condition'''
		if len(p) == 2:
			p[0] = SyntaxTreeNode('conditions', children=[p[1]])
		else:
			p[0] = SyntaxTreeNode('conditions', children=[p[1], p[2]])

	def p_condition(self, p):
		'''condition : CONDITION_START CHECK_START expression CHECK_END DO_START statements DO_END CONDITION_END
		| empty'''
		if len(p) == 2:
			p[0] = p[1]
		else:
			p[0] = SyntaxTreeNode('condition', children={'condition': p[3], 'body': p[6]}, lineno=p.lineno(1), lexpos=p.lexpos(1))
	
	def p_condition_error(self, p):
		'condition : error'
		self.ok = False
		if isinstance(p[1], str):
			sys.stderr.write(f'Illegal symbol\n')
		else:
			sys.stderr.write(f'condition error: "{p[1].value}" at {p[1].lineno}:{p[1].lexpos}\n')
			
	def p_call(self, p):
		'call : CALL_START funcname CALL_END'
		p[0] = SyntaxTreeNode('function_call', value=p[2], lineno=p.lineno(1), lexpos=p.lexpos(1))

	def p_funcname(self, p):
		'''funcname : ID
		| MAIN'''
		p[0] = SyntaxTreeNode('funcname', value=p[1], lineno=p.lineno(1))

	def p_vardeclaration(self, p): 
		'vardeclaration : VARDECLARATION_START declarations VARDECLARATION_END'
		p[0] = SyntaxTreeNode('vardeclaration', children=p[2], lineno=p.lineno(1), lexpos=p.lexpos(1))

	def p_declarations(self, p):
		'''declarations : declarations declaration
		| declaration'''
		if len(p) == 2:
			p[0] = SyntaxTreeNode('declarations', children=[p[1]])
		else:
			p[0] = SyntaxTreeNode('declarations', children=[p[1], p[2]])

	def p_declaration(self,p):
		'''declaration : declaration_var
		| declaration_var_init
		| declaration_var_const
		| declaration_array
		| declaration_array_init
		| declaration_array_const
		| empty'''
		p[0] = p[1]

	def p_declaration_var(self, p):
		'''declaration_var : VAR_START EQUALSIGN id RBRACKET TYPE_START type TYPE_END LBRACKET VAR_END
		| VAR_START EQUALSIGN id CONST EQUALSIGN FALSE RBRACKET TYPE_START type TYPE_END LBRACKET VAR_END'''
		p[0] = SyntaxTreeNode('declaration_var', value=p[len(p)-4], children=p[3], lineno=p.lineno(1), lexpos=p.lexpos(1))

	def p_declaration_var_const(self, p):
		'''declaration_var_const : VAR_START EQUALSIGN id CONST EQUALSIGN TRUE RBRACKET TYPE_START type TYPE_END VALUE_START expression VALUE_END LBRACKET VAR_END'''
		p[0] = SyntaxTreeNode('declaration_var_const', value=p[9], children=[p[3], p[12]], lineno=p.lineno(1), lexpos=p.lexpos(1))
	
	def p_declaration_var_init(self, p):
		'''declaration_var_init : VAR_START EQUALSIGN id RBRACKET TYPE_START type TYPE_END VALUE_START expression VALUE_END LBRACKET VAR_END
		| VAR_START EQUALSIGN id CONST EQUALSIGN FALSE RBRACKET TYPE_START type TYPE_END VALUE_START expression VALUE_END LBRACKET VAR_END'''
		p[0] = SyntaxTreeNode('declaration_var_init', value=p[len(p)-7], children=[p[3], p[len(p)-4]], lineno=p.lineno(1), lexpos=p.lexpos(1))

	def p_declaration_array(self,p):
		'''declaration_array : VAR_START EQUALSIGN id RBRACKET TYPE_START type TYPE_END DIMENSIONS_START COUNT EQUALSIGN const RBRACKET dimensions DIMENSIONS_END LBRACKET VAR_END
		| VAR_START EQUALSIGN id CONST EQUALSIGN FALSE RBRACKET TYPE_START type TYPE_END DIMENSIONS_START COUNT EQUALSIGN const RBRACKET dimensions DIMENSIONS_END LBRACKET VAR_END'''
		p[0] = SyntaxTreeNode('declaration_array', value=p[len(p)-11], children=[p[3], p[len(p)-6],p[len(p)-4]], lineno=p.lineno(1), lexpos=p.lexpos(1))

	def p_declaration_array_init(self,p):
		'''declaration_array_init : VAR_START EQUALSIGN id RBRACKET TYPE_START type TYPE_END DIMENSIONS_START COUNT EQUALSIGN const RBRACKET dimensions DIMENSIONS_END VALUES_START values VALUES_END LBRACKET VAR_END
		| VAR_START EQUALSIGN id CONST EQUALSIGN FALSE RBRACKET TYPE_START type TYPE_END DIMENSIONS_START COUNT EQUALSIGN const RBRACKET dimensions DIMENSIONS_END VALUES_START values VALUES_END LBRACKET VAR_END'''
		p[0] = SyntaxTreeNode('declaration_array_init', value=p[len(p)-14], children=[p[3], p[len(p)-9], p[len(p)-7], p[len(p)-4]], lineno=p.lineno(1), lexpos=p.lexpos(1))

	def p_declaration_array_const(self,p):
		'''declaration_array_const : VAR_START EQUALSIGN id CONST EQUALSIGN TRUE RBRACKET TYPE_START type TYPE_END DIMENSIONS_START COUNT EQUALSIGN const RBRACKET dimensions DIMENSIONS_END VALUES_START values VALUES_END LBRACKET VAR_END'''
		p[0] = SyntaxTreeNode('declaration_array_const', value=p[9], children=[p[3], p[14], p[16], p[19]], lineno=p.lineno(1), lexpos=p.lexpos(1))

	def p_values(self, p):
		'''values : values value
		| value'''
		if len(p) == 2:
			p[0] = SyntaxTreeNode('values', children=[p[1]]) 
		else:
			p[0] = SyntaxTreeNode('values', children=[p[1], p[2]])

	def p_value(self, p):
		'''value : VALUE_START expression VALUE_END'''
		p[0] = SyntaxTreeNode('value', children=p[2], lineno=p.lineno(1), lexpos=p.lexpos(1))
	
	def p_dimensions(self,p):
		'''dimensions : dimensions dimension
		| dimension'''
		if len(p) == 2:
			p[0] = SyntaxTreeNode('dimensions', children=[p[1]]) 
		else:
			p[0] = SyntaxTreeNode('dimensions', children=[p[1], p[2]])

	def p_dimension(self, p):
		'''dimension : DIMENSION_START expression DIMENSION_END'''
		p[0] = SyntaxTreeNode('dimension', children=p[2], lineno=p.lineno(1), lexpos=p.lexpos(1))

	def p_type(self, p):
		'''type : INT
		| CELL
		| BOOL'''
		p[0] = SyntaxTreeNode('type', value=p[1], children=[], lineno=p.lineno(1), lexpos=p.lexpos(1))

	def p_id(self,p):
		'''id : ID'''
		p[0] = SyntaxTreeNode('id', value=p[1], children=[], lineno=p.lineno(1), lexpos=p.lexpos(1))

	def p_variables(self, p):
		'''variables : variables variable
		| variable'''
		if len(p) == 2:
			p[0] = SyntaxTreeNode('variables', children=[p[1]]) 
		else:
			p[0] = SyntaxTreeNode('variables', children=[p[1], p[2]])

	def p_variable(self, p):  
		'''variable : VAR_START NAME EQUALSIGN id VAR_END
		| VAR_START NAME EQUALSIGN id RBRACKET DIM_START indexes DIM_END LBRACKET VAR_END
		| empty'''
		if len(p) == 2:
			p[0] = p[1]
		elif len(p) == 6:
			p[0] = SyntaxTreeNode('variable', value=p[4], children=[], lineno=p.lineno(1), lexpos=p.lexpos(1))
		else:
			p[0] = SyntaxTreeNode('variable_array', value=p[4], children=p[7], lineno=p.lineno(1), lexpos=p.lexpos(1))

	def p_indexes(self, p):
		'''indexes : indexes index
		| index'''
		if len(p) == 2:
			p[0] = SyntaxTreeNode('indexes', children=[p[1]]) 
		else:
			p[0] = SyntaxTreeNode('indexes', children=[p[1], p[2]])
	
	def p_index(self, p):
		'''index : INDEX_START expression INDEX_END'''
		p[0] = SyntaxTreeNode('index', children=p[2], lineno=p.lineno(1), lexpos=p.lexpos(1))

	def p_expressions(self, p):
		'''expressions : expressions expression
		| expression'''
		if len(p) == 2:
			p[0] = SyntaxTreeNode('expressions', children=[p[1]]) 
		else:
			p[0] = SyntaxTreeNode('expressions', children=[p[1], p[2]])

	def p_expression(self, p):
		'''expression : variable
		| const
		| math
		| empty
		| senddrons'''
		p[0] = p[1]

	def p_const(self, p): 
		'''const : TRUE
		| FALSE
		| NUMBER
		| EMPTY
		| WALL
		| EXIT
		| UNDEF'''
		p[0] = SyntaxTreeNode('const', value=p[1], lineno=p.lineno(1), lexpos=p.lexpos(1))

	def p_math(self, p): #нот без вызова процедуры
		'''math : ADD_START expressions ADD_END
		| MUL_START expressions MUL_END
		| SUB_START expressions SUB_END
		| DIV_START expressions DIV_END
		| OR_START expressions OR_END
		| AND_START expressions AND_END
		| MAX_START expressions MAX_END
		| MIN_START expressions MIN_END
		| EQ_START expressions EQ_END
		| NOT_START expression NOT_END'''
		p[0] = SyntaxTreeNode('math', value=p[1], children=p[2], lineno=p.lineno(1), lexpos=p.lexpos(1))
	
	def p_senddrons(self,p):
		'''senddrons : SENDDRONS_START expression SENDDRONS_END'''
		p[0] = SyntaxTreeNode('senddrons', value=p[1], children=p[2], lineno=p.lineno(1), lexpos=p.lexpos(1))
	
	def p_operator(self, p): 
		'''operator : LEFT_START expression LEFT_END
		| RIGHT_START expression RIGHT_END
		| UP_START expression UP_END
		| DOWN_START expression DOWN_END
		| GETDRONSCOUNT_START variable GETDRONSCOUNT_END'''
		p[0] = SyntaxTreeNode('operator', value=p[1], children=p[2], lineno=p.lineno(1), lexpos=p.lexpos(1))

	def p_error(self,p):
		sys.stderr.write(f'Syntax error at line {p.lineno}\n')
		self.ok = False

	def p_empty(self, p):
		'empty : '
		p[0] = SyntaxTreeNode('empty')

if __name__ == '__main__':
	parser = Parser()
	f=open('test(sorting)','r')
	tree, functions,ok = parser.parse(f.read())
	f.close()

	if tree is not None and ok is True:
		tree.print()
		#print(functions)
	else:
		print('error tree built')


