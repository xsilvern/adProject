import random
from queue import Queue

class MineSweeper:
    def __init__(self,size,mineCnt,life = 1):
        self.mineSweeperMap=self.mapGenerater(size,mineCnt)
        self.isClickMap=[[0 for i in range(size)]for j in range(size)]
        self.mineCnt=mineCnt
        self.size=size
        self.life=1
    def mapGenerater(self,size,mineCnt):
        xyList=[]
        for i in range(size):
            for j in range(size):
                xyList.append((i,j))
        mineSweeperMap=[[0 for i in range(size)]for j in range(size)]
        for i in range(mineCnt):
            xy = random.choice(xyList)
            x, y = xy
            mineSweeperMap[y][x] = -1
            xyList.remove(xy)
            for j in range(3):
                for k in range(3):
                    if 0 <= x-1+k <size and 0 <= y-1+j < size:
                        if not mineSweeperMap[y-1+j][x-1+k] == -1:
                            mineSweeperMap[y-1+j][x-1+k]+=1
        return mineSweeperMap
    def chooseBlock(self,x,y):
        clarifyList = []
        if self.isClickMap[y][x] == 1:
            return []
        
        if self.mineSweeperMap[y][x] == 0 :
            
            queue = Queue()
            queue.put((x,y))
            clarifyList.append((x,y))
            xDir=[0,0,-1,-1,-1,1,1,1]
            yDir=[-1,1,-1,0,1,-1,0,1]
            while not queue.empty():
                tx, ty = queue.get()
                if self.isClickMap[ty][tx]:
                    continue
                
                self.isClickMap[ty][tx] = 1
                if self.mineSweeperMap[ty][tx] != 0:
                    continue
                
                
                for i in range(len(xDir)):
                    if 0<=ty+yDir[i]<self.size and 0<=tx+xDir[i]<self.size:
                        if self.isClickMap[ty + yDir[i]][tx + xDir[i]] == 0:
                            clarifyList.append((tx + xDir[i],ty + yDir[i]))
                            queue.put((tx + xDir[i],ty + yDir[i]))
            
        elif self.mineSweeperMap[y][x] == -1:
            clarifyList.append((x,y))
            self.life-=1
        else:
            clarifyList.append((x,y))
            self.isClickMap[y][x]=1
        s=0
        for i in range(self.size):
            s+=sum(self.isClickMap[i])
        return clarifyList
    def isClear(self):
        s=0
        isNum=0
        for i in range(self.size):
            s+=sum(self.isClickMap[i])
        if self.size**2-s == self.mineCnt:
            isNum = 1
        elif self.life == 0 :
            isNum = 2
        return isNum
    def showBlock(self,x,y):
        return self.mineSweeperMap[y][x]
    def getMap(self):
        return self.mineSweeperMap
