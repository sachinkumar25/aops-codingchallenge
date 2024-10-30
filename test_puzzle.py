# test_pyramid.py

def create_test_file(filename, target, pyramid):
    with open(filename, 'w') as f:
        f.write(f"Target: {target}\n")
        for row in pyramid:
            f.write(','.join(map(str, row)) + '\n')

def run_tests():
    # Test Case 1: Original example
    create_test_file('test1.txt', 720, [
        [2],
        [4,3],
        [3,2,6],
        [2,9,5,2],
        [10,5,2,15,5]
    ])
    
    # Test Case 2: Simple example
    create_test_file('test2.txt', 2, [
        [1],
        [2,3],
        [4,1,1]
    ])
    
    # Run tests
    print("Running test cases...")
    print("\nTest 1 (Target 720):")
    solve_pyramid_descent('test1.txt')
    
    print("\nTest 2 (Target 2):")
    solve_pyramid_descent('test2.txt')

if __name__ == "__main__":
    from puzzleprogram import solve_pyramid_descent
    run_tests()