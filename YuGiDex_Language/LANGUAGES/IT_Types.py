from enum import Enum

class IT_CardType(Enum):
    MONSTER = "MONSTER"
    SPELL = "SPELL"
    TRAP = "TRAP"

class IT_Spell(Enum):
    EQUIP = "Equip1"
    QUICKPLAY = "Quick-Play1"
    NORMAL = "Normal1"
    FIELD = "Field1"
    RITUAL = "Ritual1"

class IT_Trap(Enum):
    NORMAL = "Normal1"
    CONTINUOUS = "Continuous1"
    COUNTER = "Counter1"

class IT_Attribute(Enum):
    DARK = "Dark1"
    DIVINE = "Divine1"
    EARTH = "Earth1"
    FIRE = "Fire1"
    LIGHT = "Light1"
    WATER = "Water1"
    WIND = "Wind1"
    SPELL = "Spell1"
    TRAP = "Trap1"
    LAUGH = "Laugh1"

class IT_Type(Enum):
    AQUA = "Aqua1"
    BEAST = "Beast1"
    BEASTWARRIOR = "Beast-Warrior1" 
    CREATORGOD = "Creator God1"
    CYBERSE = "Cyberse1"
    DINOSAUR = "Dinosaur1"
    DIVINEBEAST = "Divine-Beast1"
    DRAGON = "Dragon1"
    FAIRY = "Fairy1"
    FIEND = "Fiend1"
    FISH = "Fish1"
    INSECT = "Insect1"
    MACHINE = "Machine1"
    PLANT = "Plant1"
    PSYCHIC = "Psychic1"
    PYRO = "Pyro1"
    REPTILE = "Reptile1"
    ROCK = "Rock1"
    SEASERPENT = "Sea Serpent1"
    SPELLCASTER = "Spellcaster1"
    THUNDER = "Thunder1"
    WARRIOR = "Warrior1"
    WINGEDBEAST = "Winged Beast1"
    WYRM = "Wyrm1"
    ZOMBIE = "Zombie1"

    NORMAL = "Normal"
    EFFECT = "Effect"
    RITUAL = "Ritual"
    FUSION = "Fusion"
    SYNCHRO = "Synchro"
    XYZ = "XYZ"
    PENDULUM = "Pendulum"
    LINK = "Link"
    TOKEN = "Token"
    
class IT_Search(Enum):
    ID = 'id'
    TYPE = 'type'
    NAME = 'name'
    EN_ATTR = 'englishAttribute'
    L_ATTR = 'localAttribute'
    EFFECT = 'effectText'
    PEND_EFFECT = 'pendEffect'
    PEND_SCALE = 'pendScale'
    LEVEL = 'level'
    RANK = 'rank'
    LINKRATING = 'linkRating'
    LINKARROW = 'linkArrows'
    ATK = 'atk'
    DEF = 'def'
    PROP = 'atk'