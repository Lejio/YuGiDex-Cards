from lang.lang import Lang
from lang.DE_Types import *
from lang.EN_Types import *
from lang.ES_Types import *
from lang.FR_Types import *
from lang.IT_Types import *
from lang.JA_Types import *
from lang.KO_Types import *
from lang.PT_Types import *

class Type:
    
    def __init__(self, lang: Lang) -> None:
        
        self.LANG = None
        
        self.CARD_TYPE: enumerate = None
        self.SPELL: enumerate = None
        self.TRAP: enumerate = None
        self.ATTRIBUTE:enumerate = None
        self.TYPE: enumerate = None
        
        match lang:
            
            case Lang.ENGLISH:
                self.LANG = Lang.ENGLISH
                self.__setTypes(EN_Attribute, EN_Spell, EN_Trap, EN_Attribute, EN_Type)
                
            case Lang.GERMAN:
                self.LANG = Lang.GERMAN
                self.__setTypes(DE_Attribute, DE_Spell, DE_Trap, DE_Attribute, DE_Type)
                
            case Lang.SPANISH:
                self.LANG = Lang.SPANISH
                self.__setTypes(ES_Attribute, ES_Spell, ES_Trap, ES_Attribute, ES_Type)
                
            case Lang.FRENCH:
                self.LANG = Lang.FRENCH
                self.__setTypes(FR_Attribute, FR_Spell, FR_Trap, FR_Attribute, FR_Type)
                
            case Lang.ITALIAN:
                self.LANG = Lang.ITALIAN
                self.__setTypes(IT_Attribute, IT_Spell, IT_Trap, IT_Attribute, IT_Type)
                
            case Lang.JAPANESE:
                self.LANG = Lang.JAPANESE
                self.__setTypes(JA_Attribute, JA_Spell, JA_Trap, JA_Attribute, JA_Type)
                
            case Lang.KOREAN:
                self.LANG = Lang.KOREAN
                self.__setTypes(KO_Attribute, KO_Spell, KO_Trap, KO_Attribute, KO_Type)
                
            case Lang.PORTUGUESE:
                self.LANG = Lang.PORTUGUESE
                self.__setTypes(PT_Attribute, PT_Spell, PT_Trap, PT_Attribute, PT_Type)
    
    def __setTypes(self, cardtype: enumerate, spell: enumerate, trap: enumerate, attr:enumerate, type_:enumerate):
        
        self.CARD_TYPE = cardtype
        self.SPELL = spell
        self.TRAP = trap
        self.ATTRIBUTE = attr
        self.TYPE = type_