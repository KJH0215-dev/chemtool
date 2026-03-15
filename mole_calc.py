while True:
    print("==============몰 계산기를 실행합니다.==============")
    print("1. 계산기 가동")
    print("0. 계산기 종료")
    
    choice = input("숫자를 입력하세요:")

    if choice == "1":
        mass = float(input("질량을 입력하세요:"))
        molarmass = float(input("몰질량(g/mol)을 입력하세요."))

        def 몰_구하기(mass, molarmass):
            mole = mass / molarmass
            return mole
        result = 몰_구하기(mass, molarmass)
        print(f"몰의 값은 {result:.3f}mol입니다.")

    if choice == "0":
        print("계산기를 종료합니다.")
        break