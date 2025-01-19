import sys 
sys.path.append('../')
import nanoid
import logging
import os

class Report():
    def __init__(self, input_file_name):
        self.report = []
        self.logger = logging.getLogger(__name__)
        self.input_file_name = input_file_name.replace("input_videos/","")
        logging.basicConfig(filename=f"reports/{self.input_file_name + nanoid.generate(size=8)}.log", level=logging.INFO, format='%(message)s')


    def generate_report(self,tracks):
        for frame_num, player_track in enumerate(tracks['players']):
            for player_id, track in player_track.items():
                if('has_ball' in track):
                    self.logger.info(f"Frame: {frame_num} Player: {player_id} Team: {track['team']} Has Ball")
        self.logger.info(f"Input File: {self.input_file_name}")
        self.logger.info(f"Total Frames: {len(tracks['players'])}")