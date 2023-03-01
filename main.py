import tkinter as tk
import os

# 定义GUI的宽度和高度
gui_width = 180
gui_height = 80

# 定义GUI的背景颜色和文本颜色
gui_color = "#FFFFFF"
gui_text_color = "#000000"

# 定义GUI的标题和按钮文本
gui_title = "Floating Button"
prev_button_text = "<"
next_button_text = "          >          "
go_button_text = "Go"

# 获取脚本所在目录的路径
script_dir = os.path.dirname(os.path.abspath(__file__))

# 创建GUI窗口
root = tk.Tk()
root.title(gui_title)
root.configure(bg=gui_color)
root.attributes("-topmost", True)
root.geometry(f"{gui_width}x{gui_height}+{root.winfo_screenwidth() - gui_width}+0")

# 创建按钮和文本
line_counter = -1
total_lines = 0
lines = []

def update_label():
    label_text = f"{line_counter + 1}/{total_lines}"
    label.config(text=label_text)

def on_button_click(offset):
    global line_counter

    # 计算下一行或上一行的索引
    next_line = (line_counter + offset) % total_lines

    # 更新行计数器并复制到剪贴板
    line_counter = next_line
    next_line_text = lines[line_counter].strip()
    root.clipboard_clear()
    root.clipboard_append(next_line_text)

    # 更新文本标签
    update_label()

def on_go_button_click():
    global line_counter
    new_line_number = int(textbox.get())

    if 1 <= new_line_number <= total_lines:
        line_counter = new_line_number - 1
        next_line_text = lines[line_counter].strip()
        root.clipboard_clear()
        root.clipboard_append(next_line_text)

        update_label()

go_button_frame = tk.Frame(root, bg=gui_color)
go_button_frame.pack(side="bottom", fill="y")

textbox = tk.Entry(go_button_frame)
textbox.pack(side="left")

go_button = tk.Button(go_button_frame, text=go_button_text, command=on_go_button_click, bg=gui_color, fg=gui_text_color)
go_button.pack(side="left")

button_frame = tk.Frame(root, bg=gui_color)
button_frame.pack(side="top", fill="x")

prev_button = tk.Button(button_frame, text=prev_button_text, command=lambda: on_button_click(-1), bg=gui_color, fg=gui_text_color)
prev_button.pack(side="left", expand=True)

next_button = tk.Button(button_frame, text=next_button_text, command=lambda: on_button_click(1), bg=gui_color, fg=gui_text_color)
next_button.pack(side="left", expand=True)

label_frame = tk.Frame(root, bg=gui_color)
label_frame.pack(side="top", fill="x")

label = tk.Label(label_frame, text="0/0", bg=gui_color, fg=gui_text_color)
label.pack(expand=True)

# 读取文本文件的内容
text_file_path = os.path.join(script_dir, "list.txt")
with open(text_file_path, "r") as f:
    lines = f.readlines()
total_lines = len(lines)

# 获取文本框中的值
update_label()

# 进入事件循环
root.mainloop()
