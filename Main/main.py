def age_calculated(age):
    return age+10

def main():
    fname = str(input("Please enter your first name: "))
    lname = str(input("Please enter your lastname: "))
    age = int(input("Please enter your age: "))
    
    print(f"Your first name is {fname}")
    print(f"Your first name is {lname}")
    print(f"Your age is {age}")
    print(f"Your age in 10 years would be {age_calculated(age)}")
    
if __name__ == "__main__":
    main()
