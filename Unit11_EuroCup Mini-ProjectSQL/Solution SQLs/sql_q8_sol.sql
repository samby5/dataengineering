select * from ( select match_no, score_total, row_number() over(order by score_total desc,match_no desc) as temp_rnk, 
team_id as team1,lead(team_id) over(partition by match_no order by match_no desc  ) as team2
from (

select match_no,team_id, sum(convert(int,penalty_score))  over(partition by match_no ) as score_total
from [euro_cup_2016].match_details 
where decided_by ='P') a ) b
where  temp_rnk =1

match_no	score_total	temp_rnk	team1	team2
47			11			1			1208	1211