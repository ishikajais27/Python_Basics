# +------------------+-----------------------------+---------------------------+----------------------+
# | Built-in Function| Work / Function             | Example Input             | Output               |
# +------------------+-----------------------------+---------------------------+----------------------+
# | print()          | Display output              | print("Hello")            | Hello                |
# | input()          | Take user input             | input("Enter: ")          | User entered value   |
# | len()            | Find length                 | len("Python")             | 6                    |
# | type()           | Check datatype              | type(10)                  | <class 'int'>        |
# | int()            | Convert to integer          | int("10")                 | 10                   |
# | float()          | Convert to decimal          | float("5.5")              | 5.5                  |
# | str()            | Convert to string           | str(100)                  | "100"                |
# | range()          | Generate sequence           | range(5)                  | 0 1 2 3 4            |
# | sum()            | Add all values              | sum([1,2,3])              | 6                    |
# | max()            | Largest value               | max([1,5,2])              | 5                    |
# | min()            | Smallest value              | min([1,5,2])              | 1                    |
# | sorted()         | Sort values                 | sorted([3,1,2])           | [1,2,3]              |
# | abs()            | Absolute value              | abs(-10)                  | 10                   |
# | round()          | Round decimal               | round(3.78)               | 4                    |
# | pow()            | Power calculation           | pow(2,3)                  | 8                    |
# | enumerate()      | Index + value together      | enumerate(["A","B"])      | (0,A) (1,B)          |
# | zip()            | Combine lists               | zip([1,2],[3,4])          | (1,3) (2,4)          |
# | map()            | Apply function to items     | map(str,[1,2,3])          | ['1','2','3']        |
# | filter()         | Filter values               | filter(even,[1,2,3,4])    | [2,4]                |
# | any()            | True if any value is True   | any([False,True])         | True                 |
# | all()            | True if all values True     | all([True,True])          | True                 |
# | open()           | Open file                   | open("data.txt")          | File object          |
# | isinstance()     | Check object type           | isinstance(5,int)         | True                 |
# | dir()            | Show methods/functions      | dir(list)                 | List methods         |
# | help()           | Documentation/help          | help(len)                 | Function details     |
# | eval()           | Evaluate expression         | eval("2+3")               | 5                    |
# | id()             | Memory address              | id(10)                    | Address number       |
# | chr()            | ASCII to character          | chr(65)                   | A                    |
# | ord()            | Character to ASCII          | ord('A')                  | 65                   |
# | reversed()       | Reverse sequence            | reversed([1,2,3])         | [3,2,1]              |
# +------------------+-----------------------------+---------------------------+----------------------+

# __doc__ - prints the documentation (description/help text) of a function.


# Built-in function documents

print(abs.__doc__)

print(int.__doc__)

print(input.__doc__)   # raw_input() was used in Python 2





def square(n):
    """
    This function returns square of a number
    """

    return n ** 2


print(square.__doc__)