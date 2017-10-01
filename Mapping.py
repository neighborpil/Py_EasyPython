class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable) # __update 메소드를 사용하고 있다

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update #private copy of original update() method
                      #이를 통하여 자식 클래스에서 update메소드를 재정의 하더라도
                      # 기존의 __update메소드를 사용할 수 있
