-- create table with migration version
CREATE TABLE migration_version (version VARCHAR(32) NOT NULL,
CONSTRAINT migration_version_pk PRIMARY KEY (version));

INSERT INTO migration_version (version) VALUES (4);
