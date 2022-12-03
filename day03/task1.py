
import argparse

parser = argparse.ArgumentParser(description='Read input file')
parser.add_argument('infile', metavar='Infile', type=str, help='Csv to process')
args = parser.parse_args()
infile = vars(args)['infile']
print("Infile: %s" %infile)

infile = open(infile, 'r')

def item_points(item):
    if 97 <= ord(item) <= 122:
        return ord(item) - 96
    elif 65 <= ord(item) <= 90:
        return ord(item) - 38
    else:
        print("WARN: unexpected symbol!")

def find_common_item(part1, part2):
    checked_items = []
    for item in part1:
        if item in checked_items:
            continue

        if item in part2:
            return item
        else:
            checked_items.append(item)
            #print("checked items: %s" %checked_items)
    else:
        print("WARN: no common item")

pount_sum = 0
for line in infile.readlines():
    items = line[:-1]
    part1 = items[:len(items)//2]
    part2 = items[len(items)//2:]
    #print("Part one: %s, part two: %s" %(part1, part2))
    common = find_common_item(part1, part2)
    points = item_points(common)
    #print("Common item: %s, points: %d" %(common, points))
    pount_sum += points

print("Bad item points: %d" %pount_sum)
infile.close()
