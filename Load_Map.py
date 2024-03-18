import customtkinter
from PIL import Image

class Load_Map(customtkinter.CTkToplevel):
    def __init__(self, image_path):
        self.image_path = image_path
        super().__init__()
        self.title(f"Battlefield Map Viewer")
        self.geometry("1920x1080")

        self.open_image(self.image_path)

    def open_image(self, image_path):
        image = Image.open(image_path)
        image = customtkinter.CTkImage(dark_image=image, size=image.size)
        image_label = customtkinter.CTkLabel(self, image=image, text="")
        image_label.pack(fill="both", expand=True)
