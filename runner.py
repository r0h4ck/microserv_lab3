import sys
import requests
import getopt
import json
from pprint import pprint

help_message = '''
    script to test microservice lab by Hose
    
    -h           print this help message and exit           | OPTIONAL
    -m/--method  [GET, POST] method for testing             | REQUIRED
    -t/--text    text of message to insert for POST method  | REQUIRED/OPTIONAL
    -n/--number  count of POST requests                     | OPTIONAL
    
'''
URL= "http://127.0.0.1:9000/"

def get_messages() :
    resp = requests.get(URL)
    ret = resp.json()
    return ret

def post_messages(message: str = "base message", count: int = 1) -> list:
    header = {
        "Content-Type": "application/json"
    }

    ret = list()
    iterator = 0

    for i in range(count):
        text = f"{message}_{str(iterator)}"
        body = json.dumps({"message": text})
        resp = requests.post(URL, headers=header, data=body)
        ret.append(resp.json())
        iterator += 1

    return ret

def main(argv):
    method = None
    message = 'test message'
    count = 1
    ret = ""

    try:
        opts, args = getopt.getopt(argv, "hm:t:n:", ['help', 'method=', 'text=', 'number='])
    except getopt.GetoptError as e:
        print(f"Argument Error, reason: {e}")
        sys.exit(1)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(help_message)
            sys.exit(0)
        elif opt in ('-m', '--method'):
            method = arg.upper()
        elif opt in ('-t', '--text'):
            message = arg
        elif opt in ('-n', '--number'):
            count = int(arg)
        else:
            print(f'unknown option {opt}')
            print(help_message)
            sys.exit(1)

    if method == "GET":
        ret = get_messages()
    elif method == "POST":
        if message is None:
            ret = post_messages(count=count)
        else:
            ret = post_messages(message, count=count)
    else:
        print(f"[-] Not implemented method: {method}")
        sys.exit(1)

    print("Answer is: ")
    pprint(ret)

    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv[1:])
