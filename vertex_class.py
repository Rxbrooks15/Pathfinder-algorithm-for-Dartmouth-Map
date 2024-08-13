#Name:Raine B
#Date: 11/15/2021
#Instructor: Vasanta (best teacher on campus)
#Purpose: Build Vertex class iinitialize varibles and draw the lines and dots

from cs1lib import *

class Vertex: #meant to keep track of the different intance variables that will be used for the vertices and edges that will be created

    #Constructor that initializes all required variables
    def __init__(self, name, x_cordinate, y_cordinate, adj_list = []):
        self.name = name
        self.x_cordinate = int(x_cordinate)
        self.y_cordinate = int(y_cordinate)
        self.adj_list = adj_list
        self.radius = 15
        self.width = 5
        self.back_pointer = None
        # self.length = length



    #draws the vertices
    def draw_one_vertex(self, r, g, b):
        set_stroke_color(r, g, b)
        set_fill_color(r, g, b)
        draw_circle(self.x_cordinate, self.y_cordinate, self.radius)

    #draws vertex edges
    def draw_one_edge(self, r, g, b, other_vertex):
        set_fill_color(r, g, b)
        set_stroke_color(r, g, b)
        set_stroke_width(5)
        draw_line(self.x_cordinate, self.y_cordinate, other_vertex.x_cordinate, other_vertex.y_cordinate)
    #draws all vertex edges
    def draw_all_edges(self, r, g, b, vertex_dict):  # ot param vertex_dict
        set_fill_color(r, g, b)
        set_stroke_color(r, g, b)
        for vertex in self.adj_list:
            vertex = vertex_dict[vertex]
            self.draw_one_edge(r, g, b, vertex)

    #draws the the connecting points
    def smallest_surround_square(self, x, y):
        x1 = self.x_cordinate - self.radius
        x2 = self.x_cordinate + self.radius
        y1 = self.y_cordinate - self.radius
        y2 = self.y_cordinate + self.radius

        if x > x1 and x < x2 and y > y1 and y < y2:
            return True
        return False


    #returns string of name and coordinates
    def __str__(self):

        element_res = self.name + "; Location: " + str(self.x_cordinate) + ", " + str(self.y_cordinate) + "; Adjacent Vertices: "
        for x in self.adj_list:
            if self.adj_list[len(self.adj_list) - 1] == x: # name of last element_res in list
                element_res += x
            else:
                element_res += x + ", "

        return element_res