
ipAddress = input("Enter IP:\n")

answer = "Statement %d has %d numbers."

ips = [0]
statement = 0

for i in range(len(ipAddress)):
    if ipAddress[i] in '0123456789' :
        ips[statement] += 1
    elif ipAddress[i] == '.':
        statement += 1
        ips.append(0)
statement = 0
for i in range(len(ips)):
    statement = i+1
    print(answer % (statement, ips[i]))
