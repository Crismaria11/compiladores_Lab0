from pruebaVisitor import pruebaVisitor


class SymbolTable:
    def __init__(self):
        self.symbol_list = []

    def add_symbol(self, symbol):
        self.symbol_list.append(symbol)

    def delete_symbol(self, index):
        self.symbol_list.pop(index)

    def search_symbol(self, index):
        return self.symbol_list[index]



