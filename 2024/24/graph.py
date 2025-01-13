from graphviz import Digraph

def parse_graph(file_path):
    """Parse the graph file and return edges with labels."""
    edges = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or "->" not in line:
                continue

            # Parse the format "source OPERATOR source -> target"
            parts = line.split("->")
            sources, target = parts[0].strip(), parts[1].strip()
            if " " in sources:
                left, operator, right = sources.split(" ")
                edges.append(((left, right), operator, target))
    return edges

def visualize_graph(edges, output_file='graph_output'):
    """Visualize the graph with operators as labels."""
    dot = Digraph()

    # Add edges with labels
    for (source1, source2), operator, target in edges:
        dot.edge(source1, target, label=operator)
        dot.edge(source2, target, label=operator)

    # Render the graph
    dot.render(output_file, format='png', cleanup=True)
    print(f"Graph has been rendered and saved as {output_file}.png")

def main():
    # Input file path
    graph_file = 'input.txt'

    # Parse the file and visualize the graph
    edges = parse_graph(graph_file)
    visualize_graph(edges)

if __name__ == "__main__":
    main()