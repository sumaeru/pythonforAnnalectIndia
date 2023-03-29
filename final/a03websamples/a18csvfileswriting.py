#copy paste from geek for geeks.. as it is..


# importing the csv module
import csv
 
# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']
 
# data rows of csv file
rows = [ ['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]
 
# name of csv file
filename = "university_records.csv"
 
# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
     
    # writing the fields
    csvwriter.writerow(fields)
     
    # writing the data rows
    csvwriter.writerows(rows)

    def another():
        fields = ['Name', 'Email']
 
    # data rows of csv file
        rows = [ ['Nikhil', 'nikhil.gfg@gmail.com'],
                ['Sanchit', 'sanchit.gfg@gmail.com'],
                ['Aditya', 'aditya.gfg@gmail.com'],
                ['Sagar', 'sagar.gfg@gmail.com'],
                ['Prateek', 'prateek.gfg@gmail.com'],
                ['Sahil', 'sahil.gfg@gmail.com']]
        
        # name of csv file
        filename = "email_records.csv"
       
        # writing to csv file
        with open(filename, 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            
            # writing the fields
            csvwriter.writerow(fields)
            
            # writing the data rows
            csvwriter.writerows(rows)





