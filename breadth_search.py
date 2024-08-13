from collections import deque
#Information stored:
#frontier is queue
#back pointer dictuionary key is vertex and value is vertex from which it was reached


def bfs(start, end, vertex_dict):

    backpdic = {start: None}
    #adds start to deque
    queue = deque()
    queue.append(start)

    while queue:
        if end in backpdic:
            break
#adds adj values into the dic
        current = queue.popleft()
        for adjv in vertex_dict[current.name].adj_list:     #To check if visited use bkp_d
            adjv = vertex_dict[adjv]
#if adj value is not already in the dic add it
            if adjv not in backpdic:
                queue.append(adjv)
                backpdic[adjv] = current
    new_list = []
    new_ver = end

# adds bath point into a new list
    while backpdic[new_ver] != None:

        new_list.append(new_ver)
        # x will become backpointer of old_x
        new_ver = backpdic[new_ver]
    new_list.append(start)

    return new_list
    # return backpdic