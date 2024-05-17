import os
from datetime import datetime
from pytz import timezone
from crawling_yes24 import parsing_beautifulsoup, extract_book_data
from github_utils import get_github_repo, upload_github_issue


if __name__ == "__main__":
    access_token = os.environ['MY_GITHUB_TOKEN']
    repository_name = "github-action-with-python"

    seoul_timezone = timezone('Asia/Seoul')
    today = datetime.now(seoul_timezone)
    today_date = today.strftime("%Y년 %m월 %d일")

    yes24_it_new_product_url = "https://www.yes24.com/Product/Category/AttentionNewProduct?pageNumber=1&pageSize=24&categoryNumber=001001003"
    
    soup = parsing_beautifulsoup(yes24_it_new_product_url)
    
    issue_title = f"YES24 IT 신간 도서 알림({today_date})"
    upload_contents = extract_book_data(soup)
    repo = get_github_repo(access_token, repository_name)
    upload_github_issue(repo, issue_title, upload_contents)
    print("Upload Github Issue Success!")


