import nflgame

# Stores all the information about the players
class Player(object):

############################################################################################################################################    
    # Initialize the player object
    def __init__(self, gsis_id,name, position, team):
        
        self.gsis_id = gsis_id
        self.name = name
        self.position = position
        validTeams = [i[0] for i in nflgame.teams]
        
        if team in validTeams:
            self.team = team
        else:
            RuntimeError("Please Check the DST Name.") 
            
        
############################################################################################################################################    
    # Check the status of the player (active or not ?)
    # for the game in a given week and season    
    # If the player was in Bye Week , returns BYE
    
    def getWeekStatus(self,season,week):
        # Get statistics for the current game
        game = nflgame.one(season, week, self.team, self.team)
    
        if game is None:
            return "BYE"
    
        # Get all the players with the name
        # Sometimes you may have multiple players 
        # with the same name
    
        currentPlayers = game.players
        
        # Iterate through all the players with that name
        for p in currentPlayers:
            # Make sure the position, player name and team name matches 
            # with the current player's
            if p.player is not None and p.player.gsis_id==self.gsis_id:
                return p.player.status
                
############################################################################################################################################        
    # Get the number of passing yards for the player    

    def getPassingYards(self,season,week):
        
        #Value that will be returned from the function.
        passYards = 0
        
        # Get statistics for the current game
        game = nflgame.one(season, week, self.team, self.team)

        # Bye Week ? If yes, get out of the function
        
        if game is None:
            return passYards
        

        # Get all the players with the name
        # Sometimes you may have multiple players 
        # with the same name
    
        currentPlayers = game.players
        
        # Iterate through all the players with that name
        for p in currentPlayers:
            # Make sure the position, player name and team name matches 
            # with the current player's and that the stats dictionary has 
            # the passing_yds key 
            if p.player is not None:
                if p.player is not None and p.player.gsis_id==self.gsis_id:
                    passYards = p.stats["passing_yds"]
            
        return passYards


############################################################################################################################################        
    # Get the number of passing touchdowns for the player    
    def getPassingTDs(self,season,week):
        
        #Value that will be returned from the function.
        passTDs = 0
        
        # Get statistics for the current game
        game = nflgame.one(season, week, self.team, self.team)
        
        # Bye Week ? If yes, get out of the function
        
        if game is None:
            return passTDs

        # Get all the players with the name
        # Sometimes you may have multiple players 
        # with the same name
        currentPlayers = game.players
        
        # Iterate through all the players with that name
        for p in currentPlayers:
            # Make sure the position, player name and team name matches 
            # with the current player's and that the stats dictionary has 
            # the passing_tds key 
            if p.player is not None and p.player.gsis_id==self.gsis_id:
                if "passing_tds" in p.stats:
                    passTDs = p.stats["passing_tds"]
        return passTDs

############################################################################################################################################        
    # Get the number of rushing yards for the player    
    def getRushingYards(self,season,week):
        #Value that will be returned from the function.
        rushYards = 0
        
        # Get statistics for the current game
        game = nflgame.one(season, week, self.team, self.team)


        # Bye Week ? If yes, get out of the function
        if game is None:
            return rushYards

        # Get all the players with the name. Sometimes you may have multiple players 
        # with the same name.
        
        currentPlayers = game.players
        
        # Iterate through all the players with that name
        for p in currentPlayers:
            # Make sure the position, player name and team name matches 
            # with the current player's and that the stats dictionary has 
            # the rushing_yds key 
            if p.player is not None and p.player.gsis_id==self.gsis_id:
                if "rushing_yds" in p.stats:
                    rushYards = p.stats["rushing_yds"]

        return rushYards

############################################################################################################################################        
    # Get the number of rushing touchdowns for the player    
    def getRushingTDs(self,season,week):
        #Value that will be returned from the function.
        rushTDs = 0
        
        # Get statistics for the current game
        game = nflgame.one(season, week, self.team, self.team)

        # Bye Week ? If yes, get out of the function
        if game is None:
            return rushTDs

        # Get all the players with the name. Sometimes you may have multiple players 
        # with the same name.
        
        currentPlayers = game.players
        
        # Iterate through all the players with that name
        for p in currentPlayers:
            # Make sure the position, player name and team name matches 
            # with the current player's and that the stats dictionary has 
            # the rushing_yds key 
            if p.player is not None and p.player.gsis_id==self.gsis_id:
                if "rushing_tds" in p.stats:
                    rushTDs = p.stats["rushing_tds"]
        return rushTDs

