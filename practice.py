import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.DataFrame({
    'id':[1,2,3,4,5,6,7,8,9,10],
    'name':['ishani','riya','siya','jiya','ajay','ram','jai','dev','jacob','lara'],
    'math':[20,12,15,17,19,13,14,16,18,10],
    'science':[19,20,13,15,17,19,12,14,16,18],
    'english':[18,16,19,13,19,20,np.nan,20,15,19],
    'hindi':[19,20,15,np.nan,17,19,20,18,10,14]
})
df.set_index('id',inplace=True)
# print(df)
df.to_csv("visual.csv")
print(df.fillna(0,inplace=True))
df['total_marks']=df['math']+df['science']+df['english']+df['hindi']
print(df)
subj_Avg=[
   df['math'].mean(),
   df['english'].mean(),
   df['hindi'].mean(),
   df['science'].mean()]
# average marks of class
print("average of class marks is",df["total_marks"].mean())
#AVG MARKS ACCORDING TO PER SUB
print("the average of class accoreding to marks is ")
print("Maths average: ",df["math"].mean())
print("Science average is ",df["science"].mean())
print("english average is ",df["english"].mean())
print("hindi average is ",df["hindi"].mean())

plt.show()

df['percentage']=(df['total_marks']/80)*100
print(df)
print("top scorers are ")
top_scorers=df['total_marks']>70
print(df[top_scorers])
print("topper is ")
print(df.loc[(df['percentage']).idxmax()])
print("the lowest scorrer is ")
print(df.loc[df['percentage'].idxmin()])
subject=['math','science','english','hindi']

# bar chart
plt.bar(subject,subj_Avg,color="pink")
plt.ylabel("subj_Avg")
plt.xlabel("subject")
plt.title("subject avg marks")
plt.show()

plt.bar(df['name'],df['total_marks'],color="green")
plt.xlabel('NAME')
plt.ylabel('MARKS')
plt.title('student comparision')
plt.show()

# # plt.show()
# avg subject marks calculation/pie chart of marks division
plt.pie(subj_Avg,labels=subject,autopct="%0.1f%%")
plt.title("student average marks distribution according to subject")
plt.show()

plt.hist(df['total_marks'],color='pink')
plt.title("total marks of student")
plt.show()
