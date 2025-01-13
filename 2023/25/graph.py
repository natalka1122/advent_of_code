from graphviz import Digraph

# Read the graph description from a file
input_file = "demo.txt"
input_file = "input.txt"

# Create a directed graph
dot = Digraph()

# Parse the file and add nodes and edges
with open(input_file, "r") as file:
    for line in file:
        line = line.strip()
        if not line or ":" not in line:
            continue  # Skip empty lines or lines without edges

        # Split the line into source and targets
        source, targets = line.split(":")
        source = source.strip()
        targets = [node.strip() for node in targets.split()]

        # Add edges to the graph
        for target in targets:
            if source in ("sgc", "xvk", "pzc", "vps", "cvx", "dph"):
                continue
            if target in ("sgc", "xvk", "pzc", "vps", "cvx", "dph"):
                continue
            dot.edge(source, target, label=target)

# Render and save the graph
# for engine in ["circo", "dot", "fdp", "neato", "osage", "patchwork", "sfdp", "twopi"]:
for engine in ["dot"]:
    format = "svg"
    output_file = f"{input_file.split('.')[0]}_output_{engine}"
    dot.engine = engine
    dot.render(output_file, format=format, cleanup=True)
    print(f"Graph has been rendered and saved as {output_file}.{format}")
