import instaloader
from instaloader import Profile, Post

# Define the Instagram ID of the profile you want to scrape data from 
profile_id = " "

# Create an instance of the Instaloader class
loader = instaloader.Instaloader()

# Load the profile using its ID
profile = Profile.from_username(loader.context, profile_id)

# Get the profile's username, full name, and number of followers
username = profile.username
full_name = profile.full_name
followers = profile.followers

# Print the profile's information
print("Username:", username)
print("Full name:", full_name)
print("Followers:", followers)

# Get the profile's posts
posts = profile.get_posts()

# Iterate over the posts and print their captions and URLs
for post in posts:
    caption = post.caption
    url = post.url
    print("Caption:", caption)
    print("URL:", url)

