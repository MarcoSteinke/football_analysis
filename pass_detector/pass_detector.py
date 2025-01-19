import sys
sys.path.append('../')

import nanoid

min_pass_possession_frames = 5

class PassDetector():

    def __init__(self):
        pass
    
    def determine_passes(self, raw_report):
        passes = []
        ball_possessor = None
        from_player = None
        possessing_team = None
        ball_possession_frames = 0
        pass_candidate = False

        for entry in raw_report:

            if pass_candidate and ball_possession_frames >= min_pass_possession_frames:
                passes.append({
                    "team": possessing_team,
                    "from_player": from_player,
                    "to_player": entry["player"],
                    "pass_id": nanoid.generate(size=10)
                })
                pass_candidate = False
                ball_possession_frames = 0

            if ball_possessor == entry["player"] and possessing_team == entry["team"]:
                ball_possession_frames += 1
            else:
                if possessing_team == entry["team"] and ball_possession_frames >= min_pass_possession_frames:
                    pass_candidate = True
                    from_player = ball_possessor
                else:
                    pass_candidate = False
                ball_possessor = entry["player"]
                possessing_team = entry["team"]
                ball_possession_frames = 1

        return passes