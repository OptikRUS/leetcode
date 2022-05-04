DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	name varchar(50),
	surname varchar(50),
	family_name varchar(50),
	created_at DATE DEFAULT CURRENT_TIMESTAMP null,
	updeted_at DATE DEFAULT NOW() NULL
);

CREATE INDEX full_name_idx ON users(name, surname, family_name);
CREATE INDEX created_at_idx ON users(created_at DESC);