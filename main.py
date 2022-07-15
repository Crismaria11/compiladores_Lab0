import sys
from antlr4 import *
from dist.pruebaLexer import pruebaLexer
from dist.pruebaParser import pruebaParser
from dist.pruebaVisitor import pruebaVisitor


def get_username():
    from pwd import getpwuid
    from os import getuid
    return getpwuid(getuid())[ 0 ]


class visitor(MyGrammerVisitor):
    def visitNumberExpr(self, ctx):
        value = ctx.getText()
        return int(value)

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitInfixExpr(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        op = ctx.op.text
        operation =  {
        '+': lambda: l + r,
        '-': lambda: l - r,
        '*': lambda: l * r,
        '/': lambda: l / r,
        }
        return operation.get(op, lambda: None)()

    def visitByeExpr(self, ctx):
        print(f"goodbye {get_username()}")
        sys.exit(0)

    def visitHelloExpr(self, ctx):
        return (f"{ctx.getText()} {get_username()}")


if __name__ == "__main__":
    while 1:
        data =  InputStream(input(">>> "))
        # lexer
        lexer = pruebaLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = pruebaParser(stream)
        tree = parser.expr()
        # evaluator
        visitor = visitor()
        output = visitor.visit(tree)
        print(output)
