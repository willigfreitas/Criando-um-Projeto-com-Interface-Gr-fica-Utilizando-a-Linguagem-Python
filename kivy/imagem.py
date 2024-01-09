from kivy.app import App
from kivy.uix.image import AsyncImage

class MainApp(App):
    def build(self):
            # link que funciona
        #link_imagem = 'https://cdn.pixabay.com/photo/2017/02/20/18/03/cat-2083492_960_720.jpg'
        # link que funciona - imagem muito bonita!
        link_imagem = 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_960_720.jpg'
        # link que funciona
        #link_imagem = 'https://cdn.pixabay.com/photo/2017/09/25/13/12/dog-2785074_960_720.jpg'



        img = AsyncImage(
            source=link_imagem,
            size_hint=(1, .5),
            pos_hint={'center_x': .5, 'center_y': .5}
        )
        return img

if __name__ == '__main__':
    app = MainApp()
    app.run()
