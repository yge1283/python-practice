import re ,pickle,json
import class1


#re 라는 모듈을 실향 
# custlist=[
#           {'name': 'etw', 'gender': 'M', 'email': 'rainbow@naver.com', 'birthyear': '1999'},
#           {'name': '지은', 'gender': 'M', 'email': 'yuioh@naver.com', 'birthyear': '1987'},
#           {'name': '홍길동', 'gender': 'F', 'email': 'oiuy@naver.com', 'birthyear': '1977'}
#           ]
# # 손님의 리스트를 관리 
# page=2
# 페이지 값은 -1이다. 
# f=open('data.pickle','rb')
# custlist=pickle.load(f)
# page=len(custlist)-1

f=open('data.json','r')
custlist=json.load(f)
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
       result=class1.Customer()
       result.input1([])
   


                
    elif choice=="C":
        print("현재 고객 정보 조회")
        if page>= 0:         
          print(f'현재 페이지는 {page+1}쪽 입니다.')
          print(custlist[page])
        else:
         print("입력된 정보가 없습니다")


    elif choice == 'P':
        print("이전 고객 정보 조회")
        if page<=0:
            print('첫번쨰 페이지 입니다.')
            print(page)

        else:
            page-=1
            print(f"현제페이지는 {page+1}번쨰 페이지이다.")
            print(custlist[page])
    elif choice == 'N':
        print("다음 고객 정보 조회")
        if page>=len(custlist)-1:
            print("마지막 패이지 입니다.")
            print(page)
        else:
            page+=1
            print(f"현제페이지는 {page+1}번쨰 페이지이다.")
            print(custlist[page])




    elif choice=='D':
        print("고객 정보 삭제")
        choice1 = input("석제하려는 이메일을 입력하세요 >>>")
        delok=0
        # for i in range(0,len(custlist)):
        #     print(custlist[i])
        for i,item in enumerate(custlist):
         if item['email']== choice1:
             name=custlist.pop(i)['name']
             print(f'{name}고객님의 정보가 삭제되었습니다.')
             delok=1
             break
         if delok==0:
             print("등록되지 않은 이메일입니다.")
             print(custlist)


        



    elif choice=="U": 
        print("고객 정보 수정")
        while True:
            choice1 = input("수정하려는 이메일을 입력하세요 >>>")
            idx=-1
            for i in range(0, len(custlist)):
                if custlist[i]['email'] == choice1:
                    idx=i
                    break
            if idx==-1:
               print("등록되지 않은 이메일입니다.")
               break
            choice2=input('''
            다음 중 수정할 항목을 압력하세요
            (name,gender,birthyear)
            수정할 정보가 없으면 "exit"              
            >>>      ''')

            if choice2 in ('name','gender','birthyear'):
                custlist[idx][choice2]=input(f'수정할 {choice2}를 입력하세요 >>>')
                break
            elif choice2 == 'exit':
                break
            else:
                print("존재하지 않는 정보입니다.")
                break





    elif choice=="Q":
        # print("프로그램 종료")
        # f = open("data.pickle",'wb')
        # pickle.dump("customer",f)
        # f.close()
        # dumps -- 파일로 안되어 있는것은 
        # 파일로 바로 나감 sump

        f=open('data.json','w')
        json.dump(custlist,f,indent=2)
        f.close()
        break

# 변경되는 데이터를 불러와서 쓰는것 피클, 