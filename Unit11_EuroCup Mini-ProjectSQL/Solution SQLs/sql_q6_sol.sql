-- cant be computed as data is incorrect 

01-Feb
01-Feb
03-Mar
0-1

clean data by using -
select replace(replace(replace(replace(replace(replace( replace(goal_score,'Jan',1),'Feb',2),'Mar',3),'May',5),'01',1),'02',2),'03',3)
 goal_score from [euro_cup_2016].match_mast