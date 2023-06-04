# Instagram 게시글 스크래퍼

이 프로젝트는 Instaloader 라이브러리를 사용하여 Instagram 게시글을 크롤링하는 기능을 제공합니다.

## 설치 및 설정

1. `requirements.txt` 파일을 사용하여 필요한 라이브러리 및 패키지를 설치합니다:

   ```shell
   pip install -r requirements.txt
   ```

2. `.env` 파일을 만들고, `USER_ID` 환경 변수에 Instagram 계정 아이디를 설정합니다.

3. 프로젝트를 실행하기 전에 필요한 환경 변수를 `.env` 파일에 설정합니다:

   ```shell
   USER_ID=your_instagram_username
   ```

## 사용 방법

Instagram 게시글을 크롤링하는 방법을 안내합니다.

1. `main.py` 파일을 실행하여 Instagram 게시글을 크롤링합니다:

   ```shell
   python main.py
   ```

2. 크롤링 대상 Instagram 계정을 `TARGET` 변수에 설정합니다. 예를 들어:

   ```python
   TARGET = ["originals_kr", "nike"]
   ```

3. `SINCE` 변수와 `UNTIL` 변수를 설정하여 크롤링할 게시글의 기간을 지정합니다. 예를 들어:

   ```python
   SINCE = datetime(2022, 12, 31)
   UNTIL = datetime(2022, 1, 1)
   ```

4. 크롤링된 데이터는 `result.csv` 파일에 저장됩니다.