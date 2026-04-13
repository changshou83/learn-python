# 组合示例：电脑包含 CPU 和 Screen
class CPU:
    def run(self):
        return "CPU 运行中"

class Screen:
    def show(self):
        return "屏幕显示内容"

# 组合：电脑包含 CPU 和 Screen
class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.screen = Screen()

    def work(self):
        print(self.cpu.run())
        print(self.screen.show())

# 使用
pc = Computer()
pc.work()
