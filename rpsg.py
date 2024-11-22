import random

#승 패 무
w = 0 #승
l = 0 #패
d = 0 #무

# 플레이어가 게임을 반복하고 싶을 경우,
while True :

    rps = ["가위", "바위", "보"]

    # 플레이어가 가위, 바위, 보 중 하나를 입력합니다.
    guest = input("가위, 바위, 보 중 하나를 선택하세요: ").strip().lower()

    # 사용자의 입력값을 ‘가위 바위 보’로 제한할 수 있는가
    if guest not in rps:
        print("유효한 입력이 아닙니다 '가위', '바위', '보' 중 하나를 선택해주세요 ")
        continue

    # 컴퓨터도 무작위로 가위, 바위, 보 중 하나를 선택합니다.
    bot = random.choice(rps)

    # 플레이어와 컴퓨터의 선택을 비교하여 승패를 판정합니다.
    print(f" 사용자: {guest}, 컴퓨터: {bot}")

    # 결과를 출력하여 플레이어가 이겼는지, 컴퓨터가 이겼는지, 비겼는지를 알려줍니다.
    # 일단 코드를 사용자 결과 기준으로 잡자
    if guest == bot:
        d += 1
        print("사용자 컴퓨터 비김!")
    elif ((guest == "가위" and bot == "바위") or (guest == "바위" and bot == "보") or (guest == "보" and bot == "가위")):
        l += 1
        # g=가위 b=바위
        # g=바위 b=보
        # g=보 b=가위
        print("컴퓨터 승리!") #여기는 사용자가 지는 공간 이라 결과 값이 컴퓨터 승리
    else:
        w += 1
        print("사용자 승리!")

    # 게임 재시작 여부를 묻고 그에 따라 게임을 초기화하거나 종료하는 기능을 추가하세요.
    # 플레이어가 입력할 때 대소문자를 구분하지 않도록 프로그램을 개선하세요.
    while True:
        restart=input("다시 하시겠습니까? (y/n): ").strip().lower()
        if restart == 'y':
            break #게임을 계속 진행
        elif restart == 'n':
            print("\n게임을 종료합니다!")
            print(f"승: {w} 패: {l} 무승부: {d}") #게임 종료 후 승, 패, 무승부를 출력
            exit()
        else:
            print("유효한 입력이 아닙니다. 'y'또는 'n'을 입력해주세요")
    