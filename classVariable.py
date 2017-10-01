class Account:
    num_accounts = 0 # 클래스 변수
    def __init__(self, name):
        self.name = name #멤버변수
        Account.num_accounts += 1

    def __del__(self):
        Account.num_accounts -= 1

        
