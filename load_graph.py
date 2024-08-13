#Name:Raine B
#Date: 11/16/2021
#Instructor: Vasanta (best teacher on campus)
#Purpose: splits elements in the dartmouth_graph text file and prints information using the vertex class

from vertex_class import Vertex

 #splitting the line first by semi colon, then by comas for the 2nd and third sections

def parse_line(line):

    section_split = line.split(";")
    vertex_name = section_split[0].strip()

    #splits all elements in file by their comma
    adjacent_vertices = section_split[1].strip().split(",")
    coordinates = section_split[2].strip().split(",")
    x_c = coordinates[0]
    y_c = coordinates[1]

    # add all except empty strings
    adj_list = []
    for a in adjacent_vertices:
        if a:
            adj_list.append(a.strip())

    return vertex_name, adj_list, x_c, y_c

#reads the file(filename) and splits it
def load_graph(filename):
    #creating new dictionary
    vertex_dict = {}

    file = open(filename, "r")

    for f in file:

        if len(f.split(";")) == 3:
            vertex_name, adjacent, x, y = parse_line(f)

            v1 = Vertex(vertex_name, x, y, adjacent)
            vertex_dict[vertex_name] = v1

    return vertex_dict

#adds adj value to the list
def sec_time(filename, vertex_dict):

    file = open(filename, "r")
    # file = open("vertices.txt", "w")
    # filename = "vertices.txt"

    for line in file:

        vertex_name, adj_list, x_coord, y_coord = parse_line(line)

        for i in adj_list:

            x = vertex_dict[i]
            vertex_dict[vertex_name].adj_list.append(x)
    file.close()
