
'''
### 문제 2. CSV 비슷한 데이터 저장

`students.txt` 파일에 학생 정보를 아래 형식으로 저장하세요.
이름,점수
BTS,95
BlackPink,88
NewJeans,92

요구사항

1. 사용자에게 이름/점수를 입력받아 파일에 저장(append)하세요.
2. 점수는 정수로 저장하세요.
3. 입력이 끝나면 파일을 읽어서 전체 학생 평균을 출력하세요.
'''

from paths import DATA_DIR
import json

stu_list=[]
student_path = DATA_DIR / "students.txt"
def demo_mission2():
    print("이름/점수 형태로 입력하세요.")
    
    while len(stu_list) < 3:
        try:
            name, score = input().split("/")
            score = int(score)
            stu_list.append({"name": name, "score": score})
        except:
            break
    total = 0
    with open(student_path, "w", encoding="utf-8") as f:
        f.write("이름,점수\n")
        for elements in stu_list:
            f.writelines([f"{elements['name']},{elements['score']}\n"])
            total += elements['score']
            
    print(f"전체 학생 평균: {total/len(elements)}")
    
    
        
'''
### 문제 3. 데이터 로딩 후 필터링

`students.txt`를 읽어서 “90점 이상 학생만” 출력하세요.

출력 예시

90점 이상: BTS(95), NewJeans(92)
'''
high_students = []
def demo_mission3():
    with open(student_path, "r", encoding = "utf-8") as f:
        for elements in stu_list:
            if elements['score'] >= 90:
                high_students.append(f"{elements['name']}({elements['score']})")
    print(f"90점 이상: ", *high_students)
    
    
    
'''
### 문제 4. 저장 포맷 개선: JSON으로 내보내기

`students.txt`를 읽어서 아래 형태의 `students.json` 파일을 생성하세요.

형태

```
[
  {"name":"BTS", "score":95},
  {"name":"BlackPink", "score":88}
]
```
'''

def demo_mission4():
    students = stu_list
    student_json = DATA_DIR / "students.json"
    with open(student_json, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=2) # indent : 깔끔하게 보이도록 해주는 속성 (파일 출력 템플릿 양식을 들여쓰기 형태로)
        
    with open(student_json, "r", encoding="utf-8") as f:
        loaded = json.load(f)
    print("loaded: ", loaded)