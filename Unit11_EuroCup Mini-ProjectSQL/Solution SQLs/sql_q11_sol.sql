select pm.player_name,pm.jersey_no,pm.playing_club
from euro_cup_2016.player_mast    pm,
     euro_cup_2016.soccer_country sc
where pm.team_id = sc.country_id
  and sc.country_name = 'England'
  and pm.posi_to_play = 'GK'


--player_name	jersey_no	playing_club
--Joe Hart	1	Man. City