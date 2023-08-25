print("hello...",'Hi....',True,10+20,"Hey...")
#2. ใช้ + มีข้อแม้ว่าทุกตัวที่เอามาต่อกันต้องเป็น String
print("hello..."+str(456)+' Hi....'+str(True)+' '+str(10+20)+" Hey...")
#3. ใช้เมธอด Format
print("Hello... {} Hi... {} {} Hey... ".format(456,True,10+20))
#4. f-string
print(f"Hello... {456} Hi... {True} {10+20} Hey... ")
#5. modular operator (%)-> %d %f, %c, %s,.....
print("Hello... %d Hi... %i %d Hey..." %(456,True,10+20) )




