import sys
sys.path.append('../')

import nanoid

class PassDetector():

    def __init__(self):
        pass
    
    def determine_passes(self, raw_report):
        passes = []
        pass_id_counter = 1

        for entry in raw_report:
            for player_id, player_data in team_data.items():
                ball_possession_frames = []
                for frame_num, frame_data in enumerate(player_data):
                    if frame_data.get('has_ball', False):
                        ball_possession_frames.append(frame_num)
                    else:
                        if len(ball_possession_frames) >= 5:
                            start_frame = ball_possession_frames[0]
                            end_frame = ball_possession_frames[-1]
                            frames = end_frame - start_frame + 1
                            pass_type = self.determine_pass_type(frames)
                            pass_id = nanoid.generate(size=10)
                            passes.append({
                                "team": team,
                                "from_player": player_id,
                                "to_player": None,  # To be filled later
                                "start_frame": start_frame,
                                "end_frame": end_frame,
                                "frames": frames,
                                "pass_type": pass_type,
                                "pass_id": pass_id
                            })
                        ball_possession_frames = []

                if len(ball_possession_frames) >= 5:
                    start_frame = ball_possession_frames[0]
                    end_frame = ball_possession_frames[-1]
                    frames = end_frame - start_frame + 1
                    pass_type = self.determine_pass_type(frames)
                    pass_id = nanoid.generate(size=10)
                    passes.append({
                        "team": team,
                        "from_player": player_id,
                        "to_player": None,  # To be filled later
                        "start_frame": start_frame,
                        "end_frame": end_frame,
                        "frames": frames,
                        "pass_type": pass_type,
                        "pass_id": pass_id
                    })

        # Determine the receiver of the pass
        for i in range(len(passes) - 1):
            if passes[i]["team"] == passes[i + 1]["team"]:
                passes[i]["to_player"] = passes[i + 1]["from_player"]

        # Remove incomplete passes
        passes = [p for p in passes if p["to_player"] is not None]

        return passes

    def determine_pass_type(self, frames):
        if 5 <= frames <= 10:
            return "short"
        elif 11 <= frames <= 20:
            return "medium"
        else:
            return "long"