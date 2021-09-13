class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist_Implementation:
    def __init__(self):
        self.head=None
    def insert_at_beg(self):
        var = int(input("Enter value to insert in linkedlist : "))
        NewNode=node(var)
        NewNode.next=self.head
        self.head=NewNode
    def insert_at_specific(self):
        print("                  Note : index will start from 0")
        index = int(input("Enter index on which you want to insert value in linkedlist: "))
        tempObject1=self.head
        if index>=0 and index<(self.count_elements()):
            if index==0:
                tempObject1.insert_at_beg()
            elif index==(self.count_elements()-1):
                tempObject1.insert_at_end()
            else:
                var = int(input("Enter value to insert in linkedlist: "))
                NewObject=node(var)
                TempObject=self.head
                a=0
                while a<=(index-1):
                    TempObject=TempObject.next
                    a=a+1
                NewObject.next=TempObject.next
                TempObject.next=NewObject


    def insert_at_end(self):
        var = int(input("Enter value to insert on last index of linkedlist : "))
        tempObject=self.head
        newNode=node(var)
        while tempObject.next is not None:
            tempObject=tempObject.next
        tempObject.next=newNode
    def delete_at_beg(self):
        tempObject1=self.head
        tempObject2=tempObject1.next
        del tempObject1
        self.head=tempObject2
    def delete_at_specific(self):
        var = int(input("Enter value to delete from the specific location in linkedlist : "))
    def delete_at_end(self):
        tempObject=self.head
        while tempObject.next.next is not None:
            tempObject=tempObject.next
        deleteThisNode=tempObject.next
        tempObject.next=None
        del deleteThisNode
    def min_element(self):
        TempObject=self.head
        min_value = TempObject.data
        while TempObject is not None:
            if(min_value >TempObject.data):
                min_value=TempObject.data
            TempObject=TempObject.next
        print("Minimum element in Linkedlist is :  ", min_value)
    def max_element(self):
        TempObject = self.head
        max_value = TempObject.data
        while TempObject is not None:
            if (max_value < TempObject.data):
                max_value = TempObject.data
            TempObject = TempObject.next
        print("Minimum element in Linkedlist is :  ", max_value)
    def print___(self):
        if self is None:
            print("Linkedlist is empty")
        else:
            tempObject = self.head
            while tempObject is not None:
                print(tempObject.data)
                tempObject = tempObject.next
    def sort_element(self):
        if self is None:
            print("Linkedlist is empty")
        else:
            templist=[]
            tempObject = self.head
            while tempObject is not None:
                templist.append(tempObject.data)
                tempObject = tempObject.next
            templist.sort()
            i=0
            tempObject = self.head
            while tempObject is not None:
                tempObject.data=templist[i]
                tempObject = tempObject.next
                i=i+1
    def reverse_element(self):
        if self is None:
            print("Linkedlist is empty")
        else:
            templist=[]
            tempObject = self.head
            while tempObject is not None:
                templist.append(tempObject.data)
                tempObject = tempObject.next
            templist.reverse()
            i=0
            tempObject = self.head
            while tempObject is not None:
                tempObject.data=templist[i]
                tempObject = tempObject.next
                i=i+1
    def count_elements(self):
        tempObject=self.head
        count=0
        while tempObject is not None:
            tempObject=tempObject.next
            count=count+1
        return count
    def inputs(self):
        input_ = 1
        while (input_ != 0):
            print("Press 1.0: for insert at the beginning")
            print("Press 1.1: for insert at the specific location")
            print("Press 1.2: for insert from the end")
            print("Press 2.0: for delete element at the beginning")
            print("Press 2.1: for delete at the specific location")
            print("Press 2.2: for delete from the end")
            print("Press 3.0: for top")
            print("Press 4.0: for size of Linked list")
            print("Press 5.0: for printing elements")
            print("Press 6.0: for sort elements")
            print("Press 7.0: for reverse elements")
            print("Press 8.0: for print min element")
            print("Press 9.0: for print max element")
            print("Press 0: for exit")
            input_ = float(input("Enter operation want to perform : "))
            if (input_ == 1.0):
               self.insert_at_beg()
            elif (input_ == 1.1):
               self.insert_at_specific()
            elif (input_==1.2):
               self.insert_at_end()
            elif (input_ == 2.0):
                if self.head is None:
                    print("Linkedlist is empty")
                else:
                    self.delete_at_beg()
            elif (input_ == 2.1):
                if self.head is None:
                    print("Linkedlist is empty")
                else:
                    self.delete_at_specific()
            elif (input_ == 2.2):
                if self.head is None:
                    print("Linkedlist is empty")
                else:
                    self.delete_at_end()
            elif (input_ == 3):
                if self.head is None:
                    print("Linkedlist is empty")
                else:
                    temp=self.head
                    print("1st node contains data : ",temp.data)
            elif (input_ == 4):
                if self.head is None:
                    print("Linkedlist is empty")
                else:
                    print("Total elements in Linkedlist : ", self.count_elements())
            elif (input_ == 5):
                if self.head is None:
                    print("Linkedlist is empty")
                else:
                    self.print___()
            elif (input_ == 6):
                if self.head is None:
                    print("Linkedlist is empty")
                else:
                    self.sort_element()
            elif (input_ == 7):
                if self.head is None:
                    print("Linkedlist is empty")
                else:
                    self.reverse_element()
            elif (input_ == 8):
                if self.head is None:
                    print("Linkedlist is empty")
                else:
                    self.min_element()
            elif (input_ == 9):
                if self.head is None:
                    print("Linkedlist is empty")
                else:
                    self.max_element()
            else:
                print("Invalid input")


# Main body
Object=Linkedlist_Implementation()
Object.inputs()
