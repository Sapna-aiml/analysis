import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("data.csv")

print("Student Data:")
print(data)

data["Average"]=(
    data["Math"]+
    data["Science"]+
    data["English"]
    )/3

print("\nAverage Maks:")
print(data[["Name","Average"]])

topper=data.loc[data["Average"].idxmax()]

print("\nTopper Student:")
print(topper[["Name","Average"]])
print("Avergae Marks:",topper["Average"])


#Status 

data["Status"]=data["Average"].apply(
    lambda x:"Pass"
    if x>=70 else "Fail"
)

print("\nPass/Fail Status:")
print(data[["Name","Average","Status"]])



#Bar chart 

plt.bar(data["Name"],data["Average"])

plt.title("Student Average Marks")
plt.xlabel("Student")
plt.ylabel("Average Marks")

plt.show()