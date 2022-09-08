CREATE TABLE IF NOT EXISTS Students(
    Code VARCHAR(6) PRIMARY KEY,
    FullName NVARCHAR(50),
    Birthday VARCHAR(20),
    Sex TINYINT(1),
    Address NVARCHAR(500),
    Phone VARCHAR(20),
    Email VARCHAR(250)
)

CREATE TABLE IF NOT EXISTS Subjects(
    Code VARCHAR(6) PRIMARY KEY,
    Name NVARCHAR(50)
)

CREATE TABLE IF NOT EXISTS Scores(
    StudentCode VARCHAR(6),
    SubjectCode VARCHAR(6),
    Score1 INT,
    Score2 INT,
    PRIMARY KEY (StudentCode, SubjectCode),
    FOREIGN KEY(StudentCode) REFERENCES Students(Code),
    FOREIGN KEY(SubjectCode) REFERENCES Subjects(Code)
)

INSERT INTO Students(Code, FullName, Birthday, Sex, Address, Phone, Email)
VALUES
    ("ST0001", "Cuong Nguyen", "17/08/1994", 1, "Việt Nam", "0977677010", "cuongnhict@gmail.com"),
    ("ST0002", "Tường An", "17/08/1994", 0, "Nhật Bản", "0977677010", "tuongan@gmail.com"),
    ("ST0003", "Như Phương", "17/08/1994", 0, "Nhật Bản", "0977677010", "nhuphuong@gmail.com"),
    ("ST0004", "Phương Thảo", "02/02/2002", 0, "Việt Nam", "0977777777", "phuongthao@gmail.com"),
    ("ST0005", "Trọng Nghĩa", "01/01/2000", 1, "Nhật Bản", "1111111111", "nghia@gmail.com"),
    ("ST0006", "Đồng Tài", "03/03/2003", 1, "Nhật Bản", "1111111111", "tai@gmail.com");

INSERT INTO Subjects(Code, Name)
VALUES
	("SU0001", "Database"),
	("SU0002", "Basic Python"),
	("SU0003", "Advanced Python");

INSERT INTO Scores(StudentCode, SubjectCode, Score1, Score2)
VALUES
	("ST0002", "SU0001", 80, 85),
	("ST0002", "SU0002", 85, 85),
	("ST0002", "SU0003", 75, 80),
	("ST0003", "SU0001", 75, 75),
	("ST0003", "SU0002", 85, 80),
	("ST0003", "SU0003", 85, 80);