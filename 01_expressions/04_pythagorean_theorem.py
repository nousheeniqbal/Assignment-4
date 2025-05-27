import math  

def main():
    ab = float(input("\033[1m\033[3mEnter the length of AB:"))  
    ac = float(input("\033[1m\033[3mEnter the length of AC:"))  

    bc = math.sqrt(ab**2 + ac**2)  

    print(f"The length of the hypotenuse is: {bc}")  

if __name__ == '__main__':
    main()