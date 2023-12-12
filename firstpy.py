import argparse

def parse_input():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--num',
        type=int,
        required=True,
        help='input for the multiplyby9 function'
    )
    parser.add_argument(
        '--XX',
        type=int,
        default=7,
        help='input for XX'
    )
    args = parser.parse_args()
    return args
    

def printHello():
    print('Hello world')

def multiplyby9(inputV):
    print(9*inputV)

if __name__=="__main__":
   
   input_v = parse_input()

   print(f'the input num is {input_v.XX}')
   print('Blackpink in your area')
   multiplyby9(input_v.num)
   printHello()