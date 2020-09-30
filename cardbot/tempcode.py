
from tables.tournament import timezone, participant, tournament, participant_to_tournament, tournament_participant_to_bans, tournament_participant_to_ign, matchup
from constructorRows import timezone_rows
from db_interactions_tournaments import getParticipantInfo

def handyman(complete_call):
	print(getParticipantInfo("Chombler", 1))
	print(getParticipantInfo(2, 1))

	return("Handyman is finished")
