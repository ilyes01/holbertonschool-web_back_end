CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE total_weight FLOAT;
    DECLARE total_score FLOAT;
    DECLARE user_id INT;
    DECLARE project_id INT;
    DECLARE project_weight INT;
    DECLARE project_score FLOAT;
    DECLARE cur CURSOR FOR SELECT user_id, project_id, score, weight FROM corrections JOIN projects ON corrections.project_id = projects.id;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET @done = 1;

    OPEN cur;
    SET total_weight = 0;
    SET total_score = 0;

    SET @done = 0;
    REPEAT
        FETCH cur INTO user_id, project_id, project_score, project_weight;
        IF NOT @done THEN
            SET total_weight = total_weight + project_weight;
            SET total_score = total_score + project_score * project_weight;
        END IF;
    UNTIL @done END REPEAT;

    CLOSE cur;

    UPDATE users SET average_score = total_score / total_weight;
END;
