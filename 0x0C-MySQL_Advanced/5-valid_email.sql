-- creates a new TRIGGER
-- a trigger that resets the attribute valid_email only when the email has been changed
DELIMITER $$
CREATE TRIGGER email_validation
AFTER UPDATE ON users FOR EACH ROW
BEGIN
IF NEW.email != OLD.email THEN
UPDATE user SET valid_email = 0 WHERE email = NEW.email;
END IF;
END;
$$
