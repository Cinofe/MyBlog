"""
    base State 모듈
"""

import pynecone as pc

class Users(pc.Model, table=True):
    """Users 테이블"""

    user_id : str
    username: str
    email : str
    passwd: str
    admin : bool = False

class state(pc.State):
    Auth : bool = False

    show_signIn: bool = False
    show_user: bool = False
    show_signUp : bool = False
    
    ## 데이터베이스 연결 테스트
    # def testDB(self):
    #     with pc.session() as session:
    #         table_names = session.execute('show tables')
    #         print(*table_names)
