# Task 1

print("=== Task1 ===")

def find_and_print(messages, current_station):

    # your code here

    SongShan_Xindian = ["Songshan","NanjingSanmin","Taipei Arena","Nanjing Fuxing","Songjiang Nanjing",
        "Zhongshan","Beimen","Ximen","Xiaonanmen","Chiang Kai-Shek MemorialHall","Guting",
        "Taipower Building","Gongguan","Wanlong","Jingmei","Dapinglin","Qizhang","Xindian City Hall","Xindian","Xiaobitan"]
    people_and_station = {}
    distance = []
    people = []

    for  person,message in messages.items():
        for station in SongShan_Xindian:
            if station.title() in message.title():
                people_and_station[person] = station
                break


    for person,station in people_and_station.items():
        people.append(person)
        if station == "Xiaobitan":
            if current_station != "Xiaobitan":
                number = abs(SongShan_Xindian.index(current_station)-SongShan_Xindian.index("Qizhang")+1)  
                distance.append(number)
            else:
                number = abs(SongShan_Xindian.index(current_station)-SongShan_Xindian.index(station))  
                distance.append(number)
        else:
            if current_station == "Xiaobitan":
                number = abs(SongShan_Xindian.index(current_station)-SongShan_Xindian.index("Qizhang")+1)  
                distance.append(number)
            else:
                number = abs(SongShan_Xindian.index(current_station)-SongShan_Xindian.index(station))  
                distance.append(number)
        closest =  distance.index(min(distance))
    print(people[closest])

    


messages={
"Leslie":"I'm at home near Xiaobitan station.",
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Vivian":"I'm at Xindian station waiting for you."
}



find_and_print(messages,"Wanlong") # print Mary
find_and_print(messages,"Songshan") # print Copper
find_and_print(messages,"Qizhang") # print Leslie
find_and_print(messages,"Ximen") # print Bob
find_and_print(messages,"Xindian City Hall") # print Vivian





# Task2

# your code here, maybe
print("=== Task2 ===")

schedules = {}
price = []
rate = []

def book(consultants, hour, duration, criteria):
    # your code here

    for consultant in consultants:
        if consultant["name"] not in schedules:
            schedules[consultant["name"]] =  {i:True for i in range(0,25)}
            price.append((consultant["price"],consultant["name"]))
            rate.append((consultant["rate"],consultant["name"]))
    
    price.sort()
    rate.sort(reverse=True)
    
    if criteria == "price":
        sort_by = price
    elif criteria == "rate":
        sort_by = rate


    time_is_available = True
    appointment_status = ""
    for _,person in sort_by:
        for i in  range(duration):
            time_is_available = True
            if schedules[person][hour+i] == False :
                time_is_available = False
                appointment_status = "No serve"
                break                
        if time_is_available :
            for i  in range(duration) : 
                schedules[person][hour+i] = False
            appointment_status = person
            break
    print(appointment_status) 



consultants=[
    {"name":"John","rate":4.5,"price":1000},
    {"name":"Bob","rate":3,"price":1200},
    {"name":"Jenny","rate":3.8,"price":800}
]


book(consultants, 15, 1,"price") # Jenny
book(consultants, 11, 2,"price") # Jenny
book(consultants, 10, 2,"price") # John
book(consultants, 20, 2,"rate") # John
book(consultants, 11, 1,"rate") # Bob
book(consultants, 11, 2,"rate") # No Service
book(consultants, 14, 3,"price") # John




# Task3
print("=== Task3 ===")

def func(*data):
    # your code here
    middle_name = []
    count = {}
    for name in data:
        if len(name) < 4:
            middle_name.append(name[1])
        elif len(name) >= 4:
            middle_name.append(name[2])


    for  word in middle_name:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
    
    for word,times in count.items():
        if times  == 1:
            index = middle_name.index(word)
            print(data[index])
            return 
    print("沒有")

    



func("彭大牆","陳王明雅","吳明") # print 彭大牆
func("郭靜雅","王立強","郭林靜宜","郭立恆","林花花") # print 林花花
func("郭宣雅","林靜宜","郭宣恆","林靜花") # print 沒有
func("郭宣雅","夏曼藍波安","郭宣恆") # print 夏曼藍波安


# Task4
print("=== Task4 ===")

def get_number(index):
        # your code here
    plus_rule = [4,4,-1]
    total = 4+4-1
    x =  index // 3
    y =  index % 3
    
    if y == 0:
        result = total*x
    elif y == 1:
        result = total*x+ plus_rule[y-1]
    elif y == 2:
        result = total*x + plus_rule[y-2]+plus_rule[y-1]

    print(result)


get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70


# Task5
print("=== Task5 ===")

def find(spaces, stat, n):    
    # your code here
    seat_availble = []
    
    for i in range(len(stat)):
        if stat[i] == 1 and spaces[i] >= n:
            seat_availble.append([i,spaces[i]-n])
    
    if not seat_availble :
        print(-1)
        return
    result = sorted(seat_availble,key=lambda x: x[1])[0][0]
    print(result)


find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2