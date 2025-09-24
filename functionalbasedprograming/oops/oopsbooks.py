
class Book:
    library_name="City Library"
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    def info(self):
        print("Library name:",Book.library_name)
        print("book name:", self.title)
        print("author:", self.author)
        print("year:",self.year)
book_one=Book("adventure island","Vamsi","2006")
book_two=Book("War Zone","dinesh","2004")
book_three=Book("King of forest","Yathi","2000")

book_one.info()
book_two.info()
book_three.info()

