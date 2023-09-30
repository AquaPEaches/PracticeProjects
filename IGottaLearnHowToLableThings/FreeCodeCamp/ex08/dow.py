han =  open('mailbox.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    print('Line: ', line)
    if len(wds) < 1:
        continue
    if wds[0] != 'From':
        #print('Ignore') 
        continue


  