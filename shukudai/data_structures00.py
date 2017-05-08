## python 3
## Test stack logic using array of hashes

INSTANCE_MAX = 10
host_list = [['db-01',4],['db-02',7],['db-03',9],['db-04',15],['db-05',6]]
host_number = 0
host_groups = [[]]


while len(host_list) > 0:
    print(host_list)
    host = host_list.pop(0)
    host_groups[host_number].append(host)
    s = sum(i[1] for i in host_groups[host_number])
    if s > 15:
        host_groups[host_number].pop()
        host_groups.append([])
        host_number = host_number + 1
        host_list.insert(0,host)

print(host_groups)


