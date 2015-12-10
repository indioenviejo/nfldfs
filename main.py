
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
dfOff = df[df["Position"] <> "DST"]

dfOff = dfOff.loc[0:0,:]
print dfOff

# Get the player statistics information
playerStats = ComputationBlocks.getPlayerStatsSummary(dfOff,season,weeks)

# Group the statistics by GSIS ID
players = playerStats.groupby(["GSIS_ID"])

playerStatsAway = pda.DataFrame()
playerStatsHME = pda.DataFrame()

# Get stats for each player at and away from home
for n,g in players:
    [tempAway,tempHME] =  ComputationBlocks.statsbyHomeFldAvd(g,"HomeFldAdv")    
    playerStatsAway = playerStatsAway.append(tempAway)
    playerStatsHME = playerStatsHME.append(tempHME)

# Get average stats  @ home and away for each player 
playerAWYAvgPerf = ComputationBlocks.getPlayerAvgPerformance(playerStatsAway)
playerHMEAvgPerf = ComputationBlocks.getPlayerAvgPerformance(playerStatsHME)

playerAWYAvgPerf.to_csv("/home/raghav/playerAway.csv")

###############################################################################################################
 
# Read the data file with defense team names

# Get Defense Teams
dfDef = df[df["Position"] == "DST"]

dfDef = dfDef.iloc[0:3,:]

# Get the Stats for each defense team
defStats = ComputationBlocks.getDefStatsSummary(dfDef,season,weeks)
# Group the stats by team
defense =  defStats.groupby(["Team"])


defStatsAway = pda.DataFrame()
defStatsHME = pda.DataFrame()


# Get stats for each player at and away from home
for n,g in defense:
    print g
    [tempAway,tempHME] =  ComputationBlocks.statsbyHomeFldAvd(g,"HomeFldAdv")    
    defStatsAway = defStatsAway.append(tempAway)
    defStatsHME = defStatsHME.append(tempHME)


# ###############################################################################################################
# #Get Average Performance
# ###############################################################################################################
 
defAWYAvgPerf =  ComputationBlocks.getDefenseAvgPerformance(defStatsAway)
defHMEAvgPerf =  ComputationBlocks.getDefenseAvgPerformance(defStatsHME)


defAWYAvgPerf.to_csv("/home/raghav/defAvgAway.csv")
