import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "image/avif,image/webp,*/*",
    "Referer": "https://giaothong.hochiminhcity.gov.vn/",
    "Origin": "https://giaothong.hochiminhcity.gov.vn",
}

cookies = {
    "ASP.NET_SessionId": "t2oslxxsqllan4lgzhah3cgt",
    ".VDMS": "C50F85C6C71667BE6ED050D74003980406811A8F6C3BE32B157BABF3CD92E74B0BA3E01A4B490B8BA16EAF15828702B1FB68957AD67317B9D42579BB90FCC150AF18CA519E195678537CA47740D9831A7E454628FC6A4097185A66629BB114F7EE9611E85CE9747C30D5968598EFBF67382F9DD1",
    "_frontend": "!9YOHO1qc4zwwKz24P1VY/lC/bQptjssYZ3m9UbDnTWnCQqqoOil+geXpFacMNljkY7bQh63nOwwyIko=",
    "CurrentLanguage": "vi",
    "_pk_ses.1.2f14": "*",
    "_ga": "GA1.3.709058770.1768372334",
    "_gid": "GA1.3.969540300.1768372334",
    "_pk_id.1.2f14": "2b57dfcf6efc5ad8.1768372334.1.1768372958.1768372334.",
    "_ga_JCXT8BPG4E": "GS2.3.s1768372334$o1$g1$t1768372958$j60$l0$h0",
    "TS01e7700a": "0150c7cfd19d45b130811deec284bb08de597c3105a4f85a3faba4aaa6a660813d2a5b1aa258c8cabc797769e8c8736c1810df1ef7d4b39bdef16eddcffa7b3039a815892aa662f7ad032d8f97064986070cde4999c518edb881cbc1f7826a21f1ea185ceb"
}
url = 'https://giaothong.hochiminhcity.gov.vn/Map.aspx'
resp = requests.get(url, headers=headers, cookies=cookies)
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup)