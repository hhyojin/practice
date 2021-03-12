try:
    nums =[]
    nums.append(int(input('첫번째 숫자 입력: ')))
    nums.append(int(input('두번째 숫자 입력: ')))
    #nums.append(int(nums[0] / nums[1]))

    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print('에러 발생')
except ZeroDivisionError as err:
    print(err)
#except:
except Exception as err:
    print('알 수 없는 오류 발생')
    print(err)