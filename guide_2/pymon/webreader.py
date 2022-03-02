import requests
import re
import pandas as pd

def get_financial_statements(code):
    # 기업현황 페이지
    url = f'https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd={code}'
    html = requests.get(url).text
    re_enc = re.compile("encparam: '(.*)'", re.IGNORECASE)
    re_id = re.compile("id: '([a-zA-Z0-9]*)' ?", re.IGNORECASE)
    encparam = re_enc.search(html).group(1)
    encid = re_id.search(html).group(1)

    # 기업현황 페이지 > 재무정보 섹션 > 연간/ cmp_cd -> 종목코드
    url = f'http://companyinfo.stock.naver.com/v1/company/ajax/cF1001.aspx?cmp_cd={code}&fin_type=0&freq_type=A&encparam={encparam}&id={encid}'
    headers = {'Referer': 'HACK'}
    html = requests.get(url, headers=headers).text

    dfs = pd.read_html(html)
    df = dfs[1]  # 두번째 테이블이 진짜 테이블
    df.columns = df.columns.get_level_values(1)  # multi columns에서 두번째 칼럼으로만 설정
    df.set_index('주요재무정보', inplace=True)  # 주요재무정보열을 인덱스로 사용
    ser = df.loc['현금배당수익률']  # 현금배당수익률행를 시리즈로 저장
    ser.index = ser.index.str[:7]  # 인덱스 문구에서 '연도/날짜'만 남기기

    return ser.to_dict()


if __name__ == '__main__':
    dict = get_financial_statements('005930')
    print(dict)