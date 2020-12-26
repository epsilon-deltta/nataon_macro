from pywinauto.application import Application
import pywinauto
import sys ,os
class send_auto():
    def __init__(self,path):
        # self.path      = path
        self.file_name = os.path.basename(path)
        self.dir_path  = os.path.dirname (path)

        self.pid       =  4664
        self.name      =  "이미향"
        self.chat_name =  self.name + "님 메시지"
        self.msg_area  =  "RICHEDIT50W2"
        self.file_exp_n = "열기"

        self.app       = Application(backend='win32').connect(process=self.pid)
        self.chat_dial = self.app[self.chat_name]

    def start(self):
        self.chat_dial.type_keys("^t")
        
        file_exp = self.app[self.file_exp_n]
        file_exp.type_keys('^l '+self.dir_path+'{ENTER}')
        file_exp.Edi1.type_keys(self.file_name+'{ENTER}')



if __name__ == "__main__" :
    path = sys.argv[0]
    macro = send_auto(path)
    for _ in range(1):
        macro.start()