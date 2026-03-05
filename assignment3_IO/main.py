from paths import DATA_DIR
from mission1 import demo_mission1
from mission2 import demo_mission2, demo_mission3, demo_mission4


if __name__ == "__main__":
    print("미션 1. 로그 파일에 기록하기")
    demo_mission1()
    
    print("미션 2. CSV 비슷한 데이터 저장")
    demo_mission2()
    
    print("미션 3. 데이터 로딩 후 필터링")
    demo_mission3()
    
    print("미션 4. 저장 포맷 개선: JSON으로 내보내기")
    demo_mission4()






