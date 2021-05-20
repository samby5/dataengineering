
select country_name, playing_club, posi_to_play,count(goal_id) goal_scored from [euro_cup_2016].player_mast  p 
inner join [euro_cup_2016].goal_details g on p.player_id = g.player_id and p.team_id = g.team_id
inner join [euro_cup_2016].match_details m on m.team_id = g.team_id and  m.match_no = g.match_no
inner join [euro_cup_2016].soccer_country c  on c.country_id = m.team_id --where country_name = 'France'
group by  country_name, playing_club, posi_to_play
having count(goal_id) <> 0

country_name	playing_club	posi_to_play	goal_scored
Albania	Vaduz	FD	1
Austria	Schalke	MF	1
Belgium	Atletico	MF	1
Belgium	Chelsea	MF	1
Belgium	Everton	FD	2
Belgium	Marseille	FD	1
Belgium	Roma	MF	2
Belgium	Tottenham	DF	1
Belgium	Zenit	MF	1
Croatia	Barcelona	MF	1
Croatia	Fiorentina	FD	1
Croatia	Internazionale	MF	2
Croatia	Real Madrid	MF	1
Czech Republic	Bursaspor	FD	1
Czech Republic	Slavia Praha	FD	1
England	Leicester	FD	1
England	Liverpool	FD	1
England	Man. United	FD	1
England	Tottenham	MF	1
France	Arsenal	FD	3
France	Atletico	FD	6
France	Juventus	MF	1
France	West Ham	MF	3
Germany	Arsenal	MF	1
Germany	Bayern	DF	1
Germany	Bayern	FD	1
Germany	Besiktas	FD	2
Germany	Man. United	MF	1
Germany	Wolfsburg	MF	1
Hungary	Bursaspor	FD	2
Hungary	Ferencvaros	FD	1
Hungary	Hannover	FD	1
Hungary	Nurnberg	MF	1
Iceland	Basel	MF	2
Iceland	Hammarby	DF	1
Iceland	Kaiserslautern	FD	2
Iceland	Nantes	FD	2
Iceland	Norrkoping	DF	1
Iceland	Swansea	MF	1
Italy	Bologna	MF	1
Italy	Internazionale	FD	1
Italy	Juventus	DF	2
Italy	Southampton	FD	2
Northern Ireland	Aberdeen	FD	1
Northern Ireland	West Brom	DF	2
Poland	Ajax	FD	1
Poland	Bayern	FD	1
Poland	Fiorentina	MF	2
Portugal	Benfica	MF	1
Portugal	Besiktas	FD	1
Portugal	Fenerbahce	FD	3
Portugal	LOSC	FD	1
Portugal	Real Madrid	FD	3
Republic of Ireland	Aston Villa	DF	1
Republic of Ireland	Norwich	MF	3
Romania	Genclerbirligi	FD	2
Russia	CSKA Moskva	DF	1
Russia	Spartak Moskva	MF	1
Slovakia	Al-Gharafa	MF	1
Slovakia	Legia	MF	1
Slovakia	Napoli	MF	1
Spain	Barcelona	DF	1
Spain	Celta	FD	1
Spain	Juventus	FD	3
Switzerland	Hoffenheim	DF	1
Switzerland	Leverkusen	FD	1
Switzerland	Stoke	MF	1
Turkey	Beijing Guoan	FD	1
Turkey	Fenerbahce	MF	1
Wales	Arsenal	MF	1
Wales	Burnley	FD	1
Wales	Reading	FD	2
Wales	Real Madrid	FD	3
Wales	Swansea	DF	2