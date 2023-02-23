import pynecone as pc

config = pc.Config(
    app_name="MyBlog",
    ## 연구실 도커 마리아DB 연결
    db_url="mysql+pymysql://root:tmdsony84@210.125.31.101:443/Myblog?charset=utf8",
    env=pc.Env.DEV,
)
