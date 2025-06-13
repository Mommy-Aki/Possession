###################################
# Imports

import pygame
import tkinter
import datetime
import pathlib
import os
from subprocess import run 
import wx
from colorama import Fore as TextColour
from time import sleep as Wait
from random import randint
from typing import Callable, Optional
###########################################
def PAIDEPyVersion(Code):
    return "02.00.04" if Code == "76wfh6f4hft2wh378wth32wtcrhi2whrcttqith76qchtjqwihctrj6qh8ct62tqc86t2c" else exit()

def Help():
    CurrentTime = datetime.datetime.now()
    Info(f"""

 __^__                                                                             __^__
( ___ )---------------------------------------------------------------------------( ___ )
 | / |   __      __  ____    __        ____      _____              ____           | / |
 | / |  /\ \  __/\ \/\  _`\ /\ \      /\  _`\   /\  __`\  /'\_/``\/\  _`\          | / |
 | / |  \ \ \/\ \ \ \ \ \L\_\ \ \     \ \ \/\_  \ \ \ \/\ \/\     \ \ \L\_\        | / |
 | / |   \ \ \ \ \ \ \ \  _\L\ \ \  __ \ \ \/_/_ \ \ \ \ \ \ \ __\ \ \  _\L        | / |
 | / |    \ \ \_/ \_\ \ \ \L\ \ \ \L\ \ \ \ \L\ \ \ \ \_\ \ \ \_ /\ \ \ \L\ \      | / |
 | / |     \ `\___x___/\ \____/\ \____/  \ \____/  \ \_____\ \_\ \ \_\ \____/      | / |
 | / |      '\/__//__/  \/___/  \/___/    \/___/    \/_____/\/_/  \/_/\/___/       | / |
 | / |                                                                             | / |
 | / |                                                                             | / |
 | / |         ______  _____        ____    ______  ______    ____    ____         | / |
 | / |        /\__  _\/\  __`\     /\  _`\ /\  _  \/\__  _\  /\  _`\ /\  _`\       | / |
 | / |        \/_/\ \/\ \ \/\ \    \ \ \L\ \ \ \L\ \/_/\ \/  \ \ \/\ \ \ \L\_\     | / |
 | / |           \ \ \ \ \ \ \ \    \ \ ,__/\ \  __ \ \ \ \   \ \ \ \ \ \  _\L     | / |
 | / |            \ \ \ \ \ \_\ \    \ \ \/  \ \ \/\ \ \_\ \__ \ \ \_\ \ \ \L\ \   | / |
 | / |             \ \_\ \ \_____\    \ \_\   \ \_\ \_\/\_____\ \ \____/\ \____/   | / |
 | / |              \/_/  \/_____/     \/_/    \/_/\/_/\/_____/  \/___/  \/___/    | / |
 |___|                                                        (Version {PAIDEPyVersion("76wfh6f4hft2wh378wth32wtcrhi2whrcttqith76qchtjqwihctrj6qh8ct62tqc86t2c")})   |___|
( ___ )---------------------------------------------------------------------------( ___ )
 
         
    PAIDE is an SDk powered by Python's Pygame module, it acts as a SDK supposed to help you make 2D Games
    in Python, it comes with inn built function to help set up your game and get it in the testing stages quickly and effortlessly.
         
    Lots of Pygame's tedious functions will be simplified and made easier by the documentation, found here:
         <https://www.pygame.org/docs/> [pygame], 
         <https://github.com/Mommy-Aki/PAIDE-SDK-ALPHA/blob/main/README.md> [PAIDE] 
    
    Enjoy the Module, an remember, if you think you need to update this, make sure to check the documentation and release
    version in github, found here: <https://github.com/Mommy-Aki/PAIDE-SDK-ALPHA/releases> [Github]
    
    Make sure to read the ToS, found in the github here: <https://github.com/Mommy-Aki/PAIDE-SDK-ALPHA/blob/main/ToS.md> [Github]
     
    [{CurrentTime.date()}]: [{CurrentTime.timetz()}] PAIDE imported

    """)

# [Somehow] prints an error
def Error(text:str): print(f"{TextColour.RED}Error: {text}{TextColour.RESET}"), exit() if str(text).strip() != "" else exit()

# [Somehow] prints information
def Info(text:str): print(f"{TextColour.MAGENTA}{text}{TextColour.RESET}") if str(text).strip() != "" else Help()

# [Somehow] prints a warning
def Warn(text:str): print(f"{TextColour.YELLOW}Warning!: {text}{TextColour.RESET}") if str(text).strip() != "" else print("",end="")

