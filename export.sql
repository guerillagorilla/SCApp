PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE users (
       username	   VARCHAR(20) NOT NULL PRIMARY KEY,
       password	   CHAR(40) NOT NULL,
       firstname   VARCHAR(20) NOT NULL,
       lastname    VARCHAR(20) NOT NULL,
       email 	   VARCHAR(20) NOT NULL,
       is_director CHAR(1) DEFAULT '0'
);
INSERT INTO "users" VALUES('test','a94a8fe5ccb19ba61c4c0873d391e987982fbbd3','test','test','test@test.com','1');
CREATE TABLE bags (
       bag_name    VARCHAR(20) NOT NULL PRIMARY KEY
);
INSERT INTO "bags" VALUES('family bag');
INSERT INTO "bags" VALUES('single person bag');
CREATE TABLE sources (
       name        VARCHAR(20) NOT NULL PRIMARY KEY
);
INSERT INTO "sources" VALUES('single source');
CREATE TABLE products (
       name    	   VARCHAR(20) NOT NULL PRIMARY KEY,
       cost	   INTEGER NOT NULL,
       source_name VARCHAR(20) NOT NULL,
       FOREIGN KEY (source_name) REFERENCES sources (name)
);
INSERT INTO "products" VALUES('cereal',4,'single source');
INSERT INTO "products" VALUES('bread',3,'single source');
INSERT INTO "products" VALUES('milk',5,'single source');
INSERT INTO "products" VALUES('eggs',6,'single source');
CREATE TABLE financial_aids (
       is_fed	   CHAR(1) NOT NULL,     
       name        VARCHAR(20) NOT NULL PRIMARY KEY
);
INSERT INTO "financial_aids" VALUES('1','federal');
INSERT INTO "financial_aids" VALUES('0','state');
CREATE TABLE clients (
       id    	   INTEGER PRIMARY KEY,
       gender	   CHAR(1) NOT NULL,
       dob	   CHAR(10) NOT NULL,
       start_date  CHAR(10) NOT NULL,
       street	   VARCHAR(20) NOT NULL,
       city	   VARCHAR(20) NOT NULL,
       state	   VARCHAR(20) NOT NULL,
       zip	   CHAR(5) NOT NULL,
       apartment   VARCHAR(10) DEFAULT '0',
       firstname   VARCHAR(20) NOT NULL,
       lastname	   VARCHAR(20) NOT NULL,
       phone	   CHAR(13) NOT NULL,
       pickup_day  INTEGER NOT NULL,
       bag_name	   VARCHAR(20),
       /* on delete set null sets bag_name to null when a bag is deleted
        * to avoid a foreign key constraint violation */
       FOREIGN KEY (bag_name) REFERENCES bags (bag_name) ON DELETE SET NULL
);
INSERT INTO "clients" VALUES(1,'M','1972-08-12','2005-03-02','street a','atlanta','ga','30332','302','billy','corgan','7708621555',4,'single person bag');
INSERT INTO "clients" VALUES(2,'F','1972-02-13','2009-03-02','street b','atlanta','ga','30332','432','michelle','obama','1234567890',4,'family bag');
INSERT INTO "clients" VALUES(3,'M','1988-09-24','2010-04-09','street c','atlanta','ga','30332','999','ricky','jones','9999991234',5,'family bag');
INSERT INTO "clients" VALUES(4,'F','1985-11-13','2012-01-01','street d','atlanta','ga','30332','123','britney','spears','4832924444',6,'single person bag');
CREATE TABLE family_members (
       firstname   VARCHAR(20) NOT NULL,
       lastname	   VARCHAR(20) NOT NULL,
       dob	   VARCHAR(10) NOT NULL,
       gender	   CHAR(1) NOT NULL,
       client_id   INTEGER NOT NULL,
       /* on delete cascade means if a client gets deleted all family members
        * get deleted too */
       FOREIGN KEY (client_id) REFERENCES clients (id) ON DELETE CASCADE, 
       PRIMARY KEY (firstname, lastname, client_id)
);
INSERT INTO "family_members" VALUES('ricky','corgan','1988-12-12','M',1);
INSERT INTO "family_members" VALUES('sally','corgan','1989-12-12','F',1);
INSERT INTO "family_members" VALUES('millie','corgan','1990-12-12','F',1);
INSERT INTO "family_members" VALUES('sally','obama','1989-12-12','F',2);
INSERT INTO "family_members" VALUES('millie','obama','1990-12-12','F',2);
INSERT INTO "family_members" VALUES('lizzie','spears','1990-01-01','F',3);
CREATE TABLE bag_holds (
       current_qty INTEGER,
       last_month_qty INTEGER,
       bag_name VARCHAR(20) NOT NULL,
       product_name VARCHAR(20) NOT NULL,
       FOREIGN KEY (bag_name) REFERENCES bags (bag_name) ON DELETE CASCADE,
       FOREIGN KEY (product_name) REFERENCES products (name) ON DELETE CASCADE,
       PRIMARY KEY (bag_name, product_name)
);
INSERT INTO "bag_holds" VALUES(2,10,'family bag','bread');
INSERT INTO "bag_holds" VALUES(6,11,'family bag','milk');
INSERT INTO "bag_holds" VALUES(12,12,'family bag','cereal');
INSERT INTO "bag_holds" VALUES(5,10,'single person bag','bread');
INSERT INTO "bag_holds" VALUES(6,11,'single person bag','milk');
CREATE TABLE pickup_transaction (
       pickup_id   INTEGER PRIMARY KEY,
       pickup_date CHAR(10) NOT NULL,
       client_id   INTEGER NOT NULL,
       bag_name    VARCHAR(20) NOT NULL,
       FOREIGN KEY (client_id) REFERENCES clients (id) ON DELETE CASCADE,
       FOREIGN KEY (bag_name) REFERENCES bags (bag_name) ON DELETE CASCADE
);
CREATE TABLE client_finaid_relationships (
       client_id   INTEGER NOT NULL,
       finaid_name VARCHAR(20) NOT NULL,
       FOREIGN KEY (client_id) REFERENCES clients (id) ON DELETE CASCADE,
       FOREIGN KEY (finaid_name) REFERENCES financial_aids (name) ON DELETE CASCADE,
       PRIMARY KEY (client_id, finaid_name)
);
CREATE TABLE dropoff_transactions (
       dropoff_id   INTEGER,
       date	    CHAR(10) NOT NULL,
       qty	    INTEGER NOT NULL,
       source_name  VARCHAR(20) NOT NULL,
       product_name VARCHAR(20) NOT NULL,
       FOREIGN KEY (source_name) REFERENCES sources (name) ON DELETE CASCADE,
       FOREIGN KEY (product_name) REFERENCES products (name) ON DELETE CASCADE,
       PRIMARY KEY (dropoff_id, source_name, product_name)
);
CREATE INDEX fullname ON users(firstname, lastname);
CREATE INDEX address ON clients (street, city, state, zip, apartment);
CREATE INDEX namephone ON clients (firstname, lastname, phone);
CREATE INDEX name ON family_members(firstname, lastname);
CREATE VIEW clients_with_family_size AS
SELECT *, (SELECT COUNT(*) + 1 FROM family_members WHERE family_members.client_id = id) 
AS family_size FROM clients;
COMMIT;
