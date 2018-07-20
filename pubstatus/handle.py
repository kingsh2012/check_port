import socket


def checkport(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.settimeout(0.1)
        s.connect((ip, int(port)))
        s.shutdown(2)
        return True
    except:
        return False


if __name__ == '__main__':

    host = 'www.calmkart.com'
    port = '22'

    if checkport(host, port):
        print "OK"
    else:
        print "NO"
