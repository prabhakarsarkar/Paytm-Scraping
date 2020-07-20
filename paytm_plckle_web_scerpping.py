# import requests
# from bs4 import BeautifulSoup
# from pprint import pprint 

# def paytm_plckle():
# 	res=requests.get("https://paytm.com/shop/search?q=pickles&from=organic&child_site_id=1&site_id=1&category=101471")
# 	soup=BeautifulSoup(res.text,"html.parser")
# 	rate=soup.find_all("span",class_="_1kMS")
# 	b=0
# 	for i in rate:
# 		b+=1
# 		print(i.text)
# 	usre=input("yes/no")
# 	a=soup.find("button",class_="_2f0U").text
# 	for j in range(1):
# 		if a==usre:
# 			 	continue
# paytm_plckle()




# from   selenium import webdriver
# from bs4 import BeautifulSoup
# from pprint import pprint
# list1=[]
# def pickles():
# 	dict1={}
# 	browser = webdriver.Chrome()
# 	browser.get("https://paytm.com/shop/search?q=pickles&from=recentSearch&child_site_id=1&site_id=1&category=101471")
# 	driver=browser.execute_script("return document.documentElement.outerHTML")
# 	soup=BeautifulSoup(driver,'html.parser')
# 	price=soup.find_all('span',class_='_1kMS')
# 	for i in price:
# 		print(i.text)

	
# # pickles()






# import requests,webbrowser,random
# from bs4 import BeautifulSoup
# url=requests.get("https://paytmmall.com/sports-and-health-clpid-83?src=store&use_sf=1")
# soup=BeautifulSoup(url.text,"html.parser")
# print ("***********Welcome to %s*************"%soup.title.text)
# main_div=soup.find("div",class_="_1_Nn")
# all_a=main_div.find_all("a")
# num=1
# url_list=[]
# for a in all_a:
#     print (num,a.text)
#     url_list.append(a["href"])
#     num+=1
#     # print(url_list)
# user=input("which category you want(1,2,3) : ")
# url2=requests.get("https://paytmmall.com/"+url_list[int(user)-1])
# soup2=BeautifulSoup(url2.text,"html.parser")
# mainDiv=soup2.find("div",class_="_3RA-")
# divs=mainDiv.find_all("div",class_="_1fje")
# count=1
# h_list=[]
# color=str(random.randint(31,37))
# for div in divs:
#     DIV=div.find_all("div",class_="_2i1r")
#     for i in DIV:
#         print("\033[1;"+color+";40m"+str(count)+" "+i.find("a").get("title"))
#         count+=1
#         price=i.find("a").find("span")
#         print ("  Price : "+price.text)
#         print (" "+i.find("div",class_="_27VV").text)
#         h_list.append("https://paytmmall.com/"+i.find("a")["href"])
# user=int(input("which want to you : "))
# webbrowser.open_new_tab(h_list[user-1])







# atags=soup1.find_all("div",class_="col-s-12")
# 	address=soup1.find_all("div",class_="col-s-16  col-m-12  pl0  ")
# 	price=soup1.find("span",class_="col-s-11 col-m-12 pl0").text
# 	time=soup1.find("div",class_="res-timing clearfix")
# 	print(address)
# 	# print(time.get("title"))
# 	# for n in atags:
# 	# 	atag = n.find("a",class_="result-title")
	# 	name=atag.get("title")
	# 	print(name)
	# driver1.quit()
	
		