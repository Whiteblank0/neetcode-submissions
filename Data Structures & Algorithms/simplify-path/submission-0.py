class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        paths = path.split("/")
        
        for path in paths:
            if not path or path == '.':
                continue
            elif path == '..':
                if st:
                    st.pop()
                else:
                    continue
            else:
                st.append(path)
        
        return '/' + '/'.join(st) if st else '/'