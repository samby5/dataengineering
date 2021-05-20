with player_subst as (select * from [euro_cup_2016].player_in_out where play_half = 1 and play_schedule = 'NT')
select player_name from player_subst inner join [euro_cup_2016].player_mast p on p.player_id = player_subst.player_id

player_name
Sami Khedira
Bastian Schweinsteiger
Cristiano Ronaldo
Ricardo Quaresma
Mikael Lustig
Erik Johansson