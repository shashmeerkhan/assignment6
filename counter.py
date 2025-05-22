class Counter:
    count=0
    def __init__(self):
        Counter.count+=1
    @classmethod
    def display_count(cls):
        print(f"Total Count {cls.count}")
a=Counter()
Counter.display_count()