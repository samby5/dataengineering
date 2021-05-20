select venue_name from [euro_cup_2016].match_mast m inner join [euro_cup_2016].soccer_venue  v on 
m.venue_id = v.venue_id
 where decided_by ='P'
 
 venue_name
Stade de Bordeaux
Stade VElodrome
Stade Geoffroy Guichard