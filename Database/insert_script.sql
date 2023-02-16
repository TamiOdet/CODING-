PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;


Delete FROM cds WHERE contributer LIKE '101116702%';
Delete FROM songs WHERE contributer LIKE '101116702%';



INSERT INTO cds VALUES('101116702CD1','Thriller','Michael Jackson','Quincy Jones',1982,'101116702');
INSERT INTO cds VALUES('101116702CD2','Whitney','Whitney Houston','Narada Walden, Michael Masser, Jellybean Benitez',1982,'101116702');


INSERT OR IGNORE INTO songs  (title, composer, cd_id, track, contributer) VALUES('Wanna Be Startin Somethin','Michael Jackson','101116702CD1',1,'101116702');
INSERT INTO songs  (title, composer, cd_id, track, contributer) VALUES('Baby Be Mine','Michael Jackson','101116702CD1',2,'101116702');
INSERT INTO songs  (title, composer, cd_id, track, contributer) VALUES('Girl Is Mine,The','Michael Jackson','101116702CD1',3,'101116702');
INSERT INTO songs  (title, composer, cd_id, track, contributer) VALUES('Thriller','Rod Temperton','101116702CD1',4,'101116702');
INSERT INTO songs  (title, composer, cd_id, track, contributer) VALUES('Beat it','Michael Jackson','101116702CD1',5,'101116702');
INSERT INTO songs  (title, composer, cd_id, track, contributer) VALUES('Billie Jean','Michael Jackson','101116702CD1',6,'101116702');
INSERT INTO songs  (title, composer, cd_id, track, contributer) VALUES('Human Nature','John Bettis, Steve Porcaro','101116702CD1',7,'101116702');
INSERT INTO songs  (title, composer, cd_id, track, contributer) VALUES('Pretty Young Thing','James Ingram, Quincy Jones','101116702CD1',8,'101116702');
INSERT INTO songs  (title, composer, cd_id, track, contributer) VALUES('Lady In My Life, The','Rod Temperton','101116702CD1',9,'101116702');
INSERT INTO songs  (title, composer, cd_id, track, contributer) VALUES('I Wanna Dance With Somebody','George Merrill Shannon Rubicam','101116702CD2',1,'101116702');
INSERT INTO songs  (title, composer, cd_id, track, contributer) VALUES('Just The Lonely Talking Again','Sam Dees','101116702CD2',2,'101116702');
INSERT INTO songs  (title, composer, cd_id, track, contributer) VALUES('Love Will Save The Day','Antoinette Colandreo','101116702CD2',3,'101116702');
INSERT INTO songs  (title, composer, cd_id, track, contributer) VALUES('Didn''t We Almost Have It All','Michael Masser Will Jennings','101116702CD2',4,'101116702');
INSERT INTO songs  (title, composer, cd_id, track, contributer) VALUES('So Emotional','Billy Steinberg, Tom Kelly','101116702CD2',5,'101116702');
INSERT INTO songs  (title, composer, cd_id, track, contributer) VALUES('Where You Are','Dyan Humes, James Calabrese, LeMel Humes','101116702CD2',6,'101116702');
INSERT INTO songs  (title, composer, cd_id, track, contributer) VALUES('Love Is A Contact Sport','Preston Glass','101116702CD2',7,'101116702');
INSERT INTO songs  (title, composer, cd_id, track, contributer) VALUES('You''re Still My Man','Gerry Goffin, Michael Masser','101116702CD2',8,'101116702');
INSERT INTO songs  (title, composer, cd_id, track, contributer) VALUES('For The Love Of You','Christopher Jasper, Ernie Isley, Marvin Isley, O''Kelly Isley, Ronald Isley, Rudolph Isley','101116702CD2',9,'101116702');
INSERT INTO songs  (title, composer, cd_id, track, contributer) VALUES('Where Do Broken Hearts Go','Charles Jackson, Frank Wildhorn','101116702CD2',9,'101116702');
INSERT INTO songs  (title, composer, cd_id, track, contributer) VALUES('I Know Him So Well','Benny Andersson,Tim Rice','101116702CD2',10,'101116702');
COMMIT;
