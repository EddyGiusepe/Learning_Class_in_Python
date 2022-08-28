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
