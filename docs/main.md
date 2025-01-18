# Documentation for 

main.py



## Table of Contents
1. [Introduction and Goals](#1-introduction-and-goals)
2. Constraints
3. [Context and Scope](#3-context-and-scope)
4. [Solution Strategy](#4-solution-strategy)
5. [Building Block View](#5-building-block-view)
   - [Overall System Architecture](#51-overall-system-architecture)
   - [Detailed Component Descriptions](#52-detailed-component-descriptions)
     - [Video Reader](#521-video-reader)
     - Tracker
     - [Camera Movement Estimator](#523-camera-movement-estimator)
     - [View Transformer](#524-view-transformer)
     - [Speed and Distance Estimator](#525-speed-and-distance-estimator)
     - [Team Assigner](#526-team-assigner)
     - [Player Ball Assigner](#527-player-ball-assigner)
     - [Video Annotator](#528-video-annotator)
     - [Video Saver](#529-video-saver)
   - [Architecture Diagram](#53-architecture-diagram)
6. [Runtime View](#6-runtime-view)
7. [Deployment View](#7-deployment-view)
8. [Cross-cutting Concepts](#8-cross-cutting-concepts)
9. [Design Decisions](#9-design-decisions)
10. [Quality Requirements](#10-quality-requirements)
11. [Risks and Technical Debt](#11-risks-and-technical-debt)
12. Glossary

## 1. Introduction and Goals
This project processes a video file to track objects, estimate camera movement, transform views, interpolate ball positions, estimate speed and distance, assign player teams, and determine ball possession. The processed video is then saved with annotations. The goal is to provide a comprehensive analysis of sports videos using computer vision and AI models.

## 2. Constraints
- The project relies on pre-trained AI models for object tracking and other estimations.
- The input video file must be in a compatible format (e.g., MP4).
- The project uses specific stub files for reading precomputed data.

## 3. Context and Scope
This project is designed for analyzing sports videos, particularly for tracking players and the ball, estimating their movements, and annotating the video with this information. It is intended for use by sports analysts, coaches, and enthusiasts.

## 4. Solution Strategy
The solution involves reading a video file, processing it through various components to extract and analyze information, and then saving the annotated video. The processing includes object tracking, camera movement estimation, view transformation, speed and distance estimation, team assignment, and ball possession assignment.

## 5. Building Block View

### 5.1. Overall System Architecture
The system is composed of several components that work together to process and analyze the video. The main components are:
- **Video Reader**: Reads the input video file.
- **Tracker**: Tracks objects (players and ball) in the video.
- **Camera Movement Estimator**: Estimates and adjusts for camera movement.
- **View Transformer**: Transforms the view to a standard perspective.
- **Speed and Distance Estimator**: Estimates the speed and distance of tracked objects.
- **Team Assigner**: Assigns teams to players.
- **Player Ball Assigner**: Determines which player has possession of the ball.
- **Video Annotator**: Draws annotations on the video frames.
- **Video Saver**: Saves the annotated video to a file.

### 5.2. Detailed Component Descriptions

#### 5.2.1. Video Reader
- **Function**: `read_video`
- **Description**: Reads the input video file and returns the video frames.

#### 5.2.2. Tracker
- **Class**: `Tracker`
- **Model**: Pre-trained model (`models/best.pt`)
- **Functions**:
  - `get_object_tracks`: Retrieves object tracks from the video frames.
  - `add_position_to_tracks`: Adds positions to the tracks.
  - `interpolate_ball_positions`: Interpolates ball positions in the tracks.
  - `draw_annotations`: Draws object tracks on the video frames.

#### 5.2.3. Camera Movement Estimator
- **Class**: `CameraMovementEstimator`
- **Functions**:
  - `get_camera_movement`: Estimates camera movement for each frame.
  - `add_adjust_positions_to_tracks`: Adjusts track positions based on camera movement.
  - `draw_camera_movement`: Draws camera movement annotations on the video frames.

#### 5.2.4. View Transformer
- **Class**: `ViewTransformer`
- **Functions**:
  - `add_transformed_position_to_tracks`: Transforms and adds positions to the tracks.

#### 5.2.5. Speed and Distance Estimator
- **Class**: `SpeedAndDistance_Estimator`
- **Functions**:
  - `add_speed_and_distance_to_tracks`: Adds speed and distance information to the tracks.
  - `draw_speed_and_distance`: Draws speed and distance annotations on the video frames.

#### 5.2.6. Team Assigner
- **Class**: `TeamAssigner`
- **Functions**:
  - `assign_team_color`: Assigns team colors to players.
  - `get_player_team`: Determines the team of a player based on their position.

#### 5.2.7. Player Ball Assigner
- **Class**: `PlayerBallAssigner`
- **Functions**:
  - `assign_ball_to_player`: Determines which player has possession of the ball.

#### 5.2.8. Video Annotator
- **Functions**:
  - `draw_annotations`: Draws object tracks on the video frames.
  - `draw_camera_movement`: Draws camera movement annotations on the video frames.
  - `draw_speed_and_distance`: Draws speed and distance annotations on the video frames.

#### 5.2.9. Video Saver
- **Function**: `save_video`
- **Description**: Saves the annotated video to a file.

### 5.3. Workflow Diagram

![workflow diagram](img/processing_pipeline.png)

## 6. Runtime View
The main function orchestrates the processing pipeline, calling each component in sequence to process the video and generate the annotated output.

## 7. Deployment View
The project is intended to be run as a standalone script on a machine with the necessary dependencies installed. The output is an annotated video file saved to disk.

## 8. Cross-cutting Concepts
- **AI Models**: Pre-trained models are used for object tracking and other estimations.
- **Stub Files**: Used for reading precomputed data to speed up processing.
- **Annotations**: Visual annotations are added to the video frames to highlight tracked objects, camera movement, speed, and distance.

## 9. Design Decisions
- Use of pre-trained models for object tracking to leverage existing AI capabilities.
- Use of stub files to allow for faster processing during development and testing.
- Modular design to separate different aspects of video processing and analysis.

## 10. Quality Requirements
- **Performance**: Efficient processing of video frames to handle large video files.
- **Accuracy**: Accurate tracking and estimation of object positions, camera movement, speed, and distance.
- **Usability**: Clear and informative annotations on the video frames.

## 11. Risks and Technical Debt
- Dependency on pre-trained models which may need updates or retraining for different scenarios.
- Potential performance bottlenecks with large video files or high-resolution frames.

## 12. Glossary
- **Track**: The path or trajectory of an object (player or ball) in the video.
- **Stub File**: A file containing precomputed data used to speed up processing.
- **Annotation**: Visual markers added to the video frames to highlight important information.