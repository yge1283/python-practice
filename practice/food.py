import re,json, food_func
from tabulate import tabulate


# 함수 호출하기 

foodlist=food_func.load_data()

qus = input("""
          1. 식자재 등록
          2. 식자재 정보 수정 
          3. 식자재 내역 확인(유통기한 별)
          4. 식자재 내역 확인(남은 양 별)
          5. 식자재 검색         
          6. 식자재 유통기한 수정
          >>> """)

if qus == '1':
    print("식자재 등록")

    foodlist1 = {'name': '', 'qua': '', 'qua1': ''}

    foodlist1['name'] = input("식자재 이름 입력 >>>")
    foodlist1['qua'] = input("식자재 개수 입력 >>>")
    foodlist1['qua1'] = input("식자재 양을 입력('지금 있는 양/전체량') >>>")
    
    # while True:
    #     foodlist['date']= input("식자재 유통기한을 입력('2020-01-01') >>>")

    #     fodate = re.compile(r'\d{4}-\d{2}-\d{2}')

    #     if fodate.search(foodlist['date']):
    #         break
    #     else:
    #         print("정확한 유통기한 날짜를 입력해주세요")

    # 데이터를 딕셔너리에 저장


    # 저장된 데이터를 리스트에 추가

    # 테이블로 출력
  
    foodlist.append(foodlist1)



    food_func.save_data(foodlist)
    print(tabulate(foodlist, headers='keys'))




       




        
    



if qus=='2':
    print("식자재 정보 수정")
    print(tabulate(foodlist, headers='keys'))

if qus=='3':
    print("식자재 내역 확인") 

if qus=='4':
    print("식자재 검색창")

if qus=='5':
    print("식자재 검색창")

if qus=='6':
    print("식자재 저정보 저장")