from utils import req
import sys

def main():
    if len(sys.argv) < 3:
        print("参数过少")
        return
    username = sys.argv[1]
    password = sys.argv[2]
    req.login({
        "username":username,
        "password":password,
        "acid":"20",
    })

if __name__ == "__main__":
    main()