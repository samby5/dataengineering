 select num_of_foul_cards
from
(SELECT match_no, COUNT(*) as num_of_foul_cards
FROM euro_cup_2016.player_booked
group by match_no
ORDER BY COUNT(*) DESC) as qry
limit 1