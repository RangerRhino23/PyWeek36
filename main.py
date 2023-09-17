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
        
    def createMenu(self):
        mouse.locked=False
        self.background = Entity(parent=camera.ui,scale=[2,2],texture='bg.mp4',ignore_paused=True,model='quad')
        self.text1 = Text(text='Paused',x=-.12,y=.4,scale=3,font=font)
        self.resumeGame = Button(text='Resume Game',scale_y=.075,scale_x=.2,y=0,x=-.65,color=color.rgba(27, 18, 18, 100),highlight_color=color.rgba(27, 18, 18, 100),highlight_scale=1.1,pressed_scale=0.9,ignore_paused=True)
        self.resumeGame.on_click = self.killMenu()
        self.inMenu = not self.inMenu
        destroy(player.cursor)
        application.pause()
        
    def killMenu(self):
        application.resume()
        player.cursor = Entity(parent=camera.ui, model='quad', color=color.pink, scale=.008, rotation_z=45)
        mouse.locked=True
        destroy(self.text1)
        destroy(self.resumeGame)
        destroy(self.background)
        self.inMenu = not self.inMenu
          
    def input(self,key):
        if key=='escape':
            if not self.inMenu:
                self.createMenu()
            
def scene1():
    pass
    

GROUND=Entity(model='plane',scale_x=1000,scale_z=1000,collider='box',texture='grass',texture_scale=[31,31])
player=FirstPersonController()
MenuScreen()      

app.run()