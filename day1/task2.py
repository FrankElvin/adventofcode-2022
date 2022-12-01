
import argparse

parser = argparse.ArgumentParser(description='Read input file')
parser.add_argument('infile', metavar='Infile', type=str, help='Csv to process')
args = parser.parse_args()
infile = vars(args)['infile']
print("Infile: %s" %infile)

infile = open(infile, 'r')

richest_elfs = [0, 0, 0]
elf_cal = 0

def check_rich_elf(candidate, elf_list):
    for i in range(len(richest_elfs)):
        if candidate > elf_list[i]:
            elf_list.insert(i, candidate)
            elf_list.pop(3)
            break

# [0, 0, 0]
# [10, 0, 0]
# [10, 5, 0]
# [10, 8, 5, 0]
# [10, 8, 5]

for line in infile.readlines():
    if line != '\n':
        elf_cal += int(line[:-1])
    else:
        check_rich_elf(elf_cal, richest_elfs)
        elf_cal = 0

else:
    check_rich_elf(elf_cal, richest_elfs)

print("richest guys: %s, sum: %d" %(richest_elfs, sum(richest_elfs)))

infile.close()
