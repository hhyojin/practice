# def profile(name, age, main_lang):
#     print("이름: {0}\t나이: {1}\t사용언어: {2}"\
#         .format(name, age, main_lang))

# profile("유",20,"파이썬")
# profile("김",25,"자바")

#같은 학년 같은 반 같은 수업인 경우 나이와 언어는 동일함. 이때 >>>>기본값<<<<< 사용

# def profile(name, age=17, main_lang="파이썬"):
#      print("이름: {0}\t나이: {1}\t사용언어: {2}"\
#          .format(name, age, main_lang))

# profile("유")
# profile("김")

#=============================================================================================

#>>>>>키워드 값<<<<<<<  사용
# def profile(name, age, main_lang):
#     print("이름: {0}\t나이: {1}\t사용언어: {2}"\
#         .format(name, age, main_lang))

# profile(name="유",main_lang="파이썬", age=20)
# profile(main_lang="자바",name="김", age=25,)

#=============================================================================================

#>>>>>가변인자<<<<<<<  사용
# def profile(name, age, lang1, lang2,lang3,lang4,lang5):
#     print("이름: {0}\t나이: {1}\t".format(name, age), end=" ") #end를 빈칸으로 하면 줄바꿈 없이 계속 다음 문장 출력
#     print(lang1, lang2,lang3,lang4,lang5)
def profile(name, age, *language):
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ") #end를 빈칸으로 하면 줄바꿈 없이 계속 다음 문장 출력
    for lang in language:
        print(lang, end=" ")
    print()

profile("유",20,"python","java","C","C++","C#", "JavaScript")
profile("유",20,"Kotlin","swift")