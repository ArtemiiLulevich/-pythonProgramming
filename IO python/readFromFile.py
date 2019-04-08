# text = open('IO\\sample.txt', 'r')
# for line in text:
#     print(line)
#
# text.close()

# with open('IO\\sample.txt', 'r') as text:
#     for line in text:
#         print(line)

with open('IO samples\\sample.txt', 'r') as text:
    line = text.readline()
    while line:
        print(line, end='')
        line = text.readline()
