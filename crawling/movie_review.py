from urllib.request import urlopen
from bs4 import BeautifulSoup

#코드 설명: 네이버 영화 url로 부터 크롤링하여 cmd 창에 후기를 print 해줌
# url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=136315&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=1'
# html = urlopen(url).read() #웹에서 정보 조회
# print(html)
# soup = BeautifulSoup(html,'html.parser')

# # review = soup.find('span',{'id':'_filtered_ment_0'})
# # review.get_text().strip() #양 옆 공백 제거

# for i in range(10):
#     review = soup.find('span',{'id':f'_filtered_ment_{i}'})
#     print(f'{i+1} 번째 리뷰')
#     print(review.get_text().strip())
#     print('--------------------')

# naver_movie_request라는 파일에 txt 파일 형태로 저장해줌(위의 코드를)
import requests
review_list = []
for page in range(1,11):
    url = f'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=136873&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={page}'
    html = requests.get(url)
    soup = BeautifulSoup(html.content,'html.parser')
    for i in range(10):
        review = soup.find('span',{'id':f'_filtered_ment_{i}'})
        review = review.get_text().strip()
        review_list.append(review)

with open('./naver_movie_request.txt','w',encoding='utf-8') as f:
    for single_review in review_list:
        f.write(single_review+'\n')