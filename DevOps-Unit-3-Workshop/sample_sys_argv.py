# This is a sample app that we're going to incorporate in the bus-arrivals.py app

import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: python bus-arrivals.py <argument1> <argument2> ...")
        sys.exit(1)
    
    # Print the script name
    print("Script name:", sys.argv[0])
    
    # Access and print each command line argument using array indexing
    print(f"Argument 1:", sys.argv[1])
    print(f"Argument 2:", sys.argv[2])

if __name__ == "__main__":
    main()