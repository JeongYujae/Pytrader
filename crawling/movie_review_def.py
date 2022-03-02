from urllib import request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests



def get_url(a): #Number of review
    #Movie code
    url_data=[80737,208558]
    review_list=[]
    for i in url_data:
        url=f'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code={i}&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=1'
        html = requests.get(url) #웹에서 정보 조회
        soup = BeautifulSoup(html.content,'html.parser') #html정보 가져오는 코드
        for x in range(a):
            review = soup.find('span',{'id':f'_filtered_ment_{x}'})
            review_list.append(review.get_text().strip()) #양 옆 공백 제거
    f=open('./naver_movie_request_def.txt','w',encoding='utf-8')
    for single_review in review_list:
        f.write(single_review+'\n')
        if len(f.readlines())%a==0:
            f.write('-------------')
        
    f.close()

            
get_url(5)