-- cant be computed as data is incorrect 

01-Feb
01-Feb
03-Mar
0-1

clean data by using -
select replace(replace(replace(replace(replace(replace( replace(goal_score,'Jan',1),'Feb',2),'Mar',3),'May',5),'01',1),'02',2),'03',3)
 goal_score from [euro_cup_2016].match_mast
 
 Alternate solution -
 
 SELECT COUNT(*)
FROM euro_cup_2016.match_details AS t1, euro_cup_2016.match_details AS t2
WHERE t1.match_no = t2.match_no
AND t1.team_id != t2.team_id
AND t1.goal_score - t2.goal_score = 1
AND t1.win_lose = 'W'
AND t1.penalty_score IS NULL