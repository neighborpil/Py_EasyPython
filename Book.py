class Book(object):
    """ 책 클래스
    이 클래스는 책 정보 저장
    """

    def __init__(self, title, author):
        """ 초기화
        |name| 매개변수를 받아서 객체 멤버 변수 name에 저장한다
        """
        self.title = title
        self.author = author
        self.borrowed = False

    def borrow(self):
        """ 책을 대여한다
        책을 대여한다. 멤버 변수 borrowed 변수에
        현재 상태를 기록한다
        """
        self.borrow = True

    def takeBack(self):
        """ 책을 반납한다
        """
        self.borrow = False

    def printInfo(self):
        log = []
        log.append("Book:")
        log.append(" - title : {}".format(self.title))
        log.append(" - author : {}".format(self.author))
        log.append(" - borrowed : {}".format(self.borrowed))
        print('\n'.join(log))

