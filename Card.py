from lang.EN_Types import CardType, Attribute, Type 

class Card:
    def __init__(self, cardObj:dict, localAttribute: enumerate, Type: enumerate):
        self.localAttribute = localAttribute
        self.Type = Type
        self.NULL = "NULL"

        for param in cardObj:
            # print(type(card[param]))
            if param == "effectText" or param == "pendEffect":
                self.Card[param] = self.__stringUnwrapper(cardObj[param])
            else:
                self.Card[param] = cardObj[param]

        self.Card = map(self.__nullParser(), cardObj)
        self.__buildCard(self)

    def __buildCard(self):

        self.Card['type'] = self.__fCard(self.Card['type'])
        self.Card['englishAttribute'] = self.__fAttribute(self.Card['englishAttribute'])
        self.Card['localizedAttribute'] = self.__flocalAttribute(self.Card['localizedAttribute'])

        if self.Card['type'] == CardType.MONSTER:
            self.Card['properties'] = self.Card['properties'].strip('][').split(', ')

            for prop in range(len(self.Card['properties'])):
                self.Card['properties'][prop] = self.__fType(self.Card['properties'][prop])
                

    def __nullParser(self, cardObjCat):
        
        if cardObjCat == self.NULL:
            return None

    def __stringUnwrapper(self, cardDesc):

        if cardDesc != self.NULL:
           
            return cardDesc.replace("[newline]", "\n").replace("[quotes]", "\"")



    def __fCard(self, cardType):
        
        ct = CardType._member_names_

        for card in ct:
            if cardType == CardType[card].value:
                return CardType[card]
        
        raise TypeError(f"{cardType} is not a Card.")

    def __fAttribute(self, attr):
        
        atr = Attribute._member_names_

        for a in atr:
            if attr == Attribute[a].value:
                return Attribute[a]
        
        return None

    def __flocalAttribute(self, lattr):
        latr = self.localAttribute._member_names_

        for a in latr:
            if lattr == self.localAttribute[a].value:
                return self.localAttribute[a]
        
        return None

    def __fType(self, type_):
        
        tp = Type._member_names_

        for t in tp:
            if type_ == Type[t].value:
                return Type[t]
        
        return None
