import tkinter as tk
from tkinter import ttk


# 创建主窗口
root = tk.Tk()
root.title("检测结果显示")
root.geometry("650x420")  # 设置窗口大小

# 定义全局样式

bg_color = "lightgray"          #背景色
no_recognition_color = "gray"   #未识别
pass_color = "green"            #通过
fail_color = "red"              #异常
pending_color = "yellow"        #待确认

# 创建左侧PCB和右侧PCB Frame
frame_left = tk.Frame(root, bg=bg_color, bd=2, relief="groove")
frame_right = tk.Frame(root, bg=bg_color, bd=2, relief="groove")
frame_bottom = tk.Frame(root, bg=bg_color, bd=2, relief="groove")

frame_left.grid(row=0, column=0, sticky="nsew")   # 左侧PCB区域
frame_right.grid(row=0, column=1, sticky="nsew")  # 右侧PCB区域
frame_bottom.grid(row=1, column=0, columnspan=2, pady=2, sticky="nsew")  # 底部统计区域

# 左侧PCB布局
tk.Label(frame_left, text="左侧PCB", font=("Arial", 16), bg=bg_color).grid(row=0, column=0, columnspan=4,rowspan=2,sticky='w')

# 固定标签
tk.Label(frame_left, text="在位功能", bg=bg_color).grid(row=3, column=0, padx=5, pady=5,sticky='w')
tk.Label(frame_left, text="射频功能", bg=bg_color).grid(row=3, column=2, padx=5, pady=5,sticky='w')
tk.Label(frame_left, text="气压功能", bg=bg_color).grid(row=4, column=0, padx=5, pady=5,sticky='w')
tk.Label(frame_left, text="MOS功能", bg=bg_color).grid(row=4, column=2, padx=5, pady=5,sticky='w')
tk.Label(frame_left, text="蜂鸣器功能", bg=bg_color).grid(row=5, column=0, padx=5, pady=5,sticky='w')
tk.Label(frame_left, text="电源功能", bg=bg_color).grid(row=5, column=2, padx=5, pady=5,sticky='w')
tk.Label(frame_left, text="充电功能", bg=bg_color).grid(row=6, column=0, padx=5, pady=5,sticky='w')
tk.Label(frame_left, text="NTC功能", bg=bg_color).grid(row=6, column=2, padx=5, pady=5,sticky='w')


# 状态标签
state_width = 8
tk.Label(frame_left, text="未识别", bg=no_recognition_color,width=state_width).grid(row=2, column=0, padx=5, pady=(10,10),sticky='e')      #检测
tk.Label(frame_left, text="未配对", bg=no_recognition_color,width=state_width).grid(row=2, column=1, padx=5, pady=(10,10),sticky='w')      #配对
tk.Label(frame_left, text="未写入", bg=no_recognition_color,width=state_width).grid(row=2, column=2, padx=5, pady=(10,10),sticky='w')      #写入

tk.Label(frame_left, text="待确认", bg=pending_color,width=state_width).grid(row=3, column=1, padx=5, pady=10)
tk.Label(frame_left, text="待确认", bg=pending_color,width=state_width).grid(row=3, column=3, padx=5, pady=10)
tk.Label(frame_left, text="待确认", bg=pending_color,width=state_width).grid(row=4, column=1, padx=5, pady=10)
tk.Label(frame_left, text="待确认", bg=pending_color,width=state_width).grid(row=4, column=3, padx=5, pady=10)
tk.Label(frame_left, text="待确认", bg=pending_color,width=state_width).grid(row=5, column=1, padx=5, pady=10)
tk.Label(frame_left, text="待确认", bg=pending_color,width=state_width).grid(row=5, column=3, padx=5, pady=10)
tk.Label(frame_left, text="待确认", bg=pending_color,width=state_width).grid(row=6, column=1, padx=5, pady=10)
tk.Label(frame_left, text="待确认", bg=pending_color,width=state_width).grid(row=6, column=3, padx=5, pady=10)

tk.Label(frame_left, text="待确认", bg=pending_color,font=("Arial", 32)).grid(row=7, column=0, padx=5, pady=5,columnspan=4,rowspan=3, sticky="nsew")

# 添加其他功能类似的控件...

# 右侧PCB布局
tk.Label(frame_right, text="右侧PCB", font=("Arial", 16), bg=bg_color).grid(row=0, column=0, columnspan=4, rowspan=2, sticky='w')

