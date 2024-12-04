#pylint:disable= 'invalid character '‘' (U+2018) (<unknown>, line 10)'
#pylint:disable= 'invalid character '‘' (U+2018) (<unknown>, line 9)'
#此项目为开源项目，如有雷同，纯属巧合，本项目遵守PGL-3，如构成侵权，请联系我：xmx200712@163.com
import  random

def InputFoodName():
	global FoodList
	while True:
		print('please enter the No.'+str(len(FoodList)) +'name of food(one by one),nothing to finish')
		FoodName=input()
		if FoodName=='':
			break
		FoodList=FoodList+[FoodName]
	print('you have finish input food name,the number is'+str(len(FoodList)))
	
def RandomFood():
	global FoodList
	print(random.choice(FoodList))
	
def DeletFood_Name():
	global FoodList
	while True:
		print('input the food name you want to delet(one by one),nothing to finish')
		FoodName=input()
		if FoodName=='':
			break
		try:
			FoodList.remove(str(FoodName))
			print('you have just delet'+str(FoodName))
		except ValueError:
			print('you can not delet this ,it is not in the list')

def SeeFoodList():
	global FoodList
	if len(FoodList)==0:
		print('there is no food in the list ,please back and input')
	for i in range(1,len(FoodList)+1):
		print(str(i),+FoodList[i-1])
		
FoodList=[]

print('maybe there are lot of bugs in this app please tell me Email:xmx200712@163.com')
while True:
	print('what to eat')
	print('1.random food'
	'2.add food to the list'
	'3.delet food(use name)'
	'4.see the list'
	'5.finish')
	choice=int(input())
	if choice==1:
		RandomFood()
	elif choice==2:
		InputFoodName()
	elif choice==3:
		DeletFood_Name()
	elif choice==4:
		SeeFoodList()
	elif choice==5:
		break
print('thank you to use')
	
	
		
	