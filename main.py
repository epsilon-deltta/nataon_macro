from nate_auto.auto_sending import send_auto as sm
import sys
if __name__ == "__main__":
    path = sys.argv[1]
    
    macro = sm(path)
    macro.start()