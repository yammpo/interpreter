import ply.lex as lex

reserved = {
	'INT': 'INT', 'BOOL': 'BOOL', 'TRUE': 'TRUE', 'FALSE': 'FALSE', 'count': 'COUNT', 'CELL': 'CELL', 'EMPTY': 'EMPTY',
	'WALL': 'WALL','EXIT': 'EXIT', 'UNDEF': 'UNDEF', 'CONST': 'CONST', 'name': 'NAME', 'main': 'MAIN'
}

class Lexer():

	tokens = ['ID','NUMBER', 'EQUALSIGN','VARDECLARATION_START',
            'VARDECLARATION_END','VAR_START', 'VAR_END', 
            'TYPE_START','TYPE_END','DIMENSIONS_START',
            'DIMENSIONS_END','DIMENSION_START', 'DIMENSION_END', 
            'VALUES_START', 'VALUES_END','VALUE_START','VALUE_END', 
            'DIM_START','DIM_END','INDEX_START', 'INDEX_END','ASSIGN_START',
            'ASSIGN_END','TO_START','TO_END', 'ADD_START','ADD_END','MUL_START',
            'MUL_END','SUB_START','SUB_END','DIV_START','DIV_END','NOT_START',
            'NOT_END','OR_START','OR_END', 'AND_START', 'AND_END','MAX_START',
            'MAX_END','MIN_START','MIN_END', 'EQ_START','EQ_END','WHILE_START',
            'WHILE_END','CHECK_START','CHECK_END','LEFT_START','LEFT_END',
            'RIGHT_START','RIGHT_END','UP_START','UP_END','DOWN_START','DOWN_END',
            'DO_START','DO_END','SWITCH_START', 'SWITCH_END','CONDITION_START',
            'CONDITION_END','SENDDRONS_START','SENDDRONS_END', 
            'GETDRONSCOUNT_START','GETDRONSCOUNT_END','FUNC_START','FUNC_END',
            'CALL_START','CALL_END','PROGRAM_START','PROGRAM_END','RBRACKET','LBRACKET'] + list(reserved.values())

	t_ignore = ' \t' #переход на новую строчку?

	def t_VARDECLARATION_START(self,t):
		r'<VARDECLARATION>'
		return t

	def t_VARDECLARATION_END(self,t):
		r'</VARDECLARATION>'
		return t

	def t_VAR_START(self,t):
		r'<VAR'
		return t

	def t_VAR_END(self,t):
		r'/VAR>'
		return t

	def t_TYPE_START(self,t):
		r'<TYPE>'
		return t

	def t_TYPE_END(self,t):
		r'</TYPE>'
		return t

	def t_DIMENSIONS_START(self,t):
		r'<DIMENSIONS'
		return t

	def t_DIMENSIONS_END(self,t):
		r'</DIMENSIONS>'
		return t

	def t_DIMENSION_START(self,t):
		r'<DIMENSION>'
		return t

	def t_DIMENSION_END(self,t):
		r'</DIMENSION>'
		return t

	def t_VALUES_START(self,t):
		r'<VALUES>'
		return t

	def t_VALUES_END(self,t):
		r'</VALUES>'
		return t

	def t_VALUE_START(self,t):
		r'<VALUE>'
		return t

	def t_VALUE_END(self,t):
		r'</VALUE>'
		return t

	def t_DIM_START(self,t):
		r'<DIM>'
		return t

	def t_DIM_END(self,t):
		r'</DIM>'
		return t

	def t_INDEX_START(self,t):
		r'<INDEX>'
		return t

	def t_INDEX_END(self,t):
		r'</INDEX>'
		return t

	def t_ASSIGN_START(self,t):
		r'<ASSIGN>'
		return t

	def t_ASSIGN_END(self,t):
		r'</ASSIGN>'
		return t

	def t_TO_START(self,t):
		r'<TO>'
		return t

	def t_TO_END(self,t):
		r'</TO>'
		return t

	def t_ADD_START(self,t):
		r'<ADD>'
		return t

	def t_ADD_END(self,t):
		r'</ADD>'
		return t

	def t_MUL_START(self,t):
		r'<MUL>'
		return t

	def t_MUL_END(self,t):
		r'</MUL>'
		return t

	def t_SUB_START(self,t):
		r'<SUB>'
		return t

	def t_SUB_END(self,t):
		r'</SUB>'
		return t

	def t_DIV_START(self,t):
		r'<DIV>'
		return t

	def t_DIV_END(self,t):
		r'</DIV>'
		return t

	def t_NOT_START(self,t):
		r'<NOT>'
		return t

	def t_NOT_END(self,t):
		r'</NOT>'
		return t

	def t_OR_START(self,t):
		r'<OR>'
		return t

	def t_OR_END(self,t):
		r'</OR>'
		return t

	def t_AND_START(self,t):
		r'<AND>'
		return t

	def t_AND_END(self,t):
		r'</AND>'
		return t

	def t_MAX_START(self,t):
		r'<MAX>'
		return t

	def t_MAX_END(self,t):
		r'</MAX>'
		return t

	def t_MIN_START(self,t):
		r'<MIN>'
		return t

	def t_MIN_END(self,t):
		r'</MIN>'
		return t

	def t_EQ_START(self,t):
		r'<EQ>'
		return t

	def t_EQ_END(self,t):
		r'</EQ>'
		return t

	def t_WHILE_START(self,t):
		r'<WHILE>'
		return t

	def t_WHILE_END(self,t):
		r'</WHILE>'
		return t

	def t_CHECK_START(self,t):
		r'<CHECK>'
		return t

	def t_CHECK_END(self,t):
		r'</CHECK>'
		return t

	def t_LEFT_START(self,t):
		r'<LEFT>'
		return t

	def t_LEFT_END(self,t):
		r'</LEFT>'
		return t

	def t_RIGHT_START(self,t):
		r'<RIGHT>'
		return t

	def t_RIGHT_END(self,t):
		r'</RIGHT>'
		return t

	def t_UP_START(self,t):
		r'<UP>'
		return t

	def t_UP_END(self,t):
		r'</UP>'
		return t

	def t_DOWN_START(self,t):
		r'<DOWN>'
		return t

	def t_DOWN_END(self,t):
		r'</DOWN>'
		return t

	def t_DO_START(self,t):
		r'<DO>'
		return t

	def t_DO_END(self,t):
		r'</DO>'
		return t

	def t_SWITCH_START(self,t):
		r'<SWITCH>'
		return t

	def t_SWITCH_END(self,t):
		r'</SWITCH>'
		return t

	def t_CONDITION_START(self,t):
		r'<CONDITION>'
		return t

	def t_CONDITION_END(self,t):
		r'</CONDITION>'
		return t

	def t_SENDDRONS_START(self,t):
		r'<SENDDRONS>'
		return t

	def t_SENDDRONS_END(self,t):
		r'</SENDDRONS>'
		return t

	def t_GETDRONSCOUNT_START(self,t):
		r'<GETDRONSCOUNT>'
		return t

	def t_GETDRONSCOUNT_END(self,t):
		r'</GETDRONSCOUNT>'
		return t

	def t_FUNC_START(self,t):
		r'<FUNC'
		return t

	def t_FUNC_END(self,t):
		r'</FUNC>'
		return t

	def t_CALL_START(self,t):
		r'<CALL>'
		return t
    
	def t_CALL_END(self,t):
		r'</CALL>'
		return t
    
	def t_PROGRAM_START(self,t):
		r'<PROGRAM>'
		return t
    
	def t_PROGRAM_END(self,t):
		r'</PROGRAM>'
		return t
      
	def t_ID(self, t):
		r'[a-zA-Z_][a-zA-Z_0-9]*'
		t.type = reserved.get(t.value,'ID')    
		return t

	def t_NUMBER(self, t):
		r'(\+|-)?\d+'
		t.value = int(t.value) 
		return t
	
	def t_EQUALSIGN(self, t):
		r'='
		return t

	def t_LBRACKET(self, t):
		r'\<'
		return t

	def t_RBRACKET(self, t):
		r'\>'
		return t

	def t_newline(self, t):
		r'\n+'
		t.lexer.lineno += len(t.value)

	def t_error(self, t):
		#print("Illegal character '%s'" % t.value[0])
		t.lexer.skip(1)
		return t

	def __init__(self):
		self.lexer = lex.lex(module=self)
		
	def input(self, data):
		return self.lexer.input(data)

	def token(self):
		return self.lexer.token()

if __name__ == '__main__':
	lexer = Lexer()
	f = open('test(factorial)')
	lexer.input(f.read())
	f.close()
	for tok in lexer.lexer:
		print(tok)

	




