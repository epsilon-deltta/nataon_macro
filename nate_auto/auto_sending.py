from pywinauto.application import Application
import pywinauto
import sys ,os
class send_auto():
    def __init__(self,path):
        # self.path      = path
        path = os.path.abspath(path)
        self.file_name = os.path.basename(path)
        self.dir_path  = os.path.dirname (path)

        self.pid       =  self.get_nate_pid()
        self.name      =  "성다빈"
        self.chat_name =  self.name + "님 메시지"
        self.chat_name = "내게 쓰기" # for developing
        self.msg_area  =  "RICHEDIT50W2"
        self.file_exp_n = "열기"

        self.app       = Application(backend='win32').connect(process=self.pid)
        self.chat_dial = self.app[self.chat_name]

    def get_nate_pid(self):
        procs = pywinauto.findwindows.find_elements()
        for proc in procs :
            print(type(proc))
            print(proc.name)
            if 'nate' in proc.name.lower() :
                nate_pid = proc.process_id
                break
        return nate_pid
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