
from tables.tournament import timezone, participant, tournament, participant_to_tournament, tournament_participant_to_bans, tournament_participant_to_ign, matchup
from constructorRows import timezone_rows

def handyman(complete_call):
	matchup.dropTable()
	matchup.createTable()

	return("Handyman is finished")
