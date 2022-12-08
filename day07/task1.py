
from FileTreeNode import FileTreeNode
import argparse

parser = argparse.ArgumentParser(description='Read input file')
parser.add_argument('infile', metavar='Infile', type=str, help='Csv to process')
args = parser.parse_args()
infile = vars(args)['infile']
print("Infile: %s" %infile)

infile = open(infile, 'r')

history = []
stdout = []
command = None

def process_input_data(data, command, stdout, history):
    if data.startswith('$ '):
        #print("found command:", data, "prev command:", command)
        if command:
            #print('\t saving data:', {'command': command, 'stdout': stdout})
            history.append({'command': command, 'stdout': stdout})
            stdout = []
        command = data
    else:
        stdout.append(data)
        #print("found stdout %s for command %s" %(stdout, command))
    return command, stdout

for line in infile.readlines():
    data = line[:-1]
    #print("Raw line", data)
    command, stdout = process_input_data(data, command, stdout, history)
else:
    # write last data to history, if stopped on stdout
    if not(data.startswith('$ ')):
        history.append({'command': command, 'stdout': stdout})
infile.close()

def pprint_history(history):
    for item in history:
        print(item['command'])
        for line in item['stdout']:
            print('\t'+line)
#pprint_history(history)


filetree = FileTreeNode('/')
current_node = filetree
print(10*'-')
for item in history:
    if item['command'] == '$ cd /':
        print("Went to root! (already started there)")
        continue

    if item['command'] == '$ ls':
        #print("Listing at: ", current_node.path)
        for line in item['stdout']:
            if line.startswith('dir'):
                #print('Found directory:', current_node.path +'/' + line.split(' ')[1])
                ...
            else:
                #print("Adding file to tree:", line)
                size, filename = line.split(' ')
                current_node.add_file({"size": int(size), "filename": filename})

    elif item['command'].startswith('$ cd'):
        new_folder = item['command'].split(' ')[2]
        if new_folder == '..':
            #print("Going up one level")
            current_node = current_node.parent
        else:
            #print("Going deeper to", new_folder)
            new_node = FileTreeNode(current_node.path + '/' + new_folder, current_node)
            current_node.add_child(new_node)
            current_node = new_node

print(10*'-')
#print(filetree)

print(10*'-')
filetree.count_total_size()
#print(filetree)

print(10*'-')
small_files = []
filetree.find_interesting(100000, small_files)
print(small_files)
print(sum(small_files))
