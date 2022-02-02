BEGIN TRANSACTION;
CREATE TABLE booking(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                Customer_ID TEXT NOT NULL,
                                Firstname   TEXT NOT NULL,
                                Surname     TEXT NOT NULL,
                                Address     TEXT NOT NULL,
                                Birth_Date  TEXT,
                                Post_Code   TEXT,
                                Mobile      TEXT,
                                Email       TEXT,
                                Nationality TEXT,
                                Gender      TEXT,
                                DateIn      TEXT,
                                DateOut     TEXT,
                                ID_Type     TEXT,
                                Meal_Type   TEXT,
                                Room_Type   TEXT,
                                Room_Number TEXT,
                                Room_Phone  TEXT );
INSERT INTO "booking" VALUES(52,'95ec206e77','Lindana','Montalvo','08727 Clark Walk Apt. 290
Clarkshire, LA 86167','29-06-1933','8073908','0221597075500','jennifermontoya@caldwell-guzman.com','Uganda','M','22-12-2020','25-12-2020','Permis de conducere','Cina Duminică','Queen Room','007','102');
INSERT INTO "booking" VALUES(53,'02599bc304','Mara','Murray','0948 Gray Club Apt. 773
Kellerstad, OH 50576','30-11-1960','6046685','027920963986','matthewparsons@hotmail.com','Turkmenistan','F','22-12-2020','12-01-2021','Pașaport','Cina Duminică','Queen Room','001','106');
INSERT INTO "booking" VALUES(54,'6e4fc5cd8f','Thomas','Russell','442 Franklin Harbors
Shannonmouth, KS 50755','04-12-1938','1693872','0222817717770','christophervega@webb.biz','Wallis and Futuna','M','22-12-2020','26-12-2020','Permis de conducere','Cină mare','Twin','008','101');
INSERT INTO "booking" VALUES(58,'7ad10155ba','Alan','Walker','0902 Joseph Wells
West Paulberg, HI 57453','13-10-1956','9809134','0271706843885','spencershannon@perkins-savage.org','Egypt','M','23-12-2020','01-01-2021','Buletin','Prânz la pachet','Mini Suite Room','010','103');
INSERT INTO "booking" VALUES(61,'7ce1df0185','Jessie','Leung','91569 Erickson Trace Apt. 835
Lake Melindabury, OR 09383','23-08-1998','8890660','0291646319156','ocurry@hotmail.com','Réunion','M','15-06-2021','09-07-2021','Buletin','Dejun Instant','Triple','008','105');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('booking',62);
COMMIT;
