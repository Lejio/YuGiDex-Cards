from enum import Enum

class PT_CardType(Enum):
    MONSTER = "MONSTER"
    SPELL = "SPELL"
    TRAP = "TRAP"

class PT_Spell(Enum):
    EQUIP = "Equip"
    QUICKPLAY = "Quick-Play"
    NORMAL = "Normal"
    FIELD = "Field"
    RITUAL = "Ritual"

class PT_Trap(Enum):
    NORMAL = "Normal"
    CONTINUOUS = "Continuous"
    COUNTER = "Counter"

class PT_Attribute(Enum):
    DARK = "Dark"
    DIVINE = "Divine"
    EARTH = "Earth"
    FIRE = "Fire"
    LIGHT = "Light"
    WATER = "Water"
    WIND = "Wind"
    SPELL = "Spell"
    TRAP = "Trap"
    LAUGH = "Laugh"

class PT_Type(Enum):
    AQUA = "Aqua"
    BEAST = "Beast"
    BEASTWARRIOR = "Beast-Warrior" 
    CREATORGOD = "Creator God"
    CYBERSE = "Cyberse"
    DINOSAUR = "Dinosaur"
    DIVINEBEAST = "Divine-Beast"
    DRAGON = "Dragon"
    FAIRY = "Fairy"
    FIEND = "Fiend"
    FISH = "Fish"
    INSECT = "Insect"
    MACHINE = "Machine"
    PLANT = "Plant"
    PSYCHIC = "Psychic"
    PYRO = "Pyro"
    REPTILE = "Reptile"
    ROCK = "Rock"
    SEASERPENT = "Sea Serpent"
    SPELLCASTER = "Spellcaster"
    THUNDER = "Thunder"
    WARRIOR = "Warrior"
    WINGEDBEAST = "Winged Beast"
    WYRM = "Wyrm"
    ZOMBIE = "Zombie"

    NORMAL = "Normal"
    EFFECT = "Effect"
    RITUAL = "Ritual"
    FUSION = "Fusion"
    SYNCHRO = "Synchro"
    XYZ = "XYZ"
    PENDULUM = "Pendulum"
    LINK = "Link"
    TOKEN = "Token"
    
class PT_Search(Enum):
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