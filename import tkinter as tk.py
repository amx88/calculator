import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("calculator")

        self.entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid", justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), 
        ]

        for (text, row, col) in buttons:
            if text == '=':
                tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=self.calculate).grid(row=row, column=col)
            elif text == 'C':
                tk.Button(root, text=text, width=22, height=2, font=('Arial', 18), command=self.clear).grid(row=row, column=col, columnspan=4)
            else:
                tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda t=text: self.on_click(t)).grid(row=row, column=col)

    def on_click(self, char):
        self.entry.insert(tk.END, char)

    def clear(self):
        self.entry.delete(0, tk.END)

    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "שגיאה")

# הפעלת התוכנית
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
