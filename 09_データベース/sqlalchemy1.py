""" sqlalchemyの練習.
sqlliteやmysql独自の技法を用いずに,
DBアクセスするsqlalchemyで共通する書き方でDBにアクセスする.
"""
import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

# メモリー上にsqliteを作成する.という意味
# ENGINE = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)

# sqlite型のDBにデータを保存する.という意味.
# ENGINE = sqlalchemy.create_engine('sqlite:///test_sqlite2', echo=True)
# $ sqlite3 test_sqlite2 として, sqlite3型のDBとの対話型モードに突入.
# $ .tables で, テーブルの種類を出力.
# $ select * from persons; で, データを取得.
# $ control + D で, 対話型モード終了.

# sql型のDBにデータを保存する.という意味.
ENGINE = sqlalchemy.create_engine('mysql+pymysql://root@localhost/test_mysql_database2', echo=True)
# $ brew services start mysql で, mysqlを起動して,
# $ mysql -u root で, mysqlとの対話型モードに入って,
# mysql> show databases; で, データベースのテーブルを確認して,
# mysql> use test_mysql_database2; で, test_mysql_database2にテーブルを切り替えて,
# mysql> SELECT * FROM persons; で, テーブルの中身を確認する.
# $ control + D で, 対話型モード終了.
# $ brew services stop mysql で, mysqlを停止.

Base = sqlalchemy.ext.declarative.declarative_base()

class Person(Base):
    """ Person というクラス """
    __tablename__ = 'persons'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14))

Base.metadata.create_all(ENGINE)

SESSION = sqlalchemy.orm.sessionmaker(bind=ENGINE)
session = SESSION()

# Personというクラスのオブジェクトを生成
PERSON1 = Person(name='Mike') # Mike というPERSONを生成して,
session.add(PERSON1) # addして,
PERSON2 = Person(name='Taro') # Taro というPERSONを生成して,
session.add(PERSON2) # addして,
PERSON3 = Person(name='Jiro') # Jiro というPERSONを生成して,
session.add(PERSON3) # addして,
session.commit() # commitしてあげる.

# 一人目のMikeをMichelに変更してる.
P4 = session.query(Person).filter_by(name='Mike').first()
P4.name = 'Michel'
session.add(P4)
session.commit()

# 一人目のTaroを削除している.
P5 = session.query(Person).filter_by(name='Taro').first()
session.delete(P5)
session.commit()

# Person型のデータを全部出力.
PERSONS = session.query(Person).all()
for person in PERSONS:
    print(person.id, person.name)
