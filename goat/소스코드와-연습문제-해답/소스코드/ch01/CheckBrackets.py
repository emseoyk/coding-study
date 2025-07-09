# 생능 출판사: 초격차 자료구조와 알고리즘 with 파이썬(2023)
# 1장 스택

#=========================================================
# 코드 1.4: 괄호 검사 프로그램

from StackClass import ArrayStack

def checkBrackets(statement):
    stack = ArrayStack(100)		    # 공백상태의 스택을 준비
    for ch in statement:		    # 문자열의 각 문자에 대해
        if ch in ('{', '[', '('):	# ch가 {,[,( 중 하나이면
            stack.push(ch)		    # 스택에 삽입
        elif ch in ('}', ']', ')'):	# ch가 닫히는 괄호이면
            if stack.isEmpty() :	# 스택이 공백이면
                return False		# 조건 2 위반
            else :
                left = stack.pop()	# 문자를 pop해서 비교
                if (ch == "}" and left != "{") or \
                   (ch == "]" and left != "[") or \
                   (ch == ")" and left != "(") :
                    return False	# 조건 3 위반

    return stack.isEmpty()		    # True이면 괄호 검사 성공
					                # False이면 조건 1 위반



str1 = "{ A[(i+1)]=0; }"
str2 = "if ((x<0) && (y<3)"
str3 = "while (n<8)) {n++;}"
str4 = "arr[(i+1])=0;"

print(str1, " ---> ", checkBrackets(str1))
print(str2, " ---> ", checkBrackets(str2))
print(str3, " ---> ", checkBrackets(str3))
print(str4, " ---> ", checkBrackets(str4))

