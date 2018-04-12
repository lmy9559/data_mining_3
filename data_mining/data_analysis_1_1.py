import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy.stats as stats


def Numerical_analysis(data,data_column,output_path):
    loss = pd.DataFrame(data[data_column].isnull().sum()).T.rename(index={0: 'loss_count'})
    mode_t = data[data_column].mode().rename(index={0: 'mode'})
    des_t = pd.concat([data[data_column].describe(), mode_t,loss])
    des_t.to_csv(output_path)
    print(des_t)


def plot(data,data_columns):

    for i in data_columns:
        fig, axes = plt.subplots(1, 3, figsize=(15, 8))
        axes[0].hist(data[i].dropna(), bins=50, color='k', alpha=0.5)
        axes[0].set_title(i)

        axes[1].boxplot(data[i].dropna())
        axes[1].set_title(i)

        stats.probplot(data[i].dropna(), dist="norm", plot=axes[2])

        plt.show()
    return 0

def Nominal_analysis(data, output_path):  # data--><class 'pandas.core.frame.DataFrame'>
    '标称属性：计算词频'
    result = data.apply(pd.value_counts)
    print(result)
    result.to_csv(output_path)
    return 0


def Building_Permits_Analyse():
    # DataSet : Building_Permits.csv
    # data1_input_csv_path = "data/Building_Permits.csv"
    # data1_input_csv_path = "data/clean_Building_Permits.csv"  # missing handling 1
    data1_input_csv_path = "data/Part_Building_Permits_2.csv"   #missing handling 2
    # data1_input_csv_path = "data/Part_Building_Permits_3.csv"
    sf_permits = pd.DataFrame(pd.read_csv(data1_input_csv_path))

    # 标称分析
    # nominal_property = ['Permit Type','Street Suffix', 'Current Status', 'Structural Notification', 'Voluntary Soft-Story Retrofit', 'Fire Only Permit',
    #                     'Existing Construction Type','Proposed Construction Type','Site Permit','Supervisor District','Neighborhoods - Analysis Boundaries']
    # for i in nominal_property:
    #     nominal_data = sf_permits[[i]]
    #     Nominal_analysis(nominal_data,"data1/norminal/"+i+".csv")

    # 数值分析
    numercial_property = ['Number of Existing Stories', 'Number of Proposed Stories', 'Estimated Cost', 'Revised Cost']
    Numerical_analysis(sf_permits,numercial_property,"data1/desc.csv") # data desc
    plot(sf_permits, numercial_property)# 直方图、盒图、qq图

def NFL_Analyse():
    # DataSet : NFL.csv
    data2_input_path = "data/NFL Play by Play 2009-2017 (v4).csv"
    nfl_pbp = pd.DataFrame(pd.read_csv(data2_input_path))

    # 标称分析
    nominal_property = ['Drive', 'qtr', 'down', 'SideofField', 'ydstogo', 'GoalToGo', 'FirstDown', 'posteam',
                 'DefensiveTeam', 'PlayAttempted', 'sp', 'Touchdown', 'ExPointResult', 'TwoPointConv',
                 'DefTwoPoint', 'Safety', 'Onsidekick', 'PuntResult', 'PlayType', 'Passer', 'Passer_ID',
                 'PassAttempt', 'PassOutcome', 'PassLength', 'QBHit', 'PassLocation', 'InterceptionThrown',
                 'Interceptor', 'Rusher', 'Rusher_ID', 'RushAttempt', 'RunLocation', 'RunGap', 'Receiver',
                 'Receiver_ID', 'Reception', 'ReturnResult', 'Returner', 'BlockingPlayer', 'Tackler1', 'Tackler2',
                 'FieldGoalResult', 'Fumble', 'RecFumbTeam', 'RecFumbPlayer', 'Sack', 'Challenge.Replay',
                 'ChalReplayResult', 'Accepted.Penalty', 'PenalizedTeam', 'PenaltyType', 'PenalizedPlayer',
                 'HomeTeam', 'AwayTeam', 'Timeout_Indicator', 'Timeout_Team', 'Season']
    for i in nominal_property:
        nominal_data = nfl_pbp[[i]]
        Nominal_analysis(nominal_data, "data2/norminal/" + i + ".csv")

    # 数值分析
    numercial_property  = ['TimeUnder', 'TimeSecs', 'PlayTimeDiff', 'yrdln', 'yrdline100', 'ydsnet', 'Yards.Gained',
              'AirYards', 'YardsAfterCatch', 'FieldGoalDistance', 'Penalty.Yards', 'PosTeamScore', 'DefTeamScore',
              'ScoreDiff', 'AbsScoreDiff', 'posteam_timeouts_pre', 'HomeTimeouts_Remaining_Pre', 'AwayTimeouts_Remaining_Pre',
              'HomeTimeouts_Remaining_Post', 'AwayTimeouts_Remaining_Post', 'No_Score_Prob', 'Opp_Field_Goal_Prob',
              'Opp_Safety_Prob', 'Opp_Touchdown_Prob', 'Field_Goal_Prob', 'Safety_Prob', 'Touchdown_Prob', 'ExPoint_Prob',
              'TwoPoint_Prob', 'ExpPts', 'EPA', 'airEPA', 'yacEPA', 'Home_WP_pre', 'Away_WP_pre', 'Home_WP_post',
              'Away_WP_post', 'Win_Prob', 'WPA', 'airWPA', 'yacWPA']
    Numerical_analysis(nfl_pbp, numercial_property, "data2/desc.csv")  # data desc
    plot(nfl_pbp, numercial_property)  # 直方图、盒图、qq图

if __name__ == '__main__':
    Building_Permits_Analyse()
    # NFL_Analyse()