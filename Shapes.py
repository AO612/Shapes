import math # For pi
import sys # To exit
from abc import abstractmethod

class Shape (object): # inherits from object
# the following methods constitute a shape’s “interface”
# and should be redefined in all derived classes
          
    @abstractmethod
    def getType (self):
        pass # could also put return but this “implies” implementation
    @abstractmethod
    def getArea (self):
        pass
    @abstractmethod
    def getVolume (self):
        pass
    
class Point (Shape): # inherits from abstract class Shape
    def __init__ (self, name, x, y): 
        self._x = x # All shapes have coordinates
        self._y = y
        self._name = name # All shapes have a unique name to identify them.
    def getType (self): # This returns the shape type.
        return "Point"
    def getName (self): # This returns the shape name.
        return str(self._name)
    def __str__ (self):
        return "Coordinates = (" + str(self._x) + "," + str(self._y) + ")"
    def getX (self): # get/set coordinates methods
        return self._x
    def getY (self):
        return self._y
    def setX (self, x):
        self._x = x
    def setY (self, y):
        self._y = y
    def setName (self, name):
        self._name = name

class Circle (Point): # inherits from Point
    def __init__ (self, name, x, y, r):
        super().__init__(name, x, y) # This code is reused.
        self._r = 0 # setRadius initializes it only if r > 0
        self.setRadius(r)
    def getType (self):
        return "Circle"
    def getArea (self):
        return math.pi*self._r*self._r
    def __str__ (self):
        return super().__str__() + "; Radius = " + str(self._r)
    def getRadius (self): # get/set radius methods
        return self._r
    def setRadius (self, r):
        if r > 0:
            self._r = r

class Cylinder (Circle): # inherits from Circle
    def __init__ (self, name, x, y, r, h):
        super().__init__(name, x, y, r) # This code is reused.
        self._h = 0 # setHeight initializes it only if h > 0
        self.setHeight(h)
    def getType (self):
        return "Cylinder"
    def getArea (self):
        return 2.*super().getArea() + 2.*math.pi*self.getRadius()*self._h
    def getVolume (self):
        return super().getArea()*self._h
    def __str__ (self):
        return super().__str__() + "; Height = " + str(self._h)
    def getHeight (self): # get/set height methods
        return self._h
    def setHeight (self, h):
        if h > 0:
            self._h = h

class Sphere (Circle): # inherits from Circle
    def __init__ (self, name, x, y, r):
        super().__init__(name, x, y, r) # This code is reused.
    def getType (self):
        return "Sphere"
    def getArea (self):
        return 4.*math.pi*((self.getRadius())**2)
    def getVolume (self):
        return 4/3.*math.pi*((self.getRadius())**3)
    def __str__ (self):
        return super().__str__()

class Square (Point): # inherits from Point
    def __init__ (self, name, x, y, l):
        super().__init__(name, x, y) # This code is reused.
        self._l = 0 # setLength initializes it only if l > 0
        self.setLength(l)
    def getType (self):
        return "Square"
    def getArea (self):
        return ((self._l)**2)
    def __str__ (self):
        return super().__str__() + "; Length = " + str(self._l)
    def getLength (self): # get/set length methods
        return self._l
    def setLength (self, l):
        if l > 0:
            self._l = l

class Rectangle (Square): # inherits from Square
    def __init__ (self, name, x, y, l, w):
        super().__init__(name, x, y, l) # This code is reused.
        self._w = 0 # setWidth initializes it only if w > 0
        self.setWidth(w)
    def getType (self):
        return "Rectangle"
    def getArea (self):
        return ((self._l)*(self._w))
    def __str__ (self):
        return super().__str__() + "; Width = " + str(self._w)
    def getWidth (self): # get/set width methods
        return self._w
    def setWidth (self, w):
        if w > 0:
            self._w = w

class Cube (Square): # inherits from Square
    def __init__ (self, name, x, y, l):
        super().__init__(name, x, y, l) # This code is reused.
    def getType (self):
        return "Cube"
    def getArea (self):
        return 6.*((self._l)**2)
    def getVolume (self):
        return ((self._l)**3)
    def __str__ (self):
        return super().__str__()

