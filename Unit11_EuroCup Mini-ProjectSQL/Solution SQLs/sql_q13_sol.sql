select distinct  p.player_id,player_name  from [euro_cup_2016].goal_details g inner join [euro_cup_2016].player_mast p on g.player_id = p.player_id and p.team_id = g.team_id
where posi_to_play = 'DF'

player_id	player_name
160050	Toby Alderweireld
160165	Jerome Boateng
160216	Birkir Saevarsson
160219	Arnor Ingvi Traustason
160235	Leonardo Bonucci
160236	Giorgio Chiellini
160262	Gareth McAuley
160327	Ciaran Clark
160373	Vasili Berezutski
160423	Gerard Pique
160470	Fabian Schar
160538	Neil Taylor
160539	Ashley Williams