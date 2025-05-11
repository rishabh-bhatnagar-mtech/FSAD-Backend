CREATE TABLE drives
(
    id                 VARCHAR(16) PRIMARY KEY,
    name               VARCHAR(100) NOT NULL,
    date               DATE         NOT NULL,
    doses_available    INT          NOT NULL,
    applicable_classes VARCHAR(255) NOT NULL,
    vaccine_name       VARCHAR(255) NOT NULL
);

CREATE TABLE vaccines
(
    id   SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE students
(
    id    VARCHAR(16) PRIMARY KEY,
    name  VARCHAR(100) NOT NULL,
    class VARCHAR(16)  NOT NULL
);

CREATE TABLE student_vaccines
(
    student_id VARCHAR(16) REFERENCES students (id) ON DELETE CASCADE,
    vaccine_id INT REFERENCES vaccines (id) ON DELETE CASCADE,
    drive_id   VARCHAR(16) REFERENCES drives (id),
    PRIMARY KEY (student_id, vaccine_id)
);

INSERT INTO drives (id, name, date, doses_available, applicable_classes, vaccine_name)
VALUES ('DRV001', 'Drive A', '2024-07-01', 100, '10th,11th,12th', 'Covishield'),
       ('DRV002', 'Drive B', '2024-07-02', 150, '9th,10th', 'Covaxin'),
       ('DRV003', 'Drive C', '2024-07-03', 200, '11th,12th', 'Covishield');


INSERT INTO vaccines (name)
VALUES ('Covishield'),
       ('Covaxin'),
       ('Sputnik');

INSERT INTO students (id, name, class)
VALUES ('STU1001', 'Aarav', '10th'),
       ('STU1002', 'Isha', '12th'),
       ('STU1003', 'Rohan', '11th'),
       ('STU1004', 'Sneha', '9th'),
       ('STU1005', 'Karan', '10th');

INSERT INTO student_vaccines (student_id, vaccine_id, drive_id)
VALUES ('STU1001', (SELECT id FROM vaccines WHERE name = 'Covishield'), 'DRV001'),
       ('STU1001', (SELECT id FROM vaccines WHERE name = 'Covaxin'), 'DRV002'),
       ('STU1002', (SELECT id FROM vaccines WHERE name = 'Covishield'), 'DRV001'),
       ('STU1004', (SELECT id FROM vaccines WHERE name = 'Covaxin'), 'DRV002'),
       ('STU1005', (SELECT id FROM vaccines WHERE name = 'Covishield'), 'DRV001'),
       ('STU1005', (SELECT id FROM vaccines WHERE name = 'Sputnik'), 'DRV003');
