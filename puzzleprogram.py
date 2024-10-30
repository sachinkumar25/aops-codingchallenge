# Hey! This is my solution for the pyramid descent puzzle
# Had to scratch my head a bit but finally got it working!
# Basic idea: we start from top and try all possible paths going down
# using recursion. If we find a path that works, we return it

def read_input_file(filename):
    # Reading the file and getting our target number and pyramid structure
    # The file looks like:
    # Target: 720
    # 2
    # 4,3
    # etc...
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Get the target number from first line
    target_line = lines[0].strip()
    target = int(target_line.split(":")[1].strip())
    
    # Convert the rest of the lines into our pyramid
    # Had to be careful with the commas and empty spaces!
    pyramid = []
    for line in lines[1:]:
        # Only add non-empty lines (got some weird bugs without this check)
        if line.strip():
            row = [int(num.strip()) for num in line.strip().split(',')]
            pyramid.append(row)
            
    return target, pyramid

def find_path(pyramid, target, row, index, current_product):
    # We multiply numbers as we go down and try both left and right paths
    # If we find a path that works, we return it, otherwise return None
    
    # First multiply current number with our running product
    current_product *= pyramid[row][index]
    
    # If we reached the bottom, check if we hit our target
    if row == len(pyramid) - 1:
        return "" if current_product == target else None
    
    # If our product is already too big and next row has all positive numbers,
    # we can stop here since it'll only get bigger.
    if row < len(pyramid) - 1:
        if current_product > target and all(num > 0 for num in pyramid[row + 1]):
            return None
    
    # Try going left first
    left = find_path(pyramid, target, row + 1, index, current_product)
    if left is not None:
        return "L" + left
    
    # If left didn't work, try right
    right = find_path(pyramid, target, row + 1, index + 1, current_product)
    if right is not None:
        return "R" + right
    
    # No path found
    return None

def solve_pyramid_descent(filename):
    # Main function that puts everything together
    try:
        # Read our input file
        target, pyramid = read_input_file(filename)
        
        # Start from the top with initial product of 1
        # (since multiplying by 1 doesn't change anything)
        result = find_path(pyramid, target, 0, 0, 1)
        
        # Print what we found!
        if result:
            print("Found it! Path:", result)
        else:
            print("No path found... maybe try different numbers?")
        
        return result
        
    except Exception as e:
        # Basic error handling - just print what went wrong
        print(f"Oops, something went wrong: {str(e)}")
        return None

# Run our program!
if __name__ == "__main__":
    solve_pyramid_descent('pyramid_sample_input.txt')