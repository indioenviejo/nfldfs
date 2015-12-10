
import os
import pandas as pda

root = "/home/raghav/mygithub/nfldfs/"

os.chdir(root)

import ComputationBlocks

#####################################################################################
season = 2015
weeks = range(12)
weeks = [a+1 for a in weeks]
#####################################################################################

# Read Salary and next game info Data
df = pda.read_csv(root+"DKSalaries_Week12.csv")
# Remove Defense List
df = df[df["Position"] <> "DST"]

#df2 = df.loc[0:2,:]
#print df2

# Get the player statistics information
playerStats = ComputationBlocks.getPlayerStatsSummary(df,season,weeks)

# Group the statistics by home field advantage
players = playerStats.groupby(["GSIS_ID"])

playerStatsAway = pda.DataFrame()
playerStatsHME = pda.DataFrame()

# Get stats for each player at and away from home
for n,g in players:
    [tempAway,tempHME] =  ComputationBlocks.statsbyHomeFldAvd(g,"HomeFldAdv")    
    playerStatsAway = playerStatsAway.append(tempAway)
    playerStatsHME = playerStatsHME.append(tempHME)

# Get average stats  @ home and away for each player 
playerAWYAvgPerf = ComputationBlocks.getAvgPerformance(playerStatsAway)
playerHMEAvgPerf = ComputationBlocks.getAvgPerformance(playerStatsHME)


# ###############################################################################################################
# 
# # Read the data file with defense team names
# df = pda.read_csv("C:\\Users\\212367183\\Documents\\DK_DEF\\def.csv")
# defStats = ComputationBlocks.getDefStatsSummary(df,season,weeks)
# defStats.to_csv("C:\\Users\\212367183\\Documents\\DK_DEF\\defStatsW12.csv")
# 
# hmefldGrp = defStats.groupby(["HomeFldAdv"])
# 
# for n,g in hmefldGrp:
#     if n == "AWY":
#         defStatsAway = g
#     if n == "HME":
#         defStatsHME = g
# 
# defStatsAway.to_csv("C:\\Users\\212367183\\Documents\\DK_DEF\\defStatsAwayW12.csv")
# defStatsHME.to_csv("C:\\Users\\212367183\\Documents\\DK_DEF\\defStatsHomeW12.csv")
# 
# ###############################################################################################################
# #Get Average Performance
# ###############################################################################################################
# 
# # Read the data file with defense team names
# defStatsAway = pda.read_csv("C:\\Users\\212367183\\Documents\\DK_DEF\\defStatsAwayW12.csv")
# 
# 
# teams = defStatsAway.groupby(["Team"])
# teamAWYAvgPerf = pda.DataFrame()
# teamNames = []
# 
# for n,g in teams:
#     g = g[g.columns[3:]]
#     teamAWYAvgPerf  = teamAWYAvgPerf.append(g.mean(),ignore_index=True)
#     teamNames.extend([n])
# 
# teamAWYAvgPerf["Team"] = pda.Series(teamNames)
# teamAWYAvgPerf.to_csv("C:\\Users\\212367183\\Documents\\DK_DEF\\defAvgStatsAwayW12.csv",index=None)
# 
# 
# # Read the data file with defense team names
# defStatsAway = pda.read_csv("C:\\Users\\212367183\\Documents\\DK_DEF\\defStatsHomeW12.csv")
# teams = defStatsAway.groupby(["Team"])
# teamHMEAvgPerf = pda.DataFrame()
# teamNames = []
# 
# for n,g in teams:
#     g = g[g.columns[3:]]
#     teamHMEAvgPerf  = teamHMEAvgPerf.append(g.mean(),ignore_index=True)
#     teamNames.extend([n])
# 
# teamHMEAvgPerf["Team"] = pda.Series(teamNames)
# teamHMEAvgPerf.to_csv("C:\\Users\\212367183\\Documents\\DK_DEF\\defAvgStatsHomeW12.csv",index=None)
