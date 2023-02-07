# Importing necessary modules
import pygame
import webbrowser
from random import randint
import os

# Video class to store the video's title, link and its seen status
class Video:
    def __init__(self, title, link):
        self.title = title
        self.link = link
        self.seen = False

    # Method to open the video's link
    def open(self):
        webbrowser.open(self.link)
        self.seen = True

# Playlist class to store the playlist's name, description, rating and videos
class Playlist:
    def __init__(self, name, description, rating, videos):
        self.name = name
        self.description = description
        self.rating = rating
        self.videos = videos

# TextButton class for creating buttons with text and positioning them
class TextButton:
    def __init__(self, text, position):
        self.text = text
        self.position = position

    # Method to check if the mouse is on the text button
    def is_mouse_on_text(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if (mouse_x > self.position[0]) and (mouse_x < self.position[0] + self.text_box[2]) and (mouse_y > self.position[1]) and (mouse_y < self.position[1] + self.text_box[3]):
            return True
        else:
            return False

    # Method to draw the text button
    def draw(self):
        font = pygame.font.SysFont('sans', 40)
        text_render = font.render(self.text, True, (0, 0, 0))
        self.text_box = text_render.get_rect()

        # Change the color of text when the mouse is on it
        if self.is_mouse_on_text() == True:
            text_render = font.render(self.text, True, (0, 0, 255))
            pygame.draw.line(screen, (0, 0, 255), (self.position[0], self.position[1] + self.text_box[3]), (
                self.position[0] + self.text_box[2], self.position[1] + self.text_box[3]))
        else:
            text_render = font.render(self.text, True, (0, 0, 0))
        screen.blit(text_render, self.position)

# Background class for creating and positioning a background image
# Inherits from Pygame's Sprite class
class Background(pygame.sprite.Sprite):
    # Initialize the class
    def __init__(self, image_file, location):
        # Call the parent class's initializer
        pygame.sprite.Sprite.__init__(self)
        # Load image from file and assign it to self.image
        self.image = pygame.image.load(image_file)
        # Get the rectangle surrounding the image and assign it to self.rect
        self.rect = self.image.get_rect()
        # Set the top-left corner of the image to the specified location
        self.rect.left, self.rect.top = location

# Reads a single video from a text file and returns it as a Video object
def read_video_from_txt(file):
    # Read the title of the video from the first line of the file
    title = file.readline()
    # Read the link of the video from the second line of the file
    link = file.readline()
    # Create a Video object with the title and link
    video = Video(title, link)
    # Return the Video object
    return video

# Reads multiple videos from a text file and returns them as a list of Video objects
def read_videos_from_txt(file):
    # Create an empty list to store the Video objects
    videos = []
    # Read the total number of videos from the first line of the file
    total = file.readline()
    # Loop through the number of videos and read each video
    for i in range(int(total)):
        video = read_video_from_txt(file)
        videos.append(video)
    # Return the list of Video objects
    return videos

# Reads a single playlist from a text file and returns it as a Playlist object
def read_playlist_from_txt(file):
    # Read the name of the playlist from the first line of the file
    playlist_name = file.readline()
    # Read the description of the playlist from the second line of the file
    playlist_description = file.readline()
    # Read the rating of the playlist from the third line of the file
    playlist_rating = file.readline()
    # Read the videos of the playlist
    playlist_videos = read_videos_from_txt(file)
    # Create a Playlist object with the playlist name, description, rating, and videos
    playlist = Playlist(playlist_name, playlist_description,
                        playlist_rating, playlist_videos)
    # Return the Playlist object
    return playlist

# Reads multiple playlists from a text file and returns them as a list of Playlist objects
def read_playlists_from_txt():
    # Create an empty list to store the Playlist objects
    playlists = []
    # Open the text file for reading
    with open(r"data.txt", "r") as file:
        # Read the total number of playlists from the first line of the file
        total = file.readline()
        # Loop through the number of playlists and read each playlist
        for i in range(int(total)):
            playlist = read_playlist_from_txt(file)
            playlists.append(playlist)
    # Return the list of Playlist objects
    return playlists

pygame.init()
screen = pygame.display.set_mode((800, 450))
pygame.display.set_caption("Choi Nhac")
running = True
BLACK = (0, 0, 0)
clock = pygame.time.Clock()

prompt = 0
BackGround = Background(r'image\background.jpg', [0, 0])
BackGround1 = Background(r'image\dep.jpg', [0, 0])
BackGround2 = Background(r'image\Anh-anime.jpg', [0, 0])
BackGround3 = Background(r'image\Anh-Galaxy.jpg', [0, 0])
BackGround4 = Background(r'image\Nhung-hinh-anh.jpg', [0, 0])
BackGround5 = Background(r'image\hinh-nen.jpg', [0, 0])

playlists = read_playlists_from_txt()

playlists_btn_list = []
margins = 70

for i in range(len(playlists)):
    playlist_btn = TextButton(
        playlists[i].name.rstrip(), (50, 50 + margins * i))
    playlists_btn_list.append(playlist_btn)

videos_btn_list = []
playlist_choice = None

while running:
    clock.tick(60)
    screen.fill((255, 255, 255))
    screen.blit(BackGround.image, BackGround.rect)

    for playlist_button in playlists_btn_list:
        playlist_button.draw()

    for video_button in videos_btn_list:
        video_button.draw()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(len(playlists_btn_list)):
                    if playlists_btn_list[i].is_mouse_on_text():
                        playlist_choice = i

                        videos_btn_list = []
                        for j in range(len(playlists[i].videos)):
                            video_btn = TextButton(
                                str(j+1) + "." + playlists[i].videos[j].title.rstrip(), (350, 50 + margins * j))
                            videos_btn_list.append(video_btn)

                if playlist_choice + 1 == 1:
                    BackGround = BackGround1
                elif playlist_choice + 1 == 2:
                    BackGround = BackGround2
                elif playlist_choice + 1 == 3:
                    BackGround = BackGround3
                elif playlist_choice + 1 == 4:
                    BackGround = BackGround4
                    screen.blit(BackGround4.image, BackGround.rect)
                elif playlist_choice + 1 == 5:
                    BackGround = BackGround5
                if playlist_choice != None:
                    for i in range(len(videos_btn_list)):
                        if videos_btn_list[i].is_mouse_on_text():
                            playlists[playlist_choice].videos[i].open()

        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
