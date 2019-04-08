with open('IO samples\\sample.txt', 'a+') as text_file:
    print('\n', file=text_file)
    # print('-' * 20, file=text_file)
    print('-' * 20, file=text_file)
    for i in range(2, 13):
        for j in range(1, 13):
            print('%2d times %d is %-2d' % (j, i, i * j), file=text_file)
            # print('%2d times %2d is %-2d' % (j, i, i * j))
        print('-' * 20, file=text_file)
