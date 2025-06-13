from PAIDEv2 import *

global JumpDebounced
global JumpInter
JumpDebounce = False
JumpInter = 0
GameService.SetupGame("Possession", WindowSize = [1200, 450])
PlayerService.Add.DefaultAttribute("Health", 400)
PlayerService.Add.DefaultAttribute("Velocity", [0,0])
PlayerService.Add.DefaultAttribute("Damage", 5)
PlayerService.Add.DefaultAttribute("Attack Speed", 0.2)
PlayerService.Add.DefaultAttribute("JumpDebounce", 0)
PlayerService.Add.DefaultAttribute("Direction", ">")
PlayerService.Add.DefaultAttribute("Player Direction", ">")
PlayerService.Add.DefaultAttribute("Sprite Size", 64)
PlayerService.Add.DefaultAttribute("Attack Cooldown", False)
PlayerService.Add.DefaultAttribute("Possession Timer", 0)
PlayerService.Add.DefaultAttribute("Souls", 0)
GameService.CreateInstance("Menu")
GameService.CreateInstance("Survival")
GameService.CreateInstance("Dead")
Num = randint(1,8)
if Num == 2:
    Num = randint(1,8)
    if Num == 2:
        Num = randint(1,8)

LINK = f"Assets\Images\ENDING\GO ({Num}).png"

ObjectService.BuildObject("Ragebait", [0,0], pygame.image.load(LINK), True, "Dead")
ObjectService.BuildObject("Backer", [0,0], pygame.image.load("Assets\Images\Map.png"), False, "Survival")
ObjectService.BuildObject("Menuuuuuuu", [0,0], pygame.image.load("Assets\Images\Title_Posession.png"), False, "Menu")

NSprite = pygame.surface.Surface((64,64))
NSprite.fill("#48FF00")
NSprite.set_colorkey("#48FF00")
PSprite = pygame.image.load("Assets\Images\MainChar.png")
NSprite.blit(PSprite, (0, 0, 64, 64))

PlayerService.Add.Player("Natasha","Natasha",NSprite, [0,0], "Survival")

def Jump(Power:int = 50):
    Player = PlayerService.PlayerList.get("Natasha")
    JumpInter = Player.get("JumpDebounce")
    if JumpInter == 3:
        return
    
    x = Player.get("Velocity")[0]
    Player.update({"Velocity" : [x, Power]})
    JumpInter += 1
    Player.update({"JumpDebounce" : JumpInter})

# Fix issues with flipping the sprite
def Left(Power:int = -80):
    Player = PlayerService.PlayerList.get("Natasha")
    if Player.get("Player Direction") == ">":
        Player.update({"Sprite": pygame.transform.flip(Player.get("Sprite"), True, False)})

    Player.update({"Direction": "<", "Player Direction" : "<"})
    MaxPower = -80
    x = Player.get("Velocity")[0]
    y = Player.get("Velocity")[1]
    if x + Power > MaxPower:
        Player.update({"Velocity" : [Power + x, y]})
    else:
        Player.update({"Velocity" : [MaxPower, y]})

def Right(Power:int = 80):
    Player = PlayerService.PlayerList.get("Natasha")
    if Player.get("Player Direction") == "<":
        Player.update({"Sprite": pygame.transform.flip(Player.get("Sprite"), True, False)})

    Player.update({"Direction": ">", "Player Direction" : ">"})
    MaxPower = 80
    x = Player.get("Velocity")[0]
    y = Player.get("Velocity")[1]
    if x + Power < MaxPower:
        Player.update({"Velocity" : [Power + x, y]})
    else:
        Player.update({"Velocity" : [MaxPower, y]})

def Possess(Entity:str = None):
    
    Player = PlayerService.PlayerList.get("Natasha")
    NewEntity = None
    for entity in EntityService.Entities:
        if entity.get("Name") == Entity:
            NewEntity = entity
            break
    if NewEntity == None:
        Error("WHY DID I FUCK IT UUUUPPP")
    NewPlayerSprite = NewEntity.get("Sprite")

    Player.update({"Sprite": NewPlayerSprite, "Possession Timer": 2000, "Damage": 20, "Attack Speed": 0.5})


    

