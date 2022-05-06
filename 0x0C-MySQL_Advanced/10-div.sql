-- sql function that divides the first number by the second if the second = 0 
DELIMITER $$
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT
if b = 0
THEN RETURN 0 ;
ELSE
RETURN a / b;
END IF;
END$$
