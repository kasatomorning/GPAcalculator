import json
import string
import sys

csvcontent = ["学籍番号", "学生氏名", "科目番号", "科目名 ", "単位数",
              "春学期", "秋学期", "総合評価", "科目区分", "開講年度", "開講区分"]


def gpa(csvfile: string):
    gp: float = 0
    gpa: float = 0
    ratioOverA: float = 100
    # A+,A,B,C,Dのそれぞれの単位の合計
    creditsTotalPerGrade = [0, 0, 0, 0, 0]
    grades = ["A+", "A", "B", "C", "D"]
    gradepoints = [4.3, 4.0, 3.0, 2.0, 0]
    with open(csvfile) as f:
        _line = f.readline()
        lines = f.readlines()
        csvArray = []
        for i in lines:
            csvArray.append(i.replace('\"', '').split(','))
        for credit in csvArray:
            num = float(credit[4])
            if(i[8] == "C0"):
                continue
            for index, g in enumerate(grades):
                if(credit[7] == g):
                    creditsTotalPerGrade[index] += num
    for index, g in enumerate(creditsTotalPerGrade):
        gp += g*gradepoints[index]
    gpa = gp/sum(creditsTotalPerGrade)
    ratioOverA *= (creditsTotalPerGrade[0] +
                   creditsTotalPerGrade[1])/sum(creditsTotalPerGrade)
    for index, c in enumerate(creditsTotalPerGrade):
        print(grades[index]+"："+str(c)+"単位")
    print("GPA："+format(gpa, '.2f'))
    print("A以上の単位の割合："+format(ratioOverA, '.2f')+"%")


if __name__ == "__main__":
    args = sys.argv
    gpa(args[1])
