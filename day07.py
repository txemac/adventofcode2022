from dataclasses import dataclass
from typing import List
from typing import Optional

# input = """$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k
# """.splitlines()

file = open("day07_input.txt", "r")
input = file.readlines()
file.close()


class File:
    name: str
    size: int

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __str__(self):
        return self.name


@dataclass
class Dir:
    name: str
    father: Optional["Dir"]
    files: List[File]
    dirs: List["Dir"]

    def __init__(self, name: str, father: Optional["Dir"]):
        self.name = name
        self.father = father
        self.files = []
        self.dirs = []

    def __str__(self):
        return self.name

    @property
    def size(self) -> int:
        result = sum([file.size for file in self.files])
        result += sum([dir.size for dir in self.dirs])
        return result

    def get_dir_by_name(
            self,
            name: str,
    ) -> "Dir":
        return [dir for dir in self.dirs if dir.name == name][0]


def get_dirs_size_max(
        root: Dir,
        size_max: int = 100000,
        result: Optional[List[Dir]] = None,
) -> List["Dir"]:
    result = [] if not result else result

    if root.size <= size_max:
        result.append(root)
    for dir in root.dirs:
        result += get_dirs_size_max(root=dir, size_max=size_max)
    return result


root = Dir(name="/", father=None)
current_folder = root

for line in input:
    line = line.split()
    if line[0] == "$":
        if line[1] == "ls" or line[2] == "/":
            continue
        if line[2] == "..":
            current_folder = current_folder.father
        else:
            current_folder = current_folder.get_dir_by_name(name=line[2])
    elif line[0] == "dir":
        current_folder.dirs.append(Dir(name=line[1], father=current_folder))
    else:
        current_folder.files.append(File(size=int(line[0]), name=line[1]))

# assert root.size == 48381165
# assert root.get_dir_by_name(name="d").size == 24933642
# assert root.get_dir_by_name(name="a").size == 94853
# assert root.get_dir_by_name(name="a").get_dir_by_name("e").size == 584

total_size = 0
dirs = get_dirs_size_max(root, size_max=100000)
for dir in dirs:
    total_size += dir.size

# assert total_size == 95437
print(total_size)
