"""
    设计一个内存文件系统，模拟以下功能：

    实现文件系统类:

        FileSystem() 初始化系统对象
        List<String> ls(String path)
            如果 path 是一个文件路径，则返回一个仅包含该文件名称的列表。
            如果 path 是一个目录路径，则返回该目录中文件和 目录名 的列表。答案应该 按字典顺序 排列。

        void mkdir(String path) 根据给定的路径创建一个新目录。给定的目录路径不存在。如果路径中的中间目录不存在，您也应该创建它们。
        void addContentToFile(String filePath, String content)
        如果 filePath 不存在，则创建包含给定内容 content的文件。
        如果 filePath 已经存在，将给定的内容 content附加到原始内容。
        String readContentFromFile(String filePath) 返回 filePath下的文件内容。

https://leetcode.cn/problems/design-in-memory-file-system/description/
"""
from typing import List


class Trie(object):
    def __init__(self):
        self.children = {}
        self.content = ""
        self.is_file = False
        self.name = ""


class FileSystem:

    def __init__(self):
        self._root = Trie()

    def ls(self, path: str) -> List[str]:
        result = []

        if path == "/":
            result.extend(self._root.children.keys())
            return sorted(result)

        cur = self._root

        path_list = path[1:].split("/")

        for abs_path in path_list:
            if abs_path not in cur.children:
                return []
            cur = cur.children[abs_path]

        result.extend(cur.children.keys())

        if cur.is_file:
            result.append(cur.name)
        return sorted(result)

    def mkdir(self, path: str) -> None:
        self._get_or_mkdir_trie(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = self._get_or_mkdir_trie(filePath)
        path.content += content
        path.is_file = True

    def readContentFromFile(self, filePath: str) -> str:
        path = self._get_or_mkdir_trie(filePath)
        return path.content

    def _get_or_mkdir_trie(self, path):
        cur = self._root

        path_list = path[1:].split("/")

        for abs_path in path_list:
            if abs_path not in cur.children:
                cur.children[abs_path] = Trie()
            cur = cur.children[abs_path]
            cur.name = abs_path
        return cur
