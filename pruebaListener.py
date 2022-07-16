# Generated from prueba.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pruebaParser import pruebaParser
else:
    from pruebaParser import pruebaParser

# This class defines a complete listener for a parse tree produced by pruebaParser.
class pruebaListener(ParseTreeListener):

    # Enter a parse tree produced by pruebaParser#program.
    def enterProgram(self, ctx:pruebaParser.ProgramContext):
        pass

    # Exit a parse tree produced by pruebaParser#program.
    def exitProgram(self, ctx:pruebaParser.ProgramContext):
        pass


    # Enter a parse tree produced by pruebaParser#programData.
    def enterProgramData(self, ctx:pruebaParser.ProgramDataContext):
        pass

    # Exit a parse tree produced by pruebaParser#programData.
    def exitProgramData(self, ctx:pruebaParser.ProgramDataContext):
        pass


    # Enter a parse tree produced by pruebaParser#classSpecification.
    def enterClassSpecification(self, ctx:pruebaParser.ClassSpecificationContext):
        pass

    # Exit a parse tree produced by pruebaParser#classSpecification.
    def exitClassSpecification(self, ctx:pruebaParser.ClassSpecificationContext):
        pass


    # Enter a parse tree produced by pruebaParser#feature.
    def enterFeature(self, ctx:pruebaParser.FeatureContext):
        pass

    # Exit a parse tree produced by pruebaParser#feature.
    def exitFeature(self, ctx:pruebaParser.FeatureContext):
        pass


    # Enter a parse tree produced by pruebaParser#formal.
    def enterFormal(self, ctx:pruebaParser.FormalContext):
        pass

    # Exit a parse tree produced by pruebaParser#formal.
    def exitFormal(self, ctx:pruebaParser.FormalContext):
        pass


    # Enter a parse tree produced by pruebaParser#expr.
    def enterExpr(self, ctx:pruebaParser.ExprContext):
        pass

    # Exit a parse tree produced by pruebaParser#expr.
    def exitExpr(self, ctx:pruebaParser.ExprContext):
        pass



del pruebaParser