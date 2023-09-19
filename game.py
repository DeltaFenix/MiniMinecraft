from direct.showbase.ShowBase import ShowBase
from mapmanager import *
import pickle
from hero import *
class Game(ShowBase):
     def __init__(self):
          ShowBase.__init__(self)
          self.land = Mapmanager()
          self.land.startNew()
          self.land.loadLand('land.txt')
          base.camLens.setFov(90)
          self.hero = Hero((5, 5, 5), self.land)
game = Game()
game.run()