import re
food_list=[]
from tabulate import tabulate

qus=input("""
          1. 식자재 등록
          2. 식자재 정보 수정 
          3. 식자재 내역 확인(유통기한 별)
          4. 식자재 내역 확인(남은 양 별)
          5. 식자재 검색         
          6. 식자재 유통기한 수정
          >>> """)


if qus=='1':
    print("식자재 등록")


    foname=input("식자재 이름 입력 >>>")
    foqua=input("식자재 개수 입력 >>>")
    foqua1=input("식자재 양을 입력('지금 있는 양/전체량') >>>")


    while True:
      fodate1=input("식자재 유통기한을 입력('2020-01-01') >>>")

      fodate=re.compile(r'\d{4}-\d{2}-\d{2}')

      if fodate.search(fodate1):
        break
      else:
        print("정확한 유통기한 날짜를 입력해주세요")


foodlist={'이름':foname,'개수': foqua,'양': foqua1 ,'유통기한':fodate1}
print(tabulate(foodlist,headers=['이름',"개수","양","유통기한"]))

    
       




        
    



if qus=='2':
    print("식자재 정보 수정")


if qus=='3':
    print("식자재 내역 확인")

if qus=='4':
    print("식자재 검색창")

if qus=='5':
    print("식자재 검색창")

if qus=='6':
    print("식자재 양을 수정")
