class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        def extract_content(root_path, file):

            content = file[file.index("(") + 1: file.index(")")]
            filename = file[: file.index("(")]
            file_directory = root_path + "/" + filename

            if content not in contents:
                contents[content] = []
            contents[content].append(file_directory)

        contents = {}
        ans = []

        for directories in paths:
            directory = directories.split(" ")
            root = directory[0]

            for file in directory[1:]:
                extract_content(root, file)

        for files in contents.values():
            if len(files) > 1:                              # For case where no files have common contents
                ans.append(files)

        return ans
