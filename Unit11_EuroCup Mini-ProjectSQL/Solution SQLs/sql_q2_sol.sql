--3
select count(match_NO) from [euro_cup_2016].match_mast 
where decided_by = 'P'
and results = 'WIN'