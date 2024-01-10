from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        button = Button(text='Me pressione!')
        button.bind(on_press=self.on_press_button)
        return button

    def on_press_button(self, instance):
        print('Você apertou o botão!')

if __name__ == '__main__':
    app = ButtonApp()
    app.run()
