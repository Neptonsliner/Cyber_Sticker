import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import simpledialog
from PIL import Image, ImageDraw, ImageTk

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TODO")
        self.root.geometry("500x200")
        self.root.overrideredirect(True)  # 彻底移除标题栏 [[5]][[8]]
        self.root.configure(background="#FDF5E6")  # 主背景色
        
        style = ttk.Style()
        style.configure("Custom.TButton", background="#FDF5E6", foreground="black")  # 设置背景色和文字颜色
        style.map("Custom.TButton",
                 background=[("active", "#FDF5E6"),  # 悬停/按下时保持背景色
                             ("pressed", "#FDF5E6")])
        
        # 标题栏
        self.title_bar = ttk.Frame(self.root)
        self.title_bar.pack(fill="x")
        
        # 标题栏内容
        self.title_label = ttk.Label(self.title_bar, text="TODO", font=("Segoe UI", 10, "bold"))
        self.title_label.pack(side="left", padx=5, pady=2)
        
        # 关闭按钮（使用自定义样式）
        self.close_btn = ttk.Button(self.title_bar, text="×", style="Custom.TButton",
                                   command=self.root.destroy)
        self.close_btn.pack(side="right", padx=2, pady=2)
        
        # 置顶按钮（使用自定义样式）
        self.toggle_btn = ttk.Button(self.title_bar, text="置顶", style="Custom.TButton",
                                    command=self.toggle_topmost)
        self.toggle_btn.pack(side="right", padx=5)
        
        # 行容器
        self.rows_container = ttk.Frame(self.root)
        self.rows_container.pack(fill="both", expand=True, padx=10, pady=10)
        
        # 控制按钮区域
        self.control_frame = ttk.Frame(self.root)
        self.control_frame.pack(fill="x", padx=10, pady=5)
        
        # 添加行按钮（使用自定义样式）
        self.add_btn = ttk.Button(self.title_bar, text="添加行", style="Custom.TButton",
                                 command=self.add_row)
        self.add_btn.pack(side="right", padx=5)
        
        # 拖动支持
        self.title_bar.bind("<ButtonPress-1>", self.start_move)
        self.title_bar.bind("<B1-Motion>", self.on_move)
        
        # 全局样式配置
        style = ttk.Style()
        style.configure("TFrame", background="#FDF5E6")
        style.configure("TLabel", background="#FDF5E6")

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def on_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")

    def toggle_topmost(self):
        current = self.root.attributes("-topmost")
        self.root.attributes("-topmost", not current)
        self.toggle_btn.config(text="取消置顶" if not current else "置顶")
    
    def add_row(self):
        input_value = simpledialog.askstring(
            title="添加内容",
            prompt="请输入内容：",
            parent=self.root
        )
        if not input_value:
            return
        
        row_frame = ttk.Frame(self.rows_container, style="TFrame")
        row_frame.pack(fill="x", pady=2)
        
        number_label = ttk.Label(row_frame, text="·",
                                font=("Segoe UI", 10, "bold"), foreground="#333333")
        number_label.pack(side="left", padx=5)
        
        content_label = ttk.Label(row_frame, text=input_value, width=30)
        content_label.pack(side="left", padx=5)
        
        delete_btn = ttk.Button(row_frame, text="×", style="Custom.TButton2",
                               command=lambda f=row_frame: row_frame.destroy())
        delete_btn.pack(side="right", padx=5)

if __name__ == "__main__":
    app = ttk.Window(themename="cosmo")
    main_app = MainApp(app)
    app.mainloop()