def getWord(): # This function recieves a string from the user.
    loop = True
    while loop == True:
        answer = input()
        if answer == 'Exit': # If the string is 'Exit' it exits the program.
            print("Exiting the program.")
            sys.exit()
        elif answer == '':
            pass # If the string is empty it asks for another string.
        else: # The string is valid.
            loop = False # End loop
    return answer # Return that string

def getNumber(): # This function accepts only numbers including decimals and/or negative numbers
    loop = True
    while loop == True:
        inputString = input()
        if inputString == "": # Protect inputString[0] from an empty string
           pass # as that would raise an IndexError.
        elif inputString == 'Exit': # If the user enters Exit, exit the program.
            print("Exiting the program.")
            sys.exit()
        elif inputString.isdecimal(): # The user has inputted an integer.
            return float(inputString) # Return accepted value.
        elif inputString[0] == '-':
            if inputString[1:].isdecimal(): # The user has inputted a negative integer.
                return 0 - float(inputString[1:]) # Return accepted value.
        numberCounter, decimalPoints = 0, 0
        for i in range(0, len(inputString)): # Check string character by character.
            if inputString[i].isdecimal():
                numberCounter += 1 # Count the number of integer characters.
            if inputString[i] == '.':
                decimalPoints += 1 # Check the number of decimal points.
        if decimalPoints == 1: # If there is only one decimal point the string represents a float.
            if numberCounter == len(inputString) - 1: # If all the characters except the decimal point were integers, return the decimal number.
                return float(inputString)
            if inputString[0] == '-' and numberCounter == len(inputString) - 2:
            # If the string begins with a minus sign and all the other characters except the decimal point were integers, return the negative decimal number.
                return 0 - float(inputString[1:])
        print("Enter a suitable value.")

def getNameFromUser(shapes): # This function sets a name for the shape.
    loop = True # It imports shapes so it can see the existing names.
    while loop == True:
        print("What name should this shape have?")
        name = getWord()
        error = False
        for s in shapes:
            if name == s.getName():
                error = True # If the entered name is in use raise error.
                print("This name is already in use.")
        if error == False:
            loop = False # If no error return the entered name.
    return name

def getPoints(): # Get coordinates for the shape.
    print("What x coordinate should this shape have?")
    xCoord = getNumber()
    print("What y coordinate should this shape have?")
    yCoord = getNumber()
    return xCoord, yCoord

def getRadius(): # Get radius for the shape.
    print("What radius should this shape have?")
    radius = getNumber()
    return radius

def getHeight(): # Get height for the shape.
    print("What height should this shape have?")
    height = getNumber()
    return height

def getLength(): # Get length for the shape.
    print("What length should this shape have?")
    length = getNumber()
    return length

def getWidth(): # Get width for the shape.
    print("What width should this shape have?")
    width = getNumber()
    return width

def shapeTypes(shapes, shapeType, position = -1, name = 0 ): # This function is used for creating or modifying shapes. Shapes is the list, shapeType is the type of shape that needs to be created or modified, position can give the position in the list of a certain shape, name is the name of the shape.
    if shapeType == "Point" or shapeType == "Circle" or shapeType == "Cylinder" or shapeType == "Sphere" or shapeType == "Square" or shapeType == "Rectangle" or shapeType == "Cube": # Check for valid shape type.
        if name == 0: # If name == 0 get a name so the creation of a new shape.
            name = getNameFromUser(shapes)
        xCoord, yCoord = getPoints() # All shapes have points.
        if shapeType == "Point":
            newshape = Point(name, xCoord, yCoord)
            # Append new Point.
        elif shapeType == "Circle" or shapeType == "Cylinder" or shapeType == "Sphere": # Circles, cylinders and spheres share properties.
            radius = getRadius()
            if shapeType == "Circle":
                newshape = Circle(name, xCoord, yCoord, radius)
            elif shapeType == "Cylinder":
                height = getHeight()
                newshape = Cylinder(name, xCoord, yCoord, radius, height)
            elif shapeType == "Sphere":
                newshape = Sphere(name, xCoord, yCoord, radius)
        elif shapeType == "Square" or shapeType == "Rectangle" or shapeType == "Cube": # Squares, rectangles and cubes share properties.
            length = getLength()
            if shapeType == "Square":
                newshape = Square(name, xCoord, yCoord, length)
            elif shapeType == "Rectangle":
                width = getWidth()
                newshape = Rectangle(name, xCoord, yCoord, length, width)
            elif shapeType == "Cube":
                newshape = Cube(name, xCoord, yCoord, length)
        if position == -1: # Shape should be added to list.
            shapes.append(newshape)
        else: # Shape is already in list but needs to be modified.
            shapes[position] = newshape
    else: # The user is trying to create a shape that doesn't exist.
        print("You did not enter a valid answer.")
    return shapes # Return the updated list

