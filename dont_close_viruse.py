import tkinter as tk

def disable_event():
    pass

root = tk.Tk()
root.overrideredirect(False)  # Show window decorations (minimize, close, restore icons)
root.protocol("WM_DELETE_WINDOW", disable_event)  # Disable close button

# track whether minimize is allowed
root._allow_minimize = False

def on_unmap(event):
    if getattr(root, "_allow_minimize", False):
        # allowed; reset flag and let window stay minimized
        root._allow_minimize = False
    else:
        # prevent minimize by re-showing the window
        root.deiconify()

root.bind("<Unmap>", on_unmap)  # Prevent minimize except when allowed
root.bind("<FocusOut>", lambda e: root.focus_force())  # Force focus back to window
root.title("Don't Close or Minimize")
root.attributes('-fullscreen', True)

def minimize_with_f6(event=None):
    # allow minimize temporarily
    root._allow_minimize = True
    # exit fullscreen before iconifying on some platforms
    try:
        root.attributes('-fullscreen', False)
    except tk.TclError:
        pass
    root.iconify()

root.bind("<F6>", minimize_with_f6)

root.mainloop()