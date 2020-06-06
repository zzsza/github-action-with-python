# Github Action with Python
- (1) YES24 cron Github Action
  - YES24 IT 신간 도서에 있는 TOP 40을 가져와서, 해당 Github Issue 업로드
  - 매일 오전 9시에 업로드(한국 시간)
  - Watch 클릭시 이메일로 알람받을 수 있음
- (2) hello.py 실행하는 Github Action
  - Master로 Push할 때 실행
- (3) Job에서 생성한 파일을 공유해서 사용하는 Github Action
  - [upload-artifact](https://github.com/actions/upload-artifact)와 [download-artifact](https://github.com/actions/download-artifact) 사용 예제
