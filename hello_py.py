testCases = int(input())


for i in range(0, testCases):    
    number = int(input())
    if number <= 12:
        faceNumber = 13-number
    elif number >= 13 and number <= 24:
        faceNumber = 37-number
    elif number >= 25 and number <= 36:
        faceNumber = 61-number
    elif number >= 37 and number <= 48:        
        faceNumber = 85-number        
    elif number >= 49 and number <= 60:
        faceNumber = 109-number
    elif number >= 61 and number <= 72:
        faceNumber = 133-number
    elif number >= 73 and number <= 84:
        faceNumber = 157-number
    elif number >= 85 and number <= 96:
        faceNumber = 181-number
    elif number >= 97 and number <= 108:
        faceNumber = 205-number

    if abs(number - int(faceNumber)) == 11 or abs(number - int(faceNumber)) == 1:            
        print(str(faceNumber) + " WS")
    elif abs(number - int(faceNumber)) == 9 or abs(number - int(faceNumber)) == 3:
        print(str(faceNumber) + " MS")
    else:
        print(str(faceNumber) + " AS")
                
        
   
