-- Select average life_expectancy
select AVG(life_expectancy) -- From populations
From populations -- Where year is 2015
where year = 2015 -- Select fields


select * -- From populations
From populations -- Where life_expectancy is greater than
Where life_expectancy > -- 1.15 * subquery
    1.15 * (
        select AVG(life_expectancy)
        From populations
        where year = 2015
    )
    AND year = 2015;
