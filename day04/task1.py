import argparse

parser = argparse.ArgumentParser(description='Read input file')
parser.add_argument('infile', metavar='Infile', type=str, help='Csv to process')
args = parser.parse_args()
infile = vars(args)['infile']
print("Infile: %s" %infile)

infile = open(infile, 'r')

data = []
for line in infile.readlines():
    elf1, elf2 = line[:-1].split(',')
    elf1 = [int(x) for x in elf1.split('-')]
    elf2 = [int(x) for x in elf2.split('-')]
    data.append([elf1, elf2])
infile.close()

def fully_contains(pair):
    starts = pair[0][0] - pair[1][0]
    ends   = pair[0][1] - pair[1][1]
    #print("Pair: %s, starts: %s, ends: %s" %(pair, starts, ends))
    if (starts * ends) < 0:
        return True
    elif (starts * ends) == 0:
        return True
    else:
        return False

count_contain_pairs = 0
for pair in data:
    if fully_contains(pair):
        count_contain_pairs += 1

print("Fully overlapping pairs: %d" %count_contain_pairs)

