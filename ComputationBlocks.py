
import pandas as pda
import Player
import DST
import nflgame
import numpy as np

# Returns the players GSIS ID
def getPlayerID(name,team):
    # Find the player
    player = nflgame.find(name,team)[0]
    return player.gsis_id 


def getPlayerStatsSummary(df,season,weeks):
        
    playerStats = pda.DataFrame()
    for i in range(df.shape[0]):
        # Stats being captured for each offensive player
        ##########################################################################################################
        fumblesLost = []
        homeFldAdv = []
        OFRTD = []
        passingInterceptions = []
        passingTDs = []
        passingYards = []
        receivingTDs = []
        receivingYards = []
        receptions = []
        rushingTDs = []
        rushingYards = []
        twoPtsPassing = []
        twoPtsReceiving = []
        twoPtsRushing = []
        weekStatus = []
        name = []
        position = [] 
        teams = []
        status = []
        gsisIDs = []
        salaries = []
        nextGame = []
        ##########################################################################################################
        # Draft Kings names Jaguars as JAX while nflgame returns JAC 
        if df.loc[df.index[i],"teamAbbrev"].upper() == "JAX":
            team = "JAC"
        else:
            team = df.loc[df.index[i],"teamAbbrev"].upper()
            
        gsisID = getPlayerID(df.loc[df.index[i],"Name"],team)            
        x = Player.Player(gsisID,df.loc[df.index[i],"Name"],df.loc[df.index[i],"Position"],team)
        
        for j in weeks:
            name.extend([x.name])
            position.extend([x.position])
            teams.extend([x.team])
            fumblesLost.extend([x.getFumblesLost(season,j)])
            homeFldAdv.extend([x.getHomeFldAdv(season,j)])
            OFRTD.extend([x.getOFRTD(season,j)])
            passingInterceptions.extend([x.getPassingInterceptions(season,j)])
            passingTDs.extend([x.getPassingTDs(season,j)])
            passingYards.extend([x.getPassingYards(season,j)])
            receivingTDs.extend([x.getReceivingTDs(season,j)])
            receivingYards.extend([x.getReceivingYards(season,j)])
            receptions.extend([x.getReceptions(season,j)])
            rushingTDs.extend([x.getRushingTDs(season,j)])
            rushingYards.extend([x.getRushingYards(season,j)])
            twoPtsPassing.extend([x.getTwoPtsPassing(season,j)])
            twoPtsReceiving.extend([x.getTwoPtsReceiving(season,j)])
            twoPtsRushing.extend([x.getTwoPtsRushing(season,j)])
            weekStatus.extend([j])
            status.extend([x.getWeekStatus(season,j)])
            gsisIDs.extend([gsisID])
            salaries.extend([df.loc[df.index[i],"Salary"]])
            nextGame.extend([df.loc[df.index[i],"GameInfo"]])
            print x.name, j
        
        tempDF = pda.DataFrame(zip(name,teams,position,gsisIDs,weekStatus,homeFldAdv,nextGame,status,salaries,fumblesLost,OFRTD,passingInterceptions,passingTDs,passingYards,receivingTDs,receivingYards,receptions,rushingTDs,rushingYards,twoPtsPassing,twoPtsReceiving,twoPtsRushing))
        tempDF.columns = ["Name","Team","Position","GSIS_ID","Week","HomeFldAdv","NextGame","Status","Salary","FumblesLost","OFRTD","PassingInterceptions","PassingTDs","PassingYards","ReceivingTDs","ReceivingYards","Receptions","RushingTDs","RushingYards","TwoPtsPassing","TwoPtsReceiving","TwoPtsRushing"]
        print tempDF.head()
        playerStats = playerStats.append(tempDF)
    
    return playerStats



def statsbyHomeFldAvd(df,indexCol):
    
    hmefldGrp = df.groupby([indexCol])
    
    playerStatsAway = None
    playerStatsHME = None
    
    for n,g in hmefldGrp:
        if n == "AWY":
            playerStatsAway = g
        if n == "HME":
            playerStatsHME = g
    
    returnList = [playerStatsAway,playerStatsHME]  
    return returnList


def getPlayerAvgPerformance(df,hmfld):

    players = df.groupby(["Name","Team","Position","GSIS_ID","NextGame"])
    playerAvgPerf = pda.DataFrame()
    playerNames = []
    playerTeams = []
    playerPositions = []
    gsis = []
    salaries = []
    nextGame = []
    
    
    for n,g in players:
        g = g[g.columns[8:]]
        playerAvgPerf  = playerAvgPerf.append(g.mean(),ignore_index=True)
        playerNames.extend([n[0]])
        playerTeams.extend([n[1]])
        playerPositions.extend([n[2]])
        gsis.extend([n[3]])
        salaries.extend(list(np.unique(g["Salary"])))
        nextGame.extend([n[4]])
        
    playerAvgPerf["Name"] = pda.Series(playerNames)
    playerAvgPerf["Team"] = pda.Series(playerTeams)
    playerAvgPerf["Position"] = pda.Series(playerPositions)
    playerAvgPerf["GSIS_ID"] = pda.Series(gsis)
    playerAvgPerf["Salary"] = pda.Series(salaries)
    playerAvgPerf["HmeFldAdv"] = pda.Series([hmfld]*len(playerNames))
    playerAvgPerf["NextGame"] = pda.Series(nextGame)    
    
    return playerAvgPerf



