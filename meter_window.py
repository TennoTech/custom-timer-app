import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from PIL import Image

Image.CUBIC = Image.BICUBIC


class TimerWindow:
    def __init__(self, parent_window, time_remaining):
        self.root = parent_window
        self.time_remaining = time_remaining
        self.total_duration = time_remaining
        self.window_width, self.window_height = 500, 400

        self._setup_window()
        self._create_widgets()
        self._convert_seconds()

        self.update_meter()
        # self.root.update_idletasks()

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
            text="",
            font=("Arial", 16),
        )
        self.timer_label.pack(pady=(10, 0))

        #!########## Progress Bar ###########
        self.progress_bar = ttkb.Progressbar(
            self.root, bootstyle="info", value=0, maximum=100
        )
        self.progress_bar.pack()

    def _convert_seconds(self):
        total = self.time_remaining
        hours, remainder = divmod(total, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")

    def update_meter(self):
        total = self.time_remaining
        hours, remainder = divmod(total, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")

        if self.total_duration > 0:
            # * Calculate how many seconds have already passed
            time_elapsed = self.total_duration - total

            # * Map time_elapsed to the 0-100 range
            progress_percentage = (time_elapsed / self.total_duration) * 100
        else:
            progress_percentage = 100

        self.progress_bar["value"] = progress_percentage

        if self.time_remaining > 0:
            self.time_remaining -= 1
            #* runs every 1 sec
            self.root.after(1000, self.update_meter)
        else:
            self.timer_label.config(text="Time's Up!", bootstyle="danger")
