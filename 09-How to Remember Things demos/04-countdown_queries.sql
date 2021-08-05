
/* This script performs some queries on the Countdown
database.  You should run these queries one at a time (after
making the changes in countdown_corrections.sql). */

/* Retrieve a whole table */
select * from singers;

/* Retrieve a single column, remove duplicates
and sort alphabetically */
select distinct lead_singer from singers
order by lead_singer;

/* Get songs released in 1975 */
select song_name, group_name from songs
where year_released = 1975;

/* Get songs released by AC/DC before 1977 */
select song_name from songs
where group_name = 'AC/DC' and
year_released < 1977;

/* Find out how many songs each group released */
select group_name, count(*) as 'num_songs'
from songs group by group_name;

/* Who sang lead for AC/DC? */
select lead_singer from singers
where group_name = 'AC/DC';

/* Find out which song names begin with 'S' */
select song_name from songs
where song_name like 'S%';

/* Find Sherbet's songs released in 1975-77 */
select song_name from songs
where group_name = 'Sherbet' and
year_released between 1975 and 1977;

/* How high did Skyhooks' hits get on the charts? */
select songs.song_name, peak_position from songs, hits
where group_name = 'Skyhooks' and
songs.song_name = hits.song_name;

/* In which years did groups have a top ten hit? */
select distinct group_name, year_released from songs, hits
where songs.song_name = hits.song_name
and peak_position <= 10 order by group_name, year_released;

