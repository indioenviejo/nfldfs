
import nflgame

# Stores all the information about the Defense and Special Teams Performance
class DST(object):

############################################################################################################################################    
    # Initialize the player object
    def __init__(self, team):
        self.team = team
        
############################################################################################################################################
    #Get all sacks by the defense in week "w" of season "s"
    def getDefSacks(self,s, w):
        games = nflgame.games_gen(s, w, self.team , self.team)
        sks = 0
        # Bye Week ? If yes, get out of the function
        if games is None:
            return sks    

        plays = nflgame.combine_plays(games)

        for p in plays.filter(team__ne=self.team):
            if p.defense_sk > 0:
                sks += 1
        
        return sks

############################################################################################################################################
    #Get all interceptions by the defense in week "w" of season "s"
    def getDefInterceptions(self,s, w):
        games = nflgame.games_gen(s, w, self.team , self.team)
        interceptions = 0
        
        # Bye Week ? If yes, get out of the function
        if games is None:
            return interceptions    
        
        plays = nflgame.combine_plays(games)
        
        for p in plays.filter(team__ne=self.team, passing_int__gt=0):
                interceptions += p.passing_int

        return interceptions

############################################################################################################################################        
    # Get if the game was played at home or away for the defense in a given week+season
    # Returns "HME" if the game was played at Home or "AWY" if the game was played away
    # If the team had a bye-week , the method return "BYE"
    def getHomeFldAdv(self,season,week):
        # Get statistics for the current game
        game = nflgame.one(season, week, self.team, self.team)
        
        if game ==None:
            return "BYE"
        
        if game.away == self.team:
            return "AWY"
        elif game.home == self.team:
            return "HME"
############################################################################################################################################
    #Get the # of passing yards allowed by the defense in week "w" of season "s"
    def getDefPassingYardsAllowed(self,s, w):
        games = nflgame.games_gen(s, w, self.team , self.team)
        passYards = 0
        
        # Bye Week ? If yes, get out of the function
        if games is None:
            return passYards    
        
        plays = nflgame.combine_plays(games)
        
        for p in plays.filter(team__ne=self.team, passing_att__ge=1):
                passYards += p.passing_yds
        
        return passYards


############################################################################################################################################
    #Get the # of passing TDs allowed by the defense in week "w" of season "s"
    
    def getDefPassingTDsAllowed(self,s, w):
        games = nflgame.games_gen(s, w, self.team , self.team)
        passTDs = 0
        
        # Bye Week ? If yes, get out of the function
        if games is None:
            return passTDs    
        
        plays = nflgame.combine_plays(games)
        
        for p in plays.filter(team__ne=self.team, passing_att__ge=1):
                passTDs += p.passing_tds
        
        return passTDs

############################################################################################################################################
    #Get the # of receptions allowed by the defense in week "w" of season "s"
    
    def getDefReceptionsAllowed(self,s, w):
        games = nflgame.games_gen(s, w, self.team , self.team)
        receptions = 0
        
        # Bye Week ? If yes, get out of the function
        if games is None:
            return receptions    
        
        plays = nflgame.combine_plays(games)
        
        for p in plays.filter(team__ne=self.team, passing_att__ge=1):
                receptions += p.receiving_rec
        
        return receptions

############################################################################################################################################
    #Get the # of rushing yards allowed by the defense in week "w" of season "s"
    def getDefRushingYardsAllowed(self,s, w):
        games = nflgame.games_gen(s, w, self.team , self.team)
        rushYards = 0
        
        # Bye Week ? If yes, get out of the function
        if games is None:
            return rushYards    
        
        plays = nflgame.combine_plays(games)
        
        for p in plays.filter(team__ne=self.team, rushing_att__ge=1):
                rushYards += p.rushing_yds
        
        return rushYards

############################################################################################################################################
    #Get the # of rushing TDs allowed by the defense in week "w" of season "s"

    def getDefRushingTDsAllowed(self,s, w):
        games = nflgame.games_gen(s, w, self.team , self.team)
        rushTDs = 0
        
        # Bye Week ? If yes, get out of the function
        if games is None:
            return rushTDs    
        
        plays = nflgame.combine_plays(games)
        
        for p in plays.filter(team__ne=self.team, rushing_att__ge=1):
                rushTDs += p.rushing_tds
        
        return rushTDs

