class DynamicToolTip:
    def __init__(self, ttkb, widget):
        self.ttkb = ttkb
        self.widget = widget
        self.tip_window = None

    def show_error(self, text):
        # Prevent duplicate windows if already showing
        self.hide_error()

        # Calculate positioning below the specific entry box
        x = self.widget.winfo_rootx()
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 5

        self.tip_window = tw = self.ttkb.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")

        # Styled as an error alert (Red text/border)
        label = self.ttkb.Label(
            tw,
            text=text,
            background="#ffcccc",
            foreground="#cc0000",
            borderwidth=1,
            font=("Arial", "9", "bold"),
        )
        label.pack(ipadx=6, ipady=3)

        # Automatically hide the error after 3 seconds
        self.widget.after(3000, self.hide_error)

    def hide_error(self):
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None
