# 피클 사용을 위해서 pickle을 임포트합니다.
import pickle

#피클로 객체 저장
def pwrite01():
    f = open("./sample/players.bin", "wb")
    data = { "baseball": 9 }
    pickle.dump(data, f)
    f.close()

#pwrite01()

def pread01():
    f = open("./sample/players.bin", "rb") # 꼭 바이너리 모드로
    data = pickle.load(f)
    f.close()
    print(data, type(data))

# pread01()

def pwrite01():
    #복수의 객체저장
    with open("./sample/players.bin", "wb") as f:
        pickle.dump({"baseball":9},f,1) #protocol 1
        pickle.dump({"basketball":5},f,2) #protocol 2
        pickle.dump({"soccer":11}, f,pickle.HIGHEST_PROTOCOL)
    
#pwrite01()

def pread02():
     # 복수의 객체 읽기
     with open("./sample/players.bin", "rb") as f:
         print(pickle.load(f))
         print(pickle.load(f))
         print(pickle.load(f))
        # print(pickle.load(f)) end of file Error

#pread02() #EOFError

def pread03():
     # 복수의 객체 읽기
    with open("./sample/players.bin", "rb") as f:
        data_list = []
        while True:
            try:
                data = pickle.load(f)
            except EOFError:
                break
            
            data_list.append(data)
    
    print(data_list)      
    
    
pread03()
