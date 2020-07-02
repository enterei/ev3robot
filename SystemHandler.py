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
        print(message.get('Aktion'))
        if(message.get('gameEndSound')=="True"):
            self.robot.endGameSound()
        if(message.get('Aktion')=="Bewegung"):
            ##self.handleSystem(message)
            if message.get('Bewegung')=="straight":
                message.update()
                self.robot.goWay(**message)
        if (message.get('Aktion') == "Bewegung"):
            self.handleSystem(message)
        if message.get('Aktion') == "move":
             #   message.update()
            print("in move")
            if self.robot.goWay(**message):
                message={'Aktion':"Befehl"}
                res_bytes = json.dumps(message).encode('utf-8')
                res=True
                res=res_bytes
                return res
        if message.get('Aktion')=="wait":
            return self.wait()
        if message.get('Aktion')=="scan":
            if self.robot.goWay(**message):
               # message = {'Aktion': "Befehl"}
                #res_bytes = json.dumps(message).encode('utf-8')
                #res = True
                #res = res_bytes
                return self.robot.measure()



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



    def print(self):
        print(self.Table[0][0]+" "+self.Table[0][1]," "+self.Table[0][2]+ " "+self.Table[0][3])
        print(self.Table[1][0]+" "+self.Table[1][1]," "+self.Table[1][2]+ " "+self.Table[1][3])
        print(self.Table[2][0]+" "+self.Table[2][1]," "+self.Table[2][2]+ " "+self.Table[2][3])
        print(self.Table[3][0]+" "+self.Table[3][1]," "+self.Table[3][2]+ " "+self.Table[3][3])


    def wait(self):
        self.robot.makebeep()
        while True:
            if self.robot.tank.ts.is_pressed:
                break

        message = {'Aktion': "Befehl",'Status':'WaitOver'}
        res_bytes = json.dumps(message).encode('utf-8')
        return res_bytes


