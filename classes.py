class Classroom():
    numberofchairs=6
    numberoftables=3
    numberofstudents=6
    teachers=1
    lessons=3

    #constructor-gets called when object is created
    def __init__(self):
        print ("constructor is called")
    def changedetails(self):
        self.lessons=int(input("how many lessons "))
    def showdetails(self):
        print(self.numberofchairs,self.numberoftables,self.numberofstudents,self.lessons,self.teachers)
#creating object of the class
obj1=Classroom()
obj1.changedetails()
obj1.showdetails()