import csv

data = {}

##reads all data in the excel file
def read_data():
    csv_file = open('CSCA_database.csv', 'r')
    reader = csv.reader(csv_file)
    for row in reader:
        card_number = row[0]
        data[row[0]] = {'name':row[1], 'condition':row[2], 'severity':row[3], 'age':row[4], 'weight':row[5], 'height':row[6], 'dosage':row[7]}
        
##displays data neatly as a chart
def display_data():
    csv_file = open('CSCA_database.csv', 'r')
    reader = csv.reader(csv_file)    
    for data in reader:
        print("{: <10} {: <7} {: <7}{:<10}{:<10}{:<10}{:<10}".format(*data))
    

###given a valid health card number in the database, will return a specific data point for that patient
def search_database ():
    read_data()
    card_number_input = input("enter valid health card number of patient.")
    data_point = input("which data point for this patient do you want? ex. name, condition, severity, age, weight, height, dosage, or all: ")  
    while not(data_point == "stop"):
        if data_point == ("all"):
            print(data[card_number_input]) 
        else:
            print(data[card_number_input][data_point])
        data_point = input("next data point: ")
            

###adds new patient row to the main database
def add_patient():
    #recall read function so the new patient data doesn’t write over the rest of the data
    read_data()
     #input all the necessary info
    health_card = input("What is the patient's health card number?")
    patient_name = input("Patient name (first and last)")
    disease = input("What is the patient's disease?")
    severity = input("Severity of condition?")
    age = input("What is the patient's age?")
    weight_in_kg = input("patient weight in kg")
    height_in_cm = input("patient's height in cm")
    dosage = input("medication dosage in mL")
    #make the inner dictionary
    new_dict = {'name':patient_name, 'condition':disease, 'severity':severity, 'age':age, 'weight in kg':weight_in_kg, 'height in cm':height_in_cm, 'dosage':dosage}
#add the small dictionary to the main dictionary
    data[int(health_card)] = new_dict
#now we need to add this new data to the excel file
#to do this we will make a list that follows the necessary column format
    new_patient_list = []
    new_patient_list = [health_card,patient_name,disease,severity,age,weight_in_kg,height_in_cm,dosage]
    #now we append to the excel file
    row = new_patient_list
    with open('CSCA_database.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        lines = list(reader)
        lines.append(row)
    with open('CSCA_database.csv', 'w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
   

###edits a current patient


###creates new csv file named new_file
def create_new_file():
    import csv
    with open('new_file.csv', 'w', newline='') as new_file:
        ##recall read function to obtain patient data for new file so we don't have to reinput anything 
        read_data()
        writer =csv.writer(new_file)
        card_number_input = input("which card number are you creating a new file for?")
        header = (card_number_input),(data[card_number_input]['name'])
        writer.writerows([header])
        new_row = input("new row? y/n")
        while new_row == "y":
            date = input("date of note")
            note = input("note to write")            
            new_data = (date),(note)
            new_row = input("new row? y/n")
            writer.writerows([new_data])
        print("file created")    

        
        
###command statements below###
        
csv_file = 'CSCA_database.csv'
command = input("type 'display' to display all patient data,'search' to search for patient data, 'edit' to edit a file,'add' to add a new patient, or 'create' to create a new excel patient file: ")
while not(command=="stop"):
    if command == "display":
        display_data()
    if command == "search": 
        (card_number_input, data_point) = search_database()
    if command == "add":
        add_patient()
    if command == "create":
        create_new_file()
    if command == "edit":
        edit_patient_file()
    if command == "delete":
        delete_patient()
    command = input("type next command: 'display' to display all patient data,'search' to search for patient data, 'edit' to edit a file,'add' to add a new patient, or 'create' to create a new excel patient file: ")
print(":-)")   

