#exception handling
import sys
DIGIT_MAP={
    'zero':'0',
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
}
def convert(s):
    #in one try block you handle multiple exception
    try:
        number=''
        for i in s:
            number+=DIGIT_MAP[i]
        x=int(number)
        return number
        print('operation successeded')
    except (KeyError,TypeError) as e:#here you can handle multiple type exception
        print(f"conversion failed {e!r}",file=sys.stderr)
        return -1
        