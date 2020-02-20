to_read = "a_example.txt"

global_books = []
libraries = []

class book:
    def __init__(self,id,score):
        self.id,self.score=id,score

    def __lt__(self, b):
        return self.score < b.score

    def __gt__(self, b):
        return self.score > b.score

    def __eq__(self, b):
        return self.score == b.score

class library:
    def __init__(self, id, signup, booksperday):
        self.signup,self.booksperday = signup,booksperday
        self.books = []
    
    def sort_books(self):
        self.books.sort()

f = open(to_read,"r")
lines = f.readlines()

for id,score in enumerate(lines[2].split()):
    global_books.append(book(id,score))

i = 0
n = 4
while n < len(lines):
    this_library = lines[n:n+3]
    parms = this_library[0].split()
    libraries.append(library(int(parms[1]),i,int(parms[2])))
    for i in this_library[2].split():
        libraries[-1].books.append(global_books[int(i)])
    i += 1
    n += 3
