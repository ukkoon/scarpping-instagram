import csv
import os
from datetime import datetime
from itertools import dropwhile, takewhile
from random import randint
from time import sleep
from instaloader import Instaloader, Profile
from dotenv import load_dotenv
load_dotenv(verbose=True, override=True)

# 인스타그램 로더
L = Instaloader()

# 크롤링 타겟 (인스타그램 아이디)
# 아디다스 공식 인스타그램 계정 
TARGET = ["originals_kr"]

# 크롤링에 사용할 유저 크레덴셜
USER_ID = os.environ.get("USER_ID")

# 인스타그램 로그인
L.interactive_login(USER_ID)

# 저장된 유저 크레덴셜을 사용한  로그인
# L.load_session_from_file(USER_ID)

fields = ['shortcode', 'caption', 'hashtag']

SINCE = datetime(2022, 12, 31)
UNTIL = datetime(2022, 1, 1)

print (f"{TARGET}에 대한 {UNTIL}~{SINCE} 게시글 수집 시작")

result = []

try:
    for target in TARGET:
        #block 방지를 위한 크롤링 Delay
        sleep(randint(3, 4))
        posts = Profile.from_username(L.context, target).get_posts()

        for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):            
            caption= post.caption

            if caption is not None:
                caption = ' '.join(caption.split())

            hashtag = ' '.join(post.caption_hashtags)
            
            # 포스트 id, caption, hashtag 등을 저장
            result.append([post.shortcode, caption, hashtag])


    #결과를 csv 파일로 저장
    with open(f'{target}_{UNTIL}-{SINCE}.csv', 'w', newline='\n') as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(result[0:1000])


except KeyboardInterrupt as e:    
    print(f"크롤링 중단 : {e}")

except Exception as e:
    print(f"크롤링 실패 : {e}")