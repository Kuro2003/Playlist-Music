This code is a simple video player and playlist manager using Pygame.

Classes
Video
The Video class is used to store the title, link, and seen status of a video. The Video class also has an open() method that opens the video's link in the default web browser and sets the seen status to True.

Playlist
The Playlist class is used to store the name, description, rating, and videos of a playlist.

TextButton
The TextButton class is used to create buttons with text and position them. It has methods to check if the mouse is on the text button, and to draw the text button.

Background
The Background class is used to create and position a background image. It inherits from Pygame's Sprite class.

Functions
read_video_from_txt
This function reads a single video from a text file and returns it as a Video object.

read_videos_from_txt
This function reads multiple videos from a text file and returns them as a list of Video objects.

read_playlist_from_txt
This function reads a single playlist from a text file and returns it as a Playlist object.

Usage
To use this code, run the main.py script. You will need to have Pygame installed. The code reads playlist data from a text file and creates Playlist objects. You can then select a playlist from the main menu and view its videos. Clicking on a video will open its link in the default web browser.

Note: The text file containing the playlist data should have the following format:

[Number of Playlists]
[Playlist Name]
[Playlist Description]
[Playlist Rating]
[Number of Videos in Playlist]
[Video Title]
[Video Link]
...
