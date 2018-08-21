#this program creates a .txt file showing which people prefer which item
import os
os.chdir('C:\\users\\Daniel\\desktop')
fileName = 'hmFile.txt'

print("Hello, Mr O'Rourke")

#empty character:[items] dict
charactersDict = {}

#keeps the program running so that user can input multiple names at once
newName = True
while newName == True:	
	uInput = input("Enter the name of the character you want to add information for or type 'print' to get the finished dictionary. \n")
	if uInput == 'print':
		break
	else:
		name = uInput
		print ('Entering data for %s' % name)
		print(r'Enter the item to append. Type "done" when you are finished.')

	#makes a new dictionary for the character and list to become the value
	
	#charactersDict = {name: [itemsList]}
	itemsList = []
	
	finishedInput = False
	while finishedInput == False:
		
		uInput = input()
		if uInput == 'done':
			#creates machine readable dict
			itemsList.sort()
			charactersDict['%s' %name] = itemsList
			print(charactersDict)
			break

		else: 
			itemsList.append(uInput)
			print("Enter another item or type 'done'")
			
#makes an {'item':[characters]} dict		
allItems = []
for i in charactersDict.values():
	for j in i:
		allItems.append(j)
itemsDict = {}
allItems.sort()
for i in allItems:
	listOfCharacters = []
	for c in charactersDict.items():
		if i in c[1]:
			listOfCharacters.append(c[0])
	itemsDict[i] = listOfCharacters
print(itemsDict)

#opens and names .txt file
uInput = input('What will you name this file? (.txt is automatically appended) \n')
fileName = ('%s' % uInput + '.txt' )
hmFile = open('%s' % fileName, 'a')

#creates human readable .txt file (name: items)
for chName in charactersDict.items():
	hmFile.write('='*20 + chName[0] + '='*20 + '\n')
	for gift in chName[1]:
		hmFile.write('.' + gift + '\n')

#creates human readable .txt file (item to characters)
for item in itemsDict.items():
	#var for determining where to print item
	spacingVar = (int(len(item[0])/2))
	hmFile.write('='*(30-spacingVar) + item[0] + ('='*(30-spacingVar)) + '\n' )
	for name in item[1]:
		hmFile.write('.' + name + '\n')





