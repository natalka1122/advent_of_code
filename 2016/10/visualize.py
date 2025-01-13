from graphviz import Digraph


def parse_graph(file_path):
    """Parse the graph file and return edges with labels."""
    edges = []
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith("bot"):
                # Parse lines like "bot X gives low to Y and high to Z"
                parts = line.split()
                source = f"bot {parts[1]}"
                low_target = f"bot {parts[6]}"
                high_target = f"bot {parts[11]}"
                edges.append((source, low_target, "L"))
                edges.append((source, high_target, "H"))
            elif line.startswith("value"):
                # Parse lines like "value X goes to bot Y"
                parts = line.split()
                source = f"value {parts[1]}"
                target = f"bot {parts[5]}"
                edges.append((source, target, ""))
    return edges


def visualize_graph(edges, output_file="graph_output"):
    """Visualize the graph with direction and labels."""
    dot = Digraph()

    # Add edges with labels
    for source, target, label in edges:
        dot.edge(source, target, label=label)

    # Render the graph
    dot.render(output_file, format="svg", cleanup=True)
    print(f"Graph has been rendered and saved as {output_file}.svg")


def main():
    # Input file path
    graph_file = "input.txt"

    # Parse the file and visualize the graph
    edges = parse_graph(graph_file)
    visualize_graph(edges)


if __name__ == "__main__":
    main()
