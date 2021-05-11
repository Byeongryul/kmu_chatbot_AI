import pymysql
from src.config.DatabaseConfig import * # DB 접속 정보 불러오기

db = None
try:
    db = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWORD,
        db=DB_NAME,
        charset='utf8mb4'
    )

    # 테이블 생성 sql 정의
    answer = '''
    CREATE TABLE IF NOT EXISTS `answer` (
        `title` VARCHAR(45) NOT NULL,
        `document` VARCHAR(1000) NULL DEFAULT NULL,
        `url` VARCHAR(300) NULL DEFAULT NULL,
        PRIMARY KEY (`title`), UNIQUE INDEX `answer_UNIQUE` (`url` ASC) VISIBLE)
    ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;
    '''
    answer_button = '''
    CREATE TABLE IF NOT EXISTS `answer_button` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `title` VARCHAR(45) NOT NULL,
        `button_name` VARCHAR(45) NOT NULL,
        `button_url` VARCHAR(500) NOT NULL,
        PRIMARY KEY (`id`), UNIQUE INDEX `answer_button_UNIQUE` (`button_url` ASC) VISIBLE)
    ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;
    '''
    # 테이블 생성
    with db.cursor() as cursor:
        cursor.execute(answer)
        cursor.execute(answer_button)

except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()


