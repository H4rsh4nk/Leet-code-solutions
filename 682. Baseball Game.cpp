class Solution:
    def simplifyPath(self, path: str) -> str:
        # absolute = '/asd/../../asd/'
        temp_list = []
        temp_list = path.split('/')
        print(temp_list)

        i = 0
        n = len(temp_list)

        while i < n:
            if temp_list[i] == '':
                temp_list.pop(i)
                n = n - 1
            elif temp_list[i] == '..':
                temp_list.pop(i)
                if i > 0:
                    i = i - 1
                    temp_list.pop(i)
                    n = n - 2
                else:
                    n = n - 1
            elif temp_list[i] == '.':
                temp_list.pop(i)
                n = n - 1
            else:
                i = i + 1
        print(temp_list)
        if len(temp_list) == 0:
            return '/'

        absolute = ''
        for i in range(len(temp_list)):
            absolute = absolute + '/' + temp_list[i]
        print(absolute)

        return absolute