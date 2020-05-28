import sys
import parser
import random
from typing import List, Optional, Union

class Variable:
	#перегрузка операторов:
	def __init__(self, symtype='var', value=None, const_flag=False):
		self.type = symtype
		self.value = value
		self.const_flag = const_flag
        
	def __repr__(self):
		if self.type == 'BOOL':
			if self.value is True:
				self.value = 'TRUE'
			else:
				self.value = 'FALSE'
		return f'{self.type}, {self.value}, {self.const_flag}'

	def __deepcopy__(self, memodict={}):
		return Var(self.type, self.value, self.const_flag)
	
	def __lt__(self, other):
		if self.value < other.value:
			return True
		return False

	def __gt__(self, other):
		if self.value > other.value:
			return True
		return False

	def __eq__(self, other):
		if self.value == other.value:
			return True
		return False

	def __bool__(self):
		return bool(self.value)

class Interpreter:

	def __init__(self):
		self.parser = parser.Parser()
		self.program = None
		self.symbol_table = [dict()]
		self.functions = dict()
		self.tree = None
		self.scope = 0

	def interpreter(self, prog=None):
		self.prog = prog
		self.tree, self.functions, parsing_ok = self.parser.parse(self.prog)
		if parsing_ok:
			#self.interpreter_tree(self.tree)
			self.interpreter_node(self.tree)
			if 'main' not in self.functions.keys():
				sys.stderr.write(f'error: no main function\n')
				return
			else:
				self.interpreter_node(self.functions['main'])
		else:
			sys.stderr.write(f'Can\'t intemperate this, incorrect syntax\n')

	def interpreter_tree(self, tree):
		print("Program tree:\n")
		tree.print()
		print("\n")

	def interpreter_node(self, node: parser.SyntaxTreeNode):
		if node is None:
			return
		if node.type == 'program':
			self.interpreter_node(node.children)
		elif node.type == 'blocks': 
			for child in node.children: 
				self.interpreter_node(child)
		elif node.type == 'vardeclaration':
			self.interpreter_node(node.children)
		elif node.type == 'declarations':
			for child in node.children:
				self.interpreter_node(child)
		elif node.type == 'declaration_var':
			name = node.children.value
			if (name in self.symbol_table[self.scope].keys()) or (name in self.symbol_table[0].keys()):
				sys.stderr.write(f'error: redeclaration of variable {name}\n')
				return
			else:
				self.symbol_table[self.scope][name] = Variable(node.value.value, None, False)
		elif (node.type == 'declaration_var_init'):
			self.initialization(node, False)
		elif (node.type == 'declaration_var_const'): # можно ли константы задавать другими переменными?
			self.initialization(node, True)
		elif node.type == 'function':
			if node.value.value not in self.functions.keys():
				self.functions[node.value.value] = node.children #занесли в словарь имя функции : statements
				#self.interpreter_node(node.children)              
			else:                                                        
				sys.stderr.write(f'error: redeclaration of function {node.value.value}\n')
		#надо сделать штуку для глобальных переменных, например нулевой scope
		#переделать: в function не интерпретировать, интерпретировать в CALL и в main
		elif node.type == 'function_call': # можно ли вызывать main?
			self.function_call(node)
		elif node.type == 'statements':
			for child in node.children:
				self.interpreter_node(child)
		elif node.type == 'assignment':
			self.assignment(node)
		elif node.type == 'variables':
			variables = []
			for child in node.children:
				var = self.interpreter_node(child)
				if var is not None:
					variables.extend(var)
				else: return None
			return variables
		elif node.type == 'variable':
			name = node.value.value
			return self.find_variable(name)
		elif node.type == 'const':
			value = node.value
			if isinstance(value, int):
				return Variable('INT', value, True)
			elif value == 'FALSE':
				return Variable('BOOL', False, True)
			elif value == 'TRUE':
				return Variable('BOOL', True, True)
			else:
				return Variable('CELL', value, True) #EMPTY/WALL/EXIT/UNDEF
		elif node.type == 'expressions':
			expressions = [] #можно этот код в функцию вынести
			for child in node.children:
				expr = self.interpreter_node(child)
				if expr is not None:
					if isinstance(expr,list):
						expressions.extend(expr)
					else:
						expressions.append(expr)
				else: return None
			return expressions #проверить не может ли вернуться пустой список
		elif node.type == 'conditions':
			for child in node.children:
				self.interpreter_node(child)
		elif node.type == 'condition':
			condition = self.interpreter_node(node.children['condition'])
			if condition.type == 'CELL':
				sys.stderr.write(f'error: cannot convert CELL to BOOL to check a condition\n')
				return
			if condition.value is True:
				self.interpreter_node(node.children['body'])
		elif node.type == 'switch':
			self.interpreter_node(node.children)
		elif node.type == 'while':
			while True:
				condition = self.interpreter_node(node.children['condition'])
				if condition.type == 'CELL':
					sys.stderr.write(f'error: cannot convert CELL to BOOL to check a condition\n')
					return
				if condition.value is True:
					self.interpreter_node(node.children['body'])
				else:
					break
		elif node.type == 'math':
			if node.value == '<ADD>':
				return self.addition(node.children)
			elif node.value == '<MUL>':
				return self.multiplication(node.children)
			elif node.value == '<SUB>':
				return self.subtraction(node.children)
			elif node.value == '<DIV>':
				return self.division(node.children)
			elif node.value == '<MAX>':
				return self.maximum(node.children)
			elif node.value == '<MIN>':
				return self.minimum(node.children)
			elif node.value == '<EQ>':
				return self.equality(node.children)
			elif node.value == '<OR>':
				return self.logic_or(node.children)
			elif node.value == '<AND>':
				return self.logic_and(node.children)
			elif node.value == '<NOT>':
				return self.logic_not(node.children)
				
	def assignment(self, node: parser.SyntaxTreeNode): 
		variables = self.interpreter_node(node.children[1])
		# не очень понимаю, за счёт чего тут меняются элементы таблицы символов...
		if variables is None:
			sys.stderr.write(f'error: incorrect variables in assignment\n')
			return
		expression = self.interpreter_node(node.children[0])
		if expression is None:
			sys.stderr.write(f'error: incorrect expression in assignment\n')
			return 
		#проверить отдельно для присваивания всего массива
		if isinstance(expression,list):
			expression = expression[0]
		for var in variables:
			if var.const_flag is True:
				sys.stderr.write(f'error: cannot reinitialize the constant\n')
				return
			conversed_var = self.type_conversion(var, expression)
			if conversed_var is None: 
				sys.stderr.write(f'error: assignment error\n')
				return
			var.type = conversed_var.type
			var.value = conversed_var.value
	
	def find_variable(self, name):
		if name in self.symbol_table[0].keys():
			return [self.symbol_table[0][name]]
		if name in self.symbol_table[self.scope].keys():
			return [self.symbol_table[self.scope][name]]
		sys.stderr.write(f'error: undeclarated variable {name}\n')
	
	def bool_to_int(self, var: Variable):
		var.type = 'INT'
		if var.value is True:
			var.value = 1
		else:
			var.value = 0
		return var
		
	def int_to_bool(self, var: Variable):
		var.type = 'BOOL'
		if var.value == 0:
			var.value = False
		else:
			var.value = True
		return var
		
	def type_conversion(self, var1: Variable, var2: Variable):
		var2.const_flag = var1.const_flag
		if var1.type != var2.type:
			if (var1.type == 'CELL') or (var2.type == 'CELL'):
				sys.stderr.write(f'error: cannot convert {var2.type} to {var1.type}\n')
				return
			elif var2.type == 'BOOL':
				return self.bool_to_int(var2)
			elif var2.type == 'INT':
				return self.int_to_bool(var2)
		else:
			return var2
		
	def initialization(self, node: parser.SyntaxTreeNode, flag: bool):
		vartype = node.value.value
		name = node.children[0].value
		if (name in self.symbol_table[self.scope].keys()) or (name in self.symbol_table[0].keys()):
			sys.stderr.write(f'error: redeclaration of variable {name}\n')
			return
		expr = self.interpreter_node(node.children[1])
		if isinstance(expr,list):
			expr = expr[0]	
		var = self.type_conversion(Variable(vartype, None, flag), expr)
		if var is None: 
			sys.stderr.write(f'error: initialization error of variable {name}\n')
			return 
		self.symbol_table[self.scope][name] = var
				
	def addition(self, op: parser.SyntaxTreeNode):
		expressions = self.interpreter_node(op)
		if (expressions is None): # or (len(expressions) < 2)
			sys.stderr.write(f'error: more arguments in addition expected\n')
			return
		summ = 0
		for expression in expressions:
			if expression.type == 'CELL':
				sys.stderr.write(f'error: cannot convert CELL to INT to do the addition\n')
				return
			summ += expression.value
		return Variable('INT', summ, False)
	
	def multiplication(self, op: parser.SyntaxTreeNode):
		expressions = self.interpreter_node(op)
		if (expressions is None): # or (len(expressions) < 2
			sys.stderr.write(f'error: more arguments in multiplication expected\n')
			return
		mul = 1
		for expression in expressions:
			if expression.type == 'CELL':
				sys.stderr.write(f'error: cannot convert CELL to INT to do the multiplication\n')
				return
			mul *= expression.value
		return Variable('INT', mul, False)
	
	def subtraction(self, op: parser.SyntaxTreeNode):
		expressions = self.interpreter_node(op)
		if (expressions is None) or (len(expressions) != 2):
			sys.stderr.write(f'error: two arguments in subtraction expected\n')
			return
		if (expressions[0].type == 'CELL') or (expressions[1].type == 'CELL'):
			sys.stderr.write(f'error: cannot convert CELL to INT to do the subtraction\n')
			return
		return Variable('INT', expressions[0].value - expressions[1].value, False)

	def division(self, op: parser.SyntaxTreeNode):
		expressions = self.interpreter_node(op)
		if (expressions is None) or (len(expressions) != 2):
			sys.stderr.write(f'error: more arguments in division expected\n')
			return
		if expressions[1].value == 0:
			sys.stderr.write(f'error: division by zero\n')
			return
		if (expressions[0].type == 'CELL') or (expressions[1].type == 'CELL'):
			sys.stderr.write(f'error: cannot convert CELL to INT to do the division\n')
			return
		return Variable('INT', expressions[0].value // expressions[1].value, False)

	def maximum(self, op: parser.SyntaxTreeNode):
		expressions = self.interpreter_node(op)
		if (expressions is None):
			sys.stderr.write(f'error: more arguments in maximum expected\n')
			return
		for expression in expressions:
			if expression.type == 'CELL':
				sys.stderr.write(f'error: cannot convert CELL to INT to find the maximum\n')
				return
		return Variable('INT', max(expressions).value, False)

	def minimum(self, op: parser.SyntaxTreeNode):
		expressions = self.interpreter_node(op)
		if (expressions is None):
			sys.stderr.write(f'error: more arguments in minimum expected\n')
			return
		for expression in expressions:
			if expression.type == 'CELL':
				sys.stderr.write(f'error: cannot convert CELL to INT to find the minimum\n')
				return
		return Variable('INT', min(expressions).value, False)

	def equality(self, op: parser.SyntaxTreeNode): #непонятно, к какому типу приводить
		expressions = self.interpreter_node(op)
		if (expressions is None):
			sys.stderr.write(f'error: more arguments in equality expected\n')
			return	
		return Variable('BOOL', len(expressions) == expressions.count(expressions[0]), False)
		
	def logic_or(self, op: parser.SyntaxTreeNode):
		expressions = self.interpreter_node(op)
		if (expressions is None):
			sys.stderr.write(f'error: more arguments in logic or expected\n')
			return
		for expression in expressions:
			if expression.type == 'CELL':
				sys.stderr.write(f'error: cannot convert CELL to BOOL to do the logic or\n')
				return
		return Variable('BOOL', any(expressions), False)

	def logic_and(self, op: parser.SyntaxTreeNode):
		expressions = self.interpreter_node(op)
		if (expressions is None):
			sys.stderr.write(f'error: more arguments in logic and expected\n')
			return
		for expression in expressions:
			if expression.type == 'CELL':
				sys.stderr.write(f'error: cannot convert CELL to BOOL to do the logic and\n')
				return
		return Variable('BOOL', all(expressions), False)
		
	def logic_not(self, op: parser.SyntaxTreeNode):
		expression = self.interpreter_node(op)
		if (expression is None):
			sys.stderr.write(f'error: more arguments in logic not expected\n')
			return
		if isinstance(expression,list):
			expression = expression[0]
		if expression.type == 'CELL':
			sys.stderr.write(f'error: cannot convert CELL to BOOL to do the logic not\n')
			return
		return Variable('BOOL', not expression.value, False)

	def function_call(self, node: parser.SyntaxTreeNode):
		if self.scope == 1000:
			sys.stderr.write(f'error: recursion\n')
			return
		funcname = node.value.value
		if funcname not in self.functions.keys():
			sys.stderr.write(f'error: call of undeclarated function\n')
			return
		self.scope += 1
		self.symbol_table.append(dict())
		statements = self.functions[funcname]
		if statements is not None:
			self.interpreter_node(statements)   
		self.scope -= 1 #хз
		self.symbol_table.pop()
		
	def print_symbol(self):
		print(self.symbol_table)
		
if __name__ == '__main__':
	interpreter = Interpreter()
	f=open('test(math)','r')
	interpreter.interpreter(f.read())
	f.close()
	interpreter.print_symbol()
	
						








