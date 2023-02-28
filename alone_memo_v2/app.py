
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로
db = client.dbjungle  # 'dbjungle'라는 이름의 db사용


@app.route('/')
def home():
    return render_template('index.html')

## 메모장 리스트 가져오기
@app.route('/memo', methods=['GET'])
def getMemoList():
    DESCENDING_ORDER = -1  # 내림차순
    ASCENDING_ORDER = 1  # 오름차순

    # 좋아요 내림차순으로 정렬하고, 정렬한 값에서 idx 오름차순으로 정렬한다. 
    # idx값이 낮을수록 더 최근에 등록된 메모입니다. 따라서 좋아요가 더 많은 것들 위로 올라오고, 그중에서도 최신순으로 나열합니다. 
    sort = {
        'likes': DESCENDING_ORDER,
        'idx': ASCENDING_ORDER
    }
    print(sort)

    # mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기
    result = list(db.memos.find({}, {'_id': 0}))
    print(result)

    return jsonify({'result':'success', 'memos': result})


## 새로운 메모 저장하기
@app.route('/memo', methods=['POST'])
def saveMemo():
    # 클라이언트로부터 데이터 받기
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']

    # collection 개수 가져오기
    result = list(db.memos.find({}, {'_id': 0}))
    count = len(result)

    # idx값 세팅
    idx = count + 1
    
    memo = {
        'idx': idx,
        'title': title_receive, 
        'content': content_receive,
        'likes' : 0,
    }
    print(memo)

    # mongoDB에 데이터 넣기
    db.memos.insert_one(memo)

    return jsonify({'result':'success', 'msg':'포스팅 성공!'})


## 메모 수정하기
@app.route('/memo', methods=['PUT'])
def updateMemo():
    idx_receive = int(request.form['idx_give'])
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']

    memo = {
        'title': title_receive, 
        'content': content_receive,
    }
    print(memo)

    db.memos.update_one({'idx':idx_receive},{'$set':memo})
    return jsonify({'result':'success', 'msg':'수정 완료!'})


## 메모 삭제하기
@app.route('/memo', methods=['DELETE'])
def deleteMemo():
    idx_receive = int(request.form['idx_give'])
    print(idx_receive)

    db.memos.delete_one({'idx':idx_receive})
    return jsonify({'result':'success', 'msg':'삭제 완료!'})


## 좋아요 추가
@app.route('/memo/likes', methods=['POST'])
def addLike():
    idx_receive = int(request.form['idx_give'])

    # 해당 메모의 기존 좋아요 개수 가져오기
    result = db.memos.find_one({'idx':idx_receive})
    like_count = result['likes']

    likes = {'likes': like_count + 1}
    print(likes)

    db.memos.update_one({'idx':idx_receive},{'$set':likes})
    return jsonify({'result':'success', 'msg':'좋아요 추가 완료!'})


if __name__ == '__main__':  
   app.run('0.0.0.0',port=8000,debug=True)
