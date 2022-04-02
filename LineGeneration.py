import matplotlib.pyplot as plt
import numpy as np

def DDAGeneration(x0,y0,x1,y1):
    if abs(x1-x0) >= abs(y1-y0):
        span = abs(x1-x0)
    else:
        span = abs(y1-y0)
    
    dx = (x1-x0)/span
    dy = (y1-y0)/span

    x = x0
    y = y0
    
    x_pixel_coordinates, y_pixel_coordinates = [],[]

    for i in range(round(span)+1):
        # Generate Pixel Coordinates By Rounding Off The Values
        x_pixel_coordinates.append(round(x))
        y_pixel_coordinates.append(round(y))
        
        x=x+dx
        y=y+dy


    plt.title("DDA Generation Algorithm")
    DrawLine(x0,y0,x1,y1)
    # plt.plot(x_pixel_coordinates, y_pixel_coordinates, ":g")
    GeneratePixels(x_pixel_coordinates, y_pixel_coordinates)
    plt.yticks(range(min(y_pixel_coordinates)-1, max(y_pixel_coordinates)+3))
    plt.xticks(range(min(x_pixel_coordinates)-1, max(x_pixel_coordinates)+3))
    plt.grid()
    
    plt.show()

def BresenhamGeneration(x0,y0,x1,y1):
    x_coordinates,y_coordinates = [],[]

    def BresenhamLow(x0,y0,x1,y1):
        dx = x1 - x0
        dy = y1 - y0

        yi = 1

        if dy < 0:
            yi = -1
            dy = -dy
        
        d = 2*dy - dx
        y = y0

        

        for x in range(x0,x1+1):
            x_coordinates.append(x)
            y_coordinates.append(y)

            if d>0:
                y = y + yi
                d = d + 2 * (dy - dx)
            else:
                d = d + 2 * dy

    def BresenhamHigh(x0,y0,x1,y1):
        dx = x1 - x0
        dy = y1 - y0

        xi = 1

        if  dx < 0:
            xi = -1
            dx = -dx

        d = 2*dx - dy
        x = x0
        
        for y in range(y0,y1+1):
            x_coordinates.append(x)
            y_coordinates.append(y)

            if d > 0:
                x = x + xi
                d = d + 2 * (dx - dy)
            else:
                d = d + 2*dx

    if abs(y1-y0) < abs(x1-x0):
        if x0>x1:
            BresenhamLow(x1,y1,x0,y0)
        else:
            BresenhamLow(x0,y0,x1,y1)
    else:
        if y0 > y1:
            BresenhamHigh(x1,y1,x0,y0)
        else:
            BresenhamHigh(x0,y0,x1,y1)
    
    plt.title("Bresenham Line Generation")
    DrawLine(x0,y0,x1,y1)
    # plt.plot(x_coordinates, y_coordinates)
    GeneratePixels(x_coordinates, y_coordinates)
    plt.yticks(range(min(y_coordinates)-2, max(y_coordinates)+3))
    plt.xticks(range(min(x_coordinates)-1, max(x_coordinates)+3))
    plt.grid()
    plt.show()

def DrawLine(x0,y0,x1,y1):
    if abs(x1-x0) >= abs(y1-y0):
        span = abs(x1-x0)
    else:
        span = abs(y1-y0)
    
    dx = (x1-x0)/span
    dy = (y1-y0)/span

    x = x0
    y = y0
    
    x_line_coordinates, y_line_coordinates = [],[]
    for i in range(round(span)+1):
        x_line_coordinates.append(x)
        y_line_coordinates.append(y)

        x=x+dx
        y=y+dy
    plt.plot(x_line_coordinates, y_line_coordinates)
    

def GeneratePixels(x_coordinates, y_coordinates):
    dx = x_coordinates[-1] - x_coordinates[0]
    dy = y_coordinates[-1] - y_coordinates[0]
    
    if abs(dy) > abs(dx):
        data = np.zeros((len(set(y_coordinates))+2,len(set(x_coordinates))+1))
        for i in range(abs(dy)+1):
            row=i+1
            column=abs(x_coordinates[i]-x_coordinates[0])+1
            data[row][column] = 1
    else:
        data = np.zeros((len(set(y_coordinates)) +2,len(set(x_coordinates)) +1))
        for i in range(abs(dx)+1):
            row=abs(y_coordinates[i]-y_coordinates[0])+1
            column=i+1
            data[row][column] = 1
    
    if dy/dx >=0:
        plt.imshow(data, cmap="gray_r", origin="lower", extent=[min(x_coordinates)-1, max(x_coordinates)+1, min(y_coordinates)-1, max(y_coordinates)+2])
    else:
        # Translate y_cordinates by +1
        new_data = np.zeros((data.shape[0] + 1, data.shape[1]), np.byte)
        for i in range(0,data.shape[0]):
            new_data[i+1] = data[i]
            pass
        plt.imshow(new_data, cmap="gray_r", extent=[min(x_coordinates)-1, max(x_coordinates)+1, min(y_coordinates)-2, max(y_coordinates)+2])
    

lines=[(0,0,10,6),(0,1,5,11),(0,10,4,0),(0,20,10,15)]
for line in lines:
    DDAGeneration(line[0],line[1],line[2],line[3])
    BresenhamGeneration(line[0],line[1],line[2],line[3])
