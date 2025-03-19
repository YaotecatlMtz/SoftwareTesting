import pytest
from src.white_box import *

def test_is_even():
    """
    This fn is to test is even function
    scenarios
    True, False and str
    """
    assert is_even(6) == True
    assert is_even(5) == False
    with pytest.raises(TypeError):
        is_even('Hi I will cause an exeption')

def test_divide():
    """
    This fn will test divide method
    scenarios
    integer result, float result
    dividing with float numbers
    dividing by 0
    """

    assert divide(10,10) == 1
    assert divide(5,3) == 5/3
    assert divide(2.3,1.2) == 2.3/1.2
    assert divide(2,0) == 0

def test_get_grade():
    """
    This fn tests get grade method
    scenarios
    grade = 90 -> A
    grade = 80 -> B
    grade = 70 -> C
    grade = 69 -> F
    """

    assert get_grade(90) == 'A'
    assert get_grade(80) == 'B'
    assert get_grade(70) == 'C'
    assert get_grade(69) == 'F'

def test_is_triangle():
    assert is_triangle(1,1,3) == "No, it's not a triangle."
    assert is_triangle(1,1,1) == 'Yes, it\'s a triangle!'


def test_check_number_status():
    assert check_number_status(1) == 'Positive'
    assert check_number_status(0) == 'Zero'
    assert check_number_status(-1) == 'Negative'

def test_validate_password():
    assert validate_password('short') == False
    assert validate_password('passw0rd!') == False
    assert validate_password('Password!') == False
    assert validate_password('PASSW0RD!') == False
    assert validate_password('Passw0rd') == False
    assert validate_password('Passw0rd!') == True
    assert validate_password('Passw0rd@') == True
    assert validate_password('Passw0rd#') == True
    assert validate_password('Passw0rd$') == True
    assert validate_password('Passw0rd%') == True
    assert validate_password('Passw0rd&') == True

def test_calculate_total_discount():
    assert calculate_total_discount(99) == 0
    assert calculate_total_discount(100) == 100*0.1
    assert calculate_total_discount(501) == 501*0.2

def test_calculate_order_total():
    assert calculate_order_total([{'quantity': 3,'price':50}]) == 3*50
    assert calculate_order_total([{'quantity': 7,'price':50}]) == (7*50)*0.95
    assert calculate_order_total([{'quantity': 11,'price':50}]) == (11*50)*0.9

def test_calculate_items_shipping_cost():
    assert calculate_items_shipping_cost([{'weight':5}],'standard') == 10
    assert calculate_items_shipping_cost([{'weight':6}],'standard') == 15
    assert calculate_items_shipping_cost([{'weight':11}],'standard') == 20
    assert calculate_items_shipping_cost([{'weight':5}],'express') == 20
    assert calculate_items_shipping_cost([{'weight':6}],'express') == 30
    assert calculate_items_shipping_cost([{'weight':11}],'express') == 40
    with pytest.raises(ValueError):
        calculate_items_shipping_cost([{'weight':11}],'Hi I will cause an exeption')

def test_validate_login():
    assert validate_login('fail','12345678') == 'Login Failed'
    assert validate_login('failedwithmorecharacters','12345678') == 'Login Failed'
    assert validate_login('oneball','1234567') == 'Login Failed'
    assert validate_login('oneball','1234567890123456') == 'Login Failed'
    assert validate_login('oneball','12345678') == 'Login Successful'

def test_verify_age():
    assert verify_age(17) == 'Not Eligible'
    assert verify_age(66) == 'Not Eligible'
    assert verify_age(20) == 'Eligible'

def test_categorize_product():
    assert categorize_product(9) == 'Category D'
    assert categorize_product(201) == 'Category D'
    assert categorize_product(10) == 'Category A'
    assert categorize_product(51) == 'Category B'
    assert categorize_product(101) == 'Category C'

def test_validate_email():
    assert validate_email('@e.c') == 'Invalid Email'
    assert validate_email('test@examplecom') == 'Invalid Email'
    assert validate_email('testexample.com') == 'Invalid Email'
    assert validate_email('thisIsAVeryLongEmailThatWillFail123@example3214.com') == 'Invalid Email'
    assert validate_email('test@example.com') == 'Valid Email'

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(101) == 'Invalid Temperature'
    assert celsius_to_fahrenheit(-101) == 'Invalid Temperature'
    assert celsius_to_fahrenheit(50) == (50 * 9 / 5) + 32

