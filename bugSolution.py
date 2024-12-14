def function(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    else:
        return "Type error: cannot add different types"

result = function(5, '10')
print(result)
result2 = function(5,10)
print(result2)
result3 = function('5','10')
print(result3)