def getDefenseAvgPerformance(df):
    
    teams = df.groupby(["Team"])
    teamAvgPerf = pda.DataFrame()
    teamNames = []
    salaries = []
    
    for n,g in teams:
        g2 = g[g.columns[4:]]
        teamAvgPerf  = teamAvgPerf.append(g2.mean(),ignore_index=True)
        teamNames.extend([n])
        salaries.extend(list(np.unique(g["Salary"])))
    teamAvgPerf["Team"] = pda.Series(teamNames)
    teamAvgPerf["Salary"] = pda.Series(salaries)
    
    
    return teamAvgPerf
    


def getDefStatsSummary(dfFilter,season,weeks):
    defStats = pda.DataFrame()
    for i in range(dfFilter.shape[0]):
        
        print i
        defRecTDs = []
        defRecs = []
        defTDs =[]
        FGBlk =[]
        homeFldAdv = []
        interceptions = []
        KRTDs = []    
        PRTDs = []
        passingTDs = []
        passingYards = []
        pointsGivenUp = []
        receptions = []
        rushingTDs = []
        rushingYards = []
        sacks = []
        safetys = []
        xtraPtBlk = []
        weekStatus = []
        salaries = []
        teams = []
    
        if dfFilter.loc[dfFilter.index[i],"teamAbbrev"].upper() == "JAX":
            teamName = "JAC"
        else:
            teamName = dfFilter.loc[dfFilter.index[i],"teamAbbrev"].upper()
        
        x = DST.DST(teamName)
        
        for j in weeks:
            print x.team, j
            defRecTDs.extend([x.getDefRecoveryTDsScored(season,j)])
            defRecs.extend([x.getDefRecoveriesMade(season,j)])
            defTDs.extend([x.getDefTDsScored(season,j)])
            FGBlk.extend([x.getDefFGBlkMade(season,j)])
            homeFldAdv.extend([x.getHomeFldAdv(season,j)])
            KRTDs.extend([x.getKickRetTDsMade(season,j)])
            PRTDs.extend([x.getPuntRetTDsMade(season,j)])
            passingTDs.extend([x.getDefPassingTDsAllowed(season,j)])
            passingYards.extend([x.getDefPassingYardsAllowed(season,j)])
            pointsGivenUp.extend([x.getPointsGivenUp(season,j)])
            receptions.extend([x.getDefReceptionsAllowed(season,j)])
            rushingTDs.extend([x.getDefRushingTDsAllowed(season,j)])
            rushingYards.extend([x.getDefRushingYardsAllowed(season,j)])
            sacks.extend([x.getDefSacks(season,j)])
            safetys.extend([x.getDefSafetysMade(season,j)])
            xtraPtBlk.extend([x.getDefXtraPtBlkMade(season,j)])
            weekStatus.extend([j])
            interceptions.extend([x.getDefInterceptions(season,j)])
            teams.extend([x.team])
            salaries.extend([dfFilter.loc[dfFilter.index[i],"Salary"]])
            
        tempDF = pda.DataFrame(zip(teams,salaries,weekStatus,homeFldAdv,defRecTDs,defRecs,defTDs,FGBlk,interceptions,KRTDs,PRTDs,passingTDs,passingYards,pointsGivenUp,receptions,rushingTDs,rushingYards,sacks,safetys,xtraPtBlk))
        tempDF.columns = ["Team","Salary","Week","HomeFldAdv","DefenseRecTDs","DefenseRecoveries","DefenseTDs","FGBlk","Interceptions","KickRetTDs","PuntRetTDs","PassingTDsAllowed","PassingYardsAllowed","PointsGivenUp","ReceptionsAllowed","RushingTDsAllowed","RushingYardsAllowed","Sacks","Safetys","ExtraPointBlk"]
        print tempDF
        defStats = defStats.append(tempDF)        
    
    return defStats


def normalizeTeamStats(df):
    teams = df["Team"]
    dfNorm = df.drop("Team",1)
    dfNorm = (dfNorm - dfNorm.mean())/ dfNorm.mean()
    dfNorm["Team"] = teams
    return dfNorm


#################################################################################################

# Get Matches

def getHomenAwy(gameInfo):

    away = []
    home = []
    
    for info in gameInfo:
        away.extend([info.split(" ")[0].split("@")[0]])
        home.extend([info.split(" ")[0].split("@")[1]])
    
    matches = zip(away,home)
    matches = list(set(matches))
    
    away = [ a[0] for a in matches]
    home = [ a[1] for a in matches]
    
    away = [a.upper() if a.upper()<>"JAX" else "JAC" for a in away]
    home = [a.upper() if a.upper()<>"JAX" else "JAC" for a in home]
    #################################################################################################
    
    returnList = [away,home]
    
    return returnList