def validate_credit_card(card_number):
    assert validate_credit_card('1') == 'Invalid Card'
    assert validate_credit_card('hello') == 'Invalid Card'
    assert validate_credit_card('12345678901234567') == 'Invalid Card'
    assert validate_credit_card('12345678901234') == 'Valid Card'

def test_validate_date():
    assert validate_date(1899,1,1) == 'Invalid Date'
    assert validate_date(2101,1,1) == 'Invalid Date'
    assert validate_date(2000,0,1) == 'Invalid Date'
    assert validate_date(2000,13,1) == 'Invalid Date'
    assert validate_date(2000,1,0) == 'Invalid Date'
    assert validate_date(2000,1,32) == 'Invalid Date'
    assert validate_date(2002,11,19) == 'Valid Date'

def test_check_flight_eligibility():
    assert check_flight_eligibility(17, True) == 'Eligible to Book'
    assert check_flight_eligibility(18, False) == 'Eligible to Book'
    assert check_flight_eligibility(17, False) == 'Not Eligible to Book'
    assert check_flight_eligibility(66, False) == 'Not Eligible to Book'

def test_validate_url():
    assert validate_url('urlExamle') == 'Invalid URL'
    assert validate_url('http://www.example.com/products/category/electronics/laptops/brand/apple/model/macbook-pro-16-inch/specs/processor/intel-core-i9/memory/32gb/storage/1tb-ssd/color/space-gray/warranty/3-years/accessories/usb-c-hub/external-monitor/4k-ultrawide/bag/premium-leather-case?ref=longurltest&utm_source=google&utm_medium=cpc&utm_campaign=summer_sale&utm_term=macbook_pro') == 'Invalid URL'
    assert validate_url('http://urlExamle') == 'Valid URL'
    assert validate_url('https://urlExamle') == 'Valid URL'

def test_calculate_quantity_discount():
    assert calculate_quantity_discount(0) == '10% Discount' #This scenario should raise an error
    assert calculate_quantity_discount(1) == 'No Discount'
    assert calculate_quantity_discount(6) == '5% Discount'
    assert calculate_quantity_discount(11) == '10% Discount'

def test_check_file_size():
    assert check_file_size(10) == 'Valid File Size'
    assert check_file_size(1048577) == 'Invalid File Size'
    assert check_file_size(-1) == 'Invalid File Size' #files can't have negative file sizes

def test_check_loan_eligibility():
    assert check_loan_eligibility(3000, 800) == 'Not Eligible'
    assert check_loan_eligibility(30000, 701) == 'Standard Loan'
    assert check_loan_eligibility(30000, 700) == 'Secured Loan'
    assert check_loan_eligibility(60001, 751) == 'Premium Loan'
    assert check_loan_eligibility(300000, 701) == 'Standard Loan'

def test_calculate_shipping_cost():
    assert calculate_shipping_cost(1,10,10,10) == 5
    assert calculate_shipping_cost(1,11,10,10) == 20
    assert calculate_shipping_cost(1,10,11,10) == 20
    assert calculate_shipping_cost(1,11,10,11) == 20
    assert calculate_shipping_cost(1.1,11,11,11) == 10
    assert calculate_shipping_cost(1.1,31,11,11) == 20
    assert calculate_shipping_cost(1.1,11,31,11) == 20
    assert calculate_shipping_cost(1.1,11,11,31) == 20
    assert calculate_shipping_cost(5.1,10,10,10) == 20

def test_grade_quiz():
    assert grade_quiz(4,2) == 'Fail'
    assert grade_quiz(7,4) == 'Fail'
    assert grade_quiz(7,3) == 'Conditional Pass'
    assert grade_quiz(6,2) == 'Conditional Pass'
    assert grade_quiz(7,2) == 'Pass'

def test_authenticate_user():
    assert authenticate_user('admin', 'admin123') == 'Admin'
    assert authenticate_user('admin', '123456789') == 'User'
    assert authenticate_user('hola','user') == 'Invalid'
    assert authenticate_user('usuario','passwd') == 'Invalid'

def test_get_weather_advisory():
    assert get_weather_advisory(31,71) == 'High Temperature and Humidity. Stay Hydrated.'
    assert get_weather_advisory(-1,71) == 'Low Temperature. Bundle Up!'
    assert get_weather_advisory(30,71) == 'No Specific Advisory'
    assert get_weather_advisory(31,70) == 'No Specific Advisory'

def test_VenginMachine():
    machine = VendingMachine()
    assert machine.state == 'Ready'
    assert machine.insert_coin() == "Coin Inserted. Select your drink."
    assert machine.state == 'Dispensing'
    assert machine.insert_coin() == "Invalid operation in current state."
    assert machine.select_drink() == "Drink Dispensed. Thank you!"
    assert machine.state == 'Ready'
    assert machine.select_drink() == "Invalid operation in current state."

