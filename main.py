from kivymd.app import MDApp
from kivy.lang import Builder
from kivy import Config
Config.set('graphics', 'multisamples', '0')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'width', '600')
Config.write()

class Myapp(MDApp):
    def __init__(self, **kwargs):
        super(Myapp, self).__init__(**kwargs)

    def build(self):
        self.screen = Builder.load_file('sign-up.kv')
        return self.screen
        


def main():
    Myapp().run()


if __name__ == '__main__':
    main()