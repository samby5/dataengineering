select referee_name,venue_name,count(match_no) num_of_matches from  [euro_cup_2016].match_mast m inner join [euro_cup_2016].referee_mast r on r.referee_id = m.referee_id  
inner join [euro_cup_2016].soccer_venue v on v.venue_id = m.venue_id
group by referee_name,venue_name



Clement Turpin	Parc des Princes	1
Jonas Eriksson	Parc des Princes	1
Martin Atkinson	Parc des Princes	1
Nicola Rizzoli	Parc des Princes	1
Sergei Karasev	Parc des Princes	1
Carlos Velasco Carballo	Stade Bollaert-Delelis	2
Felix Brych	Stade Bollaert-Delelis	1
William Collum	Stade Bollaert-Delelis	1
Bjorn Kuipers	Stade de Bordeaux	1
Clement Turpin	Stade de Bordeaux	1
Cuneyt Cakir	Stade de Bordeaux	1
Svein Oddvar Moen	Stade de Bordeaux	1
Viktor Kassai	Stade de Bordeaux	1
Bjorn Kuipers	Stade de France	2
Cuneyt Cakir	Stade de France	1
Mark Clattenburg	Stade de France	1
Milorad Mazic	Stade de France	1
Szymon Marciniak	Stade de France	1
Viktor Kassai	Stade de France	1
Jonas Eriksson	Stade de Lyon	1
Mark Clattenburg	Stade de Lyon	1
Martin Atkinson	Stade de Lyon	1
Nicola Rizzoli	Stade de Lyon	1
Pavel Kralovec	Stade de Lyon	2
Damir Skomina	Stade de Nice	1
Felix Brych	Stade de Nice	1
Milorad Mazic	Stade de Nice	1
Ovidiu Hategan	Stade de Nice	1
Carlos Velasco Carballo	Stade Geoffroy Guichard	1
Cuneyt Cakir	Stade Geoffroy Guichard	1
Mark Clattenburg	Stade Geoffroy Guichard	2
Damir Skomina	Stade Pierre Mauroy	3
Martin Atkinson	Stade Pierre Mauroy	1
Ovidiu Hategan	Stade Pierre Mauroy	1
Szymon Marciniak	Stade Pierre Mauroy	1
Felix Brych	Stade VElodrome	1
Nicola Rizzoli	Stade VElodrome	2
Sergei Karasev	Stade VElodrome	1
Svein Oddvar Moen	Stade VElodrome	1
William Collum	Stade VElodrome	1
Jonas Eriksson	Stadium de Toulouse	1
Milorad Mazic	Stadium de Toulouse	1
Szymon Marciniak	Stadium de Toulouse	1
Viktor Kassai	Stadium de Toulouse	1