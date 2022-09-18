# Youtube Video Search Sample
Youtube Data API(https://developers.google.com/youtube/v3?hl=ja)を使用した、動画検索プログラムの例です。  
keywordを指定し、そのkeywordから動画の一覧を取得できます。

## 制限事項

Python 3.8 以降を使用してください。

## プログラムの実行

以下の手順で環境構築を行います。
```bash
$ git clone git@github.com:hareta0109/youtube-keyword-search.git
$ cd youtube-keyword-search
$ pip install -r requirements.txt
```

プログラム main.py の DEVELOPER_KEY を自己のものに書き換えてください。  
デフォルトでは50件までのデータが取得されます。  
取得件数を変更する場合は MAX_RESULTS を変更してください。
```python
MAX_RESULTS = 50
DEVELOPER_KEY = 'REPLACE_ME' # replace here
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
```

以下のコマンドでプログラムを実行できます。  
keywordには検索したい単語を入れてください。
```bash
$ python main.py keyword
```

実行結果は、以下のようにリストで出力されます。

```
[
    {
        # 動画ID
        "videoId": "P48G1k56mvE",
        # チャンネル名
        "channelTitle": "Tucker Budzyn",
        # 公開日時
        "publishedAt": "2022-09-18T12:30:16Z",
        # チャンネルID
        "channelId": "UCNSzfesc7IgWZwg4n6uXr1A",
        # 動画タイトル
        "title": "Dog Reviews Food With Son | Tucker Taste Test 23",
        # 動画概要
        "description": "Dog Reviews Food With Son | Tucker Taste Test 23 Introducing Tucker Treat Molds! Get your Tucker treat mold or lick mat bundle ...",
        # 再生回数
        "viewCount": "33836",
        # 高評価数
        "likeCount": "6394"
    },
    ...
]

```