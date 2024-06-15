

import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox,simpledialog
import os
import tkinter.font
import tkinter.colorchooser
import tkinter.filedialog
import tkinter.messagebox
import os
import tkinter.font
from datetime import datetime
def zoom_in():
    pass

def zoom_out():
    pass

def restore_default_zoom():
    pass
main_application = tk.Tk()
main_application.geometry("800x600")
main_application.title("AK Notepad")

main_menu = tk.Menu()
#  File menu
file = tk.Menu(main_menu,tearoff= False)
main_menu.add_cascade(label="File",menu=file)

# New Tab
text_url = " "
def new_file(event = None):
    global text_url
    text_url =" "
    text_editor.delete(1.0,tk.END)
file.add_command(label="New tab",compound=tk.LEFT,accelerator="Ctrl+N",command=new_file)

# Open file

def open_file(event = None):
    global text_url
    text_url = filedialog.askopenfilename(initialdir= os.getcwd(), title = "select file", filetypes=    (("text file","*.txt"),("All files","*_*")))
    try:
        with open(text_url,"r") as for_read:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,for_read.read())
    except FileNotFoundError:
        return        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while opening the file: {e}")
    main_application.title(os.path.basename(text_url))
file.add_command(label="Open",compound=tk.LEFT,accelerator="Ctrl+O",command=open_file)


# Save file 
def save_file():
    global text_url
    try:
        if text_url:
            content = str(text_editor.get(1.0, tk.END))
            with open(text_url, "w",encoding="utf-8") as file:
                file.write(content)
        else:
            text_url = filedialog.asksaveasfilename(mode ="w",defaultextension="txt",filetypes= (("text file","*.txt"),("All files","*_*")))
            content2 = text_editor.get(1.0,tk.END)
            text_url.write(content2)
            text_url.close()
    except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the file: {e}")        
file.add_command(label="Save",compound=tk.LEFT,accelerator="Ctrl+S",command=save_file)

# Save as file
def save_as_file():
    global text_url
    try:
        content = text_editor.get(1.0, tk.END)
        text_url = filedialog.asksaveasfile(mode="w", defaultextension=".txt",
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        text_url.write(content)
        text_url.close()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the file: {e}")

file.add_command(label="Save as",compound=tk.LEFT,accelerator="Ctrl+Shift+S",command=save_as_file)
file.add_separator()
#  Close tab function
def close_tab():
    text_editor.delete(1.0,tk.END)
    main_application.title("Ak Notepad")
file.add_command(label="Close tab",compound=tk.LEFT,accelerator="Ctrl+W",command=close_tab)
# Close Window function
def close_window():
    main_application.destroy()

file.add_command(label="Close window",compound=tk.LEFT,accelerator="Ctrl+Shift+W",command=close_window)
# Exit Function
def exit_application():
    if messagebox.askyesno("Exit AK Notepad", "Are you sure you want to exit?"):
        main_application.destroy()

file.add_command(label="Exit",compound=tk.LEFT,command=exit_application)

# Edit menu

edit = tk.Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="Edit",menu=edit)
edit.add_separator()

# Undo Function
def undo_action():
    text_editor.event_generate("<<Undo>>")
edit.add_cascade(label="Undo",compound=tk.LEFT,accelerator="Ctrl+Z",command=undo_action)
edit.add_separator()
# Cut Function
def cut_action():
    text_editor.event_generate("<<Cut>>")

edit.add_cascade(label="Cut",compound=tk.LEFT,accelerator="Ctrl+X",command=cut_action)
# Copy Function
def copy_action():
    text_editor.event_generate("<<Copy>>")
edit.add_cascade(label="Copy",compound=tk.LEFT,accelerator="Ctrl+C",command=copy_action)
# Paste Function
def paste_action():
    text_editor.event_generate("<<Paste>>")

