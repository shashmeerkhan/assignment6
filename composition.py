class Engine:
    def start(self):
        print("engine is starting")
class Car:
    def __init__(self,engine):
        self.engine=engine
    def start_engine(self):
            self.engine.start()
print(Engine.start)
print(Car.start_engine)
