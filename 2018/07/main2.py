FILENAME, WORKER_COUNT, ADD_VALUE = "demo.txt", 2, 0  # expected 15
FILENAME, WORKER_COUNT, ADD_VALUE = "input.txt", 5, 60


class Node:
    def __init__(self, name: str) -> None:
        self.name = name
        self.time: int = ADD_VALUE + ord(name) - ord("A") + 1
        self.reqire: set[str] = set()

    def add_req(self, exclude: str) -> None:
        self.reqire.add(exclude)


class Worker:
    def __init__(self) -> None:
        self.is_busy = False
        self.timer = 0
        self.work = ""

    def __repr__(self) -> str:
        return str(self.__dict__)

    def tick(self) -> str | None:
        if self.timer <= 0:
            raise NotImplementedError
        self.timer -= 1
        if self.timer == 0:
            self.is_busy = False
            done_work = self.work
            self.work = ""
            return done_work
        return None

    def assign(self, node: Node) -> None:
        if self.is_busy or self.timer > 0 or len(self.work) > 0:
            raise NotImplementedError
        self.is_busy = True
        self.work = node.name
        self.timer = node.time


def main() -> None:
    nodes: dict[str, Node] = dict()
    with open(FILENAME, "r") as file:
        for line in file:
            n1 = line.split(" ")[1]
            n2 = line.split(" ")[7]
            if n1 not in nodes:
                nodes[n1] = Node(n1)
            if n2 not in nodes:
                nodes[n2] = Node(n2)
            nodes[n2].add_req(n1)
    executed: set[str] = set()
    workers: list[Worker] = [Worker() for _ in range(WORKER_COUNT)]
    t = 0
    while len(nodes) > 0 or any(map(lambda x: x.is_busy, workers)):
        for worker in workers:
            if worker.is_busy:
                done_job = worker.tick()
                if done_job is not None:
                    executed.add(done_job)
                    print(done_job, end="")
        for worker in workers:
            if worker.is_busy:
                continue
            for node_name in sorted(nodes):
                if all(map(lambda x: x in executed, nodes[node_name].reqire)):
                    worker.assign(nodes[node_name])
                    del nodes[node_name]
                    break
        t += 1
    print()
    print(t - 1)


if __name__ == "__main__":
    main()