# 功能描述标签
tk.Label(frame_right, text="在位功能", bg=bg_color).grid(row=3, column=0, padx=5, pady=5, sticky='w')
tk.Label(frame_right, text="射频功能", bg=bg_color).grid(row=3, column=2, padx=5, pady=5, sticky='w')
tk.Label(frame_right, text="气压功能", bg=bg_color).grid(row=4, column=0, padx=5, pady=5, sticky='w')
tk.Label(frame_right, text="MOS功能", bg=bg_color).grid(row=4, column=2, padx=5, pady=5, sticky='w')
tk.Label(frame_right, text="蜂鸣器功能", bg=bg_color).grid(row=5, column=0, padx=5, pady=5, sticky='w')
tk.Label(frame_right, text="电源功能", bg=bg_color).grid(row=5, column=2, padx=5, pady=5, sticky='w')
tk.Label(frame_right, text="充电功能", bg=bg_color).grid(row=6, column=0, padx=5, pady=5, sticky='w')
tk.Label(frame_right, text="NTC功能", bg=bg_color).grid(row=6, column=2, padx=5, pady=5, sticky='w')

# 状态标签
tk.Label(frame_right, text="检测到", bg=pass_color,width=state_width).grid(row=2, column=0, padx=5, pady=10, sticky='e')     # 检测
tk.Label(frame_right, text="已配对", bg=pass_color,width=state_width).grid(row=2, column=1, padx=5, pady=10, sticky='w')     # 配对
tk.Label(frame_right, text="已写入", bg=pass_color,width=state_width).grid(row=2, column=2, padx=5, pady=10, sticky='w')     # 写入

tk.Label(frame_right, text="待确认", bg=pending_color,width=state_width).grid(row=3, column=1, padx=5, pady=10)
tk.Label(frame_right, text="待确认", bg=pending_color,width=state_width).grid(row=3, column=3, padx=5, pady=10)
tk.Label(frame_right, text="待确认", bg=pending_color,width=state_width).grid(row=4, column=1, padx=5, pady=10)
tk.Label(frame_right, text="待确认", bg=pending_color,width=state_width).grid(row=4, column=3, padx=5, pady=10)
tk.Label(frame_right, text="待确认", bg=pending_color,width=state_width).grid(row=5, column=1, padx=5, pady=10)
tk.Label(frame_right, text="待确认", bg=pending_color,width=state_width).grid(row=5, column=3, padx=5, pady=10)
tk.Label(frame_right, text="待确认", bg=pending_color,width=state_width).grid(row=6, column=1, padx=5, pady=10)
tk.Label(frame_right, text="待确认", bg=pending_color,width=state_width).grid(row=6, column=3, padx=5, pady=10)

tk.Label(frame_right, text="待确认", bg=pass_color, font=("Arial", 32)).grid(row=7, column=0, padx=5, pady=5, columnspan=4, rowspan=3, sticky="nsew")


# 添加其他功能类似的控件...

# 底部统计信息
state_width = 10
tk.Label(frame_bottom, text="质检通过计数",  width=state_width,font=("Arial", 14), bg=bg_color).grid(row=0, column=0, padx=20, pady=10)
tk.Label(frame_bottom, text="2000", font=("Arial", 16),width=state_width, bg=bg_color).grid(row=0, column=1, padx=20, pady=10)

tk.Label(frame_bottom, text="质检失败计数", font=("Arial", 14),width=state_width, bg=bg_color).grid(row=0, column=2, padx=20, pady=10)
tk.Label(frame_bottom, text="1", font=("Arial", 16), width=state_width,bg=bg_color, fg=fail_color).grid(row=0, column=3, padx=20, pady=10)

tk.Label(frame_bottom, text="通讯端口", font=("Arial", 14),width=state_width, bg=bg_color).grid(row=1, column=0, padx=20, pady=10)
tk.Label(frame_bottom, text="COM8", font=("Arial", 16),width=state_width, bg=bg_color).grid(row=1, column=1, padx=20, pady=10)

tk.Label(frame_bottom, text="标定气压", font=("Arial", 14),width=state_width, bg=bg_color).grid(row=1, column=2, padx=20, pady=10)
tk.Label(frame_bottom, text="40.3kPa", font=("Arial", 16),width=state_width, bg=bg_color).grid(row=1, column=3, padx=20, pady=10)

# 启动主循环
root.mainloop()
