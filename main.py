import pyglet
from pyglet.window import key
from pyglet.graphics import *

import stt.converter
import tts.converter
import weather.weather

class app_window(pyglet.window.Window):
    def __init__(self):
        super().__init__()  # self, game_window
        self.set_caption("PyHelper")
        self.set_size(500, 500)
        self.set_minimum_size(500, 500)
        self.set_maximum_size(500, 500)
        self.main_batch = pyglet.graphics.Batch()
        self.circle = pyglet.shapes.Circle(x=250, y=250, radius=50, color=(255, 0, 0), batch=self.main_batch)

    def on_draw(self):
        self.clear()
        self.main_batch.draw()

    def on_key_press(self, symbol, modifiers):
        # print(symbol) # use for finding id of button
        if symbol == key.SPACE:
            self.circle.color = (249, 151, 4)
            stt.converter.record()
            self.circle.color = (0, 100, 255)
            text = stt.converter.conv_online()
            self.circle.color = (0, 255, 0)
            for i in text.split(" "):
                if i == "weather":
                    forecast = weather.weather.get_weather()
                    to_speak = "The tempurature today is " + str(forecast[0]) + " degrees, with the weather being " + str(forecast[1])
                    tts.converter.save_speech(to_speak)
                    speech = pyglet.media.load('tts/speech/speech.mp3', streaming=False)
                    speech.play()
                    self.circle.color = (255, 0, 0)
                    break



app_window_run = app_window()  # width = screenresx, height=screenresy

pyglet.app.run()  # kek or cringe