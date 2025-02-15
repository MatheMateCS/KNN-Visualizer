import tkinter as tk
from tkinter import colorchooser


w_width, w_height = 400, 400


class KNNDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("KNN Visualiser")

        self.color = "black"

        self.canvas = tk.Canvas(root, bg="white", width=w_width, height=w_height)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Button-1>", self.mark_pixel)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(fill=tk.X)

        self.color_button = tk.Button(self.button_frame, text="Choose Color", command=self.choose_color)
        self.color_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.clear_button = tk.Button(self.button_frame, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT, padx=5, pady=5)

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.color = color

    def mark_pixel(self, event):
        self.canvas.create_line(event.x, event.y, event.x + 1, event.y, fill=self.color)

    def clear_canvas(self):
        self.canvas.delete("all")


if __name__ == "__main__":
    root = tk.Tk()
    app = KNNDrawer(root)
    root.mainloop()
