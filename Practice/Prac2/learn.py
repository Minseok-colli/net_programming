Nonstudy = False
Study = True


def study(subject):
    #공부를 하면
    if subject == True:
        print('공부잘됨')
        return True
        

    else:
        print('공부안됨')
        return False

#공부를 하기 싫다는 생각을 공부
Study_Nonstudy = Nonstudy and Study
study(Study_Nonstudy)
