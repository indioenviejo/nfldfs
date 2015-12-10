
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
        
        tempDF = pda.DataFrame(zip(name,teams,position,gsisIDs,salaries,weekStatus,homeFldAdv,status,fumblesLost,OFRTD,passingInterceptions,passingTDs,passingYards,receivingTDs,receivingYards,receptions,rushingTDs,rushingYards,twoPtsPassing,twoPtsReceiving,twoPtsRushing))
        tempDF.columns = ["Name","Team","Position","GSIS_ID","Salary","Week","HomeFldAdv","Status","FumblesLost","OFRTD","PassingInterceptions","PassingTDs","PassingYards","ReceivingTDs","ReceivingYards","Receptions","RushingTDs","RushingYards","TwoPtsPassing","TwoPtsReceiving","TwoPtsRushing"]
        print tempDF.head()
        playerStats = playerStats.append(tempDF)
    
    return playerStats



def statsbyHomeFldAvd(df,indexCol):
    
    hmefldGrp = df.groupby([indexCol])
    
    for n,g in hmefldGrp:
        if n == "AWY":
            playerStatsAway = g
        if n == "HME":
            playerStatsHME = g
    
    returnList = [playerStatsAway,playerStatsHME]  
    return returnList


def getPlayerAvgPerformance(df):

    players = df.groupby(["Name","Team","Position","GSIS_ID"])
    playerAvgPerf = pda.DataFrame()
    playerNames = []
    playerTeams = []
    playerPositions = []
    gsis = []
    salaries = []
    
    for n,g in players:
        g = g[g.columns[6:]]
        playerAvgPerf  = playerAvgPerf.append(g.mean(),ignore_index=True)
        playerNames.extend([n[0]])
        playerTeams.extend([n[1]])
        playerPositions.extend([n[2]])
        gsis.extend([n[3]])
        salaries.extend(list(np.unique(df["Salary"])))
        
    playerAvgPerf["Name"] = pda.Series(playerNames)
    playerAvgPerf["Team"] = pda.Series(playerTeams)
    playerAvgPerf["Position"] = pda.Series(playerPositions)
    playerAvgPerf["GSIS_ID"] = pda.Series(gsis)
    playerAvgPerf["Salary"] = pda.Series(salaries)
    playerAvgPerf["HmeFldAdv"] = pda.Series(["AWY"]*len(playerNames))
    
    
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
            salaries.extend([dfFilter.index[i],"Salary"])
            
        tempDF = pda.DataFrame(zip(teams,salaries,weekStatus,homeFldAdv,defRecTDs,defRecs,defTDs,FGBlk,interceptions,KRTDs,PRTDs,passingTDs,passingYards,pointsGivenUp,receptions,rushingTDs,rushingYards,sacks,safetys,xtraPtBlk))
        tempDF.columns = ["Team","Salary","Week","HomeFldAdv","DefenseRecTDs","DefenseRecoveries","DefenseTDs","FGBlk","Interceptions","KickRetTDs","PuntRetTDs","PassingTDsAllowed","PassingYardsAllowed","PointsGivenUp","ReceptionsAllowed","RushingTDsAllowed","RushingYardsAllowed","Sacks","Safetys","ExtraPointBlk"]
        print tempDF
        defStats = defStats.append(tempDF)        
    
    return defStats