def PossessCountdown():
    Player = PlayerService.PlayerList.get("Natasha")
    CurrentTimer = Player.get("Possession Timer")
    if CurrentTimer > 0:
        Player.update({"Possession Timer" : CurrentTimer - 1, "Souls": 0})
    else:
        NSprite = pygame.surface.Surface((64,64))
        NSprite.fill("#48FF00")
        PSprite = pygame.image.load("Assets\Images\MainChar.png")
        NSprite.blit(PSprite, (0,0))
        NSprite.set_colorkey("#48FF00")
        
        if Player.get("Player Direction") == "<":
            NSprite = pygame.transform.flip(NSprite, True, False)
        Player.update({"Sprite": NSprite, "Damage": 5, "Attack Speed": 0.2})
        

def RunVelocity():
    Player = PlayerService.PlayerList.get("Natasha")
    PlayerDirection = Player.get("Direction")
    PlayerSize = Player.get("Sprite Size")
    PlayerVelocity = PlayerService.PlayerList.get("Natasha").get("Velocity")
    PlayerPosition = PlayerService.PlayerList.get("Natasha").get("Position")
    ScreenSize = GameService.Game.get("Window Size")


    PlayerVelocity = PlayerService.PlayerList.get("Natasha").get("Velocity")
    PlayerPosition = PlayerService.PlayerList.get("Natasha").get("Position")
    Player.update({"Velocity": [PlayerVelocity[0], PlayerVelocity[1] - 1]})
    if PlayerVelocity[1] < 0 and PlayerPosition[1] != ScreenSize[1] - PlayerSize:
        Player.update({"Position": [PlayerPosition[0], PlayerPosition[1] + 2]}) 
    elif PlayerVelocity[1] > 0:
        Player.update({"Position": [PlayerPosition[0], PlayerPosition[1] - 2], "Direction": "v"})

    
    if PlayerPosition[1] == ScreenSize[1] - 64 and PlayerVelocity[1] < 0:
        Player.update({"Velocity": [PlayerVelocity[0], 0], "JumpDebounce" : 0})
        if Player.get("Direction") == "v":
            Player.update({"Direction": "O"})

    if PlayerVelocity[0] != 0:
        if PlayerVelocity[0] > 0:
            PlayerVelocity = PlayerService.PlayerList.get("Natasha").get("Velocity")
            PlayerPosition = PlayerService.PlayerList.get("Natasha").get("Position")
            if PlayerPosition[1] == ScreenSize[1] - PlayerSize:
                Player.update({"Velocity": [PlayerVelocity[0] - 1, PlayerVelocity[1]]})
            if PlayerPosition[0] + 1 in range(0, ScreenSize[0] - PlayerSize):
                Player.update({"Position": [PlayerPosition[0] + 1, PlayerPosition[1]]})
        else:
            PlayerVelocity = PlayerService.PlayerList.get("Natasha").get("Velocity")
            PlayerPosition = PlayerService.PlayerList.get("Natasha").get("Position")
            if PlayerPosition[1] == ScreenSize[1] - PlayerSize:
                Player.update({"Velocity": [PlayerVelocity[0] + 1, PlayerVelocity[1]]})
            if PlayerPosition[0] - 1 in range(1, ScreenSize[0] - PlayerSize):
                Player.update({"Position": [PlayerPosition[0] - 1, PlayerPosition[1]]})
def Play():
    GameService.ShiftCurrentInstance("Survival")

