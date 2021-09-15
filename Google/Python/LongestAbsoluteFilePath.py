"""
Suppose we have a file system that stores both files and directories. 
If we were to write this representation in code, it will look like this: "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext". Note that the '\n' and '\t' are the new-line and tab characters.

Every file and directory has a unique absolute path in the file system, which is the order of directories that must be opened to reach the file/directory itself, 
all concatenated by '/'s. Using the above example, the absolute path to file2.ext is "dir/subdir2/subsubdir2/file2.ext". Each directory name consists of letters, 
digits, and/or spaces. Each file name is of the form name.extension, where name and extension consist of letters, digits, and/or spaces.
"""

class Solution:
    def lengthLongestPathPat(self, path_input):
        paths= []
        prev = []
        
        # initial params
        lines = path_input.split('\n')
        curr_str = lines[0].replace('\n','')
        prev_t = 0 
        max_len = 0 

        # Handle the simple case
        if(len(lines)==1):
            if(len(lines[0].split('.'))>1):
                return len(lines[0])
            else:
                return 0

        for ln in lines[1:]:
            ln_count = ln.count('\t')
            ln_str = ln.replace('\t','').replace('\n','')
            #print(ln_str,ln_count,prev_t)
            if(ln_count==prev_t):
                prev_path_base = curr_str.split('/')[:-1]
                if(curr_str not in paths):
                    paths.append(curr_str)
                if(len(prev_path_base)==0):
                    paths.append(ln_str)
                    curr_str = ln_str
                else:
                    paths.append("/".join(prev_path_base)+'/'+ln_str)
            elif(ln_count>prev_t):
                curr_str = curr_str+'/'+ln_str
            else:
                paths.append(curr_str)
                if(curr_str.split('/')[:ln_count]):
                    curr_str = "/".join(curr_str.split('/')[:ln_count])+'/'+ln_str
                else:
                    curr_str = ln_str
                
            prev_t = ln_count

        if(curr_str not in paths):
            paths.append(curr_str)
        #print(paths)
        for pth in paths:
            if("." in pth):
                max_len = max(len(pth),max_len)
        return max_len

    def lengthLongestPath(self, input):
        lines = input.split('\n')
        
        path_elements = [] # [{tab_count, element}, ...] only contains a single path
        """
        assumptions:
        - root can be dir or file
        - no trailing ws 
        - all paths are valid, no invalid path like file.txt/invalid_path
        - here we call the / delimited parts in the path, elements. file and dir are elements.
        """
        
        max_path_len = 0
        
        
        for line in lines:
            # Compute tab count and actual element name
            tab_count = line.count('\t')
            element = line.replace('\t', '')
            
			# pop out the last element, of which the current element is not a sub-element
            while len(path_elements) and path_elements[-1]['tab_count'] >= tab_count:
                path_elements.pop()
            path_elements.append({
                'tab_count': tab_count,
                'element': element
            })
           
            if '.' in element:
                # element is a file
                curr_path_len = len('/'.join([e['element'] for e in path_elements]))
                max_path_len = max(max_path_len, curr_path_len)
            
            
        return max_path_len

        

if __name__ == "__main__":
    inp  = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    inp2 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    inp3 = "file"
    inp4 = "file1.txt\nfile2.txt\nlongfile.txt"
    inp5 = "a\n\tb.txt\na2\n\tb2.txt"
    inp6 = "a\n\taa\n\t\taaa\n\t\t\tfile1234567890123.txt\naaaaaaaaaaaaaaaaaaaaa\n\tsth.png"
    inp7 = "rzzmf\nv\n\tix\n\t\tiklav\n\t\t\ttqse\n\t\t\t\ttppzf\n\t\t\t\t\tzav\n\t\t\t\t\t\tkktei\n\t\t\t\t\t\t\thhmav\n\t\t\t\t\t\t\t\tbzvwf.txt"
    print(Solution().lengthLongestPath(inp))
    # print(Solution().lengthLongestPath(inp2))
    # print(Solution().lengthLongestPath(inp3))
    # print(Solution().lengthLongestPath(inp4))
    # print(Solution().lengthLongestPath(inp5))
    # print(Solution().lengthLongestPath(inp6))
    # print(Solution().lengthLongestPath(inp7))
