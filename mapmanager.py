import pickle
class Mapmanager():
     def __init__(self):
          self.model= 'block.egg'
          self.texture = 'wood.png'

     def isEmpty(self, pos):
          blocks = self.findBlocks(pos)
          if blocks:
               return False
          else:
               return True
     def findHighestEmpty(self, pos):
          x, y, z = pos
          z = 1
          while not self.isEmpty((x, y, z)):
               z += 1
          return(x, y, z)
     def startNew(self):
          self.land =render.attachNewNode('Land')
     def addBlock(self, position, color):
          self.block = loader.loadModel(self.model)
          self.block.setTexture(loader.loadTexture(self.texture))
          self.block.setPos(position)
          self.block.setColor(color)
          self.block.reparentTo(self.land)
          self.block.setTag("at", str(position))
     def findBlocks(self, pos):
          return self.land.findAllMatches('=at=' + str(pos))
     def loadLand(self, filename):
          self.clear()
          with open(filename) as file:
               y = 0
               for line in file:
                    x = 0
                    line = line.split()
                    for z in line:
                         for z0 in range(int(z)+1):
                              color = (z0/10, 0.1+z0/10, z0/10, 1)
                              block = self.addBlock((x, y, z0), color)
                         x += 1
                    y += 1
     def clear(self):
          self.land.removeNode()
          self.startNew()
     def delBlock(self, position):
          blocks = self.findBlocks(position)
          for block in blocks:
               block.removeNode()
     def buildBlock(self, pos):
          x, y, z = pos
          new = self.findHighestEmpty(pos)
          if new[2] <= z + 1:
               self.addBlock(new, (0, 0, 1, 1))
     def delBlockFrom(self, pos):
          x, y, z = self.findHighestEmpty(pos)
          pos = x, y, z - 1
          blocks = self.findBlocks(pos)
          for block in blocks:
               block.removeNode()
     def saveMap(self):
          blocks = self.land.getChildren()
          with open('my_map.dat', 'wb') as fout:
               pickle.dump(len(blocks), fout)
               for block in blocks:
                    x, y, z = block.getPos()
                    pos = (int(x), int(y), int(z))
                    pickle.dump(pos, fout)
     def loadMap(self):
          self.clear()
          with open('my_map.dat', 'rb') as fin:
               length = pickle.load(fin)
               for i in range(length):
                    pos = pickle.load(fin)
                    self.addBlock(pos, (0.5, 0.5, 0.5, 1))
