DROP TABLE IF EXISTS cohorts CASCADE;
DROP SEQUENCE IF EXISTS cohorts_id_seq;
DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS students_id_seq;

CREATE SEQUENCE IF NOT EXISTS cohorts_id_seq;
CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  cohort_name text,
  starting_date date
);

CREATE SEQUENCE IF NOT EXISTS students_id_seq;
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  student_name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id) references cohorts(id) on delete cascade
);

INSERT INTO cohorts (cohort_name, starting_date) VALUES ('Cohort A', '2022-01-01');
INSERT INTO cohorts (cohort_name, starting_date) VALUES ('Cohort B', '2022-03-01');
INSERT INTO cohorts (cohort_name, starting_date) VALUES ('Cohort C', '2022-04-01');

-- Seed students table
INSERT INTO students (student_name, cohort_id) VALUES ('John Smith', 1);
INSERT INTO students (student_name, cohort_id) VALUES ('Jane Doe', 1);
INSERT INTO students (student_name, cohort_id) VALUES ('Bob Johnson', 2);
INSERT INTO students (student_name, cohort_id) VALUES ('Sarah Lee', 2);
INSERT INTO students (student_name, cohort_id) VALUES ('Michael Davis', 3);


