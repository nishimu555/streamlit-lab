## streamlit

### install
https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker


### build

```
docker build -t streamlit-lab1 .
```

### execute

```
docker run -p 8501:8501 --name streamlit1 streamlit-lab1
```


### セッション情報
マルチページでセッション情報を保存すると、次のページは引き継ぎされるが、なぜか２ページ目以降は引き継がれない。
そのため以下のようなクラスを作成して、各ページの先頭でクリエイトすると引き継ぎされるようになる。

```python
class st_session:
    # ページ間でセッション情報を引き継ぐために、対象のキーと初期値を二重配列定義する。
    session_list=\
        [["name",""],\
        ["age",25]]
    
    def __init__(self):
        for item in self.session_list:
            if item[0] not in st.session_state:
                st.session_state[item[0]] = item[1]
            else:
                st.session_state[item[0]] = st.session_state[item[0]]
```

以下のような情報もあるが、内容がよく分からず。

https://qiita.com/niship2/items/f0c825c6f0d291583b27

