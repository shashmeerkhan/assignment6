class Logger:
    def __init__(self):
        print("Logger object is created")
    def __del__(self):
        print("Logger is destroyed")
l1=Logger()
del l1