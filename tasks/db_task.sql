DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	name varchar(50),
	surname varchar(50),
	family_name varchar(50),
	created_at DATE DEFAULT CURRENT_TIMESTAMP null,
	updeted_at DATE DEFAULT NOW() NULL
);