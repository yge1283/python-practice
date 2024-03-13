import json,re

def load_data():
    f=open('data.json','r')
    return json.load(f)

def save_data(custlist):
    f=open('data.json','w')
    json.dump(custlist,f,indent=2)
    f.close()
    
def insert_data(custlist):
    customer={'name':'','gender':'','email':'','birthyear':''}
    customer['name']=input('이름을 입력하세요>>>')
    while True:
        customer['gender']=input("성별을 입력하세요(M,F) >>>").upper()
        if customer['gender'] in ('M','F'):
         break
    while True:
        regex=re.compile('^[a-z][a-z0-9]{4,20}@[a-z]{2,10}[.][a-z]{2,10}')
        #영여소문자가 아닌(한글자), 영어소문자 or 숫자값()
        # {4,20}: 4~20자 까지만 쓰겠다
        #최대 21글자까지 올 수 있따. 
        while True:
            customer['email']=input("이메일 입력을 해주세요 >>>")
            check=regex.search(customer['email'])
            if check:
                break
            else:
                print("@를 포함한 정확한 이메일을 입력하세요 >>>")
        id_check = 0
        #0는 조건값은 FALSE로 되기 떄문에 
        # 똑같은 값을 받으면 구별하기 
        for i in custlist:
            if i['email'] == customer['email']:
                id_check=1
                break
        if id_check == 0:
            break 
        print("중복되는 이메일이 있습니다.")
    while True:
        customer['birthyear']=input('출생연도 4자리로 입력해 주세요 >>>')
        if len(customer['birthyear'])==4 and customer['birthyear'].isdigit():
            #입력받은게 숫자이면 isdigit, 두 조건을 다 만족하면
            break
    print(customer)
    custlist.append(customer)
    print(custlist)
    page = len(custlist)-1
    print(page)
    return page

def current(custlist,page):
    if page>= 0:         
          print(f'현재 페이지는 {page+1}쪽 입니다.')
          print(custlist[page])
    else:
         print("입력된 정보가 없습니다")


def before_data(custlist,page):
   
     if page <= 0:
            print('첫번쨰 페이지 입니다.')
            print(page)

     else:
            page-=1
            print(f"현제페이지는 {page+1}번쨰 페이지이다.")
            print(custlist[page])
     return page
        
     
def next_data(custlist,page):
           
        if page>=len(custlist)-1:
            print("마지막 패이지 입니다.")
            print(page)
        else:
            page+=1
            print(f"현제페이지는 {page+1}번쨰 페이지이다.")
            print(custlist[page])
            return page

def delete_data(custlist):
        choice1=input("고객님의 정보를 입력하세요")
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




def update_data(custlist):
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
                


     


