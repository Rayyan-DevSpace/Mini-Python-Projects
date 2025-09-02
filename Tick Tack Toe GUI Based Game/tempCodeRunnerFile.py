buttons = [tk.Button(root, text = "", font = ("normal", 25), width = 6, height = 2, command = lambda i=i: button_click(i)) for i in range(9)]
for i, button in enumerate(buttons):
     button.grid(row = i // 3, column = i % 3)
