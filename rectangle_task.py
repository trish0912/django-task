class Rectangle:
    def __init__(self,length:int, width:int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}


rectangle_one = Rectangle(100,80)

for item in rectangle_one:
    print(item)