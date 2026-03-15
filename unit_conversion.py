while True:
    print("=================단위 변환 계산기를 실행합니다.=================")
    print("1. cm --> inch 변환")
    print("2. m --> feet 변환")
    print("3. km --> mile 변환")
    print("4. g --> oz 변환")
    print("5. kg --> pound 변환")
    print("0. 계산 종료")

    choice = input("번호 선택")

    if choice == "1":
        cm = float(input("길이(cm)를 입력하세요:"))
        def cm_inch_변환(cm):
            inch = 2.54*cm
            return inch
        result = cm_inch_변환(cm)
        print(f"변환된 값은 {result:.4f}inch 입니다.")
    
    elif choice == "2":
        m = float(input("길이(m)를 입력하세요:"))
        def m_feet_변환(m):
            feet = 0.3048*m
            return feet
        result = m_feet_변환(m)
        print(f"변환된 값은 {result:.5f}ft입니다.")

    elif choice == "3":
        km = float(input("길이(km)를 입력하세요:"))
        def km_mile_변환(km):
            mile = 1.60934*km
            return mile
        result = km_mile_변환(km)
        print(f"변환된 값은 {result:.7f}mile입니다.")
    
    elif choice == "4":
        g = float(input("무게(g)를 입력하세요:"))
        def g_oz_변환(g):
            oz = 28.35*g
            return oz
        result = g_oz_변환(g)
        print(f"변환된 값은 {result:.4f}oz입니다")

    elif choice == "5":
        kg = float(input("무게(kg)를 입력하세요:"))
        def kg_pound_변환(kg):
            pound = 0.453*kg
            return pound
        result = kg_pound_변환(kg)
        print(f"변환된 값은 {result:.4f}lb입니다.")

    
    elif choice == "0":
        print("계산기를 yh종료합니다.")
        break
