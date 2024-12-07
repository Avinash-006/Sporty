import requests
from django.shortcuts import render


def live_updates(request):
    api_key = '375df7835df94e01827d7b01cbb64665'

    live_matches = []
    past_matches = []

    try:
        # New API URL for live and past matches
        live_matches_url = 'https://api.football-data.org/v4/matches?status=IN_PLAY'
        headers = {'X-Auth-Token': api_key}
        live_response = requests.get(live_matches_url, headers=headers)
        live_match_data = live_response.json().get('matches', [])


        for match in live_match_data:
            home_team = match['homeTeam']['name']
            away_team = match['awayTeam']['name']
            score = match.get('score', {}).get('fullTime', {'home': 'None', 'away': 'None'})

            live_matches.append({
                'home_team': home_team,
                'away_team': away_team,
                'score': f"{score['home']} - {score['away']}",
            })


        if not live_match_data:
            past_matches_url = 'https://api.football-data.org/v4/matches?status=FINISHED'
            past_response = requests.get(past_matches_url, headers=headers)
            past_match_data = past_response.json().get('matches', [])


            for match in past_match_data:
                home_team = match['homeTeam']['name']
                away_team = match['awayTeam']['name']
                score = match.get('score', {}).get('fullTime', {'home': 'None', 'away': 'None'})

                past_matches.append({
                    'home_team': home_team,
                    'away_team': away_team,
                    'score': f"{score['home']} - {score['away']}",
                })
    except KeyError as e:
        live_matches = [{'home_team': "Error fetching data", 'away_team': "Error fetching data", 'score': {'home': 'None', 'away': 'None'}}]
        past_matches = [{'home_team': "Error fetching data", 'away_team': "Error fetching data", 'score': {'home': 'None', 'away': 'None'}}]
    except requests.exceptions.RequestException as e:
        live_matches = [{'home_team': "Error fetching data", 'away_team': "Error fetching data", 'score': {'home': 'None', 'away': 'None'}}]
        past_matches = [{'home_team': "Error fetching data", 'away_team': "Error fetching data", 'score': {'home': 'None', 'away': 'None'}}]

    context = {
        'live_matches': live_matches,
        'past_matches': past_matches,
    }
    return render(request, 'liveupdatesapp/live_updates.html', context)
