from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.tab import MDTabsBase
from kivy.uix.floatlayout import FloatLayout

from kivy.core.audio import SoundLoader

from kivymd.uix.snackbar import Snackbar

from kivymd.icon_definitions import md_icons



#######################################MAIN_CLASS#########################

class Tab(FloatLayout,MDTabsBase):
    pass            
    
    


class BasketMDApp(MDApp):
    music = SoundLoader.load('Tetris.wav')
    music.loop = True
    numes = [1,2,3,4,5]
    names = ["v","f", "m","c","s"]
    p = 0
    def build(self):
        
        return Builder.load_file('tabmd.kv')

   
        
###########################MUSIC######################################
    def musicon(self, instance):
        #self.music = SoundLoader.load('Tetris.wav')
        #self.music.loop = True
        self.music.play()
        pass

    def musicoff(self, instance):
        self.music.stop()
        pass
###################################CALLBACK_PROGRESS_BAR#########################
    def vegetables_label_text(self):
        if self.root.ids.progress.value >= 0 and self.root.ids.progress.value <= 20 :
            
            self.snackbar = Snackbar(text="НИЩЕБРОД!")
            self.snackbar.open()
            self.root.ids.progress.color = (1,0,0,1)
        elif self.root.ids.progress.value > 20 and self.root.ids.progress.value <= 40:
            
            self.root.ids.progress.color = (1,1,0,1)
            self.snackbar = Snackbar(text="Братишка , я тебе покушать принёс!")
            self.snackbar.open()
        elif self.root.ids.progress.value > 40 and self.root.ids.progress.value <= 60:
            
            self.root.ids.progress.color = (0,0,1,1)
            self.snackbar = Snackbar(text="С голодными сравнялись!")
            self.snackbar.open()
        elif self.root.ids.progress.value > 60 and self.root.ids.progress.value <= 80:
            
            self.root.ids.progress.color = (0,1,1,1)
            self.snackbar = Snackbar(text="Завязался жирок!")
            self.snackbar.open()
        elif self.root.ids.progress.value > 80 :
            
            self.root.ids.progress.color = (0,1,0,1)
            self.snackbar = Snackbar(text="АЛИГАРХ!")
            self.snackbar.open()
        
#################################CALLBACK_CHECKBOXES#################################
    def checkbox_click(self, instance, value,number,name):
        
        
        if value:
            if self.p == 100:
                self.p = 0
            self.p += 20
            self.root.ids.progress.value = self.p
            self.vegetables_label_text()
            update=str(name)+str(number)
            self.root.ids[update].text= "КУПЛЕНО!"
            #print(self.root.ids[update].text)
            
        else:
            #if self.p == 100:
                #self.p = 0
            self.p = self.p - 20
            self.root.ids.progress.value = self.p
            self.vegetables_label_text()
            update=str(name)+str(number)
            self.root.ids[update].text= ""
            


    

##############################ENTRY_POINT########################################
if __name__ == '__main__':
    
    BasketMDApp().run()
