""" Given the names and grades for each student in a
 class of N students, store them in a nested list and print the name(s)
 of any student(s) having the second lowest grade."""

score_set = set()
ans_list = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        ans_list.append([name, score])
        score_set.add(score)

for name, score in sorted(ans_list):
    if score == list(sorted(score_set))[1]:
        print(name)


"""  or 
marksheet=[]
scorelist=[]
if __name__ == '__main__':
        for _ in range(int(input())):
                name = input()
                score = float(input())
                marksheet+=[[name,score]]
                scorelist+=[score]
        answer=sorted(list(set(scorelist)))[1] 

        for name,score in sorted(marksheet):
             if score==answer:
                    print(name)"""