def Attak():
    
    Player = PlayerService.PlayerList.get("Natasha") 

    PlayerSize = Player.get("Sprite Size")
    NewSprite = pygame.surface.Surface((PlayerSize,PlayerSize))
    NewSprite.fill("#00FF00")
    PSprite = pygame.image.load("Assets\Images\MainChar.png")
    NewSprite.blit(PSprite, (0,-64, 64, 64))
    NewSprite.set_colorkey("#00FF00")

    if Player.get("Player Direction") == "<":
        NewSprite = pygame.transform.flip(NewSprite, True, False)
    OldSprite = Player.get("Sprite")

    SlashEffectSheet = pygame.image.load("Assets\Images\Slash attack.png")
    LSlash = pygame.surface.Surface((PlayerSize,PlayerSize))
    RSlash = pygame.surface.Surface((PlayerSize,PlayerSize))
    USlash = pygame.surface.Surface((PlayerSize,PlayerSize))
    DSlash = pygame.surface.Surface((PlayerSize,PlayerSize))

    LSlash.fill("#AAAAAA")
    RSlash.fill("#AAAAAA")
    USlash.fill("#AAAAAA")
    DSlash.fill("#AAAAAA")

    LSlash.blit(SlashEffectSheet, (-2*PlayerSize,0,PlayerSize,PlayerSize))
    RSlash.blit(SlashEffectSheet, (0*PlayerSize,0,PlayerSize,PlayerSize))
    USlash.blit(SlashEffectSheet, (-3*PlayerSize,0,PlayerSize,PlayerSize))
    DSlash.blit(SlashEffectSheet, (-PlayerSize,0,PlayerSize,PlayerSize))

    LSlash.set_colorkey("#AAAAAA")
    RSlash.set_colorkey("#AAAAAA")
    USlash.set_colorkey("#AAAAAA")
    DSlash.set_colorkey("#AAAAAA")
    
    
    
    
    Slash = [RSlash, DSlash, LSlash, USlash]

    Player.update({"Sprite": NewSprite})

    if Player.get("Direction") == "O":
        Player.update({"Sprite": OldSprite})
        return
    
    SlashSFX = pygame.mixer.Sound("Assets\SlashSFX.wav")
    SlashSFX.play()

    if Player.get("Direction") == ">":
        Offset = [5,0]
        for slashpart in range(3):
            #Info(slashpart)
            if slashpart == 0:
                ObjectService.BuildObject("Slash", [Player.get("Position")[0] + Offset[0], Player.get("Position")[1]+ Offset[1]], USlash, False, "Survival")
            elif slashpart == 1:
                ObjectService.BuildObject("Slash", [Player.get("Position")[0] + Offset[0], Player.get("Position")[1]+ Offset[1]], RSlash, False, "Survival")
            elif slashpart == 2:
                ObjectService.BuildObject("Slash", [Player.get("Position")[0] + Offset[0], Player.get("Position")[1]+ Offset[1]], DSlash, False, "Survival")
            GameService.Display.DisplayInstance()
            Reduction = []
            index = 0
            for entity in EntityService.Entities:
                Distance = Maths.Pythagoras(Player.get("Position")[0] - entity.get("Position")[0], Player.get("Position")[1] - entity.get("Position")[1])
                if Distance < 0:
                    Distance * -1
                
                if Distance < 45:
                    Reduction.append(index)
                    if Player.get("Position")[1] < GameService.Game.get("Window Size")[1] - 64:
                        Player.update({"Velocity" : [Player.get("Velocity")[0], 90]})

            GameService.Clock.tick(10)
            ObjectService.ObjectList.pop("Slash")

    elif Player.get("Direction") == "<":
        Offset = [-5,0]
        for slashpart in range(3):
            if slashpart == 0:
                ObjectService.BuildObject("Slash", [Player.get("Position")[0] + Offset[0], Player.get("Position")[1]+ Offset[1]], DSlash, False, "Survival")
            elif slashpart == 1:
                ObjectService.BuildObject("Slash", [Player.get("Position")[0] + Offset[0], Player.get("Position")[1]+ Offset[1]], LSlash, False, "Survival")
            elif slashpart == 2:
                ObjectService.BuildObject("Slash", [Player.get("Position")[0] + Offset[0], Player.get("Position")[1]+ Offset[1]], USlash, False, "Survival")
            
            Reduction = []
            index = 0
            for entity in EntityService.Entities:
                Distance = Maths.Pythagoras(Player.get("Position")[0] - entity.get("Position")[0], Player.get("Position")[1] - entity.get("Position")[1])
                if Distance < 0:
                    Distance * -1
                
                if Distance < 45:
                    Reduction.append(index)
                    if Player.get("Position")[1] < GameService.Game.get("Window Size")[1] - 64:
                        Player.update({"Velocity" : [Player.get("Velocity")[0], 90]})

            GameService.Display.DisplayInstance()
            GameService.Clock.tick(10)
            ObjectService.ObjectList.pop("Slash")

    elif Player.get("Direction") == "v":
        Offset = [0,5]
        for slashpart in range(3):
            if slashpart == 0:
                    ObjectService.BuildObject("Slash", [Player.get("Position")[0] + Offset[0], Player.get("Position")[1]+ Offset[1]], RSlash, False, "Survival")
            elif slashpart == 1:
                    ObjectService.BuildObject("Slash", [Player.get("Position")[0] + Offset[0], Player.get("Position")[1]+ Offset[1]], DSlash, False, "Survival")
            elif slashpart == 2:
                    ObjectService.BuildObject("Slash", [Player.get("Position")[0] + Offset[0], Player.get("Position")[1]+ Offset[1]], LSlash, False, "Survival")
            
            Reduction = []
            index = 0
            for entity in EntityService.Entities:
                Distance = Maths.Pythagoras(Player.get("Position")[0] - entity.get("Position")[0], Player.get("Position")[1] - entity.get("Position")[1])
                if Distance < 0:
                    Distance * -1
                
                if Distance < 55:
                    Reduction.append(index)
                    if Player.get("Position")[1] < GameService.Game.get("Window Size")[1] - 64:
                        Player.update({"Velocity" : [Player.get("Velocity")[0], 90]})
            
            GameService.Display.DisplayInstance()
            GameService.Clock.tick(10)
            ObjectService.ObjectList.pop("Slash")

    else:
        return

        
    for index in Reduction:
        EntityService.Entities.pop(index)
        Player = PlayerService.PlayerList.get("Natasha")
        PlayerSouls = Player.get("Souls")
        Player.update({"Souls": PlayerSouls + 1})
        
    
    Reduction.clear()
    Player.update({"Sprite": OldSprite})
    

