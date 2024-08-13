#Name:Raine B
#Date: 11/18/2021
#Instructor: Vasanta (best teacher on campus)
#Purpose: Construct map of dartmouth that draws vertices and connecting paths

from cs1lib import *
from load_graph import *
from breadth_search import *

WIDTH = 1012
HEIGHT = 811
mouse_press = False
start_y = None
goal = None

curr_x = 0
curr_y = 0
start_x = 0

mpressed = False
# global vertex_dict
vertex_dict = load_graph("dartmouth_graph.txt")
for item in vertex_dict:
    print(vertex_dict[item])
    print(vertex_dict[item].adj_list)

img = load_image("dartmouth_map.png")

found_start = False

def main_draw():
    global found_start, start_y, goal,start_y,start_x, mpressed, curr_y, curr_x, curr_vertex, curr_vertex2
    draw_image(img, 0, 0) #draws dartmouth map
    select_one = False
    select_two = False

    for vertex in vertex_dict: #draws the vertices
        a = vertex_dict[vertex]
        a.draw_one_vertex(0, 0, 1)
        vertex_dict[vertex].draw_all_edges(0.5, 1, 0, vertex_dict)

        if vertex_dict[vertex].smallest_surround_square(start_x, start_y): #star point of vertex
            curr_vertex = vertex_dict[vertex]
            select_one = True
            curr_vertex.draw_one_vertex(1, 0, 0)

        if vertex_dict[vertex].smallest_surround_square(curr_x, curr_y): #end point of vertex
            curr_vertex2 = vertex_dict[vertex]
            select_two = True
            curr_vertex2.draw_one_vertex(1, 0, 0)

        if select_two & select_one == True:  #if start and end point are selected

            if curr_vertex != curr_vertex2:
                # if start and end point are selected, then
                connector = bfs(curr_vertex, curr_vertex2, vertex_dict) #make connecting path bewteen two points
                v = 0
                while v < len(connector) - 1:
                    (connector[v]).draw_one_edge(1, 0, 0, (connector[v + 1]))
                    (connector[v]).draw_one_vertex(1, 0, 0)
                    v += 1
#updates coordinate points after the mouse has been movesd
def moved_mouse(x, y):

    global curr_x, curr_y

    curr_x = x
    curr_y = y
#updates the mpressed variable when the mouse is pressed
def mousepressed(x, y):

    global mpressed

    mpressed = True
#update when mouse is relased and cords
def mouser(x,y):

    global mpressed, start_x, start_y

    start_x = x
    start_y = y
    mpressed = False

start_graphics(main_draw, width=WIDTH, height=HEIGHT, mouse_move=moved_mouse, mouse_press=mousepressed, mouse_release=mouser)