# This is the first file for creating a youtube downloader using yt_dlp
# Maison Kasprick - 11/14/2024
# Version 1.0

# Imports
from urllib.error import HTTPError
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError


# Tests link provided to see if it is a valid YouTube link
def link_validation(test_link: str) -> bool:
    """This function is used to test a link provided that it is indeed a YouTube link.
        The two starting formats for a valid YouTube link are "https://youtu.be/" and "https://www.youtube.com/"

    Args:
        test_link (str): Provided link

    Returns:
        bool: Returns True if the link provided is a valid YouTube link
              Returns False if the link is not a valid YouTube link or an expcetion occured when splitting the link
    """
    
    # Possible YouTube links
    comparative_video = 'https://youtu.be/'
    comparative_video_url = 'https://www.youtube.com/'

    try:
        # First removes any spaces in the link then 
        # Splits test link by '/'
        link_split = test_link.split()
        link_split = test_link.split('/')
        
        # Attempts to prove the link is a valid YouTube link by
        # Building the link back together to test if it is a normal YouTube video
        comparative_video_link = f'{link_split[0]}//{link_split[2]}/'
        if comparative_video == comparative_video_link or comparative_video_url == comparative_video_link:
            return True
        
        # If the provided link is not a valid youtube link
        return False
        
    # If there is an error when trying to split the link
    except ValueError:
        return False
        
    except Exception:
        return False


# Downloads YouTube video
def download_mp3(youtube_link: str, location: str = None) -> str:
    """This is the function to download your video or playlist as all mp3 files

    Args:
        youtube_link (str): Provided YouTube link
        location (str): Download path. Defaults to this folder

    Returns:
        str: Returns the string of either a successful download or unsuccessful download 
    """
    
    # Test to see if YouTube link provided is valid
    if link_validation(youtube_link) is False:
        return(f'"{youtube_link}" is not a valid YouTube link')
    
    # If nothing was inputted for location it will default to this folder
    if location is None:
        location = ''
        
    # Download path
    download_path = location + '/%(title)s.%(ext)s'
    
    # Attempts to download YouTube video if valid
    try:
        # Settings for the download
        download_options = {
            # Download location blank is to this folder or custom folder
            'outtmpl': download_path,
            # Post-process to convert to MP3
            'postprocessors': [{ 
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                # '0' means best quality, auto-determined by source
                'preferredquality': '0',
            }],
        }
        # Iterates through the playlist or just downloads the one video
        with YoutubeDL(download_options) as youtube_download:
            youtube_download.download([youtube_link])
        
        # After running through all the downloads 
        return('Successfully Downloaded MP3 File')
        
    # Informs the user of any errors has occured when downloading
    except HTTPError as he:
        if he.code == 404:
            return(f'HTTP Error from {youtube_link}')
        
        return('Unkown HTTP error')
    
    except DownloadError:
        return(f'Error downloading {youtube_link}')
    
    except Exception:
        return('Unkown error')
        
        
# Downloads YouTube video
def download_mp4(youtube_link: str, location: str = None) -> str:
    """This is the function to download your video or playlist as all mp4 files
    
    Args:
        youtube_link (str): Provided YouTube link
        location (str): Download path. Defaults to this folder

    Returns:
        str: Returns the string of either a successful download or unsuccessful download 
    """
    
    # Test to see if YouTube link provided is valid
    if link_validation(youtube_link) is False:
        return(f'"{youtube_link}" is not a valid YouTube link')
    
    # If nothing was inputted for location it will default to this folder
    if location is None:
        location = ''
        
    # Download path
    download_path = location + '/%(title)s.%(ext)s'
    
    # Attempts to download YouTube video if valid
    try:
        # Settings for the download
        download_options = {
            # Download location blank is to this folder or custom folder
            'outtmpl': download_path,
            # Try to download at 1080p quality otherwise download best quality
            'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]'
        }
        
        # Iterates through the playlist or just downloads the one video
        with YoutubeDL(download_options) as youtube_download:
            youtube_download.download([youtube_link])
            
        # After running through all the downloads 
        return('Successfully Downloaded MP4 File')
        
    # Informs the user of any errors has occured when downloading
    except HTTPError as he:
        if he.code == 404:
            return(f'HTTP Error from {youtube_link}')
        
        return('Unkown HTTP error')
    
    except DownloadError:
        return(f'Error downloading {youtube_link}')
    
    except Exception:
        return('Unkown error')
        
        
# Converts YouTube video to what the user wants
def conversion_choice(user_choice: str, youtube_link: str) -> bool:
    """This function is mainly used in execution of this file by itself.
        The two current choices are 1 for mp3 and 2 for mp4

    Args:
        user_choice (str): A numeric string between 1 and 2
        youtube_link (str): Provided link

    Returns:
        bool: Returns True if user did not enter a valid choice option
              Returns False if user did enter a valid choice and executes the corrisponding function
    """
    
    # Check if user selected to download mp3
    if user_choice == '1':
        print(download_mp3(youtube_link))
        return False
    
    # Check if user selected to download mp4
    if user_choice == '2':
        print(download_mp4(youtube_link))
        return False

    # User did not select a either a playlist or a single video option
    print('Not a valid choice \n')
    return True
    
    
# This is what will run if this file is selected
if __name__ == '__main__':
    # Gets YouTube link from user and converts to whatever the user wants
    print('Note - if you are wanting to download a playlist you will need to copy the search bar url')
    link = input('Paste YouTube link: ')

    # Starts a while loop until user enters correct inputs
    continue_loop = True

    while continue_loop:
        conversion = input('What would you like to do with the link? \n'
                           'For a mp3 video enter 1 \n'
                           'For a mp4 video enter 2 \n'
                           'To Quit enter Q \n'
                           'Choice: ')

        # Exits the while loop
        if conversion in ['q','Q']:
            continue_loop = False
            print('Quiting Program')
            
        # Executes the users choice which will set the new boolean for the while loop
        else:
            continue_loop = conversion_choice(conversion, link)
