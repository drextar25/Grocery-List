#Program name: Module 07: Project 4
#Student: Andressa Oliveira
#Course: COP1000-7
#Program description: This program will open a file with grocery items in it. The program will ask the user if they would like to see the current grocery items in the list, add more to it, and quit after. User input will rewrite the program with the old and new grocery items.


def title(): #display title of program
  print('\t \t\t Grocery List')
  print('\n')

#display the menu and get the user's choice
def get_menu_option(): #the user has 3 choices
  title()
  print('Please select from the following options:\n')
  print('\t1. View Grocery List\n\t2. Add item to Grocery List')
  print('\t3. Quit\n')
  ch=int(input('>>> '))   #input choice
  if(ch<=0 or ch>3): #validate choice
    print('Invalid option.') #if user enters something invalid
  else:
    return ch   #return user choice

#read file and store it into a list
def read_list():
  fp=open('GroceryList.txt','r') #open file 
  data = [line.strip() for line in fp] #store file contents into a list
  fp.close() #close file
  return data #return list

#display the current list
def view_grocery_list(data): 
  if len(data)!=0: #list will never be blank
    print("\nYou have the following items on your grocery list:\n")
    for num, item in enumerate(data):
      print('\t'+str(num+1)+'. '+item)#display items
    print()

#add an item to list
def add_item(data):
  print('Enter an item to add to your grocery list:')#ask for user input
  item=input('>>> ')#take input
  print(item+' was added to your list!\n')
  data.append(item) #add item to the end of list

#to exit program
def exit(data):
  print('\tHave a great day!\n')
  write_list_file(data)

#update the list with the new items
def write_list_file(data):
  fp=open('GroceryList.txt', 'w')#open file
  for item in data:
    fp.write(item+"\n")#write new items into file and update
  fp.close()#close file to make sure all updates are processed
  quit()

#main function
def main():
  data=read_list() #call function for opening file
#function for user choice
  while(True):
    ch=get_menu_option()
    if ch==1:
      view_grocery_list(data)
    elif ch==2:
      add_item(data)
    elif ch==3:
      exit(data)
    
      

if __name__=="__main__":#function to call main
    main()

