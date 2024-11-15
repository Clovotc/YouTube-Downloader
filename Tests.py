# These tests on the files of the project
# Maison Kasprick - 11/14/2024
# Version 1.0

# Imports
import YouTube


# Link_Validation Test 1
def valid_style1() -> bool:
    """Link_validation function test using the style 'https://youtu.be/'

    Returns:
        bool: Returns True if the link is good
              Returns False if the link is bad or an exception occured
    """
    good_link = 'https://youtu.be/'

    result = YouTube.link_validation(good_link)
        
    # Link is good (What we want)
    if result is True:
        print(u'\u2713')
        return True 
    
    # Link is bad (Not What we want)
    print('X')
    return False
    
    
# Link_Validation Test 2
def valid_style2() -> bool:
    """Link_validation function test using the style 'https://www.youtube.com/'

    Returns:
        bool: Returns True if the link is good
              Returns False if the link is bad or an exception occured
    """
    good_link = 'https://www.youtube.com/'
    
    result = YouTube.link_validation(good_link)
        
    # Link is good (What we want)
    if result is True:
        print(u'\u2713')
        return True
    
    # Link is bad (Not what we want)
    print('X')
    return False
    
    
# Link_Validation Test 3
def valid_bad() -> bool:
    """Link_validation function test on a link that is not a YouTube link

    Returns:
        bool: Returns True if the link is bad
              Returns False if the link is good or an exception occured
    """
    bad_link = 'https://yout.be/'
    
    result = YouTube.link_validation(bad_link)
        
    # Link is bad (What we want)
    if result is False:
        print(u'\u2713')
        return True
        
    # Link is good (Not what we want)
    print('X')
    return False


# Link_Validation Test 4
def valid_error() -> bool:
    """Link_validation function test on a link that is not a link

    Returns:
        bool: Returns True if the link is not an actual link (An exception occured)
              Returns False if the link is good
    """
    error_link = 'https:youtu.be'

    result = YouTube.link_validation(error_link)
        
    # If there is a successful exception error trigger
    if result is False:
        print(u'\u2713')
        return True
        
    # If no error occured (Not what we want)
    print('X')
    return False
    
    
# Download_MP3 test 1
def mp3_good() -> bool:
    """Download_MP3 function test to see if it will successfully download a good YouTube video

    Returns:
        bool: Returns True if it was successfully downloaded
              Returns False if it was not downloaded or an exception occured
    """
    good_video = 'https://youtu.be/enYdAxVcNZA'
    
    result = YouTube.download_mp3(good_video)
        
    # Link was downloaded (What we want)
    if result == 'Successfully Downloaded MP3 File':
        print(u'\u2713')
        return True
        
    # Link was bad and not downloaded (Not what we want)
    print('X')
    return False
    
    
# Download_MP3 test 2
def mp3_bad() -> bool:
    """Download_MP3 function test to see if a bad youtube link will download

    Returns:
        bool: Returns True if it is a bad youtube link
              Returns False if it is a good youtube link or an exception occured
    """
    bad_video = 'https://yo.be/mCSv5PL53x4'
    
    result = YouTube.download_mp3(bad_video)
        
    # Link is bad and wasn't downloaded (What we want)
    if result == '"https://yo.be/mCSv5PL53x4" is not a valid YouTube link':
        print(u'\u2713')
        return True
        
    # Link was good and was downloaded (Not what we want)
    print('X')
    return False
    
 
# Download_MP3 test 3
def mp3_error() -> bool:
    """Download_MP3 function test to see if it can catch errors occuring in function

    Returns:
        bool: Returns True if error was successfully caught
              Returns False if youtube link was downloaded or a bad link
    """
    error_video = 'https://www.youtube.com/rgaerdgr'

    result = YouTube.download_mp3(error_video)

    # If there is a successful error trigger (What we want)
    if result == f'HTTP Error from {error_video}' or result == 'Unkown HTTP error' or result == f'Error downloading {error_video}' or result == 'Unkown error':
        print(u'\u2713')
        return True
        
    # Link was a valid link and caused no exception (Not what we want)
    print('X')
    return False
    

# Download_MP4 test 1
def mp4_good() -> bool:
    """Download_MP4 function test to see if it will successfully download a good YouTube video

    Returns:
        bool: Returns True if it was successfully downloaded
              Returns False if it was not downloaded or an exception occured
    """
    good_video = 'https://youtu.be/enYdAxVcNZA'
    
    result = YouTube.download_mp4(good_video)
        
    # Link was downloaded (What we want)
    if result == 'Successfully Downloaded MP4 File':
        print(u'\u2713')
        return True
    
    # Link was bad and not downloaded (Not What we want)
    print('X')
    return False
    
   
# Download_MP4 test 2 
def mp4_bad() -> bool:
    """Download_MP4 function test to see if a bad youtube link will download

    Returns:
        bool: Returns True if it is a bad youtube link
              Returns False if it is a good youtube link or an exception occured
    """
    bad_video = 'https://yo.be/enYdAxVcNZA'
    
    result = YouTube.download_mp4(bad_video)
        
    # Link is bad and was not downloaded (What we want)
    if result == '"https://yo.be/enYdAxVcNZA" is not a valid YouTube link':
        print(u'\u2713')
        return True
    
    # Link was good and was downloaded (Not what we want)
    print('X')
    return False


# Download_MP4 test 3
def mp4_error() -> bool:
    """Download_MP4 function test to see if it can catch errors occuring in function

    Returns:
        bool: Returns True if error was successfully caught
              Returns False if youtube link was downloaded or a bad link
    """
    error_video = 'https://www.youtube.com/ragargarth'
    
    result = YouTube.download_mp4(error_video)
        
    # If there is a successful error trigger (What we want)
    if result == f'HTTP Error from {error_video}' or result == 'Unkown HTTP error' or result == f'Error downloading {error_video}' or result == 'Unkown error':
        print(u'\u2713')
        return True
            
    # Link was a valid link and caused no exception (Not what we want)
    print('X')
    return False
    

# Runs all test functions
if __name__ == '__main__':
    print('All tests should return true')
    print('Style 1 youtube link: ' + str(valid_style1()))
    print('Style 2 youtube link: ' + str(valid_style2()))
    print('Bad youtube link: ' + str(valid_bad()))
    print('Error youtube link: ' + str(valid_error()))
    print('MP3 good youtube video: ' + str(mp3_good()))
    print('MP3 bad youtube video: ' + str(mp3_bad()))
    print('MP3 error youtube video: ' + str(mp3_error()))
    print('MP4 good youtube video: ' + str(mp4_good()))
    print('MP4 bad youtube video: ' + str(mp4_bad()))
    print('MP4 error youtube video: ' + str(mp4_error()))
