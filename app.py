def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = 5
fact = factorial(num)

print(f"The factorial of {num} is {fact}")

def change_cur_dir(path):
        """
        Given a directory, cd in the directory
        return the directory path
        """
        if path == self.root:
            os.chdir(path)
            self.cur_dir = path
            return path
