from constants import MAX_CARS
import datetime
import time
import pytz
class Carparking:
    def __init__(self):
        self.capacity = MAX_CARS
        self.slotid = 0
        self.numOfOccupiedSlots = 0
        self.in_time=0
        self.out_time=0
        self.fare=0
        self.slots=[-1]*MAX_CARS

    def choose(self,argument):

        if argument == 1:
            a=self.Park()
            if a==-1:
                print("sorry, the parking is full")
            else:
                print("Slot allocated,"+str(a))

        elif argument == 2:
            a=self.Checkout()

        elif argument == 3:
            a=self.Calculate_fare()
            if a==-1:
                print("The slotid is out of range")
            else:
                print("Fare=",a)

        elif argument == 4:
            self.Parking_status()

        else:
            print("Please, Enter a valid option")

    def emptyslots(self):
        for i in range(len(self.slots)):
            if self.slots[i]==-1:
                return i

    def Park(self):
        if self.numOfOccupiedSlots<self.capacity:
            slotid=self.emptyslots()
            self.car_num = input("Enter the car number:")
            current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
            self.in_time=current_time
            #print(self.in_time)
            self.slots[slotid]=[self.car_num,self.in_time,self.out_time,self.fare]
            self.slotid+=1
            self.numOfOccupiedSlots+=1
            return slotid+1
        else:
            return -1


    def Parking_status(self):
        for i in range(self.capacity):
            if(self.slots[i]==-1):
                continue
            print(i+1,end="  ")
            print(self.slots[i][0],end="  ")
            print(str(self.slots[i][1]))
        print("Total cars in parking lot is",self.numOfOccupiedSlots)

    def Calculate_fare(self):
        slotid=int(input("enter your slot id for checkout"))
        if (slotid-1)>self.numOfOccupiedSlots or (slotid-1)>self.capacity:
            print("The Slot you have mentioned is out of range")
            return -1
        else:
            print("Calculating fare for",slotid,"........")
            time.sleep(2)
            current_time=datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
            #current_time=current_time.hour
            fare=(current_time-self.slots[slotid-1][1]).seconds//3600
            fare=int(fare)*15+30
            return fare

    def Checkout(self):
        slotid=int(input("enter your slot id for checkout"))
        if (slotid-1)>self.numOfOccupiedSlots or (slotid-1)>self.capacity:
            print("The Slot you have mentioned is out of range")
            return -1
        else:
            current_time=datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
            self.slots[slotid-1][2]=current_time  #out_time
            fare=(self.slots[slotid-1][2]-self.slots[slotid-1][1]).seconds//3600
            self.slots[slotid-1][3]=int(fare)*15+30
            print("In Time =",str(self.slots[slotid-1][1]))
            print("Out Time =",str(self.slots[slotid-1][2]))
            print("The fare = ",self.slots[slotid-1][3])
            self.slots[slotid-1]=-1
            self.numOfOccupiedSlots-=1
            return 1

def main():
    car=Carparking()
    ch='y'
    while ch=='y' or ch=='Y':
        print("1.Park the car")
        print("2.Checkout")
        print("3.Calculate Fare")
        print("4.Status")
        print("Enter your choice")
        argument=int(input())
        car.choose(argument)
        ch=input("DO you wish to continue!??")





if __name__=="__main__":
    main()
