class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        rows = len(image)
        cols = len(image[0])

        def dfs(image, curr_x, curr_y, old_colour):

            image[curr_x][curr_y] = newColor
            visited.add((curr_x, curr_y))

            for dx, dy in directions:
                new_x = curr_x + dx
                new_y = curr_y + dy

                if 0 <= new_x < rows and 0 <= new_y < cols and image[new_x][new_y] == old_colour and (
                new_x, new_y) not in visited:
                    dfs(image, new_x, new_y, old_colour)

            return

        visited = set()
        dfs(image, sr, sc, image[sr][sc])
        return image
