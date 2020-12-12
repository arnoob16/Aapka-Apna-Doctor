import selenium
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
import time
import json
driver = webdriver.Chrome('C:/Program Files (x86)/chromedriver.exe')
urlForTopicLinkPages = "https://www.webmd.com/a-to-z-guides/qa"
driver.get(urlForTopicLinkPages)
time.sleep(3)
closeModalBtn = driver.find_element_by_id("webmdHoverClose").click()
elements = driver.find_elements_by_css_selector(".channel-list li a")
topics = []
linkForTopicWiseQuestions = []
for element in elements:
    topics.append(element.text)
    linkForTopicWiseQuestions.append(element.get_attribute("href"))

topicWiseQuestions = {}
for i in range(1, len(linkForTopicWiseQuestions)):
    link = linkForTopicWiseQuestions[i]
    driver.get(link)
    time.sleep(2)
    print("Fetching all the questions for the topic - ", topics[i])
    questionTags = driver.find_elements_by_css_selector(".main-indexList-ul li a")
    questionForTopic = []
    linksForQuestionForTopic = []

    for questionTag in questionTags:
        if(questionTag.get_attribute("href") != ''):
            questionForTopic.append(questionTag.text)
            linksForQuestionForTopic.append(questionTag.get_attribute("href"))

    noobList = []
    
    for j in range (0, len(linksForQuestionForTopic)):
        driver.get(linksForQuestionForTopic[j])
        try:
            answer = driver.find_element_by_css_selector("#art-ans").text
            noobList.append({questionForTopic[j] : answer})
        except:
            continue
    topicWiseQuestions[topics[i]] = noobList

json_object = json.dumps(topicWiseQuestions, indent = 4)

with open("data.json", "w") as outfile:
    outfile.write(json_object)

driver.close()