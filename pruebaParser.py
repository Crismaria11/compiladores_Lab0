# Generated from prueba.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,46,204,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,1,1,1,1,1,1,5,1,19,8,1,10,1,12,1,22,9,1,1,1,3,1,25,8,1,1,2,
        1,2,1,2,1,2,3,2,31,8,2,1,2,1,2,1,2,1,2,5,2,37,8,2,10,2,12,2,40,9,
        2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,5,3,49,8,3,10,3,12,3,52,9,3,3,3,54,
        8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,68,8,3,3,
        3,70,8,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,
        85,8,5,10,5,12,5,88,9,5,3,5,90,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,111,8,5,10,5,12,
        5,114,9,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,123,8,5,1,5,1,5,1,5,1,
        5,1,5,1,5,3,5,131,8,5,5,5,133,8,5,10,5,12,5,136,9,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        3,5,157,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,183,8,5,1,5,1,5,
        1,5,1,5,1,5,1,5,5,5,191,8,5,10,5,12,5,194,9,5,3,5,196,8,5,1,5,5,
        5,199,8,5,10,5,12,5,202,9,5,1,5,0,1,10,6,0,2,4,6,8,10,0,0,237,0,
        12,1,0,0,0,2,24,1,0,0,0,4,26,1,0,0,0,6,69,1,0,0,0,8,71,1,0,0,0,10,
        156,1,0,0,0,12,13,3,2,1,0,13,14,5,0,0,1,14,1,1,0,0,0,15,16,3,4,2,
        0,16,17,5,1,0,0,17,19,1,0,0,0,18,15,1,0,0,0,19,22,1,0,0,0,20,18,
        1,0,0,0,20,21,1,0,0,0,21,25,1,0,0,0,22,20,1,0,0,0,23,25,5,0,0,1,
        24,20,1,0,0,0,24,23,1,0,0,0,25,3,1,0,0,0,26,27,5,20,0,0,27,30,5,
        38,0,0,28,29,5,26,0,0,29,31,5,38,0,0,30,28,1,0,0,0,30,31,1,0,0,0,
        31,32,1,0,0,0,32,38,5,2,0,0,33,34,3,6,3,0,34,35,5,1,0,0,35,37,1,
        0,0,0,36,33,1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,
        41,1,0,0,0,40,38,1,0,0,0,41,42,5,3,0,0,42,5,1,0,0,0,43,44,5,37,0,
        0,44,53,5,4,0,0,45,50,3,8,4,0,46,47,5,5,0,0,47,49,3,8,4,0,48,46,
        1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,54,1,0,0,0,
        52,50,1,0,0,0,53,45,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,55,56,5,
        6,0,0,56,57,5,7,0,0,57,58,5,38,0,0,58,59,5,2,0,0,59,60,3,10,5,0,
        60,61,5,3,0,0,61,70,1,0,0,0,62,63,5,37,0,0,63,64,5,7,0,0,64,67,5,
        38,0,0,65,66,5,8,0,0,66,68,3,10,5,0,67,65,1,0,0,0,67,68,1,0,0,0,
        68,70,1,0,0,0,69,43,1,0,0,0,69,62,1,0,0,0,70,7,1,0,0,0,71,72,5,37,
        0,0,72,73,5,7,0,0,73,74,5,38,0,0,74,9,1,0,0,0,75,76,6,5,-1,0,76,
        77,5,37,0,0,77,78,5,8,0,0,78,157,3,10,5,24,79,80,5,37,0,0,80,89,
        5,4,0,0,81,86,3,10,5,0,82,83,5,5,0,0,83,85,3,10,5,0,84,82,1,0,0,
        0,85,88,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,90,1,0,0,0,88,86,
        1,0,0,0,89,81,1,0,0,0,89,90,1,0,0,0,90,91,1,0,0,0,91,157,5,6,0,0,
        92,93,5,24,0,0,93,94,3,10,5,0,94,95,5,30,0,0,95,96,3,10,5,0,96,97,
        5,21,0,0,97,98,3,10,5,0,98,99,5,23,0,0,99,157,1,0,0,0,100,101,5,
        31,0,0,101,102,3,10,5,0,102,103,5,28,0,0,103,104,3,10,5,0,104,105,
        5,29,0,0,105,157,1,0,0,0,106,112,5,2,0,0,107,108,3,10,5,0,108,109,
        5,1,0,0,109,111,1,0,0,0,110,107,1,0,0,0,111,114,1,0,0,0,112,110,
        1,0,0,0,112,113,1,0,0,0,113,115,1,0,0,0,114,112,1,0,0,0,115,157,
        5,3,0,0,116,117,5,11,0,0,117,118,5,37,0,0,118,119,5,7,0,0,119,122,
        5,38,0,0,120,121,5,8,0,0,121,123,3,10,5,0,122,120,1,0,0,0,122,123,
        1,0,0,0,123,134,1,0,0,0,124,125,5,5,0,0,125,126,5,37,0,0,126,127,
        5,7,0,0,127,130,5,38,0,0,128,129,5,8,0,0,129,131,3,10,5,0,130,128,
        1,0,0,0,130,131,1,0,0,0,131,133,1,0,0,0,132,124,1,0,0,0,133,136,
        1,0,0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,137,1,0,0,0,136,134,
        1,0,0,0,137,138,5,25,0,0,138,157,3,10,5,18,139,140,5,32,0,0,140,
        157,5,38,0,0,141,142,5,27,0,0,142,157,3,10,5,16,143,144,5,16,0,0,
        144,157,3,10,5,11,145,146,5,33,0,0,146,157,3,10,5,7,147,148,5,4,
        0,0,148,149,3,10,5,0,149,150,5,6,0,0,150,157,1,0,0,0,151,157,5,37,
        0,0,152,157,5,36,0,0,153,157,5,41,0,0,154,157,5,34,0,0,155,157,5,
        22,0,0,156,75,1,0,0,0,156,79,1,0,0,0,156,92,1,0,0,0,156,100,1,0,
        0,0,156,106,1,0,0,0,156,116,1,0,0,0,156,139,1,0,0,0,156,141,1,0,
        0,0,156,143,1,0,0,0,156,145,1,0,0,0,156,147,1,0,0,0,156,151,1,0,
        0,0,156,152,1,0,0,0,156,153,1,0,0,0,156,154,1,0,0,0,156,155,1,0,
        0,0,157,200,1,0,0,0,158,159,10,15,0,0,159,160,5,12,0,0,160,199,3,
        10,5,16,161,162,10,14,0,0,162,163,5,13,0,0,163,199,3,10,5,15,164,
        165,10,13,0,0,165,166,5,14,0,0,166,199,3,10,5,14,167,168,10,12,0,
        0,168,169,5,15,0,0,169,199,3,10,5,13,170,171,10,10,0,0,171,172,5,
        17,0,0,172,199,3,10,5,11,173,174,10,9,0,0,174,175,5,18,0,0,175,199,
        3,10,5,10,176,177,10,8,0,0,177,178,5,19,0,0,178,199,3,10,5,9,179,
        182,10,23,0,0,180,181,5,9,0,0,181,183,5,38,0,0,182,180,1,0,0,0,182,
        183,1,0,0,0,183,184,1,0,0,0,184,185,5,10,0,0,185,186,5,37,0,0,186,
        195,5,4,0,0,187,192,3,10,5,0,188,189,5,5,0,0,189,191,3,10,5,0,190,
        188,1,0,0,0,191,194,1,0,0,0,192,190,1,0,0,0,192,193,1,0,0,0,193,
        196,1,0,0,0,194,192,1,0,0,0,195,187,1,0,0,0,195,196,1,0,0,0,196,
        197,1,0,0,0,197,199,5,6,0,0,198,158,1,0,0,0,198,161,1,0,0,0,198,
        164,1,0,0,0,198,167,1,0,0,0,198,170,1,0,0,0,198,173,1,0,0,0,198,
        176,1,0,0,0,198,179,1,0,0,0,199,202,1,0,0,0,200,198,1,0,0,0,200,
        201,1,0,0,0,201,11,1,0,0,0,202,200,1,0,0,0,20,20,24,30,38,50,53,
        67,69,86,89,112,122,130,134,156,182,192,195,198,200
    ]

