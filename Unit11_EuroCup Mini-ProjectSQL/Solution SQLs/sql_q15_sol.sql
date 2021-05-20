select top 1 referee_name, count(player_id) num_of_bookings  from  [euro_cup_2016].match_mast m inner join [euro_cup_2016].referee_mast r on r.referee_id = m.referee_id  
inner join [euro_cup_2016].player_booked b on m.match_no = b.match_no
group by referee_name
order by num_of_bookings desc 

--referee_name	num_of_bookings
--Mark Clattenburg	21