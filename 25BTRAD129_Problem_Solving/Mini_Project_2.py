d = {}
n = int(input("Enter the number of students : "))

for i in range(n):
    print(f"\nEnter the details of Student {i+1}")
    rollno = int(input("Roll No. : "))
    name = input("Name of the Student : ")
    
    print("\nEnter the marks for the following subjects : ")
    os = float(input("Operating System : "))
    coa = float(input("Computer Organization and Architecture : "))
    dmgt = float(input("Discrete Mathematics and Graph Theory : "))
    pp = float(input("Python Programming : "))
    dt = float(input("Design Thinking : "))
    
    avg = (os + coa + dmgt + pp + dt) / 5
    
    if avg >= 95:
        g = "O"
    elif avg >= 90:
        g = "A+"
    elif avg >= 85:
        g = "A"
    elif avg >= 80:
        g = "B+"
    elif avg >= 75:
        g = "B"
    elif avg >= 70:
        g = "C+"
    elif avg >= 65:
        g = "C"
    else:
        g = "D"
        
    s = (rollno, name)
    tm = (os, coa, dmgt, pp, dt)
    tg = (g,)  # Added a comma to make it a tuple
    l = [tm, tg]
    d[s] = l

print("\n" + "=" * 40)
print(f"{'STUDENT GRADES REPORT':^40}")
print("=" * 40)

for student, info in d.items():
    print(f"Roll No & Name : {student}")
    print(f"Marks (OS, COA, DMGT, PP, DT): {info[0]}")
    print(f"Grade Obtained : {info[1][0]}")
    print("-" * 40)
