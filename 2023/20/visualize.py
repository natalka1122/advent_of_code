from graphviz import Digraph

# Read the graph description from a file
input_file = 'input.txt'

# Create a directed graph
dot = Digraph()

# Parse the file and add nodes and edges
with open(input_file, 'r') as file:
    for line in file:
        line = line.strip()
        if not line or "->" not in line:
            continue  # Skip empty lines or lines without edges

        # Split the line into parts
        parts = line.split("->")
        left = parts[0].strip()
        right = parts[1].strip()

        # Handle labels
        label = ''
        if left.startswith('%') or left.startswith('&'):
            label = left[0]  # Extract the '%' or '&' symbol
            left = left[1:].strip()  # Remove the label symbol from the node

        # Handle multiple target nodes
        targets = [node.strip() for node in right.split(",")]

        # Add edges to the graph
        for target in targets:
            dot.edge(left, target, label=label)

# Render and save the graph
output_file = 'graph_output'
dot.render(output_file, format='png', cleanup=True)

print(f"Graph has been rendered and saved as {output_file}.png")