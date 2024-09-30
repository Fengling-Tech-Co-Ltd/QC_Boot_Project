import serial
import tkinter as tk
from threading import Thread
from ttkbootstrap import Style  # 导入ttkbootstrap样式库以使用现代主题

class SerialReader(Thread):
    def __init__(self, port, baudrate, text_widget):
        super().__init__()  # 初始化父类
        self.ser = serial.Serial(port, baudrate, timeout=1)  # 打开串口
        self.text_widget = text_widget  # 保存文本框引用
        self.running = True  # 控制线程运行的标志

    def run(self):
        """线程运行的方法，不断读取串口数据并显示在文本框中"""
        while self.running:
            if self.ser.in_waiting > 0:  # 如果有数据可读
                data = self.ser.readline().decode('utf-8').strip()  # 读取一行数据并解码
                self.text_widget.insert(tk.END, data + '\n')  # 在文本框中插入数据
                self.text_widget.see(tk.END)  # 滚动到最后一行

    def stop(self):
        """停止线程运行并关闭串口"""
        self.running = False  # 设置运行标志为False
        self.ser.close()  # 关闭串口

def on_closing():
    """处理窗口关闭事件"""
    reader.stop()  # 停止串口读取线程
    root.destroy()  # 销毁主窗口

port = 'COM6'  # 替换为你的串口名称
baudrate = 115200  # 设置波特率

# 创建ttkbootstrap样式
style = Style(theme='darkly')  # 选择'darkly'主题以改变界面风格

# 创建图形界面主窗口
root = style.master  # 使用ttkbootstrap的主窗口
root.title("串口数据接收")  # 设置窗口标题

# 创建一个文本框用于显示接收到的数据
text_widget = tk.Text(root, bg='black', fg='white', wrap=tk.WORD)  # 设置文本框背景为黑色，字体颜色为白色
text_widget.pack(expand=True, fill='both')  # 文本框扩展以填充整个窗口

# 创建串口读取线程
reader = SerialReader(port, baudrate, text_widget)  # 实例化串口读取线程
reader.start()  # 启动线程

# 处理窗口关闭事件
root.protocol("WM_DELETE_WINDOW", on_closing)  # 绑定窗口关闭事件到自定义函数
root.mainloop()  # 进入Tkinter主事件循环
