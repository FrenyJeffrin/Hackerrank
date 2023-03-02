n= int(input())
student_marks={}
for _ in range(n):
    name, *rest =input().split()
    scores= list(map(float, rest))
    student_marks[name]=scores
query_name=input()
res=sum(student_marks[query_name])/len(student_marks[name])
print("{:.2f}".format(res))