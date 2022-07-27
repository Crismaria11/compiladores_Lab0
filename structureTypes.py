# Data types
TYPES = ['int', 'bool', 'char', 'string']

# Scope definition
class Scope:
    def __init__(self, scope_id, name, parent, scope_type, parameters):
        self.scope_id = scope_id
        self.name = name
        self.parent = parent
        self.scope_type = scope_type
        self.parameters = parameters
        self.symbols = []
        self.child_scopes = []

    def get_scope(self, name):
        for instance in self.child_scopes:
            if instance.name == name:
                return instance


# Symbol definition
class Symbol:
    def __init__(self, position, symbol_id, symbol_type, value):
        self.position = position        # offset
        self.symbol_id = symbol_id
        self.symbol_type = symbol_type
        self.value = value              # name

# Error definition
class Error:
    def __init__(self, message, line):
        self.message = message
        self.line = line

