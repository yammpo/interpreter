import sys
import parser
import random
from typing import List, Optional, Union

class Variable:

	def __init__(self, symtype='var', value=None, const_flag=False):
		self.type = symtype
		self.value = value
		self.const_flag = const_flag
        
	def __repr__(self):
		return f'{self.type}, {self.value}, {self.const_flag}'

	def __deepcopy__(self, memodict={}):
		return Var(self.type, self.value, self.const_flag)

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
				#print(self.symbol_table)
		elif node.type == 'function':
			#self.scope += 1 #исправить проблемы с областью видимости!
			if node.value not in self.symbol_table[self.scope].keys(): #кстати надо в парсере исправить
				self.symbol_table[self.scope][node.value] = node   #не очень понимаю что это за таблица символов
				self.interpreter_node(node.children)               #что-то типа областей видимости
			else:                                                      #мб очередная функция: ее переменные?     
				sys.stderr.write(f'error: redeclaration of function\n')
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
			return expressions
		elif node.type == 'math':
			if node.value == '<ADD>':
				return self.addition(node.children)
			elif node.value == '<MUL>':
				return self.multiplication(node.children)
			elif node.value == '<SUB>':
				return self.subtraction(node.children)
			elif node.value == '<DIV>':
				return self.division(node.children)


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
		values = self.interpreter_node(op)
		if (values is None) or (len(values) < 2):
			sys.stderr.write(f'error: more arguments in addition expected\n')
			return
		summ = 0
		for value in values:
			summ += value.value
		return Variable('INT', summ, False)
	
	def multiplication(self, op: parser.SyntaxTreeNode):
		#ПРЕОБРАЗОВАНИЕ ТИПОВ!!!
		values = self.interpreter_node(op)
		if (values is None) or (len(values) < 2):
			sys.stderr.write(f'error: more arguments in multiplication expected\n')
			return
		mul = 1
		for value in values:
			mul *= value.value
		return Variable('INT', mul, False)
	
	def subtraction(self, op: parser.SyntaxTreeNode):
		#ПРЕОБРАЗОВАНИЕ ТИПОВ!!!
		values = self.interpreter_node(op)
		if (values is None) or (len(values) != 2):
			sys.stderr.write(f'error: two arguments in subtraction expected\n')
			return
		sub = values[0].value - values[1].value
		return Variable('INT', sub, False)

	def division(self, op: parser.SyntaxTreeNode):
		#ПРЕОБРАЗОВАНИЕ ТИПОВ!!!
		values = self.interpreter_node(op)
		if (values is None) or (len(values) != 2):
			sys.stderr.write(f'error: two arguments in division expected\n')
			return
		if values[1].value == 0:
			sys.stderr.write(f'error: division by zero\n')
			return
		div = values[0].value // values[1].value
		return Variable('INT', div, False)

	def print_symbol(self):
		print(self.symbol_table)
		
if __name__ == '__main__':
	interpreter = Interpreter()
	f=open('test(1)','r')
	interpreter.interpreter(f.read())
	f.close()
	interpreter.print_symbol()
	
						








