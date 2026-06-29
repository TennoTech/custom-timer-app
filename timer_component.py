from PIL import Image

Image.CUBIC = Image.BICUBIC

import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from tool_tip import DynamicToolTip

root = ttkb.Window()
# root.overrideredirect(True)
# root.title("Always on Top")
window_width, window_height = 500, 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2) - 100
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.attributes("-topmost", True)

percentage = 100


def on_submit(event=None):
    if user_input.get().isdigit():
        timer_text = user_input.get()
        print(f"Success! Timer set to: {timer_text}")
        input_validator_tip.hide_error()  # Clean up any existing error
    else:
        # Instantly fires the tooltip right below the invalid input field
        input_validator_tip.show_error("Please enter numbers only!")


#! ############# Main Text #############
main_text = ttkb.Label(
    root,
    bootstyle="info",
    text="Set Timer",
)
main_text.pack(anchor="n", pady=(10, 0))

#! ############# Separator #############
separator = ttkb.Separator(
    root,
    bootstyle="info",
    orient=HORIZONTAL,
)
separator.pack(fill="x", anchor="n", pady=(5, 0), padx=20)

# from tkinter import messagebox

#! ############# Button #############
user_input = ttkb.Entry(
    root,
    bootstyle="dark",
)
user_input.pack(pady=(25, 0))
user_input.bind("<Return>", on_submit)
input_validator_tip = DynamicToolTip(user_input)

#! ############# Button #############
button = ttkb.Button(
    root,
    bootstyle="success",
    text="Ready",
    padding=5,
)
# button.pack()

# meter = ttkb.Meter(
#     metersize=200,  # Size of the meter
#     padding=20,  # distance between window edges
#     meterthickness=5,  # thickness of the meter dial
#     stripethickness=5,  # thickness of discrete stripes,0=Continous
#     bootstyle="info",  # allows you to apply pre-defined styles like primary,danger,success etc
#     metertype="semi",  # Semicircle ,"full" =circular
#     amounttotal=100,  # max value of scale =100
#     amountused=percentage,  # current value
#     subtext="Timer",
#     subtextstyle="info",  # allows you to apply pre-defined styles like primary,danger,success etc
#     subtextfont="-size 10 -weight bold",
#     interactive=False,  # you can change meter position by mouse
# )

# meter.pack()

# update_meter()

root.mainloop()
