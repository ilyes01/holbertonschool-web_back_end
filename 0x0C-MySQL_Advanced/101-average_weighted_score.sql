-- comments 
-- commentssss
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
DROP TEMPORARY TABLE IF EXISTS users_stats;
CREATE TEMPORARY TABLE users_stats AS
SELECT cor.user_id, (SUM(cor.score * pro.weight) / SUM(pro.weight)) as weighted_score
FROM corrections AS cor
JOIN projects AS pro ON pro.id = cor.project_id
GROUP BY cor.user_id;
UPDATE users AS usr
INNER JOIN users_stats uss ON usr.id = uss.user_id
SET usr.average_score = uss.weighted_score;

DROP TEMPORARY TABLE IF EXISTS users_stats;
END//
DELIMITER ;
