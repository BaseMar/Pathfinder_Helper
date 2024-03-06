from customtkinter import filedialog
import os
from customtkinter import END
from pygame import mixer


class MusicController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_music(self):
        path = filedialog.askdirectory()
        if path:
            os.chdir(path)
            songs = os.listdir(path)
            for song in songs:
                if song.endswith(".mp3") and song not in self.view.music_listbox.get("all"):
                    self.view.music_listbox.insert(END, song)

    def play_music(self, music_name):
        self.model.is_playing = True
        mixer.music.load(self.view.music_listbox.get())
        mixer.music.play()
        self.view.pause_music_button.configure(image=self.model.pause_button)

    def pause_music(self):
        if self.model.is_playing:
            self.model.is_playing = False
            mixer.music.pause()
            self.view.pause_music_button.configure(image=self.model.play_button)
        else:
            self.model.is_playing = True
            mixer.music.unpause()
            self.view.pause_music_button.configure(image=self.model.pause_button)

    def next_music(self):
        try:
            if self.view.music_listbox.curselection() == self.view.music_listbox.size()-1:
                self.view.music_listbox.activate(0)
            else:
                self.view.music_listbox.activate(self.view.music_listbox.curselection() + 1)
        except TypeError:
            pass

    def previous_music(self):
        try:
            if self.view.music_listbox.curselection() == 0:
                self.view.music_listbox.activate(self.view.music_listbox.size()-1)
            else:
                self.view.music_listbox.activate(self.view.music_listbox.curselection() - 1)
        except TypeError:
            pass
