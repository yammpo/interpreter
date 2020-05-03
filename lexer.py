import ply.lex as lex

reserved = {
	'INT': 'INT', 'BOOL': 'BOOL', 'TRUE': 'TRUE', 'FALSE': 'FALSE', 'CELL': 'CELL', 'EMPTY': 'EMPTY', 'WALL': 'WALL',
	'EXIT': 'EXIT', 'UNDEF': 'UNDEF', 'VARDECLARATION': 'VARDECLARATION', 'VAR': 'VAR', 'CONST': 'CONST', 'TYPE': 'TYPE',
	'DIMENSIONS': 'DIMENSIONS', 'count': 'COUNT', 'DIMENSION': 'DIMENSION', 'VALUES': 'VALUES', 'VALUE': 'VALUE', 'name': 'NAME',
	'DIM': 'DIM', 'INDEX': 'INDEX', 'ASSIGN': 'ASSIGN', 'TO': 'TO', 'ADD': 'ADD', 'MUL': 'MUL', 'SUB': 'SUB', 'DIV': 'DIV',
	'NOT': 'NOT', 'OR': 'OR', 'AND': 'AND', 'MAX': 'MAX', 'MIN': 'MIN', 'EQ': 'EQ', 'WHILE': 'WHILE', 'CHECK': 'CHECK',
	'LEFT': 'LEFT', 'RIGHT': 'RIGHT', 'UP': 'UP', 'DOWN': 'DOWN', 'DO': 'DO', 'SWITCH': 'SWITCH', 'CONDITION': 'CONDITION',
	'CHECK': 'CHECK', 'SENDDRONS': 'SENDDRONS', 'GETDRONSCOUNT': 'GETDRONSCOUNT', 'FUNC': 'FUNC', 'CALL': 'CALL',
	'PROGRAM': 'PROGRAM', 'main': 'MAIN'
}

class Lexer():
	
	tokens = ['ID', 'NUMBER', 'SLASH', 'EQUALSIGN', 'LBRACKET', 'RBRACKET'] + list(reserved.values())
	t_ignore = ' \t' #переход на новую строчку?

	def t_ID(self, t):
		r'[a-zA-Z_][a-zA-Z_0-9]*'
		t.type = reserved.get(t.value,'ID')    # Check for reserved words
		return t

	def t_NUMBER(self, t):
		r'\d+'
		t.value = int(t.value) #узнать зачем это
		return t

	def t_SLASH(self, t):
		r'/'
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

lexer = Lexer()
f = open('test(factorial)')
lexer.input(f.read())
f.close()
for tok in lexer.lexer:
	print(tok)

	




