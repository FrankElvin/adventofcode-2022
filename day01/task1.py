
import argparse

parser = argparse.ArgumentParser(description='Read input file')
parser.add_argument('infile', metavar='Infile', type=str, help='Csv to process')
args = parser.parse_args()
infile = vars(args)['infile']
print("Infile: %s" %infile)

infile = open(infile, 'r')

richest_elf = 0
elf_cal = 0
for line in infile.readlines():

    if line != '\n':
        #print(line[:-1])
        elf_cal += int(line[:-1])
    else:
        #print("Elf cal: %s\n" %(elf_cal))
        if elf_cal > richest_elf:
            richest_elf = elf_cal
        elf_cal = 0

else:
    #print("Elf cal: %s\n" %(elf_cal))
    if elf_cal > richest_elf:
        richest_elf = elf_cal
    elf_cal = 0

print("richest guy: %d" %richest_elf)


infile.close()
