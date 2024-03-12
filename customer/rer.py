import re
food_list=[]


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
    # food=['foname','fodate','foqual','foqua']
    # foname=input("식자재 이름을 입력 >>>")
    # fodate=input("식자재 유통기한을 입력('2020-01-01') >>>")
    foqua1=input("식자재 개수 입력 >>>")
    # foqua=input("식자재 양을 입력('지금 있는 양/전체량') >>>")

    

    while True:
      fodate1=input("식자재 유통기한을 입력('2020-01-01') >>>")
      fodate=re.compile('[0-9][4][/][0-9][2][/][0-9][2]')
      if fodate1=='1':
        break
      else:
        print("정확한 유통기한 날짜를 입력해주세요")
       

    foqua=input("식자재 양을 입력('지금 있는 양/전체량') >>>")


        
    



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
