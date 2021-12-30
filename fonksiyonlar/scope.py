#global scope 
x="global x"

def function():
    #local x
    x="local x"
    print(x)
function()
print(x)    



###########
#global

name="Ahmed"

def changeName(new_name):
    #local
    global name
    name=new_name
    print(name)

changeName("Emir")
print(name)    

###########

name="global string"

def greeting():
    # name="Ahmed"

    def hello():
        # name="Emir"
        print("hello "+name)

    hello()

greeting()        

##############
x=50
def test():
    global x
    print(f"x +{x}")
    
    x=100
    print(f"changed x to +{x}")

test()
print(x)

