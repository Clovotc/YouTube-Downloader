# This is the combined code of both GUI and YouTUbe files
# Maison Kasprick - 11/14/2024
# Version 1.0

# Imports
from tkinter.filedialog import askdirectory
from yt_dlp import YoutubeDL
from yt_dlp import DownloadError
from requests import HTTPError
import tkinter
import customtkinter
import YouTube
import os

# Saved download location
download_folder = ''


# Get all files from folder
def read_folder() -> None:
    """This function is used to grab all files from selected folder"""  
    
    # Grabs global download_folder variable
    global download_folder
    
    # Checks download_folder for empty string
    if download_folder == '':
        return
    
    # Save string of all files in folder
    all_files = ''
    
    # Count the number of files in the folder
    count = 1
    
    # Reads all files from selected folder
    for file in os.listdir(download_folder):
        # Splits title and type
        title_file = file.split('.', 1)
        # Grabs only title
        all_files += f'{count}. {title_file[0]}\n'
        # Increases the number of files count by 1
        count += 1
        
    # Prints all files found in selected folder
    files_label.configure(text = all_files)


# Select download location
def select_folder() -> None:
    """Select folder function for the user to have a download location"""
    
    # Gets the folder location from user and sets it to globabl variable
    global download_folder 
    download_folder = askdirectory(title = 'Select a folder to download to')

    # Display to the user what download folder they have selected
    location_label.configure(text = f'Downloads set to {download_folder}')
    
    # Gets all file names from selected folder
    read_folder()


# Grab info of YouTube video
def video_info(youtube_link: str) -> None:
    """This is a function to get the information from the YouTube video 

    Args:
        youtube_link (str): Provided youtube link
    """
    
    # Test to see if YouTube link provided is valid
    if YouTube.link_validation(youtube_link) is False:
        finish_label.configure(text = f'"{youtube_link}" is not a valid YouTube link')
        return
    
    # Attempts to grab information about the YouTube video
    try:
        # Settings for download
        download_options = {}
            
        # Grabs title of video
        with YoutubeDL(download_options) as youtube_download:
            info = youtube_download.extract_info(youtube_link, download = False)
        
        # Informs user of video that is downloaded
        video_label.configure(text = f"Title: {info['title']}")
        
    # Informs the user of any errors has occured when downloading
    except HTTPError as he:
        if he.code == 404:
            finish_label.configure(text = f'HTTP Error from {youtube_link}')
        
        finish_label.configure(text = 'Unkown HTTP error')
    
    except DownloadError:
        finish_label.configure(text = 'Error downloading {youtube_link}')
    
    except Exception:
        finish_label.configure(text = 'Unkown error')


# Downloads YouTube video
def mp3() -> None:
    """This is the function used in the mp3 button call"""
    
    # Get link from label box
    youtube_link = link.get()
    
    # Get global download_folder
    global download_folder
    location = download_folder
    
    # Makes sure there is a link in the text box
    if youtube_link == '':
        return finish_label.configure(text = 'Please input a youtube link')
    
    # Clears the labels for the user
    finish_label.configure(text = '')
    video_label.configure(text = '')

    # Informs the user that it is attempting the download of the link
    finish_label.configure(text = 'Attempting to download link')
        
    # Runs the download_mp3 function from YouTube
    return_str = YouTube.download_mp3(youtube_link, location)
    finish_label.configure(text = return_str)

    # Gets information of video
    video_info(youtube_link)
    
    # Updates download folder display
    read_folder()
    
        
# Downloads YouTube video
def mp4() -> None:
    """This is the function used in the mp4 button call"""
    
    # Get link from label box
    youtube_link = link.get()
    
    # Get global download_folder
    global download_folder
    location = download_folder 
    
    # Makes sure there is a link in the text box
    if youtube_link == '':
        return finish_label.configure(text = 'Please input a youtube link')
    
    # Clears the labels for the user
    finish_label.configure(text = '')
    video_label.configure(text = '')
    
    # Informs the user that it is attempting the download of the link
    finish_label.configure(text = 'Attempting to download link')
    
    # Runs the download_mp4 function from YouTube
    return_str = YouTube.download_mp4(youtube_link, location)
    finish_label.configure(text = return_str)
    
    # Gets information of video
    video_info(youtube_link)
    
    # Updates download folder display
    read_folder()


