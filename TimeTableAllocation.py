import copy

#read the input data file of sunjects, slots and rooms
def readFile(file_name):
    with open(file_name, 'r') as inFile:
        dataIn = inFile.read()
        rows = dataIn.split('\n')
        allDataSet = []; #subject details and rooms are included to this array
        for row in rows:
            allDataSet.append(row.split(','))
        print allDataSet
        return allDataSet
    

def writeToFile(file_name, final_allocation):
    data = ""
    for row in final_allocation:
        record = ""
        for col in row:
            record += col + ','
        else:
            record = record[:-1]
        data += record + '\n'
    else:
        data = data[:-1]
    with open(file_name, 'w') as outFile:
        outFile.write(data)

                
def isSafeTheSlot(slot):
    if(slots[slot] == "N"):
        return True
    return False;

def timeTableAllocation(time_table_assignment,round_no):
    global subjectData
    global rooms
    if (round_no == len(time_table_assignment)):             
        return True  
    sub_name = subjectData[round_no][0]   
    sub_category =subjectData[round_no][1]
    reqsted_slots_of_subject = subjectData[round_no][2:]
    if(sub_category=="c"):
        for each_slot in reqsted_slots_of_subject:
            if(isSafeTheSlot(each_slot)):
                time_table_assignment[round_no]=[sub_name, each_slot, rooms[0]]
                slots[each_slot] = rooms[0]
                if (timeTableAllocation(time_table_assignment,round_no+1)):
                    return True                
                else:
                    slots[each_slot] = -1
                    time_table_assignment[round_no]= [sub_name, -1, -1]
        else:
            return False
                
    elif (sub_category== "o"):
        for each_slot in reqsted_slots_of_subject:      
            if(isSafeTheSlot(each_slot)):
                time_table_assignment[round_no]=[sub_name, each_slot, rooms[0]]
                slots[each_slot] = rooms[0]
                if (timeTableAllocation(time_table_assignment,round_no+1)):
                    return True                
                else:
                    slots[each_slot] = -1
                    time_table_assignment[round_no]= [sub_name, -1, -1]
            elif(type(slots[each_slot]) == list):
                current_rooms= slots[each_slot]
                current_rooms_1=current_rooms[:]
                if (len(rooms) == len(current_rooms)):
                    continue
                current_rooms.append(rooms[len(current_rooms)])
                time_table_assignment[round_no] = [sub_name, each_slot, current_rooms[-1]]
                slots[each_slot] = current_rooms
                if (timeTableAllocation(time_table_assignment,round_no+1)):
                    return True
                else:
                    slots[each_slot] = current_rooms_1
                    time_table_assignment[round_no]= [sub_name, -1, -1]
            else:
                return False


def initializeTheSlotDictionary():
    for subject in subjectData:
        for slot in subject[2:]:
            if (slot not in slots):
                slots[slot] = "N"
    time_table_assignment.append([subject[0],-1,-1])



dataInput = readFile('input.csv')
rooms = dataInput[-1] #hold the rooms
subjectData = dataInput[:-1]#hold the subject detais

time_table_assignment = [] #final assigments of subjeccts are added to this list
slots = {} #the dictionary which hold slots assigned

initializeTheSlotDictionary()
start=0
final_output = timeTableAllocation(time_table_assignment,start)

if (final_output):
    writeToFile('output.csv', time_table_assignment)
    print "\n"
    for subject in time_table_assignment:
       print subject


 
