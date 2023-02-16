
from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로
db = client.dbjungle  # 'dbjungle'라는 이름의 db를 만들거나 사용


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


## 메모장 리스트 가져오기
@app.route('/memo', methods=['GET'])
def getArticleList():
    # mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기 (Read)
    result = list(db.articles.find({}, {'_id': 0}))
    print(result)
    return jsonify({'result':'success', 'msg':'GET 연결되었습니다!', 'articles': result})


## 새로운 메모 저장하기
@app.route('/memo', methods=['POST'])
def saveArticle():
    # 클라이언트로부터 데이터 받기
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']
    print(url_receive)
    print(comment_receive)

    # meta tag 스크래핑하기 
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')
    og_description = soup.select_one('meta[property="og:description"]')

    url_title = og_title['content']
    url_description = og_description['content']
    url_image = og_image['content']

    article = {
        'url': url_receive, 
        'title': url_title, 
        'desc': url_description, 
        'image': url_image, 
        'comment': comment_receive
    }
    print(article)

    # mongoDB에 데이터 넣기
    db.articles.insert_one(article)

    return jsonify({'result':'success', 'msg':'카드가 생성되었습니다!'})


if __name__ == '__main__':  
   app.run('0.0.0.0',port=8000,debug=True)