############################################################################################################################################        
    # Get the number of receiveYards yards for the player    
    def getReceivingYards(self,season,week):
        #Value that will be returned from the function.
        receiveYards = 0
        
        # Get statistics for the current game
        game = nflgame.one(season, week, self.team, self.team)


        # Bye Week ? If yes, get out of the function
        if game is None:
            return receiveYards


        # Get all the players with the name. Sometimes you may have multiple players 
        # with the same name.        
        currentPlayers = game.players
        
        # Iterate through all the players with that name
        for p in currentPlayers:
            # Make sure the position, player name and team name matches 
            # with the current player's and that the stats dictionary has 
            # the receiving_yds key 
            if p.player is not None and p.player.gsis_id==self.gsis_id:
                if "receiving_yds" in p.stats:
                    receiveYards = p.stats["receiving_yds"]
        
        return receiveYards
        
############################################################################################################################################        
    # Get the number of receptions for the player    
    def getReceptions(self,season,week):
        #Value that will be returned from the function.
        receptions = 0
        
        # Get statistics for the current game
        game = nflgame.one(season, week, self.team, self.team)


        # Bye Week ? If yes, get out of the function
        if game is None:
            return receptions

        # Get all the players with the name. Sometimes you may have multiple players 
        # with the same name.        
        currentPlayers = game.players
        
        # Iterate through all the players with that name
        for p in currentPlayers:
            # Make sure the position, player name and team name matches 
            # with the current player's and that the stats dictionary has 
            # the receiving_rec key 
            if p.player is not None and p.player.gsis_id==self.gsis_id:
                if "receiving_rec" in p.stats:
                    receptions = p.stats["receiving_rec"]

        return receptions


############################################################################################################################################        
    # Get the number of receiveTDs yards for the player        
    def getReceivingTDs(self,season,week):
        #Value that will be returned from the function.
        receiveTDs = 0
        
        # Get statistics for the current game
        game = nflgame.one(season, week, self.team, self.team)


        # Bye Week ? If yes, get out of the function
        if game is None:
            return receiveTDs

        # Get all the players with the name. Sometimes you may have multiple players 
        # with the same name.        
        currentPlayers = game.players
        
        # Iterate through all the players with that name
        for p in currentPlayers:
            # Make sure the position, player name and team name matches 
            # with the current player's and that the stats dictionary has 
            # the receiving_tds key 
            if p.player is not None and p.player.gsis_id==self.gsis_id:
                if "receiving_tds" in p.stats:
                    receiveTDs = p.stats["receiving_tds"]
        
        return receiveTDs

############################################################################################################################################        
    # Get the number of offensive fumble recovery TDs for the player    
    def getOFRTD(self,season,week):
        #Value that will be returned from the function.
        OFRTD = 0
        
        # Get statistics for the current game
        game = nflgame.one(season, week, self.team, self.team)

        # Bye Week ? If yes, get out of the function
        if game is None:
            return OFRTD

        # Get all the players with the name. Sometimes you may have multiple players 
        # with the same name.        
        currentPlayers = game.players
        
        # Iterate through all the players with that name
        for p in currentPlayers:
            # Make sure the position, player name and team name matches 
            # with the current player's and that the stats dictionary has 
            # the receiving_rec key 
            if p.player is not None and p.player.gsis_id==self.gsis_id:
                if "fumbles_trcv" in p.stats:
                    OFRTD = p.stats["fumbles_trcv"]
        return OFRTD
        
