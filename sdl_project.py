import tkinter as tk

class Whiteboard:
    def _init_(self, root):
        self.root = root
        self.root.title("Whiteboard")

        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.toolbar = tk.Frame(root)
        self.toolbar.pack(pady=10)

        self.colors = ["black", "red", "blue", "green"]

        for color in self.colors:
            button = tk.Button(self.toolbar, bg=color, width=5, command=lambda c=color: self.change_color(c))
            button.pack(side=tk.LEFT, padx=5)

        erase_button = tk.Button(self.toolbar, text="Eraser", command=self.erase)
        erase_button.pack(side=tk.LEFT, padx=5)

        self.drawing = False
        self.eraser = False
        self.current_color = "black"

        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

    def change_color(self, color):
        self.eraser = False
        self.current_color = color

    def erase(self):
        self.eraser = True
        self.current_color = "white"

    def start_drawing(self, event):
        self.drawing = True
        self.draw(event)

    def stop_drawing(self, event):
        self.drawing = False
        self.canvas.create_line(event.x, event.y, event.x, event.y)

    def draw(self, event):
        if self.drawing:
            line_width = 20 if self.eraser else 5
            self.canvas.create_line(
                event.x, event.y, event.x + 1, event.y + 1,
                width=line_width, fill=self.current_color
            )

if __name__ == "_main_":
    root = tk.Tk()
    whiteboard = Whiteboard(root)
    whiteboard.canvas.bind("<Button-1>", whiteboard.start_drawing)
    root.mainloop()