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