from pruebaVisitor import pruebaVisitor
import structureTypes as structures



class antlrVisitor(pruebaVisitor):

    def visitProgram(self, ctx):
        self.visitChildren(ctx)

        # Last scope is main

class SymbolTable:
    def __init__(self):
        self.symbol_list = []

    def add_symbol(self, symbol):
        self.symbol_list.append(symbol)

    def delete_symbol(self, index):
        self.symbol_list.pop(index)

    def search_symbol(self, index):
        return self.symbol_list[index]



