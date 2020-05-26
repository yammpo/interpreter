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
		return f'{self.type}, {self.value}, {self.const_flag}'

	def __deepcopy__(self, memodict={}):
		return Var(self.type, self.value, self.const_flag)
	
	#cледующие перегрузки только для интовых переменных:
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

	#только для переменных типа bool:
	def __bool__(self):
		return self.value

class Interpreter:

	def __init__(self):
		self.parser = parser.Parser()
		self.program = None
		self.symbol_table = [dict()]
		self.functions = None
		self.tree = None
		self.scope = 0

	def interpreter(self, prog=None):
		self.prog = prog
		self.tree, self.functions, parsing_ok = self.parser.parse(self.prog)
		if parsing_ok:
			self.interpreter_tree(self.tree)
			self.interpreter_node(self.tree)
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
		elif node.type == 'blocks': #написать отдельно если один блок всего
			#for i in range(len(node.children)):
			#	self.interpreter_node(node.children[i])
			for child in node.children: 
				self.interpreter_node(child)
		elif node.type == 'vardeclaration':
			self.interpreter_node(node.children)
		elif node.type == 'declarations': #надо в словаре хранить флажочек константа это или нет
			for child in node.children:
				self.interpreter_node(child)
		elif node.type == 'declaration_var': #cделать с инициализацией
			if node.children.value in self.symbol_table[self.scope].keys():
				sys.stderr.write(f'error: redeclaration of variable {node.children.value}\n')
			else:
				self.symbol_table[self.scope][node.children.value] = Variable(node.value.value, None, False)
		elif node.type == 'declaration_var_init': #можно в парсере попробовать объединить const с init
			#ПРОВЕРКА И ПРЕОБРАЗОВАНИЕ ТИПОВ
			if node.children[0].value in self.symbol_table[self.scope].keys():
				sys.stderr.write(f'error: redeclaration of variable {node.children.value}\n')
			else:
				expr = self.interpreter_node(node.children[1])
				if isinstance(expr,list):
					expr = expr[0]
				self.symbol_table[self.scope][node.children[0].value] = Variable(node.value.value, expr.value, False)
		elif node.type == 'function':
			if node.value not in self.symbol_table[self.scope].keys(): #кстати надо в парсере исправить
				self.symbol_table[self.scope][node.value] = node   #не очень понимаю что это за таблица символов
				self.interpreter_node(node.children)               #что-то типа областей видимости
			else:                                                      #мб очередная функция: ее переменные?     
				sys.stderr.write(f'error: redeclaration of function\n')
		#надо сделать штуку для глобальных переменных, например нулевой scope
		#переделать: в function не интерпретировать, интерпретировать в CALL и в main

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
					#variables.extend(self.interpreter_node(child))
				else: return None
			return variables
		elif node.type == 'variable':
			name = node.value.value
			return self.find_variable(name)
		elif node.type == 'const':
			#if node.value == 'FALSE':
			#	return Variable('BOOL', node.value, True)
			return Variable('INT', node.value, True) # это для number
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
		if variables is None: 
			return
		expression = self.interpreter_node(node.children[0])
		if expression is None:
			return 
		#проверить типы, если надо преобразовать
		#проверить отдельно для присваивания всего массива
		#проверить константность
		if isinstance(expression,list):
			expression = expression[0]
		for i in range(len(variables)):
			variables[i].type = expression.type
			variables[i].value = expression.value
	
	def find_variable(self, name):
		if name in self.symbol_table[0].keys():
			return [self.symbol_table[0][name]]
		if name in self.symbol_table[self.scope].keys():
			return [self.symbol_table[self.scope][name]]
		sys.stderr.write(f'error: undeclarated variable {name}\n')
	
	def addition(self, op: parser.SyntaxTreeNode): #cумма кучи true чем должна быть?
		#ПРЕОБРАЗОВАНИЕ ТИПОВ!!!
		expressions = self.interpreter_node(op)
		if (expressions is None): # or (len(expressions) < 2)
			sys.stderr.write(f'error: more arguments in addition expected\n')
			return
		summ = 0
		for expression in expressions:
			summ += expression.value
		return Variable('INT', summ, False)
	
	def multiplication(self, op: parser.SyntaxTreeNode):
		#ПРЕОБРАЗОВАНИЕ ТИПОВ!!!
		expressions = self.interpreter_node(op)
		if (expressions is None): # or (len(expressions) < 2
			sys.stderr.write(f'error: more arguments in multiplication expected\n')
			return
		mul = 1
		for expression in expressions:
			mul *= expression.value
		return Variable('INT', mul, False)
	
	def subtraction(self, op: parser.SyntaxTreeNode):
		#ПРЕОБРАЗОВАНИЕ ТИПОВ!!!
		expressions = self.interpreter_node(op)
		if (expressions is None) or (len(expressions) != 2):
			sys.stderr.write(f'error: two arguments in subtraction expected\n')
			return
		return Variable('INT', expressions[0].value - expressions[1].value, False)

	def division(self, op: parser.SyntaxTreeNode):
		#ПРЕОБРАЗОВАНИЕ ТИПОВ!!!
		expressions = self.interpreter_node(op)
		if (expressions is None) or (len(expressions) != 2):
			sys.stderr.write(f'error: more arguments in division expected\n')
			return
		if expressions[1].value == 0:
			sys.stderr.write(f'error: division by zero\n')
			return
		return Variable('INT', expressions[0].value // expressions[1].value, False)

	def maximum(self, op: parser.SyntaxTreeNode):
		#ПРЕОБРАЗОВАНИЕ ТИПОВ!!!
		expressions = self.interpreter_node(op)
		if (expressions is None):
			sys.stderr.write(f'error: more arguments in maximum expected\n')
			return
		return Variable('INT', max(expressions).value, False)

	def minimum(self, op: parser.SyntaxTreeNode):
		#ПРЕОБРАЗОВАНИЕ ТИПОВ!!!
		expressions = self.interpreter_node(op)
		if (expressions is None):
			sys.stderr.write(f'error: more arguments in minimum expected\n')
			return
		return Variable('INT', min(expressions).value, False)

	def equality(self, op: parser.SyntaxTreeNode):
		#ПРЕОБРАЗОВАНИЕ ТИПОВ!!!
		expressions = self.interpreter_node(op)
		if (expressions is None):
			sys.stderr.write(f'error: more arguments in equality expected\n')
			return	
		return Variable('BOOL', len(expressions) == expressions.count(expressions[0]), False)
		
	def logic_or(self, op: parser.SyntaxTreeNode):
		#ПРЕОБРАЗОВАНИЕ ТИПОВ!!!
		expressions = self.interpreter_node(op)
		if (expressions is None):
			sys.stderr.write(f'error: more arguments in logic or expected\n')
			return
		return Variable('BOOL', any(expressions), False)

	def logic_and(self, op: parser.SyntaxTreeNode):
		#ПРЕОБРАЗОВАНИЕ ТИПОВ!!!
		expressions = self.interpreter_node(op)
		if (expressions is None):
			sys.stderr.write(f'error: more arguments in logic and expected\n')
			return
		return Variable('BOOL', all(expressions), False)
		
	def logic_not(self, op: parser.SyntaxTreeNode):
		#ПРЕОБРАЗОВАНИЕ ТИПОВ!!!
		expression = self.interpreter_node(op)
		if (expression is None):
			sys.stderr.write(f'error: more arguments in logic not expected\n')
			return
		if isinstance(expression,list):
			expression = expression[0]
		return Variable('BOOL', not expression.value, False)
	
	def print_symbol(self):
		print(self.symbol_table)
		
if __name__ == '__main__':
	interpreter = Interpreter()
	f=open('test(1)','r')
	interpreter.interpreter(f.read())
	f.close()
	interpreter.print_symbol()
	
						








