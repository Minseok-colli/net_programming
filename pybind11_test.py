import pybind11_example

if __name__ == "__main__":
    x = 0
    y = 123.3
    n = 100000

    answer = pybind11_example.cpp_function(x,y,n)
    printf(f"     In Pyhton: return val {anser:.5f}")