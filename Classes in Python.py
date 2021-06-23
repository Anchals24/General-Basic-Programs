#Constructors : used to initialize the data members of the class when an object of class is created.

#Objects and Classes : 
# An object is simply a collection of data (variables) and methods (functions) 
#that act on those data. 
#Similarly, a class is a blueprint for that object. We can think of class as a sketch (prototype) of a house.

#Python Pass statement:
#The pass statement is used as a placeholder for future code. When the pass statement is executed, 
# nothing happens, but you avoid getting an error when empty code is not allowed. 
# Empty code is not allowed in loops, function definitions, class definitions, or in if statements

#built in init function
# write a function (like we normally do) >> now write it within a class
# def __init__(self , title) [We are gonna going to give it two arguments {self} and {title}]
#Inside this function now we will write self.title = title
# init function is python's built in special function for working with classes
#When we created class , the init function is called to initialize the new object with information.
# and also it is called before any other fucntion that we have defined on the class
# this is the initializer function : not the constructor
#The object is already been created / constructed when this function has been called
#whenever we call a method on a python object the object itself gets automatically passed in as the first argument.
# "self" is just a naming convention

class Books:
    def __init__(self , name , page):
        self.name = name
        self.page = page
    Book1 = "Hello anchal"
    print(Book1)
    
    def display(self):
        print(self.name)
        print(self.page)
        #print(Book1)
B1 = Books("Tom and Jerry" , 254)
B2 = Books("Harry Potter" , 345)
print(B1)
print(B2)
B1.display()
B2.display()


#Book1 : local variable >> cannot be use anywhere. 
#whereas self.variable : instance variable >> class variable >> can be used anywhere >> class name use >> can access the value
#B1 and B2 : objects basically they are storing the books details . B1 contains detail of a book and B2 contains detail of the another book.


