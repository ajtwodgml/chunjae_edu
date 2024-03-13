#음료를 선택한다
def choose_beverage(beverages) :
    print("=================*=================")
    print("음료를 선택하세요.")
    for i,beverage in enumerate(beverages, start = 1) :
        print(f"{i}. {beverage['음료']} - 가격: {beverage['가격']}원 - 재고: {beverage['재고']}개")
    print("=================*=================")
    
    choice = int(input("번호를 입력하세요: "))
    selected_beverage = beverages[choice - 1]
    return selected_beverage
#돈을 넣는다
def insert_cash():
    cash = int(input("투입할 현금을 입력하세요: "))
    return cash
# 거스름돈을 반환한다
def calculate_change(selected_beverage, cash):
    price = selected_beverage['가격']
    
    if cash < price : 
        print("현금이 부족합니다.")
        return

    change = cash - price
    print(f"{selected_beverage['음료']}를 선택하셨습니다.")
    print(f"거스름돈: {change}원")

    # 재고 소비
    selected_beverage['재고'] -= 1
    if selected_beverage['재고'] == 0:
        print(f"{selected_beverage['음료']}가 재고 소진되었습니다.")
        return True
    
# 초기 음료 재고 설정
vending = [{'음료': '사이다', '가격': 1300, '재고': 4},
           {'음료': '콜라', '가격': 1500, '재고': 2},
           {'음료': '생수', '가격': 900, '재고': 1}]
while True:
    selected = choose_beverage(vending)
    cash_input = insert_cash()
    if calculate_change(selected, cash_input):
        break  # 재고가 다 소진되면 반복 종료