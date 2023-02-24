import pynecone as pc

with open('DB_URL.txt','r') as f:
    url = f.readline()

config = pc.Config(
    app_name="MyBlog",
    ## 연구실 도커 마리아DB 연결
    db_url=url,
    env=pc.Env.DEV,
)
