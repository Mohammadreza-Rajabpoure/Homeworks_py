class MyError(Exception):

    def __init__(self, id: int, msg='id must be 5 digit'):
                
                self.id = id
                self.msg = msg
                super().__init__(self.msg)
    
    def __repr__(self) -> str:
          return self.__class__.__name__()