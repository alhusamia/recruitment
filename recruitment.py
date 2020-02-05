def main():
	#write your code here
        skills =["Python", "C++", "JavaScript", "Meeting", "Leeting","Eating" ]
        cv ={}
        cv["name"] = input("Whats your name? ")
        cv["age"] = input("How old are you? ")
        cv["experience"] = input("How many years of experience do you have? ")
        cv["skills"] = []
        print()
        num = 1
        for i in skills:
            print(str(num)+". "+str(i))
            num+=1
            
        skill1= int(input("Choose a skill from above by entering its number: "))    
        skill2=int(input("Choose another skill from above by entering its number: "))
        cv["skills"] = [skills[skill1-1], skills[skill2-1]]
        
        if int(cv["age"]) in range(24,41) and int(cv["experience"]) >5 and (skill1==6 or skill2==6):
            
            print("You have been accepted, "+cv["name"])
        else:
            print("You have been rejected")




if __name__ == '__main__':
	main()
