'''
### 제 1. 로그 파일에 기록하기

사용자에게 문장을 입력받아 `logs.txt`에 한 줄로 저장하세요.

1. 파일이 없으면 생성하세요.
2. 기존 내용이 있으면 뒤에 이어쓰기(append) 하세요.
3. 저장 형식은 `"2026-03-05 14:30:10 - 입력내용"` 형태로 저장하세요.

힌트: `datetime`을 사용할 수 있습니다.
'''

from paths import DATA_DIR
from datetime import datetime 

def demo_mission1():
    sentence = input()
    log_path = DATA_DIR / "logs.txt"
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - {sentence}.\n")
        