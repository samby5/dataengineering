select * from [euro_cup_2016].player_mast where playing_club   like '%Liver%' and team_id = ( select country_id from  [euro_cup_2016].soccer_country where country_name  = 'England')


player_id	team_id	jersey_no	player_name	posi_to_play	dt_of_bir	age	playing_club
160131	1206	4	James Milner	MF	1986-01-04 00:00:00.0000000	30	Liverpool
160130	1206	8	Adam Lallana	MF	1988-05-10 00:00:00.0000000	28	Liverpool
160121	1206	12	Nathaniel Clyne	DF	1991-04-05 00:00:00.0000000	25	Liverpool
160129	1206	14	Jordan Henderson	MF	1990-06-17 00:00:00.0000000	26	Liverpool
160137	1206	15	Daniel Sturridge	FD	1989-09-01 00:00:00.0000000	26	Liverpool