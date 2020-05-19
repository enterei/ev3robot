import json

from Robot import Robot


class SystemHandler:
    robot=Robot()
    Table = [['N', 'N', 'N', 'N'], ['N', 'N', 'N', 'N'], ['N', 'N', 'N', 'N'], ['N', 'N', 'N', 'N']]
    target = [None,None]
    position=[0,0]
    next_corner=[None,None]
    orientation =[1,0]
    neutrals =[]
    neutral_idx=0
    active =None


    def __init__(self,**kwargs):

        self.Table[0][0]= 'P'
        self.orientation ="up"
        self.target = [None, None]
        self.position = [0, 0]
        self.next_corner = [None, None]




    def handleMessage(self,message):
        message=json.loads(message.decode('utf-8'))
        print(message.get)
        if(message.get('Aktion')=="Bewegung"):
            ##self.handleSystem(message)
            if message.get('Bewegung')=="straight":
                message.update()
                self.robot.goWay(**message)
        if (message.get('Aktion') == "Bewegung"):
            ##self.handleSystem(message)
            if message.get('Bewegung') == "move":
                message.update()
                self.robot.goWay(**message)


    def handleBewegung(self,message):
        print("System message")


    def handleTest(self,message):
        return self.testHandler.handleMessage(message)


    def handleAktion(self, message):
        if(message.get('Turn')):
            self.getEnemyMove()
            return self.getOrder()
    def getOrder(self):
        if self.active=="getEnemeyMove":
            if self.target:
                order=self.findWay()
    def findWay(self):
        res=[self.target[0]-self.position[0],self.target[1]-self.position[1]]


    def setGoal(self,corner):
        self.target=corner

    def lookUp(self,idx):
        if(idx == 0):
            return [2,0]
        if (idx == 1):
            return [2, 1]
        if (idx == 2):
            return [2, 2]
        if (idx == 3):
            return [1, 0]
        if (idx == 4):
            return [1, 1]
        if (idx == 5):
            return [1, 2]
        if (idx == 6):
            return [0, 0]
        if (idx == 7):
            return [0, 1]
        if (idx == 8):
            return [0, 2]

    def print(self):
        print(self.Table[0][0]+" "+self.Table[0][1]," "+self.Table[0][2]+ " "+self.Table[0][3])
        print(self.Table[1][0]+" "+self.Table[1][1]," "+self.Table[1][2]+ " "+self.Table[1][3])
        print(self.Table[2][0]+" "+self.Table[2][1]," "+self.Table[2][2]+ " "+self.Table[2][3])
        print(self.Table[3][0]+" "+self.Table[3][1]," "+self.Table[3][2]+ " "+self.Table[3][3])



