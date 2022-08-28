# Chapter 8
## Classes

## <font color="orange">First example: A class representing a function</font>

To start with a familiar example, we return to the formula calculating atmospheric pressure $p$ as a
function of altitude $h$. The formula we used is a simpliﬁcation of a more general barometric formula, given by:

$$
p = p_0 e^{-{\frac{M g h}{R T}}} 
$$

As mentioned above, the idea of a class is to pack together data and
methods (or functions) that naturally operate on the data. We can make a
`class Barometric` for the formula at hand, with the variables $R$, $T$,$M$, $g$, and $p0$ as data, and a method $value(t)$ for evaluating the formula. All classes should also have a method named `__init__` to initialize the variables. 

Having deﬁned this class, we can create instances of the class with speciﬁc values of the parameter $T$, and then we can call the method value with $h$ as the only argument (see the code).


# <font color="orange">More general Python classes</font> 

Of course, Python classes have far more general applicability than just the representation of mathematical functions. A general Python class deﬁnition follows the recipe outlined in the example above, as follows:

```
class MyClass:
    def __init__(self, p1, p2,...):
        self.attr1 = p1
        self.attr2 = p2
...

def method1(self, arg):
    #access attributes with self prefix
    result = self.attr1 + ...
    ...
    #create new attributes if desired
    self.attrx = arg
    ...
    return result
def method2(self):
    ...
    print(...)
```

```
m = MyClass(p1,p2, ...)
m.new_attr = p3
```
# Protected Class Attributes 

For a more classical computer science example of a Python class, let us look at a class representing a bank account. Natural attributes for such a class will be the name of the owner, the account number, and the balance, and we can include methods for deposits, withdrawals, and printing information about the account. The code for deﬁning such a class could look like this (see the file .py)



