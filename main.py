from symbol import decorator
import time
from Modules.puplpsolution import optimization

@decorator
def timer():
    start = time.time()
    stop = time.time()
    print ("Время :")
    print(stop - start)

def main():
    optimization()


if __name__:"__main__"