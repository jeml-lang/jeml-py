# Generated from jeml.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("q\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\6\2$\n\2\r\2\16")
        buf.write("\2%\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\61\n\3\3\4")
        buf.write("\3\4\5\4\65\n\4\3\4\3\4\7\49\n\4\f\4\16\4<\13\4\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\5\7G\n\7\3\b\3\b\3\b\7")
        buf.write("\bL\n\b\f\b\16\bO\13\b\3\b\3\b\3\b\3\b\5\bU\n\b\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\13\3\13\3\13\5\13`\n\13\3\f\3\f")
        buf.write("\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\21")
        buf.write("\5\21o\n\21\3\21\2\2\22\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \2\3\4\2\b\b\17\17\2p\2#\3\2\2\2\4\60\3\2\2")
        buf.write("\2\6\64\3\2\2\2\b=\3\2\2\2\n@\3\2\2\2\fF\3\2\2\2\16T\3")
        buf.write("\2\2\2\20V\3\2\2\2\22X\3\2\2\2\24_\3\2\2\2\26a\3\2\2\2")
        buf.write("\30c\3\2\2\2\32e\3\2\2\2\34g\3\2\2\2\36i\3\2\2\2 n\3\2")
        buf.write("\2\2\"$\5\4\3\2#\"\3\2\2\2$%\3\2\2\2%#\3\2\2\2%&\3\2\2")
        buf.write("\2&\3\3\2\2\2\'(\5\n\6\2()\7\3\2\2)*\5\6\4\2*+\7\4\2\2")
        buf.write("+\61\3\2\2\2,-\5\n\6\2-.\7\3\2\2./\7\4\2\2/\61\3\2\2\2")
        buf.write("\60\'\3\2\2\2\60,\3\2\2\2\61\5\3\2\2\2\62\65\5\b\5\2\63")
        buf.write("\65\5\4\3\2\64\62\3\2\2\2\64\63\3\2\2\2\65:\3\2\2\2\66")
        buf.write("9\5\b\5\2\679\5\4\3\28\66\3\2\2\28\67\3\2\2\29<\3\2\2")
        buf.write("\2:8\3\2\2\2:;\3\2\2\2;\7\3\2\2\2<:\3\2\2\2=>\5\n\6\2")
        buf.write(">?\5\f\7\2?\t\3\2\2\2@A\7\16\2\2A\13\3\2\2\2BG\5\22\n")
        buf.write("\2CG\5\16\b\2DG\5\20\t\2EG\5\24\13\2FB\3\2\2\2FC\3\2\2")
        buf.write("\2FD\3\2\2\2FE\3\2\2\2G\r\3\2\2\2HI\7\5\2\2IM\5\f\7\2")
        buf.write("JL\5\f\7\2KJ\3\2\2\2LO\3\2\2\2MK\3\2\2\2MN\3\2\2\2NP\3")
        buf.write("\2\2\2OM\3\2\2\2PQ\7\6\2\2QU\3\2\2\2RS\7\5\2\2SU\7\6\2")
        buf.write("\2TH\3\2\2\2TR\3\2\2\2U\17\3\2\2\2VW\t\2\2\2W\21\3\2\2")
        buf.write("\2XY\7\7\2\2Y\23\3\2\2\2Z`\5\26\f\2[`\5\30\r\2\\`\5\32")
        buf.write("\16\2]`\5\34\17\2^`\5\36\20\2_Z\3\2\2\2_[\3\2\2\2_\\\3")
        buf.write("\2\2\2_]\3\2\2\2_^\3\2\2\2`\25\3\2\2\2ab\7\r\2\2b\27\3")
        buf.write("\2\2\2cd\7\f\2\2d\31\3\2\2\2ef\7\13\2\2f\33\3\2\2\2gh")
        buf.write("\7\n\2\2h\35\3\2\2\2ij\7\t\2\2j\37\3\2\2\2ko\5\30\r\2")
        buf.write("lo\5\26\f\2mo\5\32\16\2nk\3\2\2\2nl\3\2\2\2nm\3\2\2\2")
        buf.write("o!\3\2\2\2\f%\60\648:FMT_n")
        return buf.getvalue()


