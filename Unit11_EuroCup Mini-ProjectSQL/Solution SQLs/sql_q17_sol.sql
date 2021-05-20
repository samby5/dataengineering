select top 1 country_name, count( ass_ref_id ) count_asst_ref from [euro_cup_2016].asst_referee_mast a inner join [euro_cup_2016].soccer_country c on c.country_id = a.country_id
group by country_name
order by count(ass_ref_id ) desc

--country_name	count_asst_ref
--England			4