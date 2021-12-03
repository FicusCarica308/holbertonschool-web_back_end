-- Temp
-- Temp

DELIMITER $$

CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score FLOAT)
BEGIN
    IF ((SELECT COUNT(name) FROM projects WHERE name = project_name) = 0)
    THEN
        INSERT INTO proejcts (name) VALUES (project_name);
    END IF;
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, (SELECT id FROM projects WHERE name = project_name LIMIT 1), score);
END
$$
DELIMITER ;