Help()

class HexColour():
    def __init__(self, Value):
        AcceptedValues = ["#","0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
        if type(Value) == int:
            self.Value = hex(Value)

            self.Value = f"#{self.Value.split("0x")[1]}"

            while len(self.Value) < 9 and len(self.Value) != 7:
                self.Value += "0"
            
            if len(self.Value) > 9:
                self.Value = self.Value[0:9]

        elif type(Value) == str:

            if "#" not in Value:
                Value = f"#{Value}"
            
            for character in Value:
                if str.lower(character) not in AcceptedValues:
                    Error(f"Character '{character}' cannot be converted to hex")
                

                try:
                    AcceptedValues.remove("#")
                except:
                    pass
            
            self.Value = str.lower(Value)
        else:
            Error("Please only convert int and str data types into hex")

        
        
class GameService(): # Game configurations
    Controllers = []
    IsGameAvailable = False
    Instances = {}
    Clock = pygame.time.Clock()

    Game = {

            "Name" : "GameName",
            "Running" : True,
            "Version" : None,
            "Current Instance" : None,
            "DefaultFallbackColour" : "DefaultFallbackColour"

        }

    def DefaultName():
        Prefix = ["Small", "Tale of a(n)", "Modified", "Reanimated", "AI-Driven", "Critical", "Baby", "Tiny", "Muscular", "Python-Made", "Puzzle-Solving", "Fast-Paced"]
        Noun = ["Yellow", "Red", "Blue", "Orange", "Magenta", "Teal", "Water", "Lava", "Zombie", "Demon", "Chicken", "Baby", "Whale", "Animation", "Bot", "Thinking", "Game"]
        Suffix = ["Book", "Madness", "Software", "Conscious", "Hosting", "Skill Tester", "Dater", "RP", "Survival Game", "Aim Trainer", "FPS", "Data Analyser", "Horror Game", "Game"]

        SelectedPrefix = Prefix[randint(0,len(Prefix) - 1)]
        Number = randint(0,len(Noun) - 1)
        SelectedNoun = Noun[Number] if SelectedPrefix != Noun[Number] else ""
        Number = randint(0,len(Suffix) - 1)
        SelectedSuffix = Suffix[Number] if SelectedNoun != Suffix[Number] else ""

        CreatedName = f"{SelectedPrefix} {SelectedNoun} {SelectedSuffix}"
        return CreatedName

    def SetupGame(GameName:str = None, IconPath = "Dependancies\ignoreme.ico", WindowSize:list = [500,500] or "-fullscreen", DefaultFallbackColour:str = "#FFFFFF"):
        External = wx.App(False)

        if GameName == None or str(GameName).strip() == "":
            GameName = GameService.DefaultName()
        ScreenWidth, ScreenHeight = wx.GetDisplaySize() if WindowSize == "-fullscreen" else WindowSize if (type(WindowSize) == list or type(WindowSize) == tuple) and len(WindowSize) == 2 else None
        #Info(f"x:{ScreenWidth} y:{ScreenHeight}")
        pygame.init()
        pygame.joystick.init()

        GameService.Controllers = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

        if ScreenWidth == None or ScreenHeight == None:
            Error("Could not get screen size, else screen size is in the wrong format")
        
        NonPenalties = 0
        AcceptedFormats = [".png",".ico",".jpeg"]

        if ".ico" not in IconPath:
            Warn("Please make sure your Icon is using the '.ico' file extender and being a square image for formality reasons")
        elif "." not in IconPath:
            Error("Please choose a file")
        else:
            for each in AcceptedFormats:
                if each in IconPath:
                    NonPenalties += 1
            
            if NonPenalties == 0:
                Error("Invalid file type")

        pygame.display.set_icon(pygame.image.load(pathlib.Path(IconPath)))
        pygame.display.set_mode((ScreenWidth,ScreenHeight))
        VersionPath = pathlib.Path("Assets\cfg\.pyversion")
        VersionTextRaw = f"({open(VersionPath).read().strip()})" if  "#--" not in open(VersionPath).read().strip() else ""
        pygame.display.set_caption(f"{GameName} {VersionTextRaw}")

        GameData = {

            "Name" : GameName,
            "Running" : True,
            "Version" : VersionTextRaw if VersionTextRaw != "" else None,
            "Current Instance" : None,
            "DefaultFallbackColour" : DefaultFallbackColour,
            "Window Size" : [ScreenWidth, ScreenHeight]

        }
        GameService.Game = GameData
        GameService.ConfigureGame(WindowSize = [500,500])
        GameService.CreateInstance("WTM+PAIDE_EXE","#000000")
        WTM = pygame.image.load("Dependancies\WTMIMG.png")
        ObjectService.BuildObject("WTM+PAIDE_TTL", [0,0], WTM, "WTM+PAIDE_EXE")
        
        pygame.display.get_surface().blit(ObjectService.ObjectList.get("WTM+PAIDE_TTL").get("Sprite"), (0,0))
        pygame.display.update()

        Wait(5)
        GameService.ConfigureGame(WindowSize = [ScreenWidth, ScreenHeight])
        return

    def ConfigureGame(GameName:str = None, IconPath = None, WindowSize:list = None, DefaultFallbackColour:str = None):
        GameSettings = GameService.Game

        if str(GameName).strip() != "" and GameName != None:
            GameSettings.update({"Name" : GameName})
            pygame.display.set_caption(GameName)
        
        if str(IconPath).strip() != "" and IconPath != None:
            try:
                NewPath = pathlib.Path(IconPath)
                NewImage = pygame.image.load(NewPath)
            except:
                Warn("Image cannot be found")
            else:
                pygame.display.set_icon(NewImage)

                if ".ico" not in IconPath:
                    Warn("it is suggested to use .ico files instead of conventional image files")

        

        External2 = wx.App(False)    
        ScreenWidth, ScreenHeight = wx.GetDisplaySize() if WindowSize == "-fullscreen" else WindowSize if (type(WindowSize) == list or type(WindowSize) == tuple) and len(WindowSize) == 2 else None
            
        GameSettings.update({"Window Size": (ScreenWidth, ScreenHeight)})
        pygame.display.set_mode((ScreenWidth, ScreenHeight))
        pygame.display.toggle_fullscreen() if WindowSize == "-fullscreen" else print(end="")
        
        if str(GameName).strip() != "" or GameName != None:
            pass

    def CreateInstance(Name:str = "Test", FallbackColour:Optional[HexColour] = None):
        
        FallbackColour = FallbackColour if FallbackColour != None else GameService.Game.get("DefaultFallbackColour")
        CreatedGameBefore = True if len(GameService.Instances) != 0 else False
        
        InstanceData = {

            "ID" : len(GameService.Instances),
            "Display Screen" : pygame.Surface(pygame.display.get_window_size()),
            "Background" : None, # Image
            "Fallback Colour" : FallbackColour # Hex Colour

        }
        InstanceData.get("Display Screen").fill(InstanceData.get("Fallback Colour"))

        GameService.Instances.update({Name : InstanceData})

        if not CreatedGameBefore:
            GameService.Game.update({"Current Instance" : Name})


    def ShiftCurrentInstance(InstanceName:str = None):
        CurrentInstance = GameService.Game.get("Current Instance", None)

        if len(GameService.Instances) == 2:
            for instance in GameService.Instances:
                if instance == CurrentInstance:
                    continue
                else:
                    GameService.Game.update({"Current Instance" : instance})
                    return
            

        elif len(GameService.Instances)  > 2 and InstanceName in GameService.Instances:
            GameService.Game.update({"Current Instance" : InstanceName})
            
        else:

            return


    def RunEvents():
        if GameService.Game.get("Current Instance") == "WTM+PAIDE_EXE":
            GameService.Instances.pop("WTM+PAIDE_EXE")

            for instance in GameService.Instances:
               GameService.Game.update({"Current Instance" : instance})
               break
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameService.Game.update({"Running" : False})
            elif event.type == pygame.KEYDOWN or event.type == pygame.JOYBUTTONDOWN:
                PlayerService.InputManager.Run.Key(event.key if event.type == pygame.KEYDOWN else event.button if event.type == pygame.JOYBUTTONDOWN else None)
            elif event.type == pygame.JOYAXISMOTION:
                PlayerService.InputManager.Run.Joystick(event)   
    
    class Display():
        def ChangeInstance(NewInstance:str = None):
            if NewInstance not in GameService.Instances:
                Warn(f"Cannot Change Instance to: '{NewInstance}', it either does not exist or cannot be found")
                return
            
            GameService.game.update({"Current Instance" : NewInstance})
            
        def DisplayInstance(InstanceName:Optional[str] = None):
            
            DisplaySurface = pygame.display.get_surface() # gets the screen
            
            InstanceName = GameService.Game.get("Current Instance", None)
            Instance = GameService.Instances.get(InstanceName, None) # finds an instance
            
            if Instance == None:
                Instance = GameService.Instances.get("Current Instance", None)
                if Instance == None:
                    if len(GameService.Instances) == 0:
                        Error("No instances created")
                    else:
                        for each in GameService.Instances:
                            Instance = GameService.Instances.get(each)
                            GameService.Game.update({"Current Instance" : each})

                            break
            #Info(Instance)
            InstanceScreen = Instance.get("Display Screen")
            DisplaySurface.blit(InstanceScreen, (0,0))
            for object in ObjectService.ObjectList:
                DisplaySurface.blit(ObjectService.ObjectList[object].get("Sprite").convert_alpha(), ObjectService.ObjectList[object].get("Position")) if ObjectService.ObjectList[object].get("Instance") == GameService.Game.get("Current Instance") else print(end="")
            for entity in EntityService.Entities:
                DisplaySurface.blit(entity.get("Sprite"), entity.get("Position")) if entity.get("Instance") == GameService.Game.get("Current Instance") else print(end="")
            
            for player in PlayerService.PlayerList:
                DisplaySurface.blit(PlayerService.PlayerList[player].get("Sprite").convert_alpha(), PlayerService.PlayerList[player].get("Position")) if PlayerService.PlayerList[player].get("Instance") == GameService.Game.get("Current Instance") else print(end="")
                #Info(f"{PlayerService.PlayerList[player]}")
            
           
            pygame.display.update()

class EntityService():
    Entities = []
    
    DefaultEntityAttributes = {
        "Name": None,
        "AI" : "Chase",
        "Position": [0,0],
        "Sprite": None,
        "Instance": None
    }

    class AIService():
        def Chase(EntityChasingPlayer):
            ClosestPlayer = None
            ClosestPlayerDistance = 999999999999
            EntityPosition = EntityChasingPlayer.get("Position")
            for player in PlayerService.PlayerList:
                PlayerPosition = PlayerService.PlayerList[player].get("Position")
                Distance = Maths.Pythagoras(EntityPosition[0] - PlayerPosition[0], EntityPosition[1] - PlayerPosition[1])
                if Distance < 0:
                    Distance * -1
                if ClosestPlayer == None or Distance < ClosestPlayerDistance:
                    ClosestPlayer = player
                    ClosestPlayerDistance = Distance
                
            TargetPlayer = PlayerService.PlayerList.get(ClosestPlayer)
            
            if Distance < 10:
                TargetPlayer.update({"Health": TargetPlayer.get("Health") - 10}) if TargetPlayer.get("Immunity", None) == None else print(end="")
                Wait(0.2)
            
            if TargetPlayer.get("Position")[0] > EntityPosition[0]:
                EntityChasingPlayer.update({"Position": [EntityPosition[0] + randint(5, 10) * 0.01, EntityPosition[1]]})
            elif TargetPlayer.get("Position")[0] < EntityPosition[0]:
                EntityChasingPlayer.update({"Position": [EntityPosition[0] - randint(5, 10) * 0.01, EntityPosition[1]]})
            


    
    
        
        



    class Add():
        def Entity(Name:str = None, Position:list = [0,0], Sprite:any = None, AI:Optional[Callable] = None, Instance:str = None):
            EntityData = EntityService.DefaultEntityAttributes

            if Name != None and str(Name).strip() != "":
                EntityData.update({"Name": Name, "Position": Position, "Sprite": Sprite, "AI": AI, "Instance": Instance})
                EntityService.Entities.append(EntityData)
            else:
                return

        def DefaultAtrribute(Name,DefaultValue):
            pass


class Maths():
    Pi = 3.14159265359

    def Pythagoras(a:float = None, b:float = None, c:float = None):
        ComparisonMode = False
        Finding = None

        if a == b == c == None:
            Error("Must provide 2 values in order to calculate")
        elif a == b == None or b == c == None or a == c == None:
            Error("Must have 2 values at least to calculate")
        
        try:
            a = float(a)
        except:
            Finding == "a"
        
        try:
            b = float(b)
        except:
            Finding == "b"
        
        try:
            c = float(c)
        except:
            Finding == "c"

        if Finding == None:
            ComparisonMode == True
        
        if ComparisonMode:
            a **= 2
            b **= 2
            c **= 2

            return True if a + b == c else False
        
        else:
            if Finding == "a":
                return (c**2 - b**2)**0.5
            elif Finding == "b":
                return (c**2 - a**2)**0.5
            else:
                return (b**2 + a**2)**0.5

      



class PlayerService():
    PlayerList = {}
    UserNameIterative = {}

    DefaultPlayerData = {

            "Display Name": None,
            "Username": None,
            "Sprite": None,
            "Sprite Type": None,
            "Position": None,
            "Instance": None,


        }
    
    class Add():
        def DefaultAttribute(AttributeName:str = None, DefaultValue:Optional[any] = None):
            if AttributeName == None or str.lower(AttributeName).strip() == "":
                Warn("Cannot add an attribute without a valid name")
                return

            PlayerService.DefaultPlayerData.update({AttributeName: DefaultValue})


        def Player(DisplayName:Optional[str] = None, Username:str = f"User_", Sprite:list = None, Position:list = [0,0], Instance:str = GameService.Instances[0] if len(GameService.Instances) > 0 else None):
        
            if Username not in PlayerService.UserNameIterative:
                PlayerService.UserNameIterative.update({Username : 1})
            else:
                PlayerService.UserNameIterative.update({Username : PlayerService.UserNameIterative.get(Username) + 1})
                

            if str(Username).strip()[-1] == "_":
                Username += str(PlayerService.UserNameIterative.get(Username) - 1)
            
            DisplayName = DisplayName if DisplayName != None and str(DisplayName).strip() != "" else Username
            PlayerInfo = PlayerService.DefaultPlayerData
            PlayerInfo.update({"Display Name": DisplayName, "Username": Username, "Sprite": Sprite, "Position": Position, "Instance" : Instance})
            PlayerService.PlayerList.update({PlayerInfo["Username"] : PlayerInfo})



    class InputManager():
        Keys = {}
        KeyID = 0
        class Bind():
            def Key(PygameKey:int, Function:Callable, InstanceBound:Optional[str] = None):
                PlayerService.InputManager.Keys.update({PlayerService.InputManager.KeyID : ["Key", PygameKey, Function, InstanceBound]})
                PlayerService.InputManager.KeyID += 1
            
            def Joystick(Direction:str, Function:Callable, InstanceBound:Optional[str] = None):
                Directions = {"up" : [1, -1], "down" : [1, 1], "left" : [0, -1], "right" : [0, 1]}

                if str.lower(Direction) not in Directions:
                    Warn("Cannot Bind Direction")
                    return
                


                PlayerService.InputManager.Keys.update({PlayerService.InputManager.KeyID : ["Joystick", Directions.get(str.lower(Direction)), Function, InstanceBound]})
                PlayerService.InputManager.KeyID += 1

        class Run():
            def Key(Key:Optional[str] = None, Instance:str = None):
                for key_bind in PlayerService.InputManager.Keys:
                    if PlayerService.InputManager.Keys.get(key_bind)[0] == "Key" and PlayerService.InputManager.Keys.get(key_bind)[1] == Key and (GameService.Game.get("Current Instance") == PlayerService.InputManager.Keys.get(key_bind)[3] or PlayerService.InputManager.Keys.get(key_bind)[3] == None):
                        PlayerService.InputManager.Keys.get(key_bind)[2].__call__()
                    

            def Joystick(EventObject, Instance:Optional[str] = None):
                for key_bind in PlayerService.InputManager.Keys:
                    if PlayerService.InputManager.Keys.get(key_bind)[0] == "Joystick" and (GameService.Game.get("Current Instance") == PlayerService.InputManager.Keys.get(key_bind)[3] or PlayerService.InputManager.Keys.get(key_bind)[3] == None):
                        #Info(PlayerService.InputManager.Keys.get(key_bind)[1][1])
                        if EventObject.axis == PlayerService.InputManager.Keys.get(key_bind)[1][0] and round(EventObject.value) == PlayerService.InputManager.Keys.get(key_bind)[1][1]:
                                PlayerService.InputManager.Keys.get(key_bind)[2].__call__()

    
class ObjectService():
    ObjectList = {}

    def BuildObject(Name:str = "Object_", Position:list = [0,0], Sprite:str = None, CanCollide:bool = True, InstanceBound:str = None):

        Name += str(len(ObjectService.ObjectList)) if Name == "Object_" else ""

        DefaultObjectData = {

            "Name" : Name,
            "Position": Position,
            "Sprite": Sprite,
            "Instance": InstanceBound,
            "CanCollide": CanCollide

        }

        ObjectService.ObjectList.update({Name: DefaultObjectData})
