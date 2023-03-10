from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd

driver = webdriver.Chrome(executable_path="E:\anaconda\chromedriver.exe")
driver.maximize_window()
driver.get('https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%252')
driver.implicitly_wait(5)
main=driver.current_window_handle
df=pd.DataFrame(columns=['Product URL','Product Name','Price','Rating','Number of reviews','Description','ASIN','Product Description','Manufacturer'])

pages=0
def hi(df,div,pages):
    pages+=1
    if pages>20:
        return df
    
    for d in range(3,div+1):
        try:
            
            driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div['+str(d)+']/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a').click()
            try:
                time.sleep(4)
                z=driver.window_handles
                driver.switch_to.window(z[1])
                url=driver.current_url
                title=driver.title

                
                scroll_time_pause = 2
                
                last_height = driver.execute_script('return document.body.scrollHeight')

                while True:
                    
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                    
                    time.sleep(scroll_time_pause)

                    
                    new_height = driver.execute_script('return document.body.scrollHeight')
                    if new_height == last_height:
                        break
                    last_height = new_height
                driver.execute_script("window.scrollTo(0,0)")
                try:
                    price=driver.find_element(By.XPATH,'//*[@id="corePrice_feature_div"]/div/span/span[2]/span[2]').text
                except:
                    try:
                        price=driver.find_element(By.XPATH,'//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[1]').text
                    except:
                        price='Price Missing'
                
                #description
                try:
                    des=driver.find_elements(By.XPATH,'//*[@id="feature-bullets"]/ul')
                    l=[]
                    for i in des:
                        l.append(i.text)
                    description=[]
                    for i in range(len(l)):
                        description.append(l[i].split('\n'))
                except:
                    description=[['Missing']]
                description=description[0]
                description=' '.join(description)






                #manufacturer
                try:
                    a=driver.find_elements(By.XPATH,'//*[@id="detailBullets_feature_div"]/ul')
                    l=[]
                    for i in a:
                        l.append(i.text)
                    for i in range(len(l)):
                        l=l[i].split('\n')
                    ma=[]
                    s=[]
                    for i in l:
                        if i[0:12]=='Manufacturer':
                            s.append(i)
                        elif i[0:4]=='ASIN':
                            s.append(i)
                        if len(s)==2:
                            ma.append(s)
                            break
                    manu=ma[0][0]
                    asin=ma[0][1]
                except:
                    try:
                        manu=driver.find_element(By.XPATH,'//*[@id="productDetails_techSpec_section_1"]/tbody/tr[2]/td').text

                        asin=driver.find_element(By.XPATH,'//*[@id="productDetails_detailBullets_sections1"]/tbody/tr[1]/td').text
                    except:
                        manu='missing'
                        asin='missing'


                





                #product description
                try:
                    a=driver.find_elements(By.XPATH,'//*[@id="aplus"]/div')
                    l=[]
                    for i in a:
                        l.append(i.text)
                    pd=[]
                    for i in range(len(l)):
                        pd.append(l[i].split('\n'))
                    pd=pd[0]
                    pd=' '.join(pd)
                except:
                    pd='missing'
                



                try:
                    rating=driver.find_element(By.XPATH,'//*[@id="reviewsMedley"]/div/div[1]/span[1]/span/div[2]/div/div[2]/div/span/span').text
                except:
                    rating='rmissing'
                
                try:
                    driver.find_element(By.XPATH,'//*[@id="reviews-medley-footer"]/div[2]/a').click()
                    time.sleep(2)
                    try:
                        reviews=driver.find_element(By.XPATH,'//*[@id="filter-info-section"]/div').text
                        rev=reviews.split(', ')
                        review=rev[1]
                        ratedBy=rev[0]
                    except:
                        review='0'
                        ratedBy='0'
                    
                    driver.back()
                    time.sleep(3)
                except:
                    review='0'
                    ratedBy='0'

                driver.close()

                driver.switch_to.window(main)

                list1=[url,title,price,rating,review,description,asin,pd,manu]
                
                df.loc[len(df)]=list1

                
            except:
                driver.switch_to.window(main)
            
            
        except:
            try:
                
                driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div['+str(d)+']/div/div/div/div/div/div[2]/div/div/div[1]/h2/a').click()
                try:
                    time.sleep(4)
                    z=driver.window_handles
                    driver.switch_to.window(z[1])
                    url=driver.current_url
                    title=driver.title
                    
                    
                    scroll_time_pause = 2
                    
                    last_height = driver.execute_script('return document.body.scrollHeight')

                    while True:
                        
                        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                        
                        time.sleep(scroll_time_pause)

                        
                        new_height = driver.execute_script('return document.body.scrollHeight')
                        if new_height == last_height:
                            break
                        last_height = new_height
                    driver.execute_script("window.scrollTo(0,0)")
                    try:
                        price=driver.find_element(By.XPATH,'//*[@id="corePrice_feature_div"]/div/span/span[2]/span[2]').text
                    except:
                        try:
                            price=driver.find_element(By.XPATH,'//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[1]').text
                        except:
                            price='Price Missing'
                    
                    #description
                    try:
                        des=driver.find_elements(By.XPATH,'//*[@id="feature-bullets"]/ul')
                        l=[]
                        for i in des:
                            l.append(i.text)
                        description=[]
                        for i in range(len(l)):
                            description.append(l[i].split('\n'))
                    except:
                        description=[['Missing']]
                    description=description[0]
                    description=' '.join(description)



                    #manufacturer
                    try:
                        a=driver.find_elements(By.XPATH,'//*[@id="detailBullets_feature_div"]/ul')
                        l=[]
                        for i in a:
                            l.append(i.text)
                        for i in range(len(l)):
                            l=l[i].split('\n')
                        ma=[]
                        s=[]
                        for i in l:
                            if i[0:12]=='Manufacturer':
                                s.append(i)
                            elif i[0:4]=='ASIN':
                                s.append(i)
                            if len(s)==2:
                                ma.append(s)
                                break
                        manu=ma[0][0]
                        asin=ma[0][1]
                    except:
                        try:
                            manu=driver.find_element(By.XPATH,'//*[@id="productDetails_techSpec_section_1"]/tbody/tr[2]/td').text
                            asin=driver.find_element(By.XPATH,'//*[@id="productDetails_detailBullets_sections1"]/tbody/tr[1]/td').text
                        except:
                            manu='missing'
                            asin='missing'

                    

                    #product description
                    try:
                        a=driver.find_elements(By.XPATH,'//*[@id="aplus"]/div')
                        l=[]
                        for i in a:
                            l.append(i.text)
                        pd=[]
                        for i in range(len(l)):
                            pd.append(l[i].split('\n'))
                        pd=pd[0]
                        pd=' '.join(pd)
                    except:
                        pd='missing'
                    


                    try:
                        rating=driver.find_element(By.XPATH,'//*[@id="reviewsMedley"]/div/div[1]/span[1]/span/div[2]/div/div[2]/div/span/span').text
                    except:
                        rating='rmissing'
                    try:
                        driver.find_element(By.XPATH,'//*[@id="reviews-medley-footer"]/div[2]/a').click()
                        time.sleep(2)
                        try:
                            reviews=driver.find_element(By.XPATH,'//*[@id="filter-info-section"]/div').text
                            rev=reviews.split(', ')
                            review=rev[1]
                            ratedBy=rev[0]
                        except:
                            review='0'
                            ratedBy='0'
                        driver.back()
                        time.sleep(3)
                    except:
                        review='0'
                        ratedBy='0'

                    driver.close()

                    
                    driver.switch_to.window(main)

                    list1=[url,title,price,rating,review,description,asin,pd,manu]
                    
                    df.loc[len(df)]=list1

                    
                except:
                    driver.switch_to.window(main)


            except:
                try:
                    
                    driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div['+str(d)+']/div/div/span/div/div/div/div/div[2]/div/div/div/div[3]/div/div[2]/a').click()
                    try:
                        time.sleep(4)
                        url=driver.current_url
                        title=driver.title
                        
                        
                        scroll_time_pause = 2
                        
                        last_height = driver.execute_script('return document.body.scrollHeight')

                        while True:
                            
                            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                            
                            time.sleep(scroll_time_pause)

                            
                            new_height = driver.execute_script('return document.body.scrollHeight')
                            if new_height == last_height:
                                break
                            last_height = new_height
                        driver.execute_script("window.scrollTo(0,0)")
                        try:
                            price=driver.find_element(By.XPATH,'//*[@id="corePrice_feature_div"]/div/span/span[2]/span[2]').text
                        except:
                            try:
                                price=driver.find_element(By.XPATH,'//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[1]').text
                            except:
                                price='Price Missing'

                        
                        #description
                        try:
                            des=driver.find_elements(By.XPATH,'//*[@id="feature-bullets"]/ul')
                            l=[]
                            for i in des:
                                l.append(i.text)
                            description=[]
                            for i in range(len(l)):
                                description.append(l[i].split('\n'))
                            
                        except:
                            description=[['Missing']]
                        description=description[0]
                        description=' '.join(description)


                        #manufacturer
                        try:
                            a=driver.find_elements(By.XPATH,'//*[@id="detailBullets_feature_div"]/ul')
                            l=[]
                            for i in a:
                                l.append(i.text)
                            for i in range(len(l)):
                                l=l[i].split('\n')
                            ma=[]
                            s=[]
                            for i in l:
                                if i[0:12]=='Manufacturer':
                                    s.append(i)
                                elif i[0:4]=='ASIN':
                                    s.append(i)
                                if len(s)==2:
                                    ma.append(s)
                                    break
                            manu=ma[0][0]
                            asin=ma[0][1]
                        except:
                            try:
                                manu=driver.find_element(By.XPATH,'//*[@id="productDetails_techSpec_section_1"]/tbody/tr[2]/td').text
                                asin=driver.find_element(By.XPATH,'//*[@id="productDetails_detailBullets_sections1"]/tbody/tr[1]/td').text
                            except:
                                manu='missing'
                                asin='missing'
                        

                        #product description
                        try:
                            a=driver.find_elements(By.XPATH,'//*[@id="aplus"]/div')
                            l=[]
                            for i in a:
                                l.append(i.text)
                            pd=[]
                            for i in range(len(l)):
                                pd.append(l[i].split('\n'))
                            pd=pd[0]
                            pd=' '.join(pd)
                        except:
                            pd='missing'
                        


                        try:
                            rating=driver.find_element(By.XPATH,'//*[@id="reviewsMedley"]/div/div[1]/span[1]/span/div[2]/div/div[2]/div/span/span').text
                        except:
                            rating='rmissing'
                        
                        try:
                            driver.find_element(By.XPATH,'//*[@id="reviews-medley-footer"]/div[2]/a').click()
                            time.sleep(2)
                            try:
                                reviews=driver.find_element(By.XPATH,'//*[@id="filter-info-section"]/div').text
                                rev=reviews.split(', ')
                                review=rev[1]
                                ratedBy=rev[0]
                            except:
                                review='0'
                                ratedBy='0'
                            driver.back()
                            time.sleep(3)
                        except:
                            review='0'
                            ratedBy='0'
                        driver.back()
                        
                        list1=[url,title,price,rating,review,description,asin,pd,manu]
                        
                        df.loc[len(df)]=list1
                        
                    except:
                        driver.back()
                except:
                    pass
        #next page
        try:
            driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div['+str(d)+']/div/div/span/a[3]').click()
            time.sleep(5)
            divs=driver.find_elements(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div')       
            df=hi(df,len(divs),pages)
        except:
            pass     
    return df
          
divs=driver.find_elements(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div')       
df=hi(df,len(divs),pages)

df.to_csv('Amazon_Data_Fetch.csv')
