#Tami Odetoyinbo

print("please enter your grade on the following pieces of work: ")
# ask user to enter grades receieved for each variable 
a1 = int(input("Assignment 1 (/15):"))
a2 = int(input("Assignment 2 (/20):"))
a3 = int(input("Assignment 3 (/25):"))
a4 = int(input("Assignment 4 (/20):"))
a5 = int(input("Assignment 5 (/30):"))
tut = int(input("Tutorials (/10):"))
mid_t = int(input("Midterm (/30):"))
Final_E = int(input("Final Exam: (/50):"))


print("Your grades:")

# print users grades by dividing it by the maximum grade
# and multiply by 100
print("======================")
print("assignment1 | {:.2f}".format (a1/15*100),"%")
print("Assignment 2| {:.2f}".format (float(a2/20*100)),"%")
print("Assignment 3| {:.2f}".format (float(a3/25*100)),"%")
print("Assignment 4| {:.2f}".format (float(a4/20*100)),"%")
print("Assignment 5| {:.2f}".format (float(a5/30*100)),"%")
print("Tutorial    | {:.2f}".format (float(tut/10*100)),"%")
print("Mid Term    | {:.2f}".format (float(mid_t/30*100)),"%")
print("Exam        | {:.2f}".format(float(Final_E/50*100)),"%")
print("=======================")

#print users average including weight for each indiviual category
print("your final grade is:{:.2f}".format(float(a1/15*8)+(a2/20*8)+
(a3/25*8)+(a4/20*8)+(a5/30*8)+(tut/10*10)+
(mid_t/30*20)+(Final_E/50*30)),"%")




