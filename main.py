from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

#  checkboxs
class BoxBuild(BoxLayout):
    select_values = []
    p_values = StringProperty()

    def process_checkbox(self, widget, state, value):
        if state == 'down':
            self.select_values.append(value)
            self.p_values = ','.join(self.select_values)
        else:
            self.select_values.remove(value)
            self.p_values = ','.join(self.select_values)


class MainApp(App):
    pass


MainApp().run()