edit.add_cascade(label="Paste",compound=tk.LEFT,accelerator="Ctrl+V",command=paste_action)
# Delete Function
def delete_action():
    text_editor.delete(tk.SEL_FIRST, tk.SEL_LAST)

edit.add_cascade(label="Delete",compound=tk.LEFT,accelerator="Del",command=delete_action)
edit.add_separator()
# Find Text Function
def find_action():
    def find_text():
        text_to_find = find_entry.get()
        if text_to_find:
            start_index = text_editor.search(text_to_find, "1.0", tk.END, nocase=True)
            if start_index:
                end_index = f"{start_index}+{len(text_to_find)}c"
                text_editor.tag_remove("found", "1.0", tk.END)
                text_editor.tag_add("found", start_index, end_index)
                text_editor.mark_set("insert", start_index)
                text_editor.see("insert")
                text_editor.focus_set()
            else:
                messagebox.showinfo("Find", f"Couldn't find '{text_to_find}'.")
        else:
            messagebox.showwarning("Find", "Please enter text to find.")

    find_dialog = tk.Toplevel(main_application)
    find_dialog.title("Find")
    find_dialog.geometry("300x100")

    find_label = ttk.Label(find_dialog, text="Find:")
    find_label.pack(pady=5)

    find_entry = ttk.Entry(find_dialog, width=30)
    find_entry.pack(pady=5)

    find_button = ttk.Button(find_dialog, text="Find", command=find_text)
    find_button.pack(pady=5)

    find_dialog.mainloop()

edit.add_cascade(label="Find text",compound=tk.LEFT,accelerator="Ctrl+F3",command=find_action)
# Replace Function
def replace_action():
    def find_text():
        text_to_find = find_entry.get()
        if text_to_find:
            start_index = text_editor.search(text_to_find, "1.0", tk.END, nocase=True)
            if start_index:
                end_index = f"{start_index}+{len(text_to_find)}c"
                text_editor.tag_remove("found", "1.0", tk.END)
                text_editor.tag_add("found", start_index, end_index)
                text_editor.mark_set("insert", start_index)
                text_editor.see("insert")
                text_editor.focus_set()
            else:
                messagebox.showinfo("Find", f"Couldn't find '{text_to_find}'.")
        else:
            messagebox.showwarning("Find", "Please enter text to find.")

    def replace_text():
        text_to_find = find_entry.get()
        replacement_text = replace_entry.get()
        if text_to_find and replacement_text:
            start_index = text_editor.search(text_to_find, "1.0", tk.END, nocase=True)
            if start_index:
                end_index = f"{start_index}+{len(text_to_find)}c"
                text_editor.delete(start_index, end_index)
                text_editor.insert(start_index, replacement_text)
                find_text()
            else:
                messagebox.showinfo("Replace", f"Couldn't find '{text_to_find}'.")
        else:
            messagebox.showwarning("Replace", "Please enter both text to find and replacement text.")

    replace_dialog = tk.Toplevel(main_application)
    replace_dialog.title("Replace")
    replace_dialog.geometry("300x150")

    find_label = ttk.Label(replace_dialog, text="Find:")
    find_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    find_entry = ttk.Entry(replace_dialog, width=30)
    find_entry.grid(row=0, column=1, padx=5, pady=5)

    replace_label = ttk.Label(replace_dialog, text="Replace with:")
    replace_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    replace_entry = ttk.Entry(replace_dialog, width=30)
    replace_entry.grid(row=1, column=1, padx=5, pady=5)

    replace_button = ttk.Button(replace_dialog, text="Replace", command=replace_text)
    replace_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    replace_dialog.mainloop()

