
author: lindaJaber

# Null and alternative hypotheses:
The hypotheses are written in both words and formulae.
However the null and alternative hupotheses should mention 'average trip duration'.
It is better also to mention the unit of the trip duration is measured in.
I believe it would be better if we just mention that the two durations are different and check how they differ in the test we run.

$H_O$: the average trip duration in minutes of riders born in 1960 or later is the same as the average trip duration for those born after 1960.
$H_a$: the average trip duration in minutes of riders born in 1960 or later is different from the average trip duration for those born after 1960.
$H_0: t_1 = t_2$
$H_a: t_! \neq t_2$

I also think it would be intersting to justify the year choice. Why 1960? 
A nice way would be is to take a known age group and compare it to the rest of the population.
For example people born between 1946 and 1964 are called **Baby Boomers** (I chose this group cause it is close to the year you have already chosen '1960').

## Data
The reducted dataframe has the required variables to proceed with the analysis.
I believe plotting a histogram would have better helped visualize the data.

## Test
I suggest to use the **t-test** for independent samples.
Reasons:
1. We are assessing the difference between two unpaired groups
2. We have 2 samples that are independent
3. We assume that the distribution is normal

