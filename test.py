# main.py
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from main import MenuScreen  # Assuming MenuScreen is in screens.py


class DemoApp(MDApp):
    def build(self):
        self.sm = ScreenManager()

        # Add the MenuScreen instance to the ScreenManager
        menu_screen = MenuScreen(name="menu")
        self.sm.add_widget(menu_screen)

        return self.sm

    def call_menu_function(self):
        # Access MenuScreen and call a function on it
        menu_screen = self.sm.get_screen("menu")
        menu_screen.some_function()


# Run the app
if __name__ == "__main__":
    DemoApp().run()
