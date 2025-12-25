CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email_address VARCHAR(255) UNIQUE NOT NULL,
    subscription_status VARCHAR(50) NOT NULL,
    email_frequency VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS email_logs (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
	first_name VARCHAR(255) NOT NULL,
    email_address VARCHAR(255) NOT NULL,
    quote_date DATE NOT NULL,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (user_id, email_address, quote_date)
	);

INSERT INTO users (
    first_name,
    last_name,
    email_address,
    subscription_status,
    email_frequency)
VALUES
('Olusegun', 'Fakayode', 'fakayodeoluseguno@gmail.com', 'active', 'daily'),
('Omosola', 'Olukayode', 'omosoladaramola@gmail.com', 'active', 'weekly'),
('Obaloluwa', 'Adebisi', 'ericolukayodeo@gmail.com', 'active', 'daily'),
('Beejan', 'Davis', 'beejan@dataengineeringcommunity.com', 'active', 'weekly'),
('Feyisayo', 'Ajiboye', 'solapeajiboye@gmail.com', 'active', 'daily'),
('Esther', 'Ogunrinde', 'ogunrindee2@gmail.com', 'active', 'daily'),
('Oluwakemi', 'Akinyede', 'akinyedeoluwakemi@gmail.com', 'active', 'daily'),
('Paul', 'Oyelaran', 'oyelaranpaul@gmail.com', 'active', 'daily'),
('Yusuf', 'Alade', 'aladeyussuf.kofo@gmail.com', 'active', 'daily'),
('Ibrahim', 'Akinyele', 'iakinyele3@gmail.com', 'inactive', 'weekly'),
('William', 'Jackson', 'william.jackson@example.com', 'active', 'daily'),
('Isabella', 'White', 'isabella.white@example.com', 'inactive', 'daily'),
('Ethan', 'Harris', 'ethan.harris@example.com', 'active', 'weekly'),
('Mia', 'Martin', 'mia.martin@example.com', 'active', 'daily'),
('Alexander', 'Thompson', 'alexander.thompson@example.com', 'inactive', 'weekly'),
('Charlotte', 'Garcia', 'charlotte.garcia@example.com', 'inactive', 'daily'),
('Benjamin', 'Clark', 'benjamin.clark@example.com', 'inactive', 'daily'),
('Amelia', 'Rodriguez', 'amelia.rodriguez@example.com', 'inactive', 'weekly'),
('Lucas', 'Lewis', 'lucas.lewis@example.com', 'inactive', 'daily'),
('Harper', 'Lee', 'harper.lee@example.com', 'inactive', 'weekly')