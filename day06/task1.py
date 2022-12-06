import argparse

parser = argparse.ArgumentParser(description='Read input file')
parser.add_argument('infile', metavar='Infile', type=str, help='Csv to process')
args = parser.parse_args()
infile = vars(args)['infile']
print("Infile: %s" %infile)

infile = open(infile, 'r')

data = ''
for line in infile.readlines():
    data = line[:-1]

infile.close()


def buffer_unique(buffer):
    found = []
    for char in buffer:
        if char in found:
            return False
        else:
            found.append(char)
    return True

print('Data: %s' %data)
# we are comparing new char with current buffer state
buffer = data[:3]
print('Buffer:', buffer)
print('Buffer unique:', buffer_unique(buffer))
curr_position = 3

for char in data[curr_position:]:
    curr_position += 1
    #print("Reading: %s, buffer: %s, position: %d" %(char, buffer, curr_position))
    if char not in buffer and buffer_unique(buffer):
        print("Gotcha! char: %s, buffer: %s, position: %d" %(char, buffer, curr_position))
        break
    else:
        buffer = buffer[1:] + char
