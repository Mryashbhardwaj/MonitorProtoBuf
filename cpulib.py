valid_load=0

def checkCpu  ( load):
    print (load)
    print("yash")
    if load < valid_load:
    	return "fine"
    else: 
    	return "overload"

if __name__=="__main__":
    print( CheckCpu(2) )