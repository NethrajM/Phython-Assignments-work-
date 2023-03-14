class multipleFunctions():
    def Elegible(*args, **kwargs):
        Gender = input("Enter your gender: ")
        Age = int(input("Enter your age: "))
        if (Gender =="male") and (Age > 18):
            print("Your Gender: "+Gender)
            print("Your Age: "+str(Age))
            print("ELIGIBILE")
#             return message

        elif(Gender =="male") and (Age == 18):
            print("Your Gender: "+Gender)
            print("Your Age: "+str(Age))
            print("NOT ELIGIBILE")
#         return message

            
    def oddEven(*args, **kwargs):
        num=int(input("Enter the number :"))
        if (num%2) == 0:
           print ("It is even")
        else:
            print("It is odd")
        
    def Subfields(*args, **kwargs):
        list = ['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing' ,'Natural Language Processing']
        print("Sub-fields in AI are:")
        for i in list:
            print(i)
            
    def percentage(*args, **kwargs):
        sub1 = int(input("Enter your subject1 mark: "))
        sub2 = int(input("Enter your subject2 mark: "))
        sub3 = int(input("Enter your subject3 mark: "))
        sub4 = int(input("Enter your subject4 mark: "))
        sub5 = int(input("Enter your subject5 mark: "))
        list1 = [sub1,sub2,sub3,sub4,sub5]
        total = 0
        for i in range(0, len(list1)):
            total = total+list1[i]
        percentage = (total/(len(list1)*100))*100

        print("Subject1: "+str(sub1))
        print("Subject2: "+str(sub2))
        print("Subject3: "+str(sub3))
        print("Subject4: "+str(sub4))
        print("Subject5: "+str(sub5))
        print("Total: "+str(total))
        print('Percentage: '+str(percentage))

   

    