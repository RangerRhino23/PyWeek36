from ursina import *
from ursina.prefabs.first_person_controller import *
from ursina.prefabs.conversation import *

app=Ursina(borderless=False)
scene1=[]
scene2=[]
scene3=[]
scene4=[]
scene5=[]

font='assets/MainFont.ttf'
class MenuScreen(Entity):
    def __init__(self, **kwargs):
        super().__init__(self,model='quad',parent='camera.ui', **kwargs)
        self.inMenu = False
        self.background = Entity(parent=camera.ui,enabled=False,scale=[1.8,1],texture='bg.mp4',model='quad',z=1)
        self.text1 = Text(text='Paused',enabled=False,x=-.12,y=.4,scale=3,font=font)
        self.resumeGame = Button(text='Resume Game',enabled=False,scale_y=.075,scale_x=.2,y=0,x=-.65,color=color.rgba(27, 18, 18, 100),highlight_color=color.rgba(27, 18, 18, 100),highlight_scale=1.1,pressed_scale=0.9,ignore_paused=True)
        self.resumeGame.on_click = self.killMenu
        self.quitGame = Button(text='Quit Game',enabled=False,scale_y=.075,scale_x=.2,y=-.2,x=-.65,color=color.rgba(27, 18, 18, 100),highlight_color=color.rgba(27, 18, 18, 100),highlight_scale=1.1,pressed_scale=0.9,ignore_paused=True)
        self.quitGame.on_click = application.quit

    def createMenu(self):
        mouse.locked=False
        self.resumeGame.enabled = True
        self.quitGame.enabled = True
        self.background.enabled = True
        self.text1.enabled = True
        self.inMenu = True
        destroy(player.cursor)
        application.pause()
        
    def killMenu(self):
        application.resume()
        player.cursor = Entity(parent=camera.ui, model='quad', color=color.pink, scale=.008, rotation_z=45)
        self.resumeGame.enabled = False
        self.background.enabled = False
        self.text1.enabled = False
        mouse.locked = True
        self.quitGame.enabled = False
        self.inMenu = False
          
    def input(self,key):
        if key=='escape':
            if not self.inMenu:
                self.createMenu()

class playerControls(Entity):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.isDashing = False
        self.SkillTimer = 0
        self.parent=player
        
    def update(self):
        if self.isDashing and self.SkillTimer <= .5:
            player.position += player.forward * .3
            self.SkillTimer += time.dt
            if self.SkillTimer <= .25:
                camera.fov += 1
        if self.isDashing and self.SkillTimer >= .5:
            self.stopPlayerDash()
        if self.isDashing and self.SkillTimer >= .25:
            camera.fov -= 1

    def input(self, key):
        if key=='shift' and not self.isDashing:
            self.playerDash()


    def playerDash(self):
        self.isDashing = True
        
    def stopPlayerDash(self):
        self.isDashing = False
        self.SkillTimer = 0


def scene1():
    pass
    

GROUND=Entity(model='plane',scale_x=1000,scale_z=1000,collider='box',texture='grass',texture_scale=[31,31])
player=FirstPersonController()
menu=MenuScreen()
controls=playerControls()
line=Entity(model='cube',scale_x=1000,color=color.red)
block=Entity(model='cube',scale=[1,1],color=color.blue,z=2)
app.run()