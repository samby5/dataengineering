select referee_name, count(player_id) num_of_bookings  from  [euro_cup_2016].match_mast m inner join [euro_cup_2016].referee_mast r on r.referee_id = m.referee_id  
inner join [euro_cup_2016].player_booked b on m.match_no = b.match_no
group by referee_name
order by num_of_bookings

referee_name	num_of_bookings
Clement Turpin	3
Svein Oddvar Moen	8
William Collum	8
Ovidiu Hategan	9
Felix Brych	9
Martin Atkinson	9
Carlos Velasco Carballo	10
Szymon Marciniak	10
Pavel Kralovec	11
Cuneyt Cakir	11
Jonas Eriksson	11
Damir Skomina	12
Bjorn Kuipers	12
Sergei Karasev	12
Viktor Kassai	12
Milorad Mazic	13
Nicola Rizzoli	20
Mark Clattenburg	21