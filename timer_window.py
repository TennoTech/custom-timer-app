import tkinter as tk


class Window:
    def __init__(self):
        root = tk.Tk()
        root.overrideredirect(True)
        # root.title("Always on Top")
        # y_pos = root.winfo_screenwidth() - 500
        root.geometry(f"300x400")
        root.attributes("-topmost", True)

        #! Add a label to demonstrate
        label = tk.Label(root, text="Test Text", padx=20, pady=20)
        label.pack()

        #! Add a button to close the window
        close_button = tk.Button(root, text="Close", command=root.destroy)
        close_button.pack()

        #! Start the event loop
        root.mainloop()


Window()
