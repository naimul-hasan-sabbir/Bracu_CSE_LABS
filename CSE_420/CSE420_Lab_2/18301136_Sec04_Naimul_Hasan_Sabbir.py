test = input("Enter Number of test cases :")

for i in test:
    email = input()
    web = input()

name = email.split("@")[0]

domain = email.split("@")[1]

web_name = web.split(".")[0]

al = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#checking email adress
def name_check(name):

    if name[0] in al:
        return True

dot_split_first = domain.split(".")[0]

dot_split_second = domain.split(".")[1]

def dot_checker(dot_split_first):

     if dot_split_first[0] in al:

         return True

def dot_checker(dot_split_second):

    if dot_split_second[0] in al:

        return True
#checking web address
def web_name_check(web_name):
    length = len(web_name)
    for i in range(1,length+1):
        if web_name[i] in al:
            return True
n=int(test)

if bool(name_check(name)) and bool(dot_checker(dot_split_first)) and bool(dot_checker(dot_split_second)):
     for i in range(1,n):
         print("Email"+","+str(i))

if bool(web_name_check(web_name)):
    for i in range (2,n+1):
        print("Web"+","+str(i))