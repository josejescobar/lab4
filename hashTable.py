'''
Jose Escobar
UTEP ID 80536060
CS3 Lab 4: Hash Table
'''


class HashTableNode:
    def __init__(self, word, next):
        self.word = word
        self.next = next


class HashTable:

    def __init__(self, size):#Creates the hash table 
        self.table = []
        for i in range(size):
            self.table.append([])

    def hash(self, k):#Converts characters into integers
        n = 0
        for i in range(len(k)):
            n = n + ord(k[i])
        return n % len(self.table)

    def insert(self, k): #Insertion Method
        index = self.hash(k)
        list = self.table[index]
        node = HashTableNode(k, list)
        list.append(node)

    def search(self,k): #Search Method
        pos = self.hash(k)
        list = self.table[pos]
        if k == list:
            return k
        else:
            return None


def createTable(file, hashtable):#Initializes hash table with values provided by file
    with open(file) as file:
        for line in file:
            items= line.split(" ")
            if items[0][0].isalpha():
                word = line.split(" ")[1]  
                hashtable.insert(word)

    return hashtable

def numberOfComparisons(self):#Counts the number of comparisons made by dividing all elements by the occupied ones
        total_elem = 0
        counter = 0
        for i in range(len(self.table)):
            temp = self.table[i]
            if temp is not None:
                counter +=1

            for temp in self.table[i]:
                total_elem +=1
                temp = temp.next

        return total_elem/counter

def loadFactor(self):#Devides number of elements by the size of table
    num_elements = 0
    for i in range(len(self.table)):
        temp = self.table[i]
        for temp in self.table[i]:
            num_elements += 1
    return num_elements / len(self.table)


def main():
    file = "glove.6B.50d.txt"
    table = HashTable(4)
    createTable(file, table)
    print("Hash Table size: 4")
    print("Load Factor: ", loadFactor(table))
    print("Comparisons made: ", numberOfComparisons(table))

main()

