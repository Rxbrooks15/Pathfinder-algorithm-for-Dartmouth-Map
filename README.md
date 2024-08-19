Methods---->
Overview:
The purpose of this project was to create a program that accurately reads a file, constructs a graph, and performs various operations on this graph, such as running a Breadth-First Search (BFS), implementing backchaining, and drawing the graph efficiently. Additionally, the project required correct selection and manipulation of the start and goal vertices, proper pathfinding from start to goal, and a clear presentation of the results with well-organized test cases. The emphasis on correctness and clarity was crucial for ensuring that the program would not only function as intended but also be easy to understand and maintain.
<img width="800" alt="pathfinder" src="https://github.com/user-attachments/assets/f8f21b42-7a0b-4a1f-96ed-cb1b5b05796f">

Process
File Reading and Graph Construction:

The first step in the project was to implement a method for reading input data from a file and using this data to build the graph. This was a foundational task, as the accuracy of graph construction directly influenced the correctness of subsequent operations. The graph was represented using an adjacency list or matrix, ensuring that it was both space-efficient and suitable for the graph traversal algorithms used later.
Breadth-First Search (BFS):

BFS was implemented as the primary traversal algorithm. This was chosen due to its effectiveness in finding the shortest path in an unweighted graph. The implementation involved systematically exploring the graph level by level, ensuring that all reachable vertices were visited in the correct order.
Backchaining Implementation:

Backchaining was implemented to reconstruct the path from the goal vertex back to the start vertex after BFS had identified the shortest path. This involved storing parent pointers during the BFS traversal and then using these pointers to trace the path backward.
Graph Drawing:

![dartmouth_map](https://github.com/user-attachments/assets/b74da2d3-febc-4822-aeaa-32401c2e435d)
The graph drawing was implemented with a focus on both correctness and efficiency. The goal was to visually represent the graph structure in a way that was easy to interpret. The implementation utilized an appropriate layout algorithm to ensure that the vertices and edges were displayed clearly and without unnecessary overlap.
Start and Goal Vertex Selection:

Methods were developed to allow for the correct selection of the start and goal vertices within the graph. This was a crucial feature, as the selected vertices determined the paths explored by BFS and the final path drawn.
Path Drawing from Start to Goal:

Once the BFS and backchaining were completed, the program was tasked with drawing the path from the start vertex to the goal vertex. This involved highlighting the path on the graph and ensuring that it was visually distinct from other edges in the graph.
Selection of Test Runs and Screenshots:

To validate the correctness of the implementation, a series of test runs were conducted. Screenshots were taken to capture the results, focusing on cases that best demonstrated the program's capabilities. The selected test cases were diverse, covering various graph structures and scenarios.
Code Design and Style:

Throughout the project, attention was paid to clear design and organization. Variable names, function names, and comments were carefully chosen to enhance readability and maintainability. The use of instance variables was handled correctly, ensuring that the state of the program was managed appropriately across different parts of the code.
Conclusion
This project was successful in meeting the outlined criteria, ensuring both correctness in graph operations and clarity in code structure. The methods implemented provided a robust solution for reading, constructing, and manipulating graphs, while also presenting the results in a clear and visually informative manner.