############################################################################################################################################        
    # Get the number of passing interceptions for the player    
    def getPassingInterceptions(self,season,week):
        #Value that will be returned from the function.
        interceptions = 0
        
        # Get statistics for the current game
        game = nflgame.one(season, week, self.team, self.team)

        # Bye Week ? If yes, get out of the function
        if game is None:
            return interceptions


        # Get all the players with the name. Sometimes you may have multiple players 
        # with the same name.        
        currentPlayers = game.players
        
        # Iterate through all the players with that name
        for p in currentPlayers:
            # Make sure the position, player name and team name matches 
            # with the current player's and that the stats dictionary has 
            # the passing_ints key 
            if p.player is not None and p.player.gsis_id==self.gsis_id:
                if "passing_ints" in p.stats:
                    interceptions = p.stats["passing_ints"]
        return interceptions
        
############################################################################################################################################        
    # Get the number of fumbles lost for the player    
    def getFumblesLost(self,season,week):
        #Value that will be returned from the function.
        fumbles = 0
        
        # Get statistics for the current game
        game = nflgame.one(season, week, self.team, self.team)

        # Bye Week ? If yes, get out of the function
        if game is None:
            return fumbles

        # Get all the players with the name. Sometimes you may have multiple players 
        # with the same name.        
        currentPlayers = game.players
        
        # Iterate through all the players with that name
        for p in currentPlayers:
            # Make sure the position, player name and team name matches 
            # with the current player's and that the stats dictionary has 
            # the fumbles_lost key 
            if p.player is not None and p.player.gsis_id==self.gsis_id:
                if "fumbles_lost" in p.stats:
                    fumbles = p.stats["fumbles_lost"]
        return fumbles
        
############################################################################################################################################        
    # Get the number of two points made by the player    
    def getTwoPtsPassing(self,season,week):
        #Value that will be returned from the function.
        twoPts = 0
        # Get statistics for the current game
        game = nflgame.one(season, week, self.team, self.team)
        

        # Bye Week ? If yes, get out of the function
        if game is None:
            return twoPts        
        
        # Get all the players with the name. Sometimes you may have multiple players 
        # with the same name.        
        currentPlayers = game.players
        
        # Iterate through all the players with that name
        for p in currentPlayers:
            # Make sure the position, player name and team name matches 
            # with the current player's and that the stats dictionary has 
            # the fumbles_lost key 
            if p.player is not None and p.player.gsis_id==self.gsis_id:
                if "passing_twoptm" in p.stats:
                    twoPts = p.stats["passing_twoptm"]
        return twoPts

############################################################################################################################################        
    # Get the number of two points made by passing plays    
    def getTwoPtsReceiving(self,season,week):
        #Value that will be returned from the function.
        twoPts = 0
        # Get statistics for the current game
        game = nflgame.one(season, week, self.team, self.team)
        
        # Bye Week ? If yes, get out of the function
        if game is None:
            return twoPts            
        
        # Get all the players with the name. Sometimes you may have multiple players 
        # with the same name.        
        currentPlayers = game.players
        
        # Iterate through all the players with that name
        for p in currentPlayers:
            # Make sure the position, player name and team name matches 
            # with the current player's and that the stats dictionary has 
            # the fumbles_lost key 
            if p.player is not None and p.player.gsis_id==self.gsis_id:
                if "receiving_twoptm" in p.stats:
                    twoPts = p.stats["receiving_twoptm"]
        return twoPts

############################################################################################################################################        
    # Get the number of two points made by passing plays    
    def getTwoPtsRushing(self,season,week):
        #Value that will be returned from the function.
        twoPts = 0
        # Get statistics for the current game
        game = nflgame.one(season, week, self.team, self.team)
        
        # Bye Week ? If yes, get out of the function
        if game is None:
            return twoPts            
        
        # Get all the players with the name. Sometimes you may have multiple players 
        # with the same name.        
        currentPlayers = game.players
        
        # Iterate through all the players with that name
        for p in currentPlayers:
            # Make sure the position, player name and team name matches 
            # with the current player's and that the stats dictionary has 
            # the fumbles_lost key 
            if p.player is not None:
                if "rushing_twoptm" in p.stats:
                    twoPts = p.stats["rushing_twoptm"]
        return twoPts

############################################################################################################################################        
    # Get if the game was played at home or away for a player in a given week+season
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