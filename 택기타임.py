import time

def game():
    print("게임을 시작합니다! 스톱워치를 임의의 시점에서 정지하여 시간을 기록하세요.")
    previous_time = None  # 이전에 멈춘 시간
    times = []  # 시간을 기록할 리스트
    count = 0  # 현재까지 기록된 시간 개수
    recorded_times = []  # 기록된 시간을 저장할 리스트
    while count < 1000:
        input("엔터를 눌러 스톱워치를 정지하세요. 정지할 때마다 시간을 기록합니다.")
        start_time = round(time.time(), 2)  # 스톱워치 시작 시간, 소숫점 둘째 자리까지 반올림
        # 이전에 멈춘 시간과 중복되지 않는 경우에만 기록
        if previous_time is not None:
            elapsed_time = round(start_time - previous_time, 2)  # 경과 시간 계산, 소숫점 둘째 자리까지 반올림
            if elapsed_time != 0:  # 0초가 아니고 중복되지 않는 경우에만 기록
                if elapsed_time not in times:
                    times.append(elapsed_time)
                    recorded_times.append(elapsed_time)
                    count += 1
                    print("현재까지 기록된 시간 개수:", count, "/ 1000")
                    print("마지막으로 멈춘 시간:", elapsed_time, "초")
                else:
                    print("이미 기록된 시간입니다.")
        else:
            elapsed_time = 0
        previous_time = start_time
        command = input("명령을 입력하세요 ('목록확인'으로 시간목록 보기 또는 Enter로 계속하기): ")
        if command == "목록확인":
            print("몇 초 대를 확인할까요?")
            time_range = input("숫자를 입력하세요 (0부터 10까지의 숫자): ")
            if time_range.isdigit() and 0 <= int(time_range) <= 10:
                time_range = int(time_range)
                filtered_times = sorted([t for t in recorded_times if int(t) == time_range])
                print(f"{time_range} 초 대의 기록된 숫자:", filtered_times)
            else:
                print("올바르지 않은 입력입니다. 0부터 10까지의 숫자를 입력하세요.")

    print("축하합니다! 1000개의 시간을 모두 기록했습니다. 게임을 완료했습니다!")

game()  # 게임 함수를 직접 호출합니다.