def test_TrafficLight():
    light = TrafficLight()

    assert light.get_current_state() == 'Red'
    light.change_state()
    assert light.get_current_state() == 'Green'
    light.change_state()
    assert light.get_current_state() == 'Yellow'
    light.change_state()
    assert light.get_current_state() == 'Red'

def test_UserAuthentication():
    user = UserAuthentication()
    assert user.state == 'Logged Out'
    assert user.login() == 'Login successful'
    assert user.state == 'Logged In'
    assert user.login() == 'Invalid operation in current state'
    assert user.logout() == 'Logout successful'
    assert user.state == 'Logged Out'
    assert user.logout() == 'Invalid operation in current state'

def test_DocumentEditingSystem():
    doc = DocumentEditingSystem()
    assert doc.state == "Editing"
    assert doc.save_document()  == 'Document saved successfully'
    assert doc.state == "Saved"
    assert doc.save_document() == 'Invalid operation in current state'
    assert doc.edit_document() == 'Editing resumed'
    assert doc.state == "Editing"
    assert doc.edit_document() == 'Invalid operation in current state'

def test_ElevatorSystem():
    elevator = ElevatorSystem()
    assert elevator.state == 'Idle'
    assert elevator.move_up() == 'Elevator moving up'
    assert elevator.state == 'Moving Up'
    assert elevator.move_up() == 'Invalid operation in current state'
    assert elevator.stop() == 'Elevator stopped'

    assert elevator.state == 'Idle'
    assert elevator.move_down() == 'Elevator moving down'
    assert elevator.state == 'Moving Down'
    assert elevator.move_up() == 'Invalid operation in current state'
    assert elevator.stop() == 'Elevator stopped'
    assert elevator.state == 'Idle'
    assert elevator.stop() == 'Invalid operation in current state'


def test_BankAccount():
    acc3 = BankAccount(None, None)
    acc2 = BankAccount(-123, -500)
    acc = BankAccount(123, 500)
    assert acc.account_number == 123
    assert acc.balance == 500
    assert acc.view_account() == None #view account does not return anything
    assert acc2.account_number == -123 #this should not be valid
    assert acc2.balance == -500 #this may be valid depending on requirements
    assert acc3.account_number == None #Should be validations for this scenarios
    assert acc3.balance == None #Should be validations for this scenario

def test_Banksystem():
    bank = BankingSystem()
    with pytest.raises(TypeError):
        bank2 = BankingSystem('test')
    assert bank.authenticate('user123','pass123') == True
    assert bank.authenticate('user123','pass123') == False
    assert bank.authenticate('user123', 'pass') == False
    assert bank.authenticate('user', 'pass') == False
    assert bank.logged_in_users == {'user123'}
    assert bank.transfer_money('notSuthenticated','myself', 100,'regular') == False
    assert bank.transfer_money('user123','myself', 100,'regular') == True
    assert bank.transfer_money('user123','myself', 100,'express') == True
    assert bank.transfer_money('user123','myself', 100,'scheduled') == True
    assert bank.transfer_money('user123','myself', 100,'personal') == False
    assert bank.transfer_money('user123','myself', 1000,'express') == False

def test_Product():
    p = Product('toy', 100)
    pNegative = Product('toy', -100) #If there was a requirement, negative values should not be valid as a price
    assert p.name  == 'toy'
    assert p.price == 100
    assert pNegative.price == -100
    assert p.view_product() == "The product toy has a price of 100"

def test_ShoppingCart():
    cart = ShoppingCart()
    p1 = Product('toy car', 10)
    p2 = Product('lego', 25)
    with pytest.raises(TypeError):
        cart2 = ShoppingCart('parameter')
    assert cart.items == []
    cart.add_product(p1)
    assert cart.items == [{'product':p1,'quantity':1}]
    cart.view_cart()
    cart.remove_product(p1)
    assert cart.items == []
    assert cart.checkout() == None #this method does not return anything
    cart.add_product(p1,2)
    cart.add_product(p2,3)
    assert cart.items == [{'product':p1,'quantity':2},{'product':p2,'quantity':3}]
    cart.checkout()
    cart.remove_product(p1,3)
    cart.remove_product(p2,3)
    assert cart.items == []
    cart.add_product([p1,p2]) #adding a list causes a malfunction on later calls
    with pytest.raises(AttributeError):
        cart.view_cart()