# Creates a pop up window of READ ME file
def read_me() -> None:
    """This function is used in the help button call"""
    
    # System Settings
    customtkinter.set_appearance_mode('system')
    customtkinter.set_default_color_theme('dark-blue')
    
    # READ ME frame
    read = customtkinter.CTk()
    read.geometry('800x300')
    read.title('HELP')
    
    # Open READ ME file
    with open('READ ME.txt', 'r') as file:
        read_me = file.readlines()
    
    # Converts the read_me list to a string
    info = ' '.join(read_me)
    
    # Pastes READ ME files content into label
    info_label = customtkinter.CTkLabel(read, width = 400, height = 400, text = info, justify = tkinter.LEFT)
    info_label.pack(fill = tkinter.BOTH)
    
    # Run READ ME
    read.mainloop()


# Clears text from GUI
def clear() -> None:
    """Clears all display text in the gui"""
    
    # Creats empty string and replaces the input string
    empty_link = tkinter.StringVar()
    link.configure(textvariable = empty_link)
    
    # Clears label text for user
    finish_label.configure(text = '')
    video_label.configure(text = '')


# Clears download location and path
def clear_download() -> None:
    """Clears the set download path, and all labels"""
    
    # Gets global download location and clears location
    global download_folder
    download_folder = ''
    
    # Clear labels
    location_label.configure(text = 'No download location selected')
    files_label.configure(text = '')


# GUI creation code
if __name__ == '__main__':
    # System Settings
    customtkinter.set_appearance_mode('system')
    customtkinter.set_default_color_theme('dark-blue')

    # GUI frame
    app = customtkinter.CTk()
    app.geometry('800x500')
    app.title('YouTube Downloader')
    
    # Frames
    downloads = customtkinter.CTkFrame(app, width = 250, height = 200)
    downloads.pack(padx = 10, pady =10, side = tkinter.RIGHT)
    buttons = customtkinter.CTkFrame(app, width = 250, height = 200)
    buttons.pack(padx =10, pady = 10, side = tkinter.LEFT)

    # UI Elements
    title = customtkinter.CTkLabel(buttons, text = 'Insert a YouTube video link')
    title.pack(padx = 10, pady = 10)

    # Link input
    input_link = tkinter.StringVar()
    link = customtkinter.CTkEntry(buttons, width = 350, height = 40, textvariable = input_link)
    link.pack(padx = 10, pady = 10)

    # Finished Downloading
    finish_label = customtkinter.CTkLabel(buttons, text = '')
    finish_label.pack()
    
    # YouTube video downloaded
    video_label = customtkinter.CTkLabel(buttons, text = '')
    video_label.pack()

    # Download buttons
    button_mp3 = customtkinter.CTkButton(buttons, text = 'Download MP3', command = mp3)
    button_mp3.pack(padx = 10, pady = 10)
    button_mp4 = customtkinter.CTkButton(buttons, text = 'Download MP4', command = mp4)
    button_mp4.pack(padx = 10, pady = 10)
    
    # Clear button
    button_clear = customtkinter.CTkButton(buttons, text = 'Clear Download', command = clear)
    button_clear.pack(padx = 10, pady = 10)

    # Help button
    button_help = customtkinter.CTkButton(buttons, text = 'Help', command = read_me)
    button_help.pack(padx = 10, pady = 10)
    
    # Download Location
    button_location = customtkinter.CTkButton(buttons, text = 'Set Download Location', command = select_folder)
    button_location.pack(padx = 10, pady = 10)
    
    # Clear download location
    button_download_clear = customtkinter.CTkButton(buttons, text = 'Clear Set Location', command = clear_download)
    button_download_clear.pack(padx = 10, pady = 10)
    
    # Display location
    location_label = customtkinter.CTkLabel(downloads, text = 'No download location selected')
    location_label.pack(padx = 10, pady = 10)
    
    # Files in folder
    files_label = customtkinter.CTkLabel(downloads, text = '', justify = tkinter.LEFT)
    files_label.pack(padx = 10, pady = 10)

    # Run GUI
    app.mainloop()
