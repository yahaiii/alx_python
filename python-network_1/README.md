# Python Network Tasks
This repository contains the solutions for the Python Almost a Circle tasks for the ALX iSWE program. Some tasks build on the same file but are provided with accompanying test case files, and the directory structure is organized as follows:


```
python-inheritance/
│
├── 0-hbtn_status.py
├── 1-hbtn_status.py
├── 2-post_email.py
├── 4-error_code.py
├── 5-json_api.py
├── 6-my_github.py
├── README.md
```
## Task Descriptions
### 0. What's my status? #1
Write a Python script that fetches `https://alu-intranet.hbtn.io/status`

* You must use the package requests
* You are not allow to import packages other than requests
* The body of the response must be display like the following example (tabulation before -)

### 1. First Rectangle
Write the class Rectangle that inherits from Base:

* In the file models/rectangle.py
* Class Rectangle inherits from Base
* Private instance attributes, each with its own public getter and setter:
    * __width -> width
    * __height -> height
    * __x -> x
    * __y -> y
* Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
    * Call the super class with id - this super call with use the logic of the __init__ of the Base class
    * Assign each argument width, height, x and y to the right attribute
Why private attributes with getter/setter? Why not directly public attribute?

Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can “trust” these attributes.

### 2. Validate attributes
Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded):

* If the input is not an integer, raise the TypeError exception with the message: `<name of the attribute>` must be an integer. Example: width must be an integer
* If `width` or `height` is under or equals 0, raise the ValueError exception with the message: `<name of the attribute> must be > 0`. Example: `width must be > 0`
*  If x or y is under 0, raise the ValueError exception with the message: `<name of the attribute> must be >= 0`. Example: `x must be >= 0`

### 3. Area first
Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.

### 4. Display #0
Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here.

### 5. __str__
Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>

### 6. Display #1
Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y

### 7. Update #0
Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute:

* 1st argument should be the id attribute
* 2nd argument should be the width attribute
* 3rd argument should be the height attribute
* 4th argument should be the x attribute
* 5th argument should be the y attribute
This type of argument is called a “no-keyword argument” - Argument order is super important.

### 8. Update #1
Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes:

* **kwargs can be thought of as a double pointer to a dictionary: key/value
    *As Python doesn’t have pointers, **kwargs is not literally a double pointer – describing it as such is just a way of explaining its behavior in terms you’re already familiar with
* **kwargs must be skipped if *args exists and is not empty
* Each key in this dictionary represents an attribute to the instance
This type of argument is called a “key-worded argument”. Argument order is not important.

### 9. And now, the Square!
Write the class Square that inherits from Rectangle:

* In the file models/square.py
* Class Square inherits from Rectangle
* Class constructor: def __init__(self, size, x=0, y=0, id=None)::
    * Call the super class with id, x, y, width and height - this super call will use the logic of the __init__ of the Rectangle class. The width and height must be assigned to the value of size
    * You must not create new attributes for this class, use all attributes of Rectangle - As reminder: a Square is a Rectangle with the same width and height
All width, height, x and y validation must inherit from Rectangle - same behavior in case of wrong data
* The overloading __str__ method should return [Square] (<id>) <x>/<y> - <size> - in our case, width or height
As you know, a Square is a special Rectangle, so it makes sense this class Square inherits from Rectangle. Now you have a Square class who has the same attributes and same methods.

### 10. Square size
Update the class Square by adding the public getter and setter size

* The setter should assign (in this order) the width and the height - with the same value
* The setter should have the same value validation as the Rectangle for width and height - No need to change the exception error message (It should be the one from width)


## How to Use
To run any specific task, simply execute the corresponding Python file. For example, to run `python_class.py`, use the following command:

`python3 python_class.py`

Make sure you have Python installed on your system.

Happy coding!