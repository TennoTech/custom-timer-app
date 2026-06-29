import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from tool_tip import DynamicToolTip


class MainWindow:
    timer_value = 0

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
        #TODO -- make where it can auto grab value when onclicked
        val = self.user_input.get()
        if val.isdigit() and int(val) > 0:
            #! calculate time || hour/minute/seconds
            self.timer_value = int(val)
        else:
            print("Error: Please enter numbers only!")
            self.input_validator_tip.show_error("Error: Please enter numbers only!")

    def on_click(self):
        #! Placeholder logic for now
        #! ### adjust screen size for main window
        # self.root.geometry(
        #     f"{int(self.root.winfo_width()/2)}x{int(self.root.winfo_width()/2)}"
        # )
        #! ### auto minimize main window
        self.root.update_idletasks()
        self.root.iconify()

        #! ### open new window with timer number on it
        TimerWindow(self.timer_value)
        # print("Exiting Program")
        # self.root.destroy()


class TimerWindow:
    def __init__(self, time_remaining):
        self.root = ttkb.Window(themename="darkly")
        self.time_remaining = time_remaining
        self.window_width, self.window_height = 500, 400

        self._setup_window()
        self._create_widgets()
        self.convert_seconds()

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
        self.timer_label = ttkb.Label(
            self.root,
            bootstyle="info",
            text=self.time_remaining,
            font=("Arial", 16),
        )
        self.timer_label.pack(pady=(10, 0))

    def convert_seconds(self):
        total = self.time_remaining
        hours, remainder = divmod(total, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