edit.add_cascade(label="Replace",compound=tk.LEFT,accelerator="Ctrl+H",command=replace_action)
# Go to Function
def go_to_action():
    def go_to_line():
        line_number = line_entry.get()
        if line_number.isdigit():
            line_index = f"{line_number}.0"
            text_editor.mark_set("insert", line_index)
            text_editor.see("insert")
            text_editor.focus_set()
            go_to_dialog.destroy()
        else:
            messagebox.showwarning("Go To", "Please enter a valid line number.")

    go_to_dialog = tk.Toplevel(main_application)
    go_to_dialog.title("Go To")
    go_to_dialog.geometry("250x100")

    line_label = ttk.Label(go_to_dialog, text="Line Number:")
    line_label.grid(row=0, column=0, padx=5, pady=5)

    line_entry = ttk.Entry(go_to_dialog, width=10)
    line_entry.grid(row=0, column=1, padx=5, pady=5)

    go_to_button = ttk.Button(go_to_dialog, text="Go To", command=go_to_line)
    go_to_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    go_to_dialog.mainloop()

edit.add_cascade(label="Go to",compound=tk.LEFT,accelerator="Ctrl+G",command=go_to_action)
edit.add_separator()
# Select All Function
def select_all_action():
    text_editor.tag_add("sel", "1.0", "end")
    return "break"

edit.add_cascade(label="Select all",compound=tk.LEFT,accelerator="Ctrl+A",command=select_all_action)
# Time/Date Function
def insert_time_date():
    now = datetime.now()
    current_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    text_editor.insert(tk.INSERT, current_date_time)
edit.add_cascade(label="Time/Date",compound=tk.LEFT,accelerator="F5",command=delete_action)
edit.add_separator()

# Font Function 
def open_font_dialog():
    def apply_font():
        family = family_var.get()
        size = size_var.get()
        text_editor.config(font=(family, size))
        font_dialog.destroy()

    font_dialog = tk.Toplevel(main_application)
    font_dialog.title("Select Font")

    family_var = tk.StringVar()
    size_var = tk.IntVar(value=12)

    font_label = ttk.Label(font_dialog, text="Font Family:")
    font_label.grid(row=0, column=0, padx=10, pady=5)

    family_box = ttk.Combobox(font_dialog, textvariable=family_var, values=tkinter.font.families())
    family_box.grid(row=0, column=1, padx=10, pady=5)

    size_label = ttk.Label(font_dialog, text="Font Size:")
    size_label.grid(row=1, column=0, padx=10, pady=5)

    size_entry = ttk.Entry(font_dialog, textvariable=size_var)
    size_entry.grid(row=1, column=1, padx=10, pady=5)

    apply_button = ttk.Button(font_dialog, text="Apply", command=apply_font)
    apply_button.grid(row=2, columnspan=2, padx=10, pady=5)
edit.add_command(label="Font", compound=tk.LEFT, accelerator="Ctrl+Z", command=open_font_dialog)

# View menu
view =  tk.Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="View",menu=view)
zoom_menu = tk.Menu(view, tearoff=False)
view.add_cascade(label="Zoom", menu=zoom_menu)

# Zoom in Function
def zoom_in():
    current_font = text_editor["font"]
    font_info = tkinter.font.Font(font=current_font)
    new_size = font_info.actual()["size"] + 2
    text_editor.config(font=(font_info.actual()["family"], new_size))
zoom_menu.add_command(label="Zoom In", compound=tk.LEFT, command=zoom_in,accelerator="Ctrl+plus")

# Zoom out Function
def zoom_out():
    current_font = text_editor["font"]
    font_info = tkinter.font.Font(font=current_font)
    new_size = max(font_info.actual()["size"] - 2, 1)  # Ensure font size doesn't become negative
    text_editor.config(font=(font_info.actual()["family"], new_size))
zoom_menu.add_command(label="Zoom Out", compound=tk.LEFT, command=zoom_out,accelerator="Ctrl+minus")

# Restore Default Zoom Function
DEFAULT_FONT_SIZE = 12

def restore_default_zoom():
    text_editor.config(font=(font_now, DEFAULT_FONT_SIZE))
