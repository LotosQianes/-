import os
import tkinter as tk
from tkinter import filedialog, messagebox

def find_files_with_string(directory, search_string):
    found_files = []
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.py'):
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                for line_num, line in enumerate(lines, 1):
                    if search_string in line:
                        found_files.append((file_path, line_num))
    return found_files

def search_files():
    directory = directory_entry.get()
    search_string = search_entry.get()
    
    if not os.path.isdir(directory):
        messagebox.showerror("错误", "无效的目录！")
        return
    
    if not search_string:
        messagebox.showerror("错误", "请输入搜索字符串！")
        return

    found_files = find_files_with_string(directory, search_string)
    if found_files:
        result_text.config(state='normal')
        result_text.delete(1.0, tk.END)
        for file_path, line_num in found_files:
            result_text.insert(tk.END, f"{file_path} - 第 {line_num} 行\n")
        result_text.config(state='disabled')
    else:
        result_text.config(state='normal')
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "未找到包含搜索字符串的文件。")
        result_text.config(state='disabled')

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        directory_entry.delete(0, tk.END)
        directory_entry.insert(tk.END, directory)

# 创建主窗口
root = tk.Tk()
root.title("Python文件搜索")

# 设置窗口最小尺寸
root.minsize(500, 300)

# 添加输入框和按钮
directory_label = tk.Label(root, text="目录:")
directory_label.grid(row=0, column=0, padx=5, pady=5)
directory_entry = tk.Entry(root, width=50)
directory_entry.grid(row=0, column=1, padx=5, pady=5, columnspan=2)
browse_button = tk.Button(root, text="浏览", command=browse_directory)
browse_button.grid(row=0, column=3, padx=5, pady=5)

search_label = tk.Label(root, text="搜索字符串:")
search_label.grid(row=1, column=0, padx=5, pady=5)
search_entry = tk.Entry(root, width=50)
search_entry.grid(row=1, column=1, padx=5, pady=5, columnspan=2)

search_button = tk.Button(root, text="搜索", command=search_files)
search_button.grid(row=1, column=3, padx=5, pady=5)

# 添加搜索结果显示区域
result_label = tk.Label(root, text="搜索结果:")
result_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

result_text = tk.Text(root, width=70, height=20, wrap=tk.WORD)
result_text.grid(row=3, column=0, padx=5, pady=5, columnspan=4)
result_text.config(state='disabled')

# 运行主循环
root.mainloop()
