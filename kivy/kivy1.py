from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        # Cria um rótulo (Label) com texto 'Fala galera!' e ajusta o tamanho e a posição
        label = Label(text='Fala galera!', size_hint=(.5, .5), pos_hint={'center_x': .5, 'center_y': .5})
        return label

if __name__ == '__main__':
    # Cria uma instância da classe MainApp e inicia a aplicação
    app = MainApp()
    app.run()
