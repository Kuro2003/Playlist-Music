import pygame
import webbrowser
from random import randint
import os

class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link
		self.seen = False

	def open(self):
		webbrowser.open(self.link)
		self.seen = True

class Playlist:
	def __init__(self, name, description, rating, videos):
		self.name = name
		self.description = description
		self.rating = rating
		self.videos = videos

class TextButton:
	def __init__(self, text, position):
		self.text = text
		self.position = position

	def is_mouse_on_text(self):
		mouse_x,mouse_y = pygame.mouse.get_pos()
		if (mouse_x > self.position[0]) and (mouse_x < self.position[0] + self.text_box[2]) and (mouse_y > self.position[1]) and (mouse_y < self.position[1] + self.text_box[3]):
			return True
		else:
			return False			

	def draw(self):
		font = pygame.font.SysFont('sans',40)
		text_render = font.render(self.text,True,(0,0,0))
		self.text_box = text_render.get_rect()

		if self.is_mouse_on_text() == True:
			text_render = font.render(self.text,True,(0,0,255))
			pygame.draw.line(screen,(0,0,255),(self.position[0],self.position[1] + self.text_box[3]),(self.position[0] + self.text_box[2], self.position[1] + self.text_box[3]))
		else:
			text_render = font.render(self.text,True,(0,0,0))
		screen.blit(text_render,self.position)

class Background(pygame.sprite.Sprite):
	def __init__(self, image_file, location):
		pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location

def read_video_from_txt(file):
	title = file.readline()
	link = file.readline()
	video = Video(title, link)
	return video

def read_videos_from_txt(file):
	videos = []
	total = file.readline()		
	for i in range(int(total)):
		video = read_video_from_txt(file)
		videos.append(video)
	return videos

def read_playlist_from_txt(file):
	playlist_name = file.readline()
	playlist_description = file.readline()
	playlist_rating = file.readline()
	playlist_videos = read_videos_from_txt(file)
	playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
	return playlist

def read_playlists_from_txt():
	playlists = []
	with open(r"data.txt", "r") as file:
		total = file.readline()
		for i in range(int(total)):
			playlist = read_playlist_from_txt(file)
			playlists.append(playlist)
	return playlists

pygame.init()
screen = pygame.display.set_mode((800,450))
pygame.display.set_caption("Choi Nhac")
running = True
BLACK = (0,0,0)
clock = pygame.time.Clock()

BackGround = Background("image\de-thuong.jpg", [0,0])

prompt = 0
BackGround1 = Background(r'image\dep.jpg', [0,0])
BackGround2 = Background(r'image\Anh-anime.jpg', [0,0])
BackGround3 = Background(r'image\Anh-Galaxy.jpg', [0,0])
BackGround4 = Background(r'image\Nhung-hinh-anh.jpg',[0,0])
BackGround5 = Background(r'image\hinh-nen.jpg', [0,0])


#Load data

playlists = read_playlists_from_txt()

playlists_btn_list = []
margins = 70
for i in range(len(playlists)):
	playlist_btn = TextButton(playlists[i].name.rstrip(), (50,50 + margins *i))
	playlists_btn_list.append(playlist_btn)

videos_btn_list = []
playlist_choice = None

while running:
	clock.tick(60)
	screen.fill((255,255,255))
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
							video_btn = TextButton(str(j+1) + "." + playlists[i].videos[j].title.rstrip(),(350,50 + margins * j))
							videos_btn_list.append(video_btn)
				if playlist_choice +1 == 1:
					BackGround =BackGround1
				elif playlist_choice+1 == 2:
					BackGround =BackGround2
				elif playlist_choice+1 == 3:
					BackGround =BackGround3
				elif playlist_choice+1 == 4:
					BackGround =BackGround4
					screen.blit(BackGround4.image, BackGround.rect)
				elif playlist_choice+1 == 5:
					BackGround =BackGround5
				if playlist_choice != None:
					for i in range(len(videos_btn_list)):
						if videos_btn_list[i].is_mouse_on_text():
							playlists[playlist_choice].videos[i].open()

		if event.type == pygame.QUIT:
			running = False

	pygame.display.flip()

pygame.quit()