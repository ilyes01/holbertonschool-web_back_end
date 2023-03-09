-- comments 
-- coments 
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE total_weighted_score FLOAT DEFAULT 0;
    DECLARE total_weight FLOAT DEFAULT 0;
    DECLARE user_id INT;
    DECLARE project_id INT;
    DECLARE project_weight INT;
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    DECLARE project_cursor CURSOR FOR SELECT id, weight FROM projects;

    -- Open user cursor anddd loop through all users
    OPEN user_cursor;
    user_loop: LOOP
        FETCH user_cursor INTO user_id;
        IF (user_id IS NULL) THEN
            LEAVE user_loop;
        END IF;

        -- Reset the weight score and total weight for users
        SET total_weighted_score = 0;
        SET total_weight = 0;

        -- Open project cursor and loop through all projects
        OPEN project_cursor;
        project_loop: LOOP
            FETCH project_cursor INTO project_id, project_weight;
            IF (project_id IS NULL) THEN
                LEAVE project_loop;
            END IF;

            -- Compute the weighted score in the current project and ad it to the total
            SET total_weighted_score = total_weighted_score + (SELECT score FROM corrections WHERE user_id = user_id AND project_id = project_id) * project_weight;
            SET total_weight = total_weight + project_weight;
        END LOOP;
        CLOSE project_cursor;

        -- Compute the average weighted score for the user and update table
        UPDATE users SET average_score = total_weighted_score / total_weight WHERE id = user_id;
    END LOOP;
    CLOSE user_cursor;
END $$
DELIMITER ;
