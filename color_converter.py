def rgb_to_hex(r, g, b):
    """
    Converts an RGB color value to a Hex color string.

    Args:
        r (int): Red component (0-255).
        g (int): Green component (0-255).
        b (int): Blue component (0-255).

    Returns:
        str: The hexadecimal color string (e.g., "#ffffff").
    """
# https://python-academy.org/en/handbook/format
# according to the souce above the format function formats strings
# so to catch the corner case of any rgb value being 15 or less a 0 can be 
# added to the output

# https://realpython.com/ref/builtin-functions/format/
# based on the source above the added zeros could be put outside the curly braces
# at least that is my current theory at the moment
    
    #adding if statments to include leading zeros if there can be any
    #if any of the rgb values are 15 or less then a leading zero will be added
    #since the format function seems to not add them- thus they will be a hardcoded addition\

    #chceking if all values are less than 16
    if (r <= 15 and g <= 15 and b <=15):
        return "#0{:x}0{:x}0{:x}".format(r, g, b)
        
    #checking if only r and g values are less than 16 
    #(including  requirement of b being greater than 15 to prevent 
    #this statment also being used after the statment above)
    if(r <= 15 and g <= 15 and b > 15):
        return "#0{:x}0{:x}{:x}".format(r, g, b)

    #checking if only g and b are less than 16
    if(r > 15 and g <= 15 and b <= 15):
        return "#{:x}0{:x}0{:x}".format(r, g, b)
        
    #checking if only r and b are less than 16
    if(r <= 15 and g > 15 and b <= 15):
        return "#0{:x}{:x}0{:x}".format(r, g, b)

    #checking if only r is less than 16
    if(r <= 15 and g > 15 and b > 15):
            return "#0{:x}{:x}{:x}".format(r, g, b)

    #checking if only g is less than 16
    if(r > 15 and g <= 15 and b > 15):
        return "#{:x}0{:x}{:x}".format(r, g, b)

    #checking if only b is less than 16
    if(r > 15 and g > 15 and b <= 15):
        return "#{:x}{:x}0{:x}".format(r, g, b)

    #it is assumed if we get this far that all values are above 15
    else:
    #if any rgb value is greater than 15 then the code here works (all other code
    #has been added)
        return "#{:x}{:x}{:x}".format(r, g, b)
