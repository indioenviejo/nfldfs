
import pandas as pda
import Player
import nflgame

# Returns the players GSIS ID
def getPlayerID(name,team):
    # Find the player
    player = nflgame.find(name,team)[0]
    return player.gsis_name 


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
        ##########################################################################################################
        # Draft Kings names Jaguars as JAX while nflgame returns JAC 
        if df.loc[df.index[i],"teamAbbrev"].upper() == "JAX":
            team = "JAC"
        else:
            team = df.loc[df.index[i],"teamAbbrev"].upper()
            
        gsisID = getPlayerID(df.loc[df.index[i],"Name"],team)            
        x = Player.Player(gsisID,df.loc[df.index[i],"Name"],df.loc[df.index[i],"Name"],df.loc[df.index[i],"Position"],team)
        
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
            print x.name, j
        
        tempDF = pda.DataFrame(zip(name,teams,position,weekStatus,homeFldAdv,status,fumblesLost,OFRTD,passingInterceptions,passingTDs,passingYards,receivingTDs,receivingYards,receptions,rushingTDs,rushingYards,twoPtsPassing,twoPtsReceiving,twoPtsRushing))
        tempDF.columns = ["Name","Team","Position","Week","HomeFldAdv","Status","FumblesLost","OFRTD","PassingInterceptions","PassingTDs","PassingYards","ReceivingTDs","ReceivingYards","Receptions","RushingTDs","RushingYards","TwoPtsPassing","TwoPtsReceiving","TwoPtsRushing"]
        print tempDF.head()
        playerStats = playerStats.append(tempDF)
    
    return playerStats