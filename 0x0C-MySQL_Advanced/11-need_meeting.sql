-- sql script that create view
CREATE VIEW need_meeting AS
SELECT name FROM students
where last_meeting < ADDDATE(CURDATE(), INTERVAL -1 MONTH)
OR score < 80 AND ISNULL(last_meeting);
