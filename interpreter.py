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
		elif node.type == 'declaration_var':
			if node.children.value in self.symbol_table[self.scope].keys():
				sys.stderr.write(f'error: redeclaration of variable\n')
			else:
				self.symbol_table[self.scope][node.children.value] = Variable(node.value.value, None, False)
				#print(self.symbol_table)
		elif node.type == 'function':
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
					variables.extend(self.interpreter_node(child))
				else:
					return None
			#for i in range(len(node.children)):
			#	variables.extend(self.interpreter_node(node.children[i]))
			return variables
		elif node.type == 'variable':
			name = node.value.value
			return self.find_variable(name)
		elif node.type == 'const':
			return Variable('INT', node.value, True) #в лексере уже сделали интом. можно убрать и сделать тут.
			#или писать это после всех проверок на остальные константы

	def assignment(self, node: parser.SyntaxTreeNode): # с множественными пока не работает, хз почему
		#variables = []
		#for i in range(len(node.children[1].children)):
		#	variables.extend(self.interpreter_node(node.children[1].children[i]))
		#	if variables[i] is None:
		#		sys.stderr.write(f'error: undeclarated variable {i}\n') #вывести, какая именно undeclarated
		#		return
		variables = self.interpreter_node(node.children[1])
		if variables is None: return
		expression = self.interpreter_node(node.children[0]) 
		#проверить типы, если надо преобразовать
		#проверить отдельно для присваивания всего массива
		#проверить константность
		for i in range(len(variables)):
			variables[i].type = expression.type
			variables[i].value = expression.value
	
	def find_variable(self, name):
		if name in self.symbol_table[0].keys():
			return [self.symbol_table[0][name]]
		elif name in self.symbol_table[self.scope].keys():
			return [self.symbol_table[self.scope][name]]
		else:
			sys.stderr.write(f'error: undeclarated variable {name}\n')
	
	def print_symbol(self):
		print(self.symbol_table)
		
if __name__ == '__main__':
	interpreter = Interpreter()
	f=open('test(1)','r')
	interpreter.interpreter(f.read())
	f.close()
	interpreter.print_symbol()
	
						