class pruebaParser ( Parser ):

    grammarFileName = "prueba.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'{'", "'}'", "'('", "','", "')'", 
                     "':'", "'<-'", "'@'", "'.'", "'let'", "'+'", "'-'", 
                     "'*'", "'/'", "'~'", "'<'", "'<='", "'='", "<INVALID>", 
                     "<INVALID>", "'false'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'true'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'self'", "'SELF_TYPE'", "<INVALID>", "'(*'", "'*)'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "CLASS", "ELSE", "FALSE", "FI", "IF", "IN", "INHERITS", 
                      "ISVOID", "LOOP", "POOL", "THEN", "WHILE", "NEW", 
                      "NOT", "TRUE", "LET", "INTEGER", "ID", "TYPE", "SELF", 
                      "SELF_TYPE", "STRING", "START_COMMENT", "END_COMMENT", 
                      "COMMENT", "LINE_COMMENT", "WHITESPACE" ]

    RULE_program = 0
    RULE_programData = 1
    RULE_classSpecification = 2
    RULE_feature = 3
    RULE_formal = 4
    RULE_expr = 5

    ruleNames =  [ "program", "programData", "classSpecification", "feature", 
                   "formal", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    CLASS=20
    ELSE=21
    FALSE=22
    FI=23
    IF=24
    IN=25
    INHERITS=26
    ISVOID=27
    LOOP=28
    POOL=29
    THEN=30
    WHILE=31
    NEW=32
    NOT=33
    TRUE=34
    LET=35
    INTEGER=36
    ID=37
    TYPE=38
    SELF=39
    SELF_TYPE=40
    STRING=41
    START_COMMENT=42
    END_COMMENT=43
    COMMENT=44
    LINE_COMMENT=45
    WHITESPACE=46

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def programData(self):
            return self.getTypedRuleContext(pruebaParser.ProgramDataContext,0)


        def EOF(self):
            return self.getToken(pruebaParser.EOF, 0)

        def getRuleIndex(self):
            return pruebaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = pruebaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.programData()
            self.state = 13
            self.match(pruebaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramDataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classSpecification(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pruebaParser.ClassSpecificationContext)
            else:
                return self.getTypedRuleContext(pruebaParser.ClassSpecificationContext,i)


        def EOF(self):
            return self.getToken(pruebaParser.EOF, 0)

        def getRuleIndex(self):
            return pruebaParser.RULE_programData

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgramData" ):
                listener.enterProgramData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgramData" ):
                listener.exitProgramData(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgramData" ):
                return visitor.visitProgramData(self)
            else:
                return visitor.visitChildren(self)




    def programData(self):

        localctx = pruebaParser.ProgramDataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_programData)
        self._la = 0 # Token type
        try:
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==pruebaParser.CLASS:
                    self.state = 15
                    self.classSpecification()
                    self.state = 16
                    self.match(pruebaParser.T__0)
                    self.state = 22
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.match(pruebaParser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassSpecificationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(pruebaParser.CLASS, 0)

        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(pruebaParser.TYPE)
            else:
                return self.getToken(pruebaParser.TYPE, i)

        def INHERITS(self):
            return self.getToken(pruebaParser.INHERITS, 0)

        def feature(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pruebaParser.FeatureContext)
            else:
                return self.getTypedRuleContext(pruebaParser.FeatureContext,i)


        def getRuleIndex(self):
            return pruebaParser.RULE_classSpecification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassSpecification" ):
                listener.enterClassSpecification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassSpecification" ):
                listener.exitClassSpecification(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassSpecification" ):
                return visitor.visitClassSpecification(self)
            else:
                return visitor.visitChildren(self)




    def classSpecification(self):

        localctx = pruebaParser.ClassSpecificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classSpecification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(pruebaParser.CLASS)
            self.state = 27
            self.match(pruebaParser.TYPE)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==pruebaParser.INHERITS:
                self.state = 28
                self.match(pruebaParser.INHERITS)
                self.state = 29
                self.match(pruebaParser.TYPE)


            self.state = 32
            self.match(pruebaParser.T__1)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==pruebaParser.ID:
                self.state = 33
                self.feature()
                self.state = 34
                self.match(pruebaParser.T__0)
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
            self.match(pruebaParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FeatureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(pruebaParser.TYPE, 0)

        def expr(self):
            return self.getTypedRuleContext(pruebaParser.ExprContext,0)


        def ID(self):
            return self.getToken(pruebaParser.ID, 0)

        def formal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pruebaParser.FormalContext)
            else:
                return self.getTypedRuleContext(pruebaParser.FormalContext,i)


        def getRuleIndex(self):
            return pruebaParser.RULE_feature

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeature" ):
                listener.enterFeature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeature" ):
                listener.exitFeature(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFeature" ):
                return visitor.visitFeature(self)
            else:
                return visitor.visitChildren(self)




    def feature(self):

        localctx = pruebaParser.FeatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_feature)
        self._la = 0 # Token type
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.match(pruebaParser.ID)
                self.state = 44
                self.match(pruebaParser.T__3)
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==pruebaParser.ID:
                    self.state = 45
                    self.formal()
                    self.state = 50
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==pruebaParser.T__4:
                        self.state = 46
                        self.match(pruebaParser.T__4)
                        self.state = 47
                        self.formal()
                        self.state = 52
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 55
                self.match(pruebaParser.T__5)
                self.state = 56
                self.match(pruebaParser.T__6)
                self.state = 57
                self.match(pruebaParser.TYPE)
                self.state = 58
                self.match(pruebaParser.T__1)
                self.state = 59
                self.expr(0)
                self.state = 60
                self.match(pruebaParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(pruebaParser.ID)
                self.state = 63
                self.match(pruebaParser.T__6)
                self.state = 64
                self.match(pruebaParser.TYPE)
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==pruebaParser.T__7:
                    self.state = 65
                    self.match(pruebaParser.T__7)
                    self.state = 66
                    self.expr(0)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(pruebaParser.ID, 0)

        def TYPE(self):
            return self.getToken(pruebaParser.TYPE, 0)

        def getRuleIndex(self):
            return pruebaParser.RULE_formal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormal" ):
                listener.enterFormal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormal" ):
                listener.exitFormal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormal" ):
                return visitor.visitFormal(self)
            else:
                return visitor.visitChildren(self)




    def formal(self):

        localctx = pruebaParser.FormalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_formal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(pruebaParser.ID)
            self.state = 72
            self.match(pruebaParser.T__6)
            self.state = 73
            self.match(pruebaParser.TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(pruebaParser.ID)
            else:
                return self.getToken(pruebaParser.ID, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pruebaParser.ExprContext)
            else:
                return self.getTypedRuleContext(pruebaParser.ExprContext,i)


        def IF(self):
            return self.getToken(pruebaParser.IF, 0)

        def THEN(self):
            return self.getToken(pruebaParser.THEN, 0)

        def ELSE(self):
            return self.getToken(pruebaParser.ELSE, 0)

        def FI(self):
            return self.getToken(pruebaParser.FI, 0)

        def WHILE(self):
            return self.getToken(pruebaParser.WHILE, 0)

        def LOOP(self):
            return self.getToken(pruebaParser.LOOP, 0)

        def POOL(self):
            return self.getToken(pruebaParser.POOL, 0)

        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(pruebaParser.TYPE)
            else:
                return self.getToken(pruebaParser.TYPE, i)

        def IN(self):
            return self.getToken(pruebaParser.IN, 0)

        def NEW(self):
            return self.getToken(pruebaParser.NEW, 0)

        def ISVOID(self):
            return self.getToken(pruebaParser.ISVOID, 0)

        def NOT(self):
            return self.getToken(pruebaParser.NOT, 0)

        def INTEGER(self):
            return self.getToken(pruebaParser.INTEGER, 0)

        def STRING(self):
            return self.getToken(pruebaParser.STRING, 0)

        def TRUE(self):
            return self.getToken(pruebaParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(pruebaParser.FALSE, 0)

        def getRuleIndex(self):
            return pruebaParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = pruebaParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 76
                self.match(pruebaParser.ID)
                self.state = 77
                self.match(pruebaParser.T__7)
                self.state = 78
                self.expr(24)
                pass

            elif la_ == 2:
                self.state = 79
                self.match(pruebaParser.ID)
                self.state = 80
                self.match(pruebaParser.T__3)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pruebaParser.T__1) | (1 << pruebaParser.T__3) | (1 << pruebaParser.T__10) | (1 << pruebaParser.T__15) | (1 << pruebaParser.FALSE) | (1 << pruebaParser.IF) | (1 << pruebaParser.ISVOID) | (1 << pruebaParser.WHILE) | (1 << pruebaParser.NEW) | (1 << pruebaParser.NOT) | (1 << pruebaParser.TRUE) | (1 << pruebaParser.INTEGER) | (1 << pruebaParser.ID) | (1 << pruebaParser.STRING))) != 0):
                    self.state = 81
                    self.expr(0)
                    self.state = 86
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==pruebaParser.T__4:
                        self.state = 82
                        self.match(pruebaParser.T__4)
                        self.state = 83
                        self.expr(0)
                        self.state = 88
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 91
                self.match(pruebaParser.T__5)
                pass

            elif la_ == 3:
                self.state = 92
                self.match(pruebaParser.IF)
                self.state = 93
                self.expr(0)
                self.state = 94
                self.match(pruebaParser.THEN)
                self.state = 95
                self.expr(0)
                self.state = 96
                self.match(pruebaParser.ELSE)
                self.state = 97
                self.expr(0)
                self.state = 98
                self.match(pruebaParser.FI)
                pass

            elif la_ == 4:
                self.state = 100
                self.match(pruebaParser.WHILE)
                self.state = 101
                self.expr(0)
                self.state = 102
                self.match(pruebaParser.LOOP)
                self.state = 103
                self.expr(0)
                self.state = 104
                self.match(pruebaParser.POOL)
                pass

            elif la_ == 5:
                self.state = 106
                self.match(pruebaParser.T__1)
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pruebaParser.T__1) | (1 << pruebaParser.T__3) | (1 << pruebaParser.T__10) | (1 << pruebaParser.T__15) | (1 << pruebaParser.FALSE) | (1 << pruebaParser.IF) | (1 << pruebaParser.ISVOID) | (1 << pruebaParser.WHILE) | (1 << pruebaParser.NEW) | (1 << pruebaParser.NOT) | (1 << pruebaParser.TRUE) | (1 << pruebaParser.INTEGER) | (1 << pruebaParser.ID) | (1 << pruebaParser.STRING))) != 0):
                    self.state = 107
                    self.expr(0)
                    self.state = 108
                    self.match(pruebaParser.T__0)
                    self.state = 114
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 115
                self.match(pruebaParser.T__2)
                pass

            elif la_ == 6:
                self.state = 116
                self.match(pruebaParser.T__10)
                self.state = 117
                self.match(pruebaParser.ID)
                self.state = 118
                self.match(pruebaParser.T__6)
                self.state = 119
                self.match(pruebaParser.TYPE)
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==pruebaParser.T__7:
                    self.state = 120
                    self.match(pruebaParser.T__7)
                    self.state = 121
                    self.expr(0)


                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==pruebaParser.T__4:
                    self.state = 124
                    self.match(pruebaParser.T__4)
                    self.state = 125
                    self.match(pruebaParser.ID)
                    self.state = 126
                    self.match(pruebaParser.T__6)
                    self.state = 127
                    self.match(pruebaParser.TYPE)
                    self.state = 130
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==pruebaParser.T__7:
                        self.state = 128
                        self.match(pruebaParser.T__7)
                        self.state = 129
                        self.expr(0)


                    self.state = 136
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 137
                self.match(pruebaParser.IN)
                self.state = 138
                self.expr(18)
                pass

            elif la_ == 7:
                self.state = 139
                self.match(pruebaParser.NEW)
                self.state = 140
                self.match(pruebaParser.TYPE)
                pass

            elif la_ == 8:
                self.state = 141
                self.match(pruebaParser.ISVOID)
                self.state = 142
                self.expr(16)
                pass

            elif la_ == 9:
                self.state = 143
                self.match(pruebaParser.T__15)
                self.state = 144
                self.expr(11)
                pass

            elif la_ == 10:
                self.state = 145
                self.match(pruebaParser.NOT)
                self.state = 146
                self.expr(7)
                pass

            elif la_ == 11:
                self.state = 147
                self.match(pruebaParser.T__3)
                self.state = 148
                self.expr(0)
                self.state = 149
                self.match(pruebaParser.T__5)
                pass

            elif la_ == 12:
                self.state = 151
                self.match(pruebaParser.ID)
                pass

            elif la_ == 13:
                self.state = 152
                self.match(pruebaParser.INTEGER)
                pass

            elif la_ == 14:
                self.state = 153
                self.match(pruebaParser.STRING)
                pass

            elif la_ == 15:
                self.state = 154
                self.match(pruebaParser.TRUE)
                pass

            elif la_ == 16:
                self.state = 155
                self.match(pruebaParser.FALSE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 200
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 198
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = pruebaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 158
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 159
                        self.match(pruebaParser.T__11)
                        self.state = 160
                        self.expr(16)
                        pass

                    elif la_ == 2:
                        localctx = pruebaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 161
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 162
                        self.match(pruebaParser.T__12)
                        self.state = 163
                        self.expr(15)
                        pass

                    elif la_ == 3:
                        localctx = pruebaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 164
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 165
                        self.match(pruebaParser.T__13)
                        self.state = 166
                        self.expr(14)
                        pass

                    elif la_ == 4:
                        localctx = pruebaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 167
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 168
                        self.match(pruebaParser.T__14)
                        self.state = 169
                        self.expr(13)
                        pass

                    elif la_ == 5:
                        localctx = pruebaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 170
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 171
                        self.match(pruebaParser.T__16)
                        self.state = 172
                        self.expr(11)
                        pass

                    elif la_ == 6:
                        localctx = pruebaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 173
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 174
                        self.match(pruebaParser.T__17)
                        self.state = 175
                        self.expr(10)
                        pass

                    elif la_ == 7:
                        localctx = pruebaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 176
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 177
                        self.match(pruebaParser.T__18)
                        self.state = 178
                        self.expr(9)
                        pass

                    elif la_ == 8:
                        localctx = pruebaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 179
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 182
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==pruebaParser.T__8:
                            self.state = 180
                            self.match(pruebaParser.T__8)
                            self.state = 181
                            self.match(pruebaParser.TYPE)


                        self.state = 184
                        self.match(pruebaParser.T__9)
                        self.state = 185
                        self.match(pruebaParser.ID)
                        self.state = 186
                        self.match(pruebaParser.T__3)
                        self.state = 195
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pruebaParser.T__1) | (1 << pruebaParser.T__3) | (1 << pruebaParser.T__10) | (1 << pruebaParser.T__15) | (1 << pruebaParser.FALSE) | (1 << pruebaParser.IF) | (1 << pruebaParser.ISVOID) | (1 << pruebaParser.WHILE) | (1 << pruebaParser.NEW) | (1 << pruebaParser.NOT) | (1 << pruebaParser.TRUE) | (1 << pruebaParser.INTEGER) | (1 << pruebaParser.ID) | (1 << pruebaParser.STRING))) != 0):
                            self.state = 187
                            self.expr(0)
                            self.state = 192
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==pruebaParser.T__4:
                                self.state = 188
                                self.match(pruebaParser.T__4)
                                self.state = 189
                                self.expr(0)
                                self.state = 194
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 197
                        self.match(pruebaParser.T__5)
                        pass

             
                self.state = 202
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 23)
         




