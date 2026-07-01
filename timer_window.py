import ttkbootstrap as ttkb
from ttkbootstrap.constants import *


class TimerWindow:
    def __init__(self, parent_window, time_remaining):
        self.root = parent_window
        self.time_remaining = time_remaining
        self.total_duration = time_remaining
        self.window_width, self.window_height = 150, 100

        self._setup_window()
        self._create_widgets()

        self._update_meter()

    def _setup_window(self):
        x = int(self.root.winfo_screenwidth() / 2)
        y = int(self.root.winfo_screenheight() / 2) - self.window_height

        self.root.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")
        self.root.attributes("-topmost", True)
        self.root.overrideredirect(True)

    def _create_widgets(self):
        #!########## Top Frame ###########
        self.title_bar = ttkb.Frame(self.root, bootstyle="primary")
        self.title_bar.pack(fill=X, side=TOP)

        #!########## Exit Button ###########
        style = ttkb.Style()
        style.configure(
            "TinyClose.danger-outline.TButton",
            font=("Helvetica", 7),
            padding=(2, 0),
        )
        self.close_btn = ttkb.Button(
            self.title_bar,
            text="✖",
            style="TinyClose.danger-outline.TButton",
            command=self.root.destroy,
            width=2,
        )
        self.close_btn.pack(side=RIGHT, padx=0, pady=0)

        #!########## Binding Functions ###########
        self.root.bind("<ButtonPress-1>", self._start_drag)
        self.root.bind("<B1-Motion>", self._drag_window)

        #!########## Timer Text ###########
        self.timer_label = ttkb.Label(
            self.root,
            bootstyle="info",
            text="",
            font=("Arial", 16),
        )
        self.timer_label.pack(pady=(10, 0))

        #!########## Progress Bar ###########
        self.progress_bar = ttkb.Progressbar(
            self.root, bootstyle="info", value=0, maximum=100
        )
        self.progress_bar.pack()

    def _start_drag(self, event):
        # Record the mouse position relative to the title bar
        self.x_offset = event.x
        # Use winfo_y() to include title bar offset if it sits below anything else
        self.y_offset = event.y

    def _drag_window(self, event):
        # 1. Calculate the intended new position
        new_loc_x = self.root.winfo_x() + (event.x - self.x_offset)
        new_loc_y = self.root.winfo_y() + (event.y - self.y_offset)

        win_width = self.root.winfo_width()
        win_height = self.root.winfo_height()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        #! clamp window to screen dimensions
        if new_loc_x < 0:
            new_loc_x = 0
        elif new_loc_x > (screen_width - win_width):
            new_loc_x = screen_width - win_width

        if new_loc_y < 0:
            new_loc_y = 0
        elif new_loc_y > (screen_height - win_height):
            new_loc_y = screen_height - win_height

        self.root.geometry(f"+{new_loc_x}+{new_loc_y}")

    def _update_meter(self):
        total = self.time_remaining
        hours, remainder = divmod(total, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")

        if self.total_duration > 0:
            # * calculating how many seconds have passed from original time
            time_elapsed = self.total_duration - total

            # * mapping time from 0 - 100
            normalized_percentage = (time_elapsed / self.total_duration) * 100
            # * reversing to --> 100 - 0
            current_percentage = 100 - normalized_percentage
        else:
            current_percentage = 0

        self.progress_bar["value"] = current_percentage

        if self.time_remaining > 0:
            self.time_remaining -= 1
            # * runs every 1 sec
            self.root.after(1000, self._update_meter)
        else:
            self.timer_label.config(text="Time's Up!", bootstyle="danger")
            # self.root.destroy()