def main():

    shapes = [] # Create list for shapes.
    loop = True
    while loop == True: # Loop so user can use program multiple times if desired.

        print("Type Create if you wish to introduce a new shape.\nType Print if you wish to print shapes.\nType Remove if you wish to remove a shape from the list.\nType Modify if you wish to modify a specific shape.\nType Exit if you wish to quit the program.")

        answer = input()
        if answer == "Exit":
            loop = False # If the user chooses to exit, end the while loop

        elif answer == 'Create':
            print("What shape do you want to create?\nThe options are Point, Circle, Cylinder, Sphere, Square, Rectangle and Cube.")
            answer = getWord() # Get shape type from user to pass on.
            shapeTypes(shapes, answer) # Pass on shapes list and the type of shape that should be added.

        elif answer == 'Print':
            if shapes: # Check if there is something in the list.
                print("Do you want to print a specific shape of all of them?\nEnter Specific for Option 1 or All for Option 2.")
                answer = getWord()
                if answer == "Specific":
                    printCheck = False
                    print("Enter the name of the shape you wish to print.")
                    answer = getWord()
                    for s in shapes: # Find shape with specified name.
                        if s.getName() == answer: # If found print the shape.
                            printCheck = True
                            print("Shape: " + s.getType() + " Name: '" + s.getName() + "' " + str(s) + " Area: " + str(s.getArea()) + " Volume: " + str(s.getVolume()))
                    if printCheck == False:
                        print("You did not enter a valid name.")
                elif answer == "All":
                    for s in shapes: # Print all the shapes.
                        print("Shape: " + s.getType() + " Name: '" + s.getName() + "' " + str(s) + " Area: " + str(s.getArea()) + " Volume: " + str(s.getVolume()))
                else:
                    print("You did not enter a valid answer.")
            else:
                print("There is nothing to print.")

        elif answer == 'Remove':
            if shapes:
                print("Enter the name of the shape you wish to remove.")
                remove = False
                answer = getWord()
                for s in shapes: # Find the shape that is to be removed.
                    if s.getName() == answer:
                        shapes.remove(s) # Remove the shape from the list.
                        remove = True
                if remove == False:
                    print("You did not enter a valid name.")
            else:
                print("There is nothing to remove.")

        elif answer == 'Modify':
            if shapes:
                print("Enter the name of the shape you wish to modify.")
                modify = False
                answer = getWord()
                for s in shapes: # Find the shape that is to be modified.
                    if s.getName() == answer:
                        position = shapes.index(s) # Save position in list
                        shapeType = s.getType() # Save the shape's type.
                        modify = True 
                if modify == True: # Recreate the shape with new parameters.
                    shapeTypes(shapes, shapeType, position, answer)
                    # Pass on the shapes list, and the type, position and name of the shape that should be modified.
                else:    
                    print("You did not enter a valid name.")
            else:
                print("There is nothing to modify.")

        else:
            print("You did not enter a valid answer.")

    print("Exiting the program.")
    sys.exit()

if __name__ == "__main__":
    main()