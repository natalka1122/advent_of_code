import re
from graphviz import Digraph

# Read the graph description from a file
input_file = "graph_source.txt"

# Create a directed graph
dot = Digraph()

# Parse the file and add nodes and edges
with open(input_file, "r", encoding="UTF-16") as file:
    for line in file:
        line = line.strip()
        # if not line or ")): {" not in line:
        #     continue  # Skip empty lines or lines without edges

        # Split the line into parts
        line_match = re.match(r"\((\(\d+, \d+\)), (\(\d+, \d+\))\): ({\d+})", line)
        if line_match is None:
            continue
        left = line_match.group(1)
        right = line_match.group(2)
        label = line_match.group(3)
        if left < right:
            dot.edge(left, right, label=label)
            print(left, right, label)

        # # Handle labels
        # label = ''
        # if left.startswith('%') or left.startswith('&'):
        #     label = left[0]  # Extract the '%' or '&' symbol
        #     left = left[1:].strip()  # Remove the label symbol from the node

        # # Handle multiple target nodes
        # targets = [node.strip() for node in right.split(",")]

        # # Add edges to the graph
        # for target in targets:
        #     dot.edge(left, target, label=label)

# Render and save the graph
for engine in ["circo", "dot", "fdp", "neato", "osage", "patchwork", "sfdp", "twopi"]:
    # engine = "circo"
    # engine = "neato"
    # engine = "dot"
    output_file = "graph_output_" + engine
    dot.engine = engine
    dot.render(output_file, format="png", cleanup=True)
    print(f"Graph has been rendered and saved as {output_file}.png")
