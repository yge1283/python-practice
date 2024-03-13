import re 
import func
# 함수 호출하기 

custlist = func.load_data()
page=len(custlist)-1


while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
     >>>''' ).upper()  

    if choice=="I":   
         print("고객 정보 입력")
         page=func.insert_data(custlist)
         continue
                
    elif choice=="C":
        print("현재 고객 정보 조회")
        func.current(custlist,page)
        continue
    


    elif choice == 'P':
        print("이전 고객 정보 조회")
        func.before_data(custlist,page)
        continue



    elif choice == 'N':
        print("ㄱㄱ아아ㅏㄴㅇㅎ")
        func.next_data(custlist,page)
        continue
    

    elif choice=='D':
        print("고객 정보 삭제")
        func.delete_data(custlist)
        continue


        



    elif choice=="U": 
        print("고객 정보 수정")
        func.update_data(custlist)
        continue





    elif choice=="Q":
        # print("프로그램 종료")
        # f = open("data.pickle",'wb')
        # pickle.dump("customer",f)
        # f.close()
        # dumps -- 파일로 안되어 있는것은 
        # 파일로 바로 나감 sump

      func.save_data(custlist)
      print("프로그램 종료")
    break

# 변경되는 데이터를 불러와서 쓰는것 피클, 