class SymbolTable:
    def __init__(self):
        self.symbol_list = []

    def add_symbol(self, symbol):
        self.symbol_list.append(symbol)

    def delete_symbol(self, index):
        self.symbol_list.pop(index)

    def search_symbol(self, index):
        return self.symbol_list[index]


class Symbol:
    def __init__(self, position, symbol_id, symbol_type, value):
        self.position = position
        self.symbol_id = symbol_id
        self.symbol_type = symbol_type
        self.value = value

