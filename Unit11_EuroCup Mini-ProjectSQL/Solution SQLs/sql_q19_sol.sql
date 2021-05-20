select count(c.player_captain) num_of_gk_cptns from [euro_cup_2016].match_captain c inner join  [euro_cup_2016].player_mast p on c.player_captain = p.player_id and p.posi_to_play = 'GK'


num_of_gk_cptns
17