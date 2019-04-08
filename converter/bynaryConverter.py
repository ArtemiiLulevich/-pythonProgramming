decNumber = int(input('Enter decimal number: \n'))
binNumberStr = '0b'
power = 16
count = 0
while True:
    if decNumber > (2**16)-1:
        print('Exit...')
        break
    elif power == -1:
        print(binNumberStr)
        break
    count = (2 ** power)
    binNumberStr += str(decNumber // count)
    decNumber %= count
    power -= 1
