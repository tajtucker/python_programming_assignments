class Student: #This line defines a class called "Student"
    major = "CS" #This line creates a class variable (major) and assigns it to "CS"

    def __init__(self, name): #This line is a constructor, it takes in self, and name. 
        self.name = name #This line takes self.name, which is what object is passed through, and assigns it to name. 


s1 = Student("John") #This line creates an object (s1) and calls the class "Student" with the argument "John". "John" is assigned to name.
s2 = Student("David") #Same as above but the object is (s2) and the name is "David".

print(s1.major) #This line prints the major of the object (s1) which is "CS".
print(s2.major) #Same as above but for object (s2).

print(s1.name) #This line prints the name of the object (s1) which is "John".
print(s2.name) #Same as above but for (s2) and it prints "David".

Student.major = "Math" #This line calls the class variable "major" from the class "Student" and reassigns it to "Math".
print(s1.major) #This line prints the new major of the object (s1) which is "Math".
print(s2.major) #Same as above but for object (s2).

s1.major = "Engr" #This line assigns the major for object (s1) to be "Engr".
print(s1.major) #This line prints the major for object (s1) which is now "Engr".
print(s2.major) #This line still prints "Math" as the major for object s2 has not changed.