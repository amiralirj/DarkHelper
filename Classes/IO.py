import base64

class IO:
    def __init__(self , Text=None , Chat_id=None , kind=None ) -> None:
        if Chat_id:
            self.code=base64.b64encode((f'{Chat_id}||||{Text}||||{kind}'.encode('utf-8')))
            self.chat_id=int(Chat_id)
            self.kind=kind
        else:
            try:
                x=((base64.b64decode(Text)).decode()).split('||||')
                self.chat_id=int(x[0])
                self.code=str(x[1])
                self.kind=str(x[2])
            except:print(f'\n\n\n{Text}\n')
        print(self.code)

    def __str__(self) -> str:
        try:
            print((self.code).decode('utf-8'))
            return (self.code).decode()
        except AttributeError:
            print(self.code)
            return self.code
            
    def __int__(self) -> str:
        return self.chat_id
