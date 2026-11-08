homework = int(input("Enter homework time in number:"))

if homework > 60:
    plan = "Start your homework now!!"
    print("It is a long homework session")
else:
    plan = "Complete your homework quickly"
    print("It is a short homework session")

free_time = print("Is there any free time after homework?(yes/no):")
if free_time == "yes":
    print("Reminder: pick a hobbie for your free time!")

print("=====Daily Planner=====")
print("Homework minutes:", homework)
print("Plan:",plan )
print("Free Time:", free_time)