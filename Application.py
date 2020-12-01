from constants import MAX_CARS,MAX_BIKES
import datetime
import time
import pytz
import re

class Vehicle:
    def __init__(self,regno,in_time):
        self.regno = regno
        self.in_time=in_time
        self.out_time=0
        self.fare=0

class parking:
    def __init__(self):
        self.capacity_cars = MAX_CARS
        self.capacity_bikes = MAX_BIKES
        self.slotid_cars = 0
        self.slotid_bikes = 0
        self.numOfOccupiedSlots_cars = 0
        self.numOfOccupiedSlots_bikes = 0
        self.slots_cars=[-1]*MAX_CARS
        self.slots_bikes=[-1]*MAX_BIKES

    def fare_calculation(self,in_time,opt):
        current_time=datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        time_delta=(current_time-in_time)
        days=time_delta.days
        hours=time_delta.seconds//3600
        fare=0
        if opt == 2:
            if days>0:
                fare+=100*days
            if hours>=0 and hours<=6:
                fare+=20
            elif hours>=6 and hours<=12:
                fare+=20+30
            elif hours>12:
                fare+=20+30+40
        else:
            if days>0:
                fare+=50*days
            if hours>=0 and hours<=6:
                fare+=10
            elif hours>=6 and hours<=12:
                fare+=10+20
            elif hours>12:
                fare+=10+20+30
        return fare,hours,days

    def choose(self,argument):
        if argument == 1:
            print("1.Park Bike")
            print("2.Park Car")
            opt=int(input("Enter your option"))
            if opt==1: #Bike Parking_status
                capacity=self.capacity_bikes
                occupied=self.numOfOccupiedSlots_bikes
                slot_list=self.slots_bikes
                a=self.Park(capacity,occupied,slot_list)
                if a==-1:
                    print("sorry, the parking is full")
                elif a==-2:
                    print("The regno is invalid")
                else:
                    print("Slot allocated,"+str(a))
                    self.numOfOccupiedSlots_bikes+=1
            elif opt==2:
                capacity=self.capacity_cars
                #slotid=self.slotid_bikes
                occupied=self.numOfOccupiedSlots_cars
                slot_list=self.slots_cars
                a=self.Park(capacity,occupied,slot_list)
                if a==-1:
                    print("sorry, the parking is full")
                elif a==-2:
                    print("The regno is invalid")
                else:
                    print("Slot allocated,"+str(a))
                    self.numOfOccupiedSlots_cars+=1
            else:
                print("Please, Enter a correct option. You will be redirected to main menu.")

        elif argument == 2:
            a=self.Checkout()

        elif argument == 3:
            a=self.Calculate_fare()
            if a==-1:
                pass
            else:
                pass

        elif argument == 4:
            self.Parking_status()

        else:
            print("Please, Enter a valid option")

    def emptyslots(self,slot_list):
        for i in range(len(slot_list)):
            if slot_list[i]==-1:
                return i

    def Park(self,capacity,occupied,slot_list):
        if occupied<capacity:
            slotid=self.emptyslots(slot_list)
            p = re.compile('(^[A-Za-z]{2}\s[0-9]{1,2}\s[A-Za-z]{1,2}\s[0-9]{1,4}$)|(^[A-Za-z]{2}-[0-9]{1,2}-[A-Za-z]{1,2}-[0-9]{1,4}$)')
            r_num = input("Enter the regno number:")
            if re.search(p,r_num):
                valid=True
            else:
                valid=False
            if valid:
                current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
                in_time=current_time
                V=Vehicle(r_num,in_time)
                slot_list[slotid]=V
                return slotid+1
            else:
                return -2
        else:
            return -1

    def Parking_status(self):
        for i in range(self.capacity_cars):
            if(self.slots_cars[i]==-1):
                continue
            print(i+1,end="  ")
            print(self.slots_cars[i].regno,end="  ")
            print(str(self.slots_cars[i].in_time.year),str(self.slots_cars[i].in_time.month),str(self.slots_cars[i].in_time.day),sep='-',end=" ")
            print(str(self.slots_cars[i].in_time.hour).zfill(2),str(self.slots_cars[i].in_time.minute).zfill(2),sep=':')
        print("Total cars in parking lot is",self.numOfOccupiedSlots_cars)

        for i in range(self.capacity_bikes):
            if(self.slots_bikes[i]==-1):
                continue
            print(i+1,end="  ")
            print(self.slots_bikes[i].regno,end="  ")
            print(str(self.slots_bikes[i].in_time.year),str(self.slots_bikes[i].in_time.month),str(self.slots_bikes[i].in_time.day),sep='-',end=" ")
            print(str(self.slots_bikes[i].in_time.hour).zfill(2),str(self.slots_bikes[i].in_time.minute).zfill(2),sep=':')
        print("Total bikes in parking lot is",self.numOfOccupiedSlots_bikes)

    def Calculate_fare(self):
        print("1.Calculate Fare for Bike")
        print("2.Calculate fare for Car")
        opt=int(input("Enter the vehicle type to calculate fare"))
        if opt==1: #Bike checkout
            capacity=self.capacity_bikes
            occupied=self.numOfOccupiedSlots_bikes
            slot_list=self.slots_bikes
        elif opt==2: #car checkout
            capacity=self.capacity_cars
            occupied=self.numOfOccupiedSlots_cars
            slot_list=self.slots_cars
        else:
            print("Please, Enter a correct option. You will be redirected to main menu.")
            return -1
        slotid=int(input("enter your slot id"))

        if (slotid<=0 or ((slotid-1)>=occupied or (slotid-1)>=capacity)):
            print("The Slot you have mentioned is out of range")
            return -1
        else:
            print("Calculating fare for",slotid,"........")
            time.sleep(2)
            fare,hours,days = self.fare_calculation(slot_list[slotid-1].in_time,opt)
            print("The amount to be paid for {0} days and {1} hours is {2}".format(days,hours,fare))
            return fare

    def Checkout(self):
        print("1.Checkout Bike")
        print("2.Checkout Car")
        opt=int(input("Enter the vehicle type to checkout"))
        if opt==1: #Bike checkout
            capacity=self.capacity_bikes
            occupied=self.numOfOccupiedSlots_bikes
            slot_list=self.slots_bikes
        elif opt==2: #car checkout
            capacity=self.capacity_cars
            occupied=self.numOfOccupiedSlots_cars
            slot_list=self.slots_cars
        else:
            print("Please, Enter a correct option. You will be redirected to main menu.")
            return -1

        slotid=int(input("enter your slot id for checkout"))
        if (slotid<=0 or ((slotid-1)>=capacity or (slotid-1)>=occupied)):
            print("The Slot you have mentioned is out of range")
            return -1
        else:
            current_time=datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
            slot_list[slotid-1].out_time=current_time  #out_time
            slot_list[slotid-1].fare,hours,days=self.fare_calculation(slot_list[slotid-1].in_time,opt)
            print("In Time ="+str(slot_list[slotid-1].in_time.year),str(slot_list[slotid-1].in_time.month),str(slot_list[slotid-1].in_time.day),sep='-',end=" ")
            print(str(slot_list[slotid-1].in_time.hour).zfill(2),str(slot_list[slotid-1].in_time.minute).zfill(2),sep=':')
            print("Out Time ="+str(slot_list[slotid-1].out_time.year),str(slot_list[slotid-1].out_time.month),str(slot_list[slotid-1].out_time.day),sep='-',end=" ")
            print(str(slot_list[slotid-1].out_time.hour).zfill(2),str(slot_list[slotid-1].out_time.minute).zfill(2),sep=':')
            print("The amount to be paid for {0} days and {1} hours is {2}".format(days,hours,slot_list[slotid-1].fare))
            #print("The fare = ",slot_list[slotid-1].fare)
            slot_list[slotid-1]=-1
            if opt==1: #Bike checkout
                self.numOfOccupiedSlots_bikes-=1
            else:#car checkout
                self.numOfOccupiedSlots_cars-=1
            return 1

def main():
    car_bike=parking()
    ch='y'
    while ch=='y' or ch=='Y':
        print("1.Park Vehicle")
        print("2.Checkout")
        print("3.Calculate Fare")
        print("4.Status",end="\n\n")
        print("Enter your choice")
        argument=int(input())
        car_bike.choose(argument)
        ch=input("DO you wish to continue!??")





if __name__=="__main__":
    main()
