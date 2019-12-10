from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Schedule:
    def __init__(self, title, room, start, end, day):
        self.title = title
        self.room = room
        self.start = start
        self.end = end
        self.day = day
    def __str__(self):
        return self.title+self.room+self.start+self.end+self.day

def chunks(l, n): 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 

def generate_day(n):
    if n == 1:
        return "Senin"
    elif n == 2:
        return "Selasa"
    elif n == 3:
        return "Rabu"
    elif n == 4:
        return "Kamis"
    elif n == 5:
        return "Jumat"
    elif n == 6:
        return "Sabtu"
    elif n == 7:
        return "Minggu"

def get_course_schedule(username, password):
    driver = webdriver.Chrome()
    driver.get("https://academic.ui.ac.id/main/CoursePlan/CoursePlanViewSchedule")
    elem = driver.find_element_by_id("u")
    elem.send_keys(username)
    elem = driver.find_element_by_name("p")
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)

    driver.get("https://academic.ui.ac.id/main/CoursePlan/CoursePlanViewSchedule")
    result = []
    for day in range(2,7):
        row = driver.find_element_by_xpath(f'//*[@id="ti_m1"]/table/tbody/tr[2]/td[{day}]')
        subjects_per_day = list(chunks(row.text.split('\n'), 3))
        for subject in subjects_per_day:
            start_end_time = subject[0].split(" - ")
            res = Schedule(subject[1], subject[2],  start_end_time[0], start_end_time[1], generate_day(day-1))
            result.append(res)
        
    driver.close()
    return result