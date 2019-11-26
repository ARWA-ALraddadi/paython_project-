/* This exported "dump" script creates and populates the
tables for the Countdown database. It is notintended for
human consumption, so is not laid out nicely
or commented. */

CREATE TABLE "songs" (
	`song_name`	TEXT NOT NULL,
	`year_released`	INTEGER,
	`group_name`	TEXT,
	PRIMARY KEY(`song_name`)
);
INSERT INTO `songs` VALUES ('I Like It Both Ways',1976,'Supernaut');
INSERT INTO `songs` VALUES ('Too Hot to Touch',1976,'Supernaut');
INSERT INTO `songs` VALUES ('High Voltage',1975,'AC/DC');
INSERT INTO `songs` VALUES ('It''s a Long Way to the Top',1975,'AC/DC');
INSERT INTO `songs` VALUES ('TNT',1976,'AC/DC');
INSERT INTO `songs` VALUES ('Jailbreak',1976,'AC/DC');
INSERT INTO `songs` VALUES ('Highway to Hell',1979,'AC/DC');
INSERT INTO `songs` VALUES ('Living in the 70s',1974,'Skyhooks');
INSERT INTO `songs` VALUES ('Horror Movie',1975,'Skyhooks');
INSERT INTO `songs` VALUES ('Ego is Not a Dirty Word',1975,'Skyhooks');
INSERT INTO `songs` VALUES ('All My Friends Are Getting Married',1975,'Skyhooks');
INSERT INTO `songs` VALUES ('Million Dollar Riff',1975,'Skyhooks');
INSERT INTO `songs` VALUES ('Women in Uniform',1978,'Skyhooks');
INSERT INTO `songs` VALUES ('C''mon We''re Taking Over',1974,'Hush');
INSERT INTO `songs` VALUES ('Bony Moronie',1975,'Hush');
INSERT INTO `songs` VALUES ('Glad All Over',1975,'Hush');
INSERT INTO `songs` VALUES ('Free the People',1971,'Sherbet');
INSERT INTO `songs` VALUES ('Slipstream',1974,'Sherbet');
INSERT INTO `songs` VALUES ('Silvery Moon',1974,'AC/DC');
INSERT INTO `songs` VALUES ('Summer Love',1975,'Sherbet');
INSERT INTO `songs` VALUES ('Howzat',NULL,'Sherbet');
INSERT INTO `songs` VALUES ('Magazine Madonna',1977,'Sherbet');
INSERT INTO `songs` VALUES ('Whole Lotta Rosie',1978,'AC/DC');
CREATE TABLE "singers" (
	`group_name`	TEXT NOT NULL,
	`lead_singer`	TEXT NOT NULL,
	`year_joined`	INTEGER,
	`year_left`	INTEGER,
	PRIMARY KEY(`group_name`,`lead_singer`)
);
INSERT INTO `singers` VALUES ('Sherbet','Daryl Braithwaite',1970,1979);
INSERT INTO `singers` VALUES ('Hush','Keith Lamb',1971,1977);
INSERT INTO `singers` VALUES ('Skyhooks','Shirley Strachan',1974,1978);
INSERT INTO `singers` VALUES ('AC/DC','Bon Scott',1974,1980);
INSERT INTO `singers` VALUES ('Supernaut','Gary Twinn',1974,1980);
INSERT INTO `singers` VALUES ('AC/DC','Brian Johnson',1980,NULL);
INSERT INTO `singers` VALUES ('The Party Boys','Shirley Strachan',1984,1986);
CREATE TABLE "hits" (
	`song_name`	TEXT NOT NULL,
	`peak_position`	INTEGER,
	PRIMARY KEY(`song_name`)
);
INSERT INTO `hits` VALUES ('Slipstream',5);
INSERT INTO `hits` VALUES ('Silvery Moon',5);
INSERT INTO `hits` VALUES ('Summer Love ',1);
INSERT INTO `hits` VALUES ('Howzat',1);
INSERT INTO `hits` VALUES ('Bony Moronie',4);
INSERT INTO `hits` VALUES ('High Voltage',10);
INSERT INTO `hits` VALUES ('TNT',19);
INSERT INTO `hits` VALUES ('Jailbreak',10);
INSERT INTO `hits` VALUES ('Horror Movie',1);
INSERT INTO `hits` VALUES ('Million Dollar Riff',6);