##########################################################################################################
# Offensive Matchup Performance


def offMatchupPerformance (playerHMEAvgPerf,playerAWYAvgPerf,teamHMEAvgPerfNorm,teamAWYAvgPerfNorm,home,away):
    
    ###############################################################################################
    ##########################################################################################################
    fumblesLost = []
    OFRTD = []
    passingInterceptions = []
    passingTDs = []
    passingYards = []
    receivingTDs = []
    receivingYards = []
    receptions = []
    rushingTDs = []
    rushingYards = []
    twoPtsPassing = []
    twoPtsReceiving = []
    twoPtsRushing = []
    name = [] 
    position = [] 
    teams = []
    salaries = []
    
    ##########################################################################################################    
    #playerConsolidatedAvgPerfStats
    PCAPStats = playerHMEAvgPerf.append(playerAWYAvgPerf)
    grouped = PCAPStats.groupby(["GSIS_ID"])
    
    defTeamHme = teamHMEAvgPerfNorm
    defTeamAwy = teamAWYAvgPerfNorm
    
    opponent = None
    
    for n,g in grouped:
        if pda.unique(g["Team"])[0] in away:
            g = g[g["HmeFldAdv"]=="AWY"]
            if len(g.index) > 0 :
                index = [i for i,j in enumerate(away) if j == pda.unique(g["Team"])[0]]
                opponent = home[index[0]]

        if pda.unique(g["Team"])[0] in home:
            g = g[g["HmeFldAdv"]=="HME"]
            if len(g.index) > 0:
                index = [i for i,j in enumerate(home) if j == pda.unique(g["Team"])[0]]
                opponent = away[index[0]]                
                
        oppStats = defTeamHme[defTeamHme["Team"] == opponent]
        #DefenseRecoveries Interceptions PassingTDsAllowed    PassingYardsAllowed    PointsGivenUp    PuntRetTDs    ReceptionsAllowed    RushingTDsAllowed    RushingYardsAllowed
        oppStats = oppStats[["DefenseRecoveries","Interceptions","PassingTDsAllowed","PassingYardsAllowed","ReceptionsAllowed","RushingTDsAllowed","RushingYardsAllowed"]]
        
        fumblesLost.extend([(1+oppStats["DefenseRecoveries"][oppStats.index[0]])*g["FumblesLost"][g.index[0]]])
        OFRTD.extend([g["OFRTD"][g.index[0]]])
        passingInterceptions.extend([(1+oppStats["Interceptions"][oppStats.index[0]])*g["PassingInterceptions"][g.index[0]]])
        passingTDs.extend([(1+oppStats["PassingTDsAllowed"][oppStats.index[0]])*g["PassingTDs"][g.index[0]]])
        passingYards.extend([(1+oppStats["PassingYardsAllowed"][oppStats.index[0]])*g["PassingYards"][g.index[0]]])
        receivingTDs.extend([(1+oppStats["PassingTDsAllowed"][oppStats.index[0]])*g["ReceivingTDs"][g.index[0]]])    
        receivingYards.extend([(1+oppStats["PassingYardsAllowed"][oppStats.index[0]])*g["ReceivingYards"][g.index[0]]])
        receptions.extend([(1+oppStats["ReceptionsAllowed"][oppStats.index[0]])*g["Receptions"][g.index[0]]])
        rushingTDs.extend([(1+oppStats["RushingTDsAllowed"][oppStats.index[0]])*g["RushingTDs"][g.index[0]]])
        rushingYards.extend([(1+oppStats["RushingYardsAllowed"][oppStats.index[0]])*g["RushingYards"][g.index[0]]])
        twoPtsPassing.extend([g["TwoPtsPassing"][g.index[0]]])
        twoPtsReceiving.extend([g["TwoPtsReceiving"][g.index[0]]])
        twoPtsRushing.extend([g["TwoPtsRushing"][g.index[0]]])
        name.extend([pda.unique(g["Name"])[0]]) 
        position.extend([pda.unique(g["Position"])[0]]) 
        teams.extend([pda.unique(g["Team"])[0]])
        salaries.extend([g["Salary"][g.index[0]]])

    offPerf = pda.DataFrame(zip(name,teams,position,salaries,fumblesLost,OFRTD,passingInterceptions,passingTDs,passingYards,receivingTDs,receivingYards,receptions,rushingTDs,rushingYards,twoPtsPassing,twoPtsReceiving,twoPtsRushing))
    offPerf.columns = ["Name","Team","Position","Salary","FumblesLost","OFRTD","PassingInterceptions","PassingTDs","PassingYards","ReceivingTDs","ReceivingYards","Receptions","RushingTDs","RushingYards","TwoPtsPassing","TwoPtsReceiving","TwoPtsRushing"]
    
    return offPerf
    
    
    
