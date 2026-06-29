from PIL import Image

Image.CUBIC = Image.BICUBIC

import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from tool_tip import DynamicToolTip


class TimerWindow:
    def __init__(self):
        self.root = ttkb.Window(themename="darkly")
        self.window_width, self.window_height = 500, 400

        self._setup_window()
        self._create_widgets()

        self.root.update_idletasks()
        self.root.mainloop()

    def _setup_window(self):
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        x = int((screenwidth - self.window_width) / 2)
        y = int((screenheight - self.window_height) / 2) - 100

        self.root.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")
        self.root.attributes("-topmost", True)
        # self.root.overrideredirect(True)

    def _create_widgets(self):
        #!########## Title ###########
        ttkb.Label(
            self.root, bootstyle="info", text="Set Timer", font=("Arial", 16)
        ).pack(pady=(10, 0))

        #!########## Separator ###########
        ttkb.Separator(self.root, bootstyle="info", orient=HORIZONTAL).pack(
            fill="x", pady=(5, 0), padx=20
        )

        #!########## Input ###########
        self.user_input = ttkb.Entry(self.root, bootstyle="dark")
        self.user_input.pack(pady=(25, 0))
        self.input_validator_tip = DynamicToolTip(ttkb, self.user_input)
        self.user_input.bind("<Return>", self.on_submit)

        #!########## Action Button ###########
        ttkb.Button(
            self.root,
            bootstyle="success",
            text="Ready",
            padding=5,
            command=self.on_click,
        ).pack(pady=10)

    def on_submit(self, event=None):
        val = self.user_input.get()
        if val.isdigit():
            #! calculate time || hour/minute/seconds
            print(f"Success! Timer set to: {val}")
        else:
            print("Error: Please enter numbers only!")
            self.input_validator_tip.show_error("Error: Please enter numbers only!")

    def on_click(self):
        #! Placeholder logic for now
        print("Exiting Program")
        self.root.destroy()


window = TimerWindow()
