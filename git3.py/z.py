def main(int a,int b):
	print("swapped numbers are :",swap())
	return a+b

def swap(x,y):
	temp=x
	x=y
	y=temp
	return(x,y)
