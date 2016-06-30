
f=open('data.txt')
def file_stats(f):
    input=open(f)
    long=''
    for line in open('data.txt'):
        if len(line)>len(long):
            long=line
print(long)
f.close