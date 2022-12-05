import argparse

parser = argparse.ArgumentParser(description='Read input file')
parser.add_argument('infile', metavar='Infile', type=str, help='Csv to process')
args = parser.parse_args()
infile = vars(args)['infile']
print("Infile: %s" %infile)

infile = open(infile, 'r')

stacks = []
raw_stacks = []
commands = []
reading = 'stacks'
for line in infile.readlines():
    if line == '\n':
        reading = 'commands'
        continue

    if reading == 'stacks':
        raw_stacks.append(line[:-1])

    if reading == 'commands':
        words = line[:-1].split(' ')
        # substract 1 from stack number for starting with 0 index
        command = {"number": int(words[1]), "from": int(words[3])-1, "to": int(words[5])-1}
        commands.append(command)

infile.close()

def process_raw_stacks(raw_stacks):
    cols = len(raw_stacks[-1].split())
    result = []

    char_matrix = []
    for line in raw_stacks[:-1]:
        col_data = []
        for i in range(cols):
            data = line[1 + i*4]
            col_data.append(data)
        char_matrix.append(col_data)

    heigth = len(char_matrix)

    for i in range(cols):
        column = []
        for j in range(heigth):
            if char_matrix[j][i] != ' ':
                column.append(char_matrix[j][i])
        result.append(column)

    return result

stacks = process_raw_stacks(raw_stacks)

def print_stacks(stacks):
    for item in stacks:
        print(item)

for item in commands:
    #print('+'*20, item)
    #print_stacks(stacks)
    to_move = stacks[item['from']][0:item['number']]
    #print('moving:', to_move)
    # removing old
    #print("cleaning stack %s" %stacks[item['from']])
    stacks[item['from']][0:item['number']] = []
    # adding new
    #print("putting to %s" %stacks[item['to']])
    stacks[item['to']] = to_move[::-1] + stacks[item['to']] 


print("=====")
result = ''
for item in stacks:
    #print(item)
    result += item[0]
print("Result: %s" %result)
