select distinct  player_name,jersey_no ,playing_club from [euro_cup_2016].player_mast  p
inner join [euro_cup_2016].match_details m on m.player_gk = p.player_id
inner join [euro_cup_2016].soccer_country c  on c.country_id = m.team_id
where country_name  = 'England'


--player_name	jersey_no	playing_club
--Joe Hart	1	Man. City