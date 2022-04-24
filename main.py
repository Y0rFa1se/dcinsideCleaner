from selenium import webdriver
import time

Driver = webdriver.Chrome(executable_path="../chromedriver.exe")

id = input("식별 코드 >> ")
url = "https://sign.dcinside.com/login?s_url=https%3A%2F%2Fgallog.dcinside.com%2F" + id

def  wait(sec):
    Driver.implicitly_wait(sec)

def run(_url):
    delAtr = input("게시글 지우기 : 1 입력/ 댓글 지우기 : 2 입력 >> ")

    if delAtr == "1":
        url = _url + "/posting"
        Driver.get(url)
        num = int(input("게시글 개수 >> "))
        for i in range(num):
            delBtn = Driver.find_element_by_xpath("//button[@class='btn_delete btn_listdel sp_img']")
            delBtn.click()
            Alert = Driver.switch_to.alert
            Alert.accept()
            print("남은 게시글: " + str(num - (i + 1)))
            time.sleep(5)

    elif delAtr == "2":
        url = _url + "/comment"
        Driver.get(url)
        num = int(input("댓글 개수 >> "))
        for i in range(num):
            delBtn = Driver.find_element_by_xpath("//button[@class='btn_delete btn_listdel sp_img']")
            delBtn.click()
            Alert = Driver.switch_to.alert
            Alert.accept()
            print("남은 댓글: " + str(num - (i + 1)))
            time.sleep(5)

Driver.get(url)
wait(1)

url = "https://gallog.dcinside.com/" + id

input("로그인 하고 엔터 >> ")

while True:
    try:
        run(url)

    except:
        input("캡챠 해결한 후에 엔터 >> ")