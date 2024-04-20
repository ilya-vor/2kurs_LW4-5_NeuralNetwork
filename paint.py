import tkinter as tk
from tkinter import Canvas, Button
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance


class DrawingApp:
    def __init__(self, master, canvas_width=280, canvas_height=280, save_resolution=(28, 28)):
        self.draw = None
        self.image = None
        self.master = master
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.save_resolution = save_resolution

        self.canvas = Canvas(master, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        self.button_save = Button(master, text="Save", command=self.save_image)
        self.button_save.pack()

        self.setup()

    def setup(self):
        self.canvas.bind("<B1-Motion>", self.draw_event)
        self.image = Image.new("L", (self.save_resolution[0], self.save_resolution[1]), color="white")
        self.draw = ImageDraw.Draw(self.image)

    def draw_event(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.canvas.create_oval(x1, y1, x2, y2, fill="black", outline="black", width=7)
        # Масштабируем координаты для рисования на холсте размером 28x28, сохраняя изображение в 28x28
        scaled_x = round(event.x * self.save_resolution[0] / self.canvas_width)
        scaled_y = round(event.y * self.save_resolution[1] / self.canvas_height)
        self.draw.point([scaled_x, scaled_y], fill="black")

    def save_image(self):
        filename = "drawing.png"
        # Масштабируем изображение до разрешения 28x28 перед сохранением
        resized_image = self.image.resize(self.save_resolution)
        # Применяем эффект размытия с меньшим радиусом
        blurred_image = resized_image.filter(ImageFilter.GaussianBlur(radius=1))
        enhancer = ImageEnhance.Contrast(blurred_image)
        contrast_image = enhancer.enhance(5.0)
        contrast_image.save('drawing.png')
        print(f"Image saved as {filename}")
        self.master.quit()  # Закрыть приложение


def main():
    root = tk.Tk()
    root.title("Drawing App")
    DrawingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
