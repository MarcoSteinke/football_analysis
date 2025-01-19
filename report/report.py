import sys 
sys.path.append('../')
import nanoid
import logging
import os

class Report():
    def __init__(self, input_file_name):
        self.report = []
        self.logger = logging.getLogger(__name__)
        self.input_file_name = self.__produce_file_name(input_file_name)
        self.__raw_report = []
        self.__total_frames = 0
        logging.basicConfig(filename=f"reports/{self.input_file_name}", level=logging.INFO, format='%(message)s')

    def __produce_file_name(self, input_file_name):
        return f"{input_file_name.replace("input_videos/","") + nanoid.generate(size=8)}.log"
    
    def generate_report(self,tracks):
        for frame_num, player_track in enumerate(tracks['players']):
            for player_id, track in player_track.items():
                if('has_ball' in track):
                    self.__raw_report.append({"frame": frame_num, "player": player_id, "team": track['team'], "has_ball": True})
        self.__total_frames = len(tracks['players'])

        return self.__raw_report

    def save_report(self):
        if len(self.__raw_report) == 0:
            raise Exception("Raw Report is empty. Please generate the raw report before saving.")
        
        for entry in self.__raw_report:
            self.logger.info(f"Frame: {entry["frame"]} Player: {entry["player"]} Team: {entry["team"]} Has Ball")

        self.logger.info(f"Input File: {self.input_file_name}")
        self.logger.info(f"Total Frames: {self.__total_frames}")