import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Student

# データベース接続情報
DATABASE_URL = "postgresql://user:password@localhost:5432/db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def seed_data():
    session = SessionLocal()
    try:
        # サンプルデータを挿入
        session.add_all(
            [
                Student(
                    name="Alice",
                    age=6,
                    created_at=datetime.datetime(2024, 1, 1, 10, 0, 0),
                ),
                Student(
                    name="Bob",
                    age=5,
                    created_at=datetime.datetime(2024, 1, 2, 11, 0, 0),
                ),
                Student(
                    name="Charlie",
                    age=7,
                    created_at=datetime.datetime(2024, 1, 3, 12, 0, 0),
                ),
            ]
        )
        session.commit()
        print("Sample data inserted successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error occurred: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)  # 必要ならテーブル作成
    seed_data()
