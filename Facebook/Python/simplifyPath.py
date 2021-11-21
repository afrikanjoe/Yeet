"""
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.


Input: path = "/a/./b/../../c/"
Output: "/c"


"""
class Solution:
    def simplifyPath(self, path):
        path_list = path.split("/")
        stack = []
        for i in path_list:
            if(i==".."):
                if(len(stack)>0):
                    stack.pop()
            elif(i=="."):
                continue
            elif(i==""):
                continue
            else:
                stack.append(i)
        res = "/".join(stack)
        while "//" in res:
            res = res.replace("//","/")
        if( len(res)>1 and res[-1]=="/"):
            res = res[:-1]
        elif(len(res)==0):
            return "/"
        if(res[0]!="/"):
            res = "/"+res
        return res
        
if __name__ == "__main__":
    path = "/a/./b/../../c/"
    print(Solution().simplifyPath(path))
