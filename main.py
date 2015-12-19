# 
import os
import pandas as pda
# 
root = "/home/raghav/mygithub/nfldfs/"
 
os.chdir(root)
 
import ComputationBlocks
 
#####################################################################################
season = 2015
weeks = [7,8,9,10,11,12,13,14]
#####################################################################################
 
# Read Salary and next game info Data
df = pda.read_csv(root+"DKSalaries.csv")
 
# # Remove Defense List
# dfOff = df[df["Position"] <> "DST"]
#  
# # Get the player statistics information
# playerStats = ComputationBlocks.getPlayerStatsSummary(dfOff,season,weeks)
#  
# # Group the statistics by GSIS ID
# players = playerStats.groupby(["GSIS_ID"])
#  
# playerStatsAway = pda.DataFrame()
# playerStatsHME = pda.DataFrame()
#  
# # Get stats for each player at and away from home
# for n,g in players:
#     [tempAway,tempHME] =  ComputationBlocks.statsbyHomeFldAvd(g,"HomeFldAdv")    
#     playerStatsAway = playerStatsAway.append(tempAway)
#     playerStatsHME = playerStatsHME.append(tempHME)
#  
# print "----"
# print playerStatsAway
# print "----"
# # Get average stats  @ home and away for each player 
# playerAWYAvgPerf = ComputationBlocks.getPlayerAvgPerformance(playerStatsAway,"AWY")
# playerHMEAvgPerf = ComputationBlocks.getPlayerAvgPerformance(playerStatsHME,"HME")
#  
# playerAWYAvgPerf.to_csv(root+"playerAwayMax.csv",index=None)
# playerHMEAvgPerf.to_csv(root+"playerHomeMax.csv",index=None)
# 
###############################################################################################################
  
# Get Defense Teams
# dfDef = df[df["Position"] == "DST"]
#  
# # Get the Stats for each defense team
# defStats = ComputationBlocks.getDefStatsSummary(dfDef,season,weeks)
# # Group the stats by team
# defense =  defStats.groupby(["Team"])
#  
# defStatsAway = pda.DataFrame()
# defStatsHME = pda.DataFrame()
# # 
# # 
# # # Get stats for each player at and away from home
# for n,g in defense:
#     [tempAway,tempHME] =  ComputationBlocks.statsbyHomeFldAvd(g,"HomeFldAdv")    
#     defStatsAway = defStatsAway.append(tempAway)
#     defStatsHME = defStatsHME.append(tempHME)
#  
# # ###############################################################################################################
# # #Get Average Performance and normalize them
# # ############################################################################################################### 
# defAWYAvgPerf =  ComputationBlocks.getDefenseAvgPerformance(defStatsAway)
# defHMEAvgPerf =  ComputationBlocks.getDefenseAvgPerformance(defStatsHME)
#  
#  
# teamHMEAvgPerfNorm = ComputationBlocks.normalizeTeamStats(defHMEAvgPerf)
# teamAWYAvgPerfNorm = ComputationBlocks.normalizeTeamStats(defAWYAvgPerf)
 
 
teamHMEAvgPerfNorm = pda.read_csv(root+"teamNormHome.csv")
teamAWYAvgPerfNorm= pda.read_csv(root+"teamNormAway.csv")
playerAWYAvgPerf= pda.read_csv(root+"playerAway.csv")
playerHMEAvgPerf= pda.read_csv(root+"playerHome.csv")
 
 
# ############################################################################################################### 
[away,home] = ComputationBlocks.getHomenAwy(df["GameInfo"])
# 
# 
offensiveMatchup = ComputationBlocks.offMatchupPerformance (playerHMEAvgPerf,playerAWYAvgPerf,teamHMEAvgPerfNorm,teamAWYAvgPerfNorm,home,away)
# 
# print "-----------------------------------------"
# print offensiveMatchup.head()
# print "-----------------------------------------"
# 
offensiveMatchup.to_csv(root+"offMatchup.csv",index=None)




#############################################################################################################################################
# Offensive Player Points
x = pda.read_csv(root+"offMatchup.csv")
# 
points = []
for i in range(x.shape[0]):
    points.extend([4*x.loc[x.index[i],"PassingTDs"]+0.04*x.loc[x.index[i],"PassingYards"]+3*max(0,min(1,x.loc[x.index[i],"PassingYards"]-300))-x.loc[x.index[i],"PassingInterceptions"]+0.1*x.loc[x.index[i],"RushingYards"]+6*x.loc[x.index[i],"RushingTDs"]+3*max(0,min(1,x.loc[x.index[i],"RushingYards"]-100))+0.1*x.loc[x.index[i],"ReceivingYards"]+6*x.loc[x.index[i],"ReceivingTDs"]+3*max(0,min(1,x.loc[x.index[i],"ReceivingYards"]-100))-x.loc[x.index[i],"FumblesLost"] + 2*(x.loc[x.index[i],"TwoPtsPassing"]+x.loc[x.index[i],"TwoPtsReceiving"]+x.loc[x.index[i],"TwoPtsRushing"])+6*x.loc[x.index[i],"OFRTD"]])
 
x["Points"] = pda.Series(points)
x.to_csv(root+"Wk15PlayerValue.csv")