class Hero():
     def __init__(self, pos, land):
          self.land  = land
          self.hero = loader.loadModel('smiley')
          self.hero.setColor(1, 0.5, 1)
          self.hero.setScale(0.3)
          self.hero.setPos(pos)
          self.hero.reparentTo(render)
          self.cameraBind()
          self.accept_events()
          self.mode = True
     def cameraBind(self):
          base.disableMouse()
          base.camera.setH(180)
          base.camera.reparentTo(self.hero)
          base.camera.setPos(2, 5, 5)
          self.cameraOn = True
     def cameraUp(self):
          pos = self.hero.getPos()
          base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2]-3)
          base.camera.reparentTo(render)
          base.enableMouse()
          self.cameraOn = False
     def accept_events(self):
          base.accept('k', self.land.saveMap)
          base.accept('l', self.land.loadMap)
          base.accept('c', self.changeView)
          base.accept('u', self.build)
          base.accept('u'+'-repeat', self.build)
          base.accept('i', self.destroy)
          base.accept('i'+'-repeat', self.destroy)
          base.accept('q', self.turnleft)
          base.accept('q'+'-repeat', self.turnleft)
          base.accept('e', self.turnright)
          base.accept('e'+'-repeat', self.turnright)
          base.accept('w', self.forward)
          base.accept('w'+'-repeat', self.forward)
          base.accept('d', self.right)
          base.accept('d'+'-repeat', self.right)
          base.accept('s', self.back)
          base.accept('s'+'-repeat', self.back)
          base.accept('a', self.left)
          base.accept('a'+'-repeat', self.left)
          base.accept('z', self.up)
          base.accept('z'+'-repeat', self.up)
          base.accept('x', self.down)
          base.accept('x'+'-repeat', self.down)
          base.accept('r', self.changemode)
     def changeView(self):
          if self.cameraOn:
               self.cameraUp()
          else:
               self.cameraBind()
     def turnleft(self):
          self.hero.setH((self.hero.getH()+5)%360)
     def turnright(self):
          self.hero.setH((self.hero.getH()-5)%360)
     def justmove(self, angle):
          pos = self.lookat(angle)
          self.hero.setPos(pos)
     def up(self):
          self.hero.setZ(self.hero.getZ()+1)
     def down(self):
          self.hero.setZ(self.hero.getZ()-1)
     def forward(self):
          angle = (self.hero.getH()+0)%360
          self.moveto(angle)
     def back(self):
          angle = (self.hero.getH()+180)%360
          self.moveto(angle)
     def left(self):
          angle = (self.hero.getH()+90)%360
          self.moveto(angle)
     def right(self):
          angle = (self.hero.getH()+270)%360
          self.moveto(angle)
     def trymove(self, angle):
          pos = self.lookat(angle)
          if self.land.isEmpty(pos):
               pos = self.land.findHighestEmpty(pos)
               self.hero.setPos(pos)
          else:
               pos = pos[0], pos[1], pos[2]+1
               if self.land.isEmpty(pos):
                    self.hero.setPos(pos)
     def moveto(self, angle):
          if self.mode:
               self.justmove(angle)
          else:
               self.trymove(angle)
     def lookat(self, angle):
          from_x = round(self.hero.getX())
          from_y = round(self.hero.getY())
          from_z = round(self.hero.getZ())
          dx, dy = self.checkdir(angle)
          return from_x + dx, from_y + dy, from_z
     def checkdir(self, angle):
          if 0 <= angle <= 20:
               return(0, -1)
          elif angle <= 65:
               return(1, -1)
          elif angle <= 110:
               return(1, 0)
          elif angle <= 155:
               return(1, 1)
          elif angle <= 200:
               return(0, 1)
          elif angle <= 245:
               return(-1, 1)
          elif angle <= 290:
               return(-1, 0)
          elif angle <= 335:
               return(-1, -1)
          else:
               return(0, -1)
     def changemode(self):
          self.mode = not self.mode
     def build(self):
          angle = self.hero.getH()%360
          pos = self.lookat(angle)
          if self.mode:
               self.land.addBlock(pos, (0, 0, 1, 1))
          else:
               self.land.buildBlock(pos)
     def destroy(self):
          angle = self.hero.getH() % 360
          pos = self.lookat(angle)
          if self.mode:
               self.land.delBlock(pos)
          else:
               self.land.delBlockFrom(pos)
     

