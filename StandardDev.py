import csv
import statistics
import pandas as pd 

df=pd.read_csv('Graph.csv')

height_list=df['Height(Inches)'].to_list()
weight_list=df['Weight(Pounds)'].to_list()

height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)

print(height_mean,weight_mean)

height_mode=statistics.mode(height_list)
weight_mode=statistics.mode(weight_list)

print(height_mode,weight_mode)

height_median=statistics.median(height_list)
weight_median=statistics.median(weight_list)

print(height_median,weight_median)

height_sd=statistics.stdev(height_list)
weight_sd=statistics.stdev(weight_list)

print(height_sd,weight_sd)


#finding first sd for start and end values 
height_first_std_deviation_start,height_first_std_deviation_end=height_mean-height_sd,height_mean+height_sd

height_second_std_deviation_start,height_second_std_deviation_end=height_mean-(2*height_sd),height_mean+(2*height_sd)

height_third_std_deviation_start,height_third_std_deviation_end=height_mean-(3*height_sd),height_mean+(3*height_sd)



weight_first_std_deviation_start,weight_first_std_deviation_end=weight_mean-weight_sd,weight_mean+weight_sd

weight_second_std_deviation_start,weight_second_std_deviation_end=weight_mean-(2*weight_sd),weight_mean+(2*weight_sd)

weight_third_std_deviation_start,weight_third_std_deviation_end=weight_mean-(3*weight_sd),weight_mean+(3*weight_sd)
#now find percentage in 123 std of height

#height_list_of_data_within_1_std_deviation=[result for]


#99 % of data lie between mean - 3sd and mean + 3sd 95 % of data lie between mean - 2sd and mean + 2sd 68 % of data lie between mean - sd and mean + sd
height_list_of_data_within_1_std_deviation = [ result for result in height_list if result > height_first_std_deviation_start and result < height_first_std_deviation_end]

height_list_of_data_within_2_std_deviation = [ result for result in height_list if result > height_second_std_deviation_start and result < height_second_std_deviation_end]

height_list_of_data_within_3_std_deviation = [ result for result in height_list if result > height_third_std_deviation_start and result < height_third_std_deviation_end]



weight_list_of_data_within_1_std_deviation = [ result for result in height_list if result > height_first_std_deviation_start and result < height_first_std_deviation_end]

weight_list_of_data_within_2_std_deviation = [ result for result in height_list if result > height_second_std_deviation_start and result < height_second_std_deviation_end]

weight_list_of_data_within_3_std_deviation = [ result for result in height_list if result > height_third_std_deviation_start and result < height_third_std_deviation_end]


print("{} % of data lies in first std".format(len(height_list_of_data_within_1_std_deviation)*100.0/len(height_list)))