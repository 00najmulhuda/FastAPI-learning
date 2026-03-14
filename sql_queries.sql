-- create table leads

CREATE TABLE leads (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    company VARCHAR(100),
    budget INTEGER
);

INSERT INTO leads (name,company,budget)
VALUES ('najmul','FLIPKART',100000);

INSERT INTO leads (name,company,budget)
VALUES('huda','AMAZON',150000);

INSERT INTO leads(name,company,budget)
VALUES('noor','ALIBABA',200000);

SELECT * FROM leads;

SELECT * FROM leads WHERE budget > 50000;

UPDATE leads SET company = 'ZOMATO' WHERE company = 'AMAZON';
DELETE FROM leads WHERE id = 3;

SELECT * FROM leads;