zoom_menu.add_command(label="Restore Default Zoom", compound=tk.LEFT, command=restore_default_zoom,accelerator="Ctrl+0")
# Status bar Fuction 
def update_status_bar(event=None):
    character_count = len(text_editor.get("1.0", "end-1c"))
    word_count = len(text_editor.get("1.0", "end-1c").split())
    status_bars.config(text=f"Character Count: {character_count}   Word Count: {word_count}")

# Create Text Editor
text_editor = tk.Text(main_application)
text_editor.config(wrap="word", relief=tk.FLAT)

# Bind events to update status bar
text_editor.bind("<KeyRelease>", update_status_bar)
text_editor.bind("<ButtonRelease>", update_status_bar)

view.add_checkbutton(label="Status bar",onvalue=True,offvalue=0,compound=tk.LEFT,command=update_status_bar)
# # Word Wrap function
# def toggle_word_wrap():
#     if word_wrap_var.get():
#         text_editor.config(wrap="word")
#     else:
#         text_editor.config(wrap="none")

# # Create a Checkbutton for word wrap
# word_wrap_var = tk.BooleanVar()
# word_wrap_var.set(True)  # Set default value to True (word wrap enabled by default)
# word_wrap_checkbutton = ttk.Checkbutton(main_application, text="Word Wrap", variable=word_wrap_var, command=toggle_word_wrap)
# word_wrap_checkbutton.pack(side=tk.RIGHT)

# view.add_checkbutton(label="Word wrab",onvalue=True,offvalue=0,compound=tk.LEFT,command=toggle_word_wrap)

# Colour theme
color_theme = tk.Menu(main_menu,tearoff=False)
# main_menu.add_cascade(label="Color Theme",menu=color_theme)

color_dict = {
    'Light Default': ("#000000","#ffffff"),
    'Light Plus' : ("#474747","#e0e0e0"),
    'Dark' : ("#c4c4c4","#2d2d2d"),
    'Red' : ("#ff0000","#ff0000"),
    'Monokai' : ("#d3b774","#474747"),
    'Night Blue' : ("#ededed","#6b9dc2"),
    'Blue' : ("#0000ff","#0000ff"),
    'Purple' : ("#800080","#800080")
}
def change_color_theme(theme_name):
    selected_theme = color_dict[theme_name]
    text_editor.config(bg=selected_theme[0], fg=selected_theme[1])

# Create Color Theme menu
color_theme_menu = tk.Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="Color Theme", menu=color_theme_menu)

# Add color themes to the menu
for theme in color_dict:
    color_theme_menu.add_command(label=theme, command=lambda t=theme: change_color_theme(t))


# Font style
tool_bar_label = ttk.Label(main_application)
tool_bar_label.pack(side=tk.TOP,fill=tk.X)

font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box =  ttk.Combobox(tool_bar_label,width=30, textvariable= font_family,state= "readonly")
font_box["values"] = font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row= 0,column=0,padx=5,pady=5)

# Font size
size_variable = tk.IntVar()
font_size = ttk.Combobox(tool_bar_label,width=20,textvariable=  size_variable,state= "readonly")
font_size["values"] = tuple(range(8,100,2))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5,pady=5)

# bold button
# bold_icon = tk.PhotoImage(file= "Ak Notepad/R.png")
bold_btn = ttk.Button(tool_bar_label,text="B",width=3)
bold_btn.grid(row=0,column=2,padx=5)

def toggle_bold():
    current_font = text_editor["font"]
    font_info = tkinter.font.Font(font=current_font)
    if "bold" in font_info.actual()["weight"]:
        new_font = font_info.actual()["family"], font_info.actual()["size"]
    else:
        new_font = font_info.actual()["family"], font_info.actual()["size"], "bold"
    text_editor.configure(font=new_font)

bold_btn.config(command=toggle_bold)


# Italic Button
italic_btn = ttk.Button(tool_bar_label,text="I",width=3)
italic_btn.grid(row=0,column=3,padx=5)

