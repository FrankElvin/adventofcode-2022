
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

def find_common_items(part1, part2):
    checked_items = []
    common_items = ''
    for item in part1:
        if item in checked_items:
            continue

        if item in part2:
            checked_items.append(item)
            common_items += item
        else:
            checked_items.append(item)

    if not(common_items):
        print("WARN: no common item")
    #print("Rucksacks: %s, %s. Common: %s" %(part1, part2, common_items))
    return common_items

def find_common_in_group(group):
    common1 = find_common_items(group[0], group[1])
    common2 = find_common_items(common1, group[2])
    if len(common2) != 1:
        print("WARN: strange common sequence")
        return None
    return common2


pount_sum = 0
current_group = []
for line in infile.readlines():
    items = line[:-1]
    if len(current_group) <= 2:
        current_group.append(items)

    if len(current_group) == 3:
        #print("Group: %s" %(current_group))
        common = find_common_in_group(current_group)
        points = item_points(common)
        #print("Common item: %s, points: %d" %(common, points))
        pount_sum += points

        current_group = []

print("Bad item points: %d" %pount_sum)
infile.close()
