#Body  Mass  Index
bodyweight=float(input('enter the weight of person'))
if(bodyweight<18.5):
    print("the person is underweight")
elif(bodyweight<=24.9):
    print("the person is normal")
elif(bodyweight<=29.9):
    print('the person is overweight')
elif(bodyweight<=34.9):
    print('the person is obesity class1')
elif(bodyweight<=39.9):
    print('the person is obesity class2')
else:
    print("extreme obesity")
    