############################################################################################################################################
    #Get the # of points given up by the defense in week "w" of season "s"

    def getPointsGivenUp(self,s, w):
        game = nflgame.one(s,w,self.team, self.team)
        ptsGVU = 0
        
        # Bye Week ? If yes, get out of the function
        if game is None:
            return ptsGVU    
        
    
        if game.away == self.team:
            ptsGVU = game.score_home
        elif game.home == self.team:
            ptsGVU = game.score_away

        return ptsGVU

############################################################################################################################################
    #Get the # of defensive TDs allowed by the defense in week "w" of season "s"
    def getDefTDsScored(self,s, w):
        games = nflgame.games_gen(s, w, self.team ,self.team)
        defTDs = 0
        # Bye Week ? If yes, get out of the function
        if games is None:
            return defTDs    
        plays = nflgame.combine_plays(games)
        for play in plays.filter(team__ne=self.team):
            if play.defense_tds>0:
                defTDs = defTDs+1
        return defTDs
############################################################################################################################################
    #Get the # of defensive recoveries made by the defense in week "w" of season "s"
    def getDefRecoveriesMade(self,s, w):
        games = nflgame.games_gen(s, w, self.team ,self.team)
        defRecs = 0
        # Bye Week ? If yes, get out of the function
        if games is None:
            return defRecs    
        plays = nflgame.combine_plays(games)
        for play in plays.filter(team__ne=self.team):
            if play.defense_frec>0:
                defRecs = defRecs+1
        return defRecs

############################################################################################################################################
    #Get the # of defensive recovery touchdowns made by the defense in week "w" of season "s"    
    
    def getDefRecoveryTDsScored(self,s, w):
        games = nflgame.games_gen(s, w, self.team ,self.team)
        defRecTDs = 0
        # Bye Week ? If yes, get out of the function
        if games is None:
            return defRecTDs
        plays = nflgame.combine_plays(games)
        for play in plays.filter(team__ne=self.team):
            if play.defense_frec_tds>0:
                defRecTDs = defRecTDs+1
        return defRecTDs
        
#defense_safe        
        
############################################################################################################################################
    #Get the # of defensive recovery touchdowns made by the defense in week "w" of season "s"    
    
    def getDefSafetysMade(self,s, w):
        games = nflgame.games_gen(s, w, self.team ,self.team)
        sftys = 0
        # Bye Week ? If yes, get out of the function
        if games is None:
            return sftys
        plays = nflgame.combine_plays(games)
        for play in plays.filter(team__ne=self.team):
            if play.defense_safe>0:
                sftys = sftys+1
        return sftys



############################################################################################################################################
    #Get the # of Extra Points Blocked by the defense in week "w" of season "s"    
    
    def getDefXtraPtBlkMade(self,s, w):
        games = nflgame.games_gen(s, w, self.team ,self.team)
        xpblk = 0
        # Bye Week ? If yes, get out of the function
        if games is None:
            return xpblk
        plays = nflgame.combine_plays(games)
        for play in plays.filter(team__ne=self.team):
            if play.defense_xpblk>0:
                xpblk = xpblk+1
        return xpblk



############################################################################################################################################
    #Get the # of Field Goals Blocked by the defense in week "w" of season "s"    
    
    def getDefFGBlkMade(self,s, w):
        games = nflgame.games_gen(s, w, self.team ,self.team)
        fgblk = 0
        # Bye Week ? If yes, get out of the function
        if games is None:
            return fgblk
        plays = nflgame.combine_plays(games)
        for play in plays.filter(team__ne=self.team):
            if play.defense_fgblk>0:
                fgblk = fgblk+1
        return fgblk

############################################################################################################################################
    #Get the # of Punt Return Touch downs by the Special teams in week "w" of season "s"    
    
    def getPuntRetTDsMade(self,s, w):
        games = nflgame.games_gen(s, w, self.team ,self.team)
        prtds = 0
        # Bye Week ? If yes, get out of the function
        if games is None:
            return prtds
        plays = nflgame.combine_plays(games)
        for play in plays.filter(team__ne=self.team):
            if play.puntret_tds>0:
                prtds = prtds+1
        return prtds

#kickret_tds    


############################################################################################################################################
    #Get the # of Kick Return Touch downs by the Special teams in week "w" of season "s"    
    
    def getKickRetTDsMade(self,s, w):
        games = nflgame.games_gen(s, w, self.team ,self.team)
        krtds = 0
        # Bye Week ? If yes, get out of the function
        if games is None:
            return krtds
        plays = nflgame.combine_plays(games)
        for play in plays.filter(team__ne=self.team):
            if play.kickret_tds>0:
                krtds = krtds+1
        return krtds