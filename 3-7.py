with open('sample.txt', 'r') as f:
    lines = f.readlines()
    print(lines)

with open('samlpe.txt','w') as f:
    f.write('test')

with open('samlpe.txt','w') as f:
    print('test/n')
