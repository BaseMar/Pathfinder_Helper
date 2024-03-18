import customtkinter

class Player(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        self.player_list = []
        self.button_list = []

    def add_item(self, item):
        label = customtkinter.CTkLabel(self, text=item, padx=5, anchor="w")
        button = customtkinter.CTkButton(self, text="Remove", width=100, height=24)
        if self.command is not None:
            button.configure(command=lambda: self.command(item))
        label.grid(row=len(self.player_list), column=0, pady=(0, 10), sticky="w")
        button.grid(row=len(self.button_list), column=1, pady=(0, 10), padx=5)
        self.player_list.append(label)
        self.button_list.append(button)

    def remove_item(self, item):
        for label, button in zip(self.player_list, self.button_list):
            if item == label.cget("text"):
                label.destroy()
                button.destroy()
                self.player_list.remove(label)
                self.button_list.remove(button)
                return
