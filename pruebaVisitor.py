# Generated from prueba.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pruebaParser import pruebaParser
else:
    from pruebaParser import pruebaParser

# This class defines a complete generic visitor for a parse tree produced by pruebaParser.

class pruebaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by pruebaParser#program.
    def visitProgram(self, ctx:pruebaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#programData.
    def visitProgramData(self, ctx:pruebaParser.ProgramDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#classSpecification.
    def visitClassSpecification(self, ctx:pruebaParser.ClassSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#feature.
    def visitFeature(self, ctx:pruebaParser.FeatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#formal.
    def visitFormal(self, ctx:pruebaParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#expr.
    def visitExpr(self, ctx:pruebaParser.ExprContext):
        return self.visitChildren(ctx)



del pruebaParser