def NewPossess():
    Player = PlayerService.PlayerList.get("Natasha")
    PlayerSouls = Player.get("Souls")
    if PlayerSouls > 50:
        Player.update({"Souls": 0})
        Possess("Brick Bot")

# Keyboard
PlayerService.InputManager.Bind.Key(pygame.K_RETURN, Play, "Menu")
PlayerService.InputManager.Bind.Key(pygame.K_SPACE, Jump, "Survival")
PlayerService.InputManager.Bind.Key(pygame.K_a, Left, "Survival")
PlayerService.InputManager.Bind.Key(pygame.K_d, Right, "Survival")
PlayerService.InputManager.Bind.Key(pygame.K_LEFT, Left, "Survival")
PlayerService.InputManager.Bind.Key(pygame.K_RIGHT, Right, "Survival")
PlayerService.InputManager.Bind.Key(pygame.K_LCTRL, Attak, "Survival")
PlayerService.InputManager.Bind.Key(pygame.K_q, NewPossess, "Survival")

#Controller
PlayerService.InputManager.Bind.Key(pygame.CONTROLLER_BUTTON_GUIDE, Play, "Menu")
PlayerService.InputManager.Bind.Key(pygame.CONTROLLER_BUTTON_X, Jump, "Survival")
PlayerService.InputManager.Bind.Key(pygame.CONTROLLER_BUTTON_B, Attak, "Survival")
PlayerService.InputManager.Bind.Key(pygame.CONTROLLER_BUTTON_Y, NewPossess, "Survival")

PlayerService.InputManager.Bind.Joystick("Left", Left, "Survival")
PlayerService.InputManager.Bind.Joystick("Right", Right, "Survival")

EntityService.Add.DefaultAtrribute("Velocity", [0,0])

def CreateEnemies(Number:int = 10):
    for x in range(Number):
        NewXDist = randint(0,250)
        Sprite = pygame.surface.Surface((64,64))
        Sprite.fill("#00FF37")
        Sprite.blit(pygame.image.load("Assets\Images\Brik bo.png"), [0,0])
        Sprite.set_colorkey("#00FF37")
        EntityService.Add.Entity(f"Brick Bot", [NewXDist,GameService.Game.get("Window Size")[1] - 64], Sprite, "EntityService.AIService.Chase", "Survival")



while GameService.Game.get("Running"):
    GameService.Clock.tick(120)
    Info(PlayerService.PlayerList.get("Natasha").get("Possession Timer"))
    if PlayerService.PlayerList.get("Natasha").get("Souls") >= 50:
        Ping = pygame.mixer.Sound("Assets\Activate.wav")
        Ping.play()
    if len(EntityService.Entities) == 0:
        CreateEnemies(7)
    GameService.RunEvents()
    for entity in EntityService.Entities:
        EntityService.AIService.Chase(entity)

    if PlayerService.PlayerList.get("Natasha").get("Health") <= 0:
        GameService.ShiftCurrentInstance("Dead")
        GameService.Display.DisplayInstance()
        GameService.Instances.pop("Survival")
        Wait(5)
        exit()
    RunVelocity() if GameService.Game.get("Current Instance") == "Survival" else print(end="")
    PossessCountdown() if GameService.Game.get("Current Instance") == "Survival" else print(end="")
    GameService.Display.DisplayInstance()