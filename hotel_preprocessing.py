import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('hotel_bookings.csv')

print(data.info())

print(data.children.unique())

[ 0.  1.  2. 10.  3. nan]

print(data.country.unique())

print(data.agent.unique())

print(data.company.unique())

a = {'arrival_date_year':data.arrival_date_year,
     'arrival_date_month':data.arrival_date_month,
     'arrival_date_week_number':data.arrival_date_week_number,
     'arrival_date_day_of_month':data.arrival_date_day_of_month,
     'stays_in_weekend_nights':data.stays_in_weekend_nights,
     'stays_in_week_nights':data.stays_in_week_nights,
     'adults':data.adults,
     'babies':data.babies,
     'country':data.country,
     'market_segment':data.market_segment,
     'distribution_channel':data.distribution_channel,
     'is_repeated_guest':data.is_repeated_guest,
     'previous_cancellations':data.previous_cancellations,
     'previous_bookings_not_canceled':data.previous_bookings_not_canceled,
     'days_in_waiting_list':data.days_in_waiting_list,
     'customer_type':data.customer_type,
     'required_car_parking_spaces':data.required_car_parking_spaces,
     'is_canceled':data.is_canceled
     }


df = pd.DataFrame(a)



print(df.info())


#Below Function convert the attribute (object type) to attribute (interger type)
n = 0
for i in df.arrival_date_month.unique():
    n = n + 1
    
print(n)



value = []
for i in range(1,n+1):
    value.append(i)

i = 0
for x in df.arrival_date_month.unique():
    value[i] = x
    print(value[i])
    i = i + 1

for j in range(0,119390):
    for k in range(0,n):
        if df.arrival_date_month[j] == value[k]:
            df.arrival_date_month[j] = k
            break
        
        

print("done")

#Next task convert all the object type attribute to the integer type attribute
#below code to convert the country strings into integer

#********** we have to take care of nan value*************
#nan replaced by the 6
n = 0
for i in df.country.unique():
    n = n + 1
    
print(n)



value = []
for i in range(1,n+1):
    value.append(i)

i = 0
for x in df.country.unique():
    value[i] = x
    print(value[i])
    i = i + 1

for j in range(0,119390):
    for k in range(0,n):
        if df.country[j] == value[k]:
            df.country[j] = k
            break
        


print("done")



del(i)
del(j)
del(k)
del(n)
del(value)
del(x)
#below code for market_segment
#the value undefined replaced by the 6

n = 0
for i in df.market_segment.unique():
    n = n + 1
    
print(n)



value = []
for i in range(1,n+1):
    value.append(i)

i = 0
for x in df.market_segment.unique():
    value[i] = x
    print(value[i])
    i = i + 1

for j in range(0,119390):
    for k in range(0,n):
        if df.market_segment[j] == value[k]:
            df.market_segment[j] = k
            break
        


print("done")

#below code for distribution channel
#replaced undefined with 4
n = 0
for i in df.distribution_channel.unique():
    n = n + 1
    
print(n)



value = []
for i in range(1,n+1):
    value.append(i)

i = 0
for x in df.distribution_channel.unique():
    value[i] = x
    print(value[i])
    i = i + 1

for j in range(0,119390):
    for k in range(0,n):
        if df.distribution_channel[j] == value[k]:
            df.distribution_channel[j] = k
            break
        


print("done")


#Below code for customer_type

n = 0
for i in df.customer_type.unique():
    n = n + 1
    
print(n)



value = []
for i in range(1,n+1):
    value.append(i)

i = 0
for x in df.customer_type.unique():
    value[i] = x
    print(value[i])
    i = i + 1

for j in range(0,119390):
    for k in range(0,n):
        if df.customer_type[j] == value[k]:
            df.customer_type[j] = k
            break
        


print("done")


#replace all the value back to the na 
 
i = 0
for i in range(0,119390):
    if df.country[i] == '6':
        df.country[i] = np.nan
        
        
print(df.country.unique())

for i in range(0,119390):
    if df.market_segment[i] == 6:
        df.market_segment[i] = np.nan
        
print(df.market_segment.unique())

for i in range(0,119390):
    if df.distribution_channel[i] == 4:
        df.distribution_channel[i] = np.nan
  

print(df.distribution_channel.unique())
      
df.to_csv(r'hotel_preprocess_data_1.csv')

data1 = pd.read_csv('hotel_preprocess_data_1.csv')

# We replace the value of nan with mean value

print(int(data1["country"].mean()))
print(int(data1["market_segment"].mean()))
print(int(data1["distribution_channel"].mean()))

