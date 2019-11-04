name1=input("type your first name: ")
name2=input("type your last name: ")
full_name=name1+" "+name2
def reverse(full_name): 
    full_name = full_name[::-1] 
    return full_name 
 
print ("The original name   is : ") 
print (full_name) 
  
print ("The reversed name  is : ",) 
print (reverse(full_name)) 