def toggle_italic():
    current_font = text_editor["font"]
    font_info = tkinter.font.Font(font=current_font)
    if "italic" in font_info.actual()["slant"]:
        new_font = font_info.actual()["family"], font_info.actual()["size"]
    else:
        new_font = font_info.actual()["family"], font_info.actual()["size"], "italic"
    text_editor.configure(font=new_font)

italic_btn.config(command=toggle_italic)

# Underline Button
underline_btn = ttk.Button(tool_bar_label,text="U",width=3)
underline_btn.grid(row=0,column=4,padx=5)

def toggle_underline():
    current_font = text_editor["font"]
    font_info = tkinter.font.Font(font=current_font)
    if "underline" in font_info.actual()["weight"]:
        new_font = font_info.actual()["family"], font_info.actual()["size"]
    else:
        new_font = font_info.actual()["family"], font_info.actual()["size"], "underline"
    text_editor.configure(font=new_font)

underline_btn.config(command=toggle_underline)

# font color Button
font_color_btn = ttk.Button(tool_bar_label,text="FontColor")
font_color_btn.grid(row=0,column=5,padx=5,pady=5)

def color_choose():
    color_var = tk.colorchooser.askcolor()
    text_editor.config(fg=color_var[1])

font_color_btn.config(command=color_choose)

# Align left
align_btn = ttk.Button(tool_bar_label,text="AlignLeft")
align_btn.grid(row=0,column=6,padx=5)

def align_left():
    text_get_all = text_editor.get(1.0,"end")
    text_editor.tag_config("left",justify= tk.LEFT)
    text_editor.delete(1.0,tk.END )
    text_editor.insert(tk.INSERT,text_get_all,"left")
align_btn.config(command=align_left)
# Align Center
align_center_btn = ttk.Button(tool_bar_label,text="AlignCenter")
align_center_btn.grid(row=0,column=7,padx=5)

def align_center():
    text_get_all = text_editor.get(1.0,"end")
    text_editor.tag_config("center",justify= tk.CENTER)
    text_editor.delete(1.0,tk.END )
    text_editor.insert(tk.INSERT,text_get_all,"center")
align_center_btn.config(command=align_center)
# Align Right
align_right_btn = ttk.Button(tool_bar_label,text="AlignRight")
align_right_btn.grid(row=0,column=8,padx=5)

def align_right():
    text_get_all = text_editor.get(1.0,"end")
    text_editor.tag_config("right",justify= tk.RIGHT)
    text_editor.delete(1.0,tk.END )
    text_editor.insert(tk.INSERT,text_get_all,"right")
align_right_btn.config(command=align_right)

# Text Editor 
text_editor = tk.Text(main_application)
text_editor.config(wrap="word",relief=tk.FLAT)

# scroll bar
scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill= tk.Y)
text_editor.pack(fill= tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# font family and function 
font_now = "Arial"
font_size_now = 16

def change_font(main_application):
    global font_now
    font_now = font_family.get()
    text_editor.config(font = (font_now,font_size_now))
def change_size(main_application):
    global font_size_now
    font_size_now = size_variable.get()
    text_editor.config(font=(font_now,font_size_now))
    
font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_size)


# status bar word and character count

status_bars = ttk.Label(main_application,text="Status bar")
status_bars.pack(side=tk.BOTTOM)

text_change = False

def change_word(event= None):
    global text_change
    if text_editor.edit_modified():
        text_change= True
        word = len(text_editor.get(1.0,"end-1c").split())
        character = len(text_editor.get(1.0,"end-1c".replace(" ","")))
        status_bars.config(text = f"character :{character} word : {word}")
    text_editor.edit_modified(False)
text_editor.bind("<<Modified>>",change_word)

count = 0 
for i in color_dict:
    color_theme.add_radiobutton(label= i,compound=tk.LEFT)
    count+=1



main_application.config(menu=main_menu)  

main_application.mainloop()