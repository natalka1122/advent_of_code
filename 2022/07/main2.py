from __future__ import annotations

FILENAME = "demo.txt"  # expected 95437
FILENAME = "input.txt"

TOTAL = 70000000
REQUIRED = 30000000


class File:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size


class Directory:
    def __init__(self, parent: Directory | None = None) -> None:
        self.parent = parent
        self.files: set[File] = set()
        self.dirs: dict[str, Directory] = dict()

    def add_file(self, filesize: int, filename: str) -> None:
        self.files.add(File(filename, filesize))

    def add_dir(self, name: str) -> None:
        self.dirs[name] = Directory(parent=self)

    @property
    def size(self) -> int:
        files_size = sum(map(lambda x: x.size, self.files))
        dirs_size = sum(map(lambda x: x.size, self.dirs.values()))
        return files_size + dirs_size


def main() -> None:
    root = Directory()
    current_directory = root
    dirs = [current_directory]
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            print(line)
            if line == "$ cd /":
                current_directory = root
                is_ls = False
            elif line == "$ ls":
                is_ls = True
            elif line.startswith("$ cd "):
                cd = line.split(" ")[2]
                if cd == "..":
                    if current_directory.parent is None:
                        raise NotImplementedError
                    current_directory = current_directory.parent
                else:
                    current_directory = current_directory.dirs[cd]
            elif is_ls:
                if line.startswith("dir "):
                    dirname = line.split(" ")[1]
                    current_directory.add_dir(dirname)
                    dirs.append(current_directory.dirs[dirname])
                else:
                    filesize, filename = line.split(" ")
                    current_directory.add_file(int(filesize), filename)

            else:
                raise NotImplementedError

    target_size = REQUIRED - TOTAL + root.size
    result = None
    for directory in dirs:
        d_size = directory.size
        if d_size >= target_size:
            if result is None or result > d_size:
                result = d_size
    print(result)


if __name__ == "__main__":
    main()
