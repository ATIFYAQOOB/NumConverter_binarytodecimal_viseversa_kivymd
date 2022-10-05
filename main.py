from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '700')

from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar

class ConverterApp(MDApp):
    def flip(self):
        if self.state ==0:
            self.state =1
            self.toolbar.title = "Decimal to Binary"
            self.input.hint_text = "Enter the Decimal number"
            self.converted.text = ""
            self.label.text = ""
        else:
            self.state =0
            self.toolbar.title = "Binary to Decimal"
            self.input.hint_text = "Enter the Binary number"
            self.converted.text = ""
            self.label.text = ""
    def convert(self, *args):
        try:
            if "." not in self.input.text:
                if self.state == 0:
                    val = int(self.input.text,2)
                    self.converted.text = str(val)
                    self.label.text = "In the Decimal is"
                else:
                    val = bin(int(self.input.text))[2:]
                    self.converted.text = str(val)
                    self.label.text = "In the Binary is"
            else:
                whole , fract = self.input.text.split(".")
                if self.state == 0:
                    whole = int(whole,2)
                    floating = 0
                    for indx,digit in enumerate(fract):
                        floating += int(digit)*2**(-(indx+1))
                    self.converted.text = str(whole + floating)
                    self.label.text = "In the Decimal is"
                else:
                    decimal_places = 10
                    whole = bin(int(whole))[2:]
                    fract = float("0." + fract)
                    floating =[]
                    for i in range(decimal_places):
                        if fract*2 < 1:
                            floating.append("0")
                            fract*=2
                        elif fract*2 >1:
                            floating.append("1")
                            fract*=2
                        elif fract*2 ==1:
                            floating.append("1")
                            break
                    self.converted.text = whole+"."+ "".join(floating)
                    self.label.text = "In the Binary is"
        except ValueError:
            self.converted.text = ""
            if self.state  ==0:
                self.label.text = "Please Enter the valid Binary number"
            else:
                self.label.text = "Please Enter the valid Decimal number"
        
    def build(self):
        self.state = 0
        self.theme_cls.primary_palette = "Blue"
        screen = MDScreen()
        self.toolbar = MDToolbar(title = "Binary to Decimal")
        self.toolbar.pos_hint = {"top":1}
        self.toolbar.right_action_items = [["rotate-3d-variant" , lambda x: self.flip()]]
        screen.add_widget(self.toolbar)
        screen.add_widget(Image(
            source = "logo.png",
            pos_hint = {"center_x": 0.5, "center_y": 0.7},
            size_hint = (1,1)))
        self.input = MDTextField(
            hint_text = "Enter the binary number",
            halign  = "center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y": 0.5},
            font_size = "24dp",
        )
        screen.add_widget(self.input)
        self.label = MDLabel(
            
            halign  = "center",
            pos_hint = {"center_x": 0.5, "center_y": 0.35},
            theme_text_color = "Secondary"
        )
        self.converted = MDLabel(
            
            halign  = "center",
            pos_hint = {"center_x": 0.5, "center_y": 0.3},
            theme_text_color = "Primary" , 
            font_style = "H5"
        )
        screen.add_widget(self.label)
        screen.add_widget(self.converted)
        screen.add_widget(MDFillRoundFlatButton(
            text = "CONVERT",
            font_size = "17dp",
            pos_hint = {"center_x": 0.5, "center_y": 0.15},
            size_hint = (0.3,0.1),
            on_press = self.convert
            ))
        return screen
if __name__ == '__main__':
    ConverterApp().run()