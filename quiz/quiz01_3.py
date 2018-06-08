 students = [
        {
            "name": "kim",
            "kor" : 80,
            "kor" : 90,
            "math" : 80
            
        },

        {
            "name": "Lee",
            "kor" : 90,
            "kor" : 85,
            "math" : 85
            
        }

   


]
score = dict()
print(score)

avg =250/3
total =(80+90+80)


keys = ('name','kor','eng','avg','sum')
values = ("Kim", 80, 90, 80, avg, total)
score = dict(zip(keys, values))    
print(score)


score2 = dict()

avg = 260/3
total =(85+90+85)

keys = ('name', 'kor','eng','avg','sum')
values = ("Lee", 90, 85, 85, avg, total)
score2 = dict(zip(keys, values))   
print(score2)



#students=[score,score2]
print(students)

