import json
def show_menu():
    main_menu="""
*************welcome***********
1.register service
2.edit service
3.delete service
4.quit
"""
print(main_menu)
def ask_option ():
    return input("enter the desired option")
def create_service():
    request_name= input"enter the desired name"
    request_price= input"enter the desired price"
    request_type= input"enter the desired type of event"
    request_duration= input"enter the desired duration"
    request = {
        "name": request_name,
        "price": request_price,
        "type": request_type,
        "duration" request_duration
    }
print("request saved")

