from direct.showbase.ShowBase import ShowBase
import math, sys, random
import DefensePaths as defensePaths
import SpaceJamClasses as spaceJamClasses

class SpaceJam(ShowBase): #Constructor
    def __init__(self):
        ShowBase.__init__(self)
        
        self.SetupScene()

        fullCycle = 60

        self.parent = self.loader.loadModel("./Assets/Drones/JulesVerne.obj")

        x = 0
        for j in range(fullCycle):
            spaceJamClasses.Drone.droneCount += 1
            nickName = "Drone" + str(spaceJamClasses.Drone.droneCount)
            self.DrawCloudDefense(self.Planet1, nickName)
            self.DrawBaseballSeams(self.Planet1, nickName, j, fullCycle, 1)
            # Figure out how to draw circles around the planets.

        for i in range(150):
            # self.DrawCircleXY            
            theta = x
            self.placeholder2 = self.render.attachNewNode('Placeholder2')
            # How can I get this to form a circle?
            self.placeholder2.setPos(10.0 * math.cos(theta), 10.0 * math.sin(theta), 0.0 * math.tan(theta))
            self.parent.instanceTo(self.placeholder2)
            x = x + 0.06

        for k in range(150):
            # self.DrawCircleYZ            
            theta = x
            self.placeholder3 = self.render.attachNewNode('Placeholder3')
            # How can I get this to form a circle (what do I need to remove)?
            self.placeholder3.setPos(0.0, 10.0 * math.sin(theta), 10.0 * math.tan(theta))
            self.placeholder3.setColorScale(1.0, 0, 0, 0)
            self.parent.instanceTo(self.placeholder3)
            x = x + 0.06

        for l in range(150):
            # self.DrawCircleXZ            
            theta = x
            self.placeholder4 = self.render.attachNewNode('Placeholder4')
            self.placeholder4.setPos(10.0 * math.cos(theta), 0.0, 10.0 * math.tan(theta))
            self.placeholder4.setColorScale(0, 1.0, 0, 0)
            self.parent.instanceTo(self.placeholder4)
            x = x + 0.06

    def DrawCloudDefense(self, centralObject, droneName):
        unitVec = defensePaths.Cloud()
        unitVec.normalize()
        position = unitVec * 500 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/Drones/JulesVerne.obj", self.render, droneName, "./Assets/Drones/Textures/sh3.jpg", position, 50)
    def DrawBaseballSeams(self, centralObject, droneName, step, numSeams, radius = 1):
        unitVec = defensePaths.BaseballSeams(step, numSeams, B = 0.4)
        unitVec.normalize()
        position = unitVec * radius * 1000 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/Drones/JulesVerne.obj", self.render, droneName, "./Assets/Drones/Textures/sh3.jpg", position, 200)
    '''def DrawCircleXY(self, centralObject, droneName):
        # Figure out how to import math from warmups into DefensePaths.
        unitVec = defensePaths.CircleXY()
        unitVec.normalize()
        #position = unitVec * 100 * 1000 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/Drones/JulesVerne.obj", self.render, droneName, "./Assets/Drones/Textures/sh3.jpg", position, 100)'''    



    def SetupScene(self):
        # Universe setup
        self.Universe = spaceJamClasses.Universe(self.loader, "./Assets/Universe/Universe.x", self.render, 'Universe', "Assets/Universe/space-galaxy.jpg", (0, 0, 0), 15000)
        '''self.Universe.reparentTo(self.render)
        self.Universe.setScale(15000)
        tex = self.loader.loadTexture("./Assets/Universe/space-galaxy.jpg")
        self.Universe.setTexture(tex, 1)'''

        # Player setup
        self.Player = spaceJamClasses.Player(self.loader, "./Assets/Player/theBorg.x", self.render, 'Player', "Assets/Player/theBorg.jpg", (150, 1500, 67), 5)
        '''self.Player = self.loader.loadModel("./Assets/Player/theBorg.x")
        self.Player.reparentTo(self.render)
        self.Player.setPos(150, 1500, 67)
        self.Player.setScale(5)
        tex = self.loader.loadTexture("./Assets/Player/theBorg.jpg")
        self.Player.setTexture(tex, 1)'''

        # Space station setup
        self.Station = spaceJamClasses.Station(self.loader, "./Assets/SpaceStation1B/spaceStation.x", self.render, 'Station', "Assets/SpaceStation1B/SpaceStation1_Dif2.png", (-1500, 7000, 100), 100)
        '''self.Station = self.loader.loadModel("./Assets/SpaceStation1B/spaceStation.x")
        self.Station.reparentTo(self.render)
        self.Station.setPos(-1500, 7000, 100)
        self.Station.setScale(100)
        tex = self.loader.loadTexture("./Assets/SpaceStation1B/SpaceStation1_Dif2.png")
        self.Station.setTexture(tex, 1)'''

        # Planet 1 setup
        self.Planet1 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet1', "Assets/Planets/planet1.jpg", (300, 5000, 67), 350)
        '''self.Planet1.reparentTo(self.render)
        self.Planet1.setPos(300, 5000, 67) # Change positions
        self.Planet1.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/planet1.jpg")
        self.Planet1.setTexture(tex, 1)'''

        # Planet 2 setup
        self.Planet2 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet2', "Assets/Planets/planet2.jpg", (1500, 5000, 67), 350)
        '''self.Planet2.reparentTo(self.render)
        self.Planet2.setPos(1500, 5000, 67)
        self.Planet2.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/planet2.jpg")
        self.Planet2.setTexture(tex, 1)'''

        # Planet 3 setup
        self.Planet3 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet3', "Assets/Planets/planet3.jpg", (-1500, 5000, 100), 350)
        '''self.Planet3.reparentTo(self.render)
        self.Planet3.setPos(-1500, 5000, 100)
        self.Planet3.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/planet3.jpg")
        self.Planet3.setTexture(tex, 1)       '''

        # Planet 4 setup
        self.Planet4 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet4', "Assets/Planets/planet4.jpg", (-2500, 5000, -67), 350)      
        '''self.Planet4 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet4.reparentTo(self.render)
        self.Planet4.setPos(-2500, 5000, -67)
        self.Planet4.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/planet4.jpg")
        self.Planet4.setTexture(tex, 1)'''

        # Planet 5 setup
        self.Planet5 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet5', "Assets/Planets/planet5.jpg", (2500, 5000, -67), 350)
        '''self.Planet5 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet5.reparentTo(self.render)
        self.Planet5.setPos(2500, 5000, -67)
        self.Planet5.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/planet5.jpg")
        self.Planet5.setTexture(tex, 1)'''

        # Planet 6 setup
        self.Planet6 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet6', "Assets/Planets/planet6.jpg", (-650, 5000, 67), 350)
        '''self.Planet6.reparentTo(self.render)
        self.Planet6.setPos(-650, 5000, 67)
        self.Planet6.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/planet6.jpg")
        self.Planet6.setTexture(tex, 1)'''


app = SpaceJam()
app.run()