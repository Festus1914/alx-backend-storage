DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE user_score FLOAT;
    
    -- Calculate the average score for the specified user
    SELECT AVG(score) INTO user_score
    FROM corrections
    WHERE user_id = user_id;
    
    -- Update the user's average_score in the users table
    UPDATE users
    SET average_score = user_score
    WHERE id = user_id;
    
END//

DELIMITER ;
