

class FileTreeNode:
    def __init__(self, path, parent=None):
        self.path = path
        self.data = []
        self.children = []
        self.parent = parent
        self.total_size = None

    def add_file(self, data):
        self.data.append(data)

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        intent_level = self.path.count('/')-1
        print("%s= Folder: %s (size: %s)" %('\t'*intent_level, self.path, self.total_size))
        for item in self.data:
            print('\t'*intent_level + '---' + str(item))
        for item in self.children:
            print(item)
        return ''

    def step_deeper(self, child):
        for item in self.children:
            # return existing FileTreeNode if already created it
            if item.path.split('/')[-1] == child:
                return item
        else:
            return FileTreeNode(self.path+'/'+ child)

    def count_file_size(self):
        sum_ = 0
        for item in self.data:
            sum_ += item['size']
        return sum_

    def count_total_size(self, indent=0):
        total_size = self.count_file_size()
        #print('%sOn node: %s self size: %d' %('--'*indent, self.path, total_size))

        for child in self.children:
            add_value = child.count_total_size(indent+1)
            #print('%schild: %s, add value: %s' %('--'*indent, child.path, add_value))
            total_size += child.count_total_size()
        self.total_size = total_size
        return total_size

    def find_interesting(self, target, result):
        if self.total_size < target:
            #print("Node %s size less than %d: %d" %(self.path, self.total_size, target))
            result.append(self.total_size)
        
        for child in self.children:
            child.find_interesting(target, result)

    def find_to_delete(self, to_free, search):
        if self.total_size - to_free >= 0:
            if not search['size']:
                search['size'] = self.total_size
                search['path'] = self.path
            else:
                if self.total_size < search['size']:
                    search['size'] = self.total_size
                    search['path'] = self.path

        for child in self.children:
            child.find_to_delete(to_free, search)
