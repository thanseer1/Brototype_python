import csv
with open("name.csv","w") as f:

     w = csv.writer(f)

    
     w.writerow([101,'somesh',89])
     w.writerow([102,'yogesh',85])
     w.writerow([103,'akhilesh',75])
     w.writerow([874,'supreet',87])  
      
        
print("end")    