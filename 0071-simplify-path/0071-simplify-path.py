class Solution:
    def dotLogic(self, cntDot:int, stack:List[str]) -> List[str]:
        # '.'이 한 개일 경우 삭제한다.
        if cntDot == 1:
            stack.pop()
            stack.pop()
        # '.'이 두 개일 경우 이전 파일 경로까지 삭제한다.
        elif cntDot == 2:
            cntSlash = 0
            while cntSlash < 2 and len(stack) > 0:
                if stack.pop() == '/':
                    cntSlash += 1
        return stack
    
    def simplifyPath(self, path: str) -> str:
        stack = []
        cntDot = 0
        for s in path:
            if s == '/':
                # '/'는 두 번 중복 되서는 안된다.
                if len(stack) > 0 and stack[-1] == '/': continue
                if cntDot != 0:
                    stack = self.dotLogic(cntDot, stack)
                    cntDot = 0
            elif s == '.':
                if cntDot == 0 and len(stack) > 0:
                    if stack[-1] == '/':
                        cntDot += 1
                elif cntDot > 0:
                    cntDot += 1
            else:
                cntDot = 0
            stack.append(s)
        
        # 반복문이 끝나면 마지막에 '/'인지 확인하고 맞으면 삭제한다.
        if len(stack) > 1 and stack[-1] == '/':
            stack.pop()
        # .이 남아있는지도 확인한다.
        if cntDot !=0:
            stack = self.dotLogic(cntDot, stack)
        # 빈 리스트이면 '/' 추가해서 반환
        if len(stack) == 0:
            stack.append('/')
        
        return ''.join(stack)