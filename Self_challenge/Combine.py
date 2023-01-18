import csv
import os

final_order=[]

with open('order.csv', 'r') as csvfile:
    rw=csv.reader(csvfile,dialect='excel')
    for row in rw:
        final_order.append(row)
    for a in range(len(final_order)):
            final_order[a].pop(0)
    for a in range(len(final_order)):
            final_order[a].pop(0)



product_order=[]
with open('product.csv', 'r') as csvfile:
    rw=csv.reader(csvfile,dialect='excel')
    for row in rw:
        product_order.append(row)
    for a in range(len(product_order)):
            product_order[a].pop(0)
            product_order[a].pop(1)
    for a in range(len(product_order)):
            product_order[a].pop(0)



#Merging both the List.
for i in range(len(final_order)):
     final_order[i].insert(0,product_order[i])


#Function to convert the List in 1-D array
def Final_list(final_order):
    result = [item for sublist in final_order for item in sublist]
    return result

def data_preprocessing(report_data):
    listToStr = ' '.join([str(row) for row in report_data])
    s=""
    for i in listToStr:
        s=s+i.strip('[]').replace("'",'') 
        y=s.split(' ')
    return y

#Function to calculate the No-of-rows in the List.
def count_rows(_report_data):
    FinalD=[]
    rows=int(len(_report_data)/3)
    for times in range(rows):
        newtempD=[]
        for i in range(3):
            newtempD.append(_report_data[0])
            _report_data.pop(0)
        FinalD.append(newtempD)
    FinalD.pop(0)
    return FinalD
    print(len(FinalD))




if __name__ == "__main__":
    report_data=Final_list(final_order)
    _report_data=data_preprocessing(report_data)
    _Final_data=count_rows(_report_data)
    percentage=[]
    for times in _Final_data:
        for i in range(2,1,-1):
            val1=float(int(times[i]))/(int(times[i-1]))
            val1=round(val1,2)
            percentage.append(val1*100)
    
#Merging the percenatge data to the FinalD.

    for i in range(len(_Final_data)):
        _Final_data[i].insert(3,percentage[i])
    print(_Final_data)


#Creating the Report.csv file to store the Final Report collected.
    if not os.path.exists("Self_challenge/Data"):
            os.makedirs("Self_challenge/Data") 
    with open('Self_challenge/Data/Real_Combine.csv', 'w') as csvfile:
        wr=csv.writer(csvfile,dialect='excel')
        wr.writerow(['department_id', 'number_of_orders', 'number_of_first_orders','percentage'])
        for row in _Final_data:
            #  for ele in row:
                 wr.writerow(row)