class jemlParser ( Parser ):

    grammarFileName = "jeml.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BOOLEAN", "STRING", "INTEGER", "DECIMAL", 
                      "HEXIDECIMAL_NUMBER", "BINARY_NUMBER", "OCTAL_NUMBER", 
                      "KEY", "MULTILINE_STRING", "EXPONENT", "COMMENT", 
                      "MULTILINE_COMMENT", "WS", "NL" ]

    RULE_document = 0
    RULE_j_map = 1
    RULE_j_map_body = 2
    RULE_j_pair = 3
    RULE_j_key = 4
    RULE_j_value = 5
    RULE_j_list = 6
    RULE_j_string = 7
    RULE_j_bool = 8
    RULE_j_number = 9
    RULE_j_octal = 10
    RULE_j_binary = 11
    RULE_j_hex = 12
    RULE_j_decimal = 13
    RULE_j_integer = 14
    RULE_j_complex = 15

    ruleNames =  [ "document", "j_map", "j_map_body", "j_pair", "j_key", 
                   "j_value", "j_list", "j_string", "j_bool", "j_number", 
                   "j_octal", "j_binary", "j_hex", "j_decimal", "j_integer", 
                   "j_complex" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    BOOLEAN=5
    STRING=6
    INTEGER=7
    DECIMAL=8
    HEXIDECIMAL_NUMBER=9
    BINARY_NUMBER=10
    OCTAL_NUMBER=11
    KEY=12
    MULTILINE_STRING=13
    EXPONENT=14
    COMMENT=15
    MULTILINE_COMMENT=16
    WS=17
    NL=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class DocumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def j_map(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jemlParser.J_mapContext)
            else:
                return self.getTypedRuleContext(jemlParser.J_mapContext,i)


        def getRuleIndex(self):
            return jemlParser.RULE_document

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDocument" ):
                listener.enterDocument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDocument" ):
                listener.exitDocument(self)




    def document(self):

        localctx = jemlParser.DocumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_document)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.j_map()
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==jemlParser.KEY):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class J_mapContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def j_key(self):
            return self.getTypedRuleContext(jemlParser.J_keyContext,0)


        def j_map_body(self):
            return self.getTypedRuleContext(jemlParser.J_map_bodyContext,0)


        def getRuleIndex(self):
            return jemlParser.RULE_j_map

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJ_map" ):
                listener.enterJ_map(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJ_map" ):
                listener.exitJ_map(self)




    def j_map(self):

        localctx = jemlParser.J_mapContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_j_map)
        try:
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.j_key()
                self.state = 38
                self.match(jemlParser.T__0)

                self.state = 39
                self.j_map_body()
                self.state = 40
                self.match(jemlParser.T__1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.j_key()
                self.state = 43
                self.match(jemlParser.T__0)
                self.state = 44
                self.match(jemlParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class J_map_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def j_pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jemlParser.J_pairContext)
            else:
                return self.getTypedRuleContext(jemlParser.J_pairContext,i)


        def j_map(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jemlParser.J_mapContext)
            else:
                return self.getTypedRuleContext(jemlParser.J_mapContext,i)


        def getRuleIndex(self):
            return jemlParser.RULE_j_map_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJ_map_body" ):
                listener.enterJ_map_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJ_map_body" ):
                listener.exitJ_map_body(self)




    def j_map_body(self):

        localctx = jemlParser.J_map_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_j_map_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 48
                self.j_pair()
                pass

            elif la_ == 2:
                self.state = 49
                self.j_map()
                pass


            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==jemlParser.KEY:
                self.state = 54
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 52
                    self.j_pair()
                    pass

                elif la_ == 2:
                    self.state = 53
                    self.j_map()
                    pass


                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class J_pairContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def j_key(self):
            return self.getTypedRuleContext(jemlParser.J_keyContext,0)


        def j_value(self):
            return self.getTypedRuleContext(jemlParser.J_valueContext,0)


        def getRuleIndex(self):
            return jemlParser.RULE_j_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJ_pair" ):
                listener.enterJ_pair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJ_pair" ):
                listener.exitJ_pair(self)




    def j_pair(self):

        localctx = jemlParser.J_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_j_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.j_key()
            self.state = 60
            self.j_value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class J_keyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY(self):
            return self.getToken(jemlParser.KEY, 0)

        def getRuleIndex(self):
            return jemlParser.RULE_j_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJ_key" ):
                listener.enterJ_key(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJ_key" ):
                listener.exitJ_key(self)




    def j_key(self):

        localctx = jemlParser.J_keyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_j_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(jemlParser.KEY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class J_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def j_bool(self):
            return self.getTypedRuleContext(jemlParser.J_boolContext,0)


        def j_list(self):
            return self.getTypedRuleContext(jemlParser.J_listContext,0)


        def j_string(self):
            return self.getTypedRuleContext(jemlParser.J_stringContext,0)


        def j_number(self):
            return self.getTypedRuleContext(jemlParser.J_numberContext,0)


        def getRuleIndex(self):
            return jemlParser.RULE_j_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJ_value" ):
                listener.enterJ_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJ_value" ):
                listener.exitJ_value(self)




    def j_value(self):

        localctx = jemlParser.J_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_j_value)
        try:
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [jemlParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.j_bool()
                pass
            elif token in [jemlParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.j_list()
                pass
            elif token in [jemlParser.STRING, jemlParser.MULTILINE_STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 66
                self.j_string()
                pass
            elif token in [jemlParser.INTEGER, jemlParser.DECIMAL, jemlParser.HEXIDECIMAL_NUMBER, jemlParser.BINARY_NUMBER, jemlParser.OCTAL_NUMBER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 67
                self.j_number()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class J_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def j_value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jemlParser.J_valueContext)
            else:
                return self.getTypedRuleContext(jemlParser.J_valueContext,i)


        def getRuleIndex(self):
            return jemlParser.RULE_j_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJ_list" ):
                listener.enterJ_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJ_list" ):
                listener.exitJ_list(self)




    def j_list(self):

        localctx = jemlParser.J_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_j_list)
        self._la = 0 # Token type
        try:
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.match(jemlParser.T__2)
                self.state = 71
                self.j_value()
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jemlParser.T__2) | (1 << jemlParser.BOOLEAN) | (1 << jemlParser.STRING) | (1 << jemlParser.INTEGER) | (1 << jemlParser.DECIMAL) | (1 << jemlParser.HEXIDECIMAL_NUMBER) | (1 << jemlParser.BINARY_NUMBER) | (1 << jemlParser.OCTAL_NUMBER) | (1 << jemlParser.MULTILINE_STRING))) != 0):
                    self.state = 72
                    self.j_value()
                    self.state = 77
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 78
                self.match(jemlParser.T__3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.match(jemlParser.T__2)
                self.state = 81
                self.match(jemlParser.T__3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class J_stringContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(jemlParser.STRING, 0)

        def MULTILINE_STRING(self):
            return self.getToken(jemlParser.MULTILINE_STRING, 0)

        def getRuleIndex(self):
            return jemlParser.RULE_j_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJ_string" ):
                listener.enterJ_string(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJ_string" ):
                listener.exitJ_string(self)




    def j_string(self):

        localctx = jemlParser.J_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_j_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            _la = self._input.LA(1)
            if not(_la==jemlParser.STRING or _la==jemlParser.MULTILINE_STRING):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class J_boolContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(jemlParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return jemlParser.RULE_j_bool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJ_bool" ):
                listener.enterJ_bool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJ_bool" ):
                listener.exitJ_bool(self)




    def j_bool(self):

        localctx = jemlParser.J_boolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_j_bool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(jemlParser.BOOLEAN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class J_numberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def j_octal(self):
            return self.getTypedRuleContext(jemlParser.J_octalContext,0)


        def j_binary(self):
            return self.getTypedRuleContext(jemlParser.J_binaryContext,0)


        def j_hex(self):
            return self.getTypedRuleContext(jemlParser.J_hexContext,0)


        def j_decimal(self):
            return self.getTypedRuleContext(jemlParser.J_decimalContext,0)


        def j_integer(self):
            return self.getTypedRuleContext(jemlParser.J_integerContext,0)


        def getRuleIndex(self):
            return jemlParser.RULE_j_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJ_number" ):
                listener.enterJ_number(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJ_number" ):
                listener.exitJ_number(self)




    def j_number(self):

        localctx = jemlParser.J_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_j_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [jemlParser.OCTAL_NUMBER]:
                self.state = 88
                self.j_octal()
                pass
            elif token in [jemlParser.BINARY_NUMBER]:
                self.state = 89
                self.j_binary()
                pass
            elif token in [jemlParser.HEXIDECIMAL_NUMBER]:
                self.state = 90
                self.j_hex()
                pass
            elif token in [jemlParser.DECIMAL]:
                self.state = 91
                self.j_decimal()
                pass
            elif token in [jemlParser.INTEGER]:
                self.state = 92
                self.j_integer()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class J_octalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OCTAL_NUMBER(self):
            return self.getToken(jemlParser.OCTAL_NUMBER, 0)

        def getRuleIndex(self):
            return jemlParser.RULE_j_octal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJ_octal" ):
                listener.enterJ_octal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJ_octal" ):
                listener.exitJ_octal(self)




    def j_octal(self):

        localctx = jemlParser.J_octalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_j_octal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(jemlParser.OCTAL_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class J_binaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BINARY_NUMBER(self):
            return self.getToken(jemlParser.BINARY_NUMBER, 0)

        def getRuleIndex(self):
            return jemlParser.RULE_j_binary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJ_binary" ):
                listener.enterJ_binary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJ_binary" ):
                listener.exitJ_binary(self)




    def j_binary(self):

        localctx = jemlParser.J_binaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_j_binary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(jemlParser.BINARY_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class J_hexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HEXIDECIMAL_NUMBER(self):
            return self.getToken(jemlParser.HEXIDECIMAL_NUMBER, 0)

        def getRuleIndex(self):
            return jemlParser.RULE_j_hex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJ_hex" ):
                listener.enterJ_hex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJ_hex" ):
                listener.exitJ_hex(self)




    def j_hex(self):

        localctx = jemlParser.J_hexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_j_hex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(jemlParser.HEXIDECIMAL_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class J_decimalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL(self):
            return self.getToken(jemlParser.DECIMAL, 0)

        def getRuleIndex(self):
            return jemlParser.RULE_j_decimal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJ_decimal" ):
                listener.enterJ_decimal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJ_decimal" ):
                listener.exitJ_decimal(self)




    def j_decimal(self):

        localctx = jemlParser.J_decimalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_j_decimal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(jemlParser.DECIMAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class J_integerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(jemlParser.INTEGER, 0)

        def getRuleIndex(self):
            return jemlParser.RULE_j_integer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJ_integer" ):
                listener.enterJ_integer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJ_integer" ):
                listener.exitJ_integer(self)




    def j_integer(self):

        localctx = jemlParser.J_integerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_j_integer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(jemlParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class J_complexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def j_binary(self):
            return self.getTypedRuleContext(jemlParser.J_binaryContext,0)


        def j_octal(self):
            return self.getTypedRuleContext(jemlParser.J_octalContext,0)


        def j_hex(self):
            return self.getTypedRuleContext(jemlParser.J_hexContext,0)


        def getRuleIndex(self):
            return jemlParser.RULE_j_complex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJ_complex" ):
                listener.enterJ_complex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJ_complex" ):
                listener.exitJ_complex(self)




    def j_complex(self):

        localctx = jemlParser.J_complexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_j_complex)
        try:
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [jemlParser.BINARY_NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.j_binary()
                pass
            elif token in [jemlParser.OCTAL_NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.j_octal()
                pass
            elif token in [jemlParser.HEXIDECIMAL_NUMBER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 107
                self.j_hex()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





