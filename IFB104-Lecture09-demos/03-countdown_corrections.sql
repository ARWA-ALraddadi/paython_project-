/* This script makes all the additions and corrections to
the Countdown database */

/* Add a song from AC/DC */
insert into songs
    values ('Dirty Deeds Done Dirt Cheap', 1976, 'AC/DC');

/* Add a top-ten hit from AC/DC */
insert into songs
    values ('You Shook Me All Night Long', 1980, 'AC/DC');
insert into hits values ('You Shook Me All Night Long', 8);

/* Add a minor hit from Skyhooks */
insert into songs (song_name, group_name)
    values ('Party to End All Parties', 'Skyhooks');
insert into hits values ('Party to End All Parties', 24);

/* Add Brian Johnson's departure */
update singers set year_left = 2016
where lead_singer = 'Brian Johnson';

/* Add Howzat's release date */
update songs set year_released = 1976
where song_name = 'Howzat';

/* Correct the group name for Silvery Moon */
update songs set group_name = 'Sherbet'
where song_name = 'Silvery Moon';

/* Save the changes in the database */
commit


