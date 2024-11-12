import json
from collections import defaultdict

class UserProfile:
    def __init__(self, user_id):
        self.user_id = user_id
        self.posts = []  # List of posts by the user
        self.flagged_posts = []  # List of flagged posts
        self.connections = set()  # Set of other users that this user is connected to
        self.suspicious_behavior_score = 0  # Score based on behavior analysis

    def add_post(self, post):
        """Add a post to the user's profile."""
        self.posts.append(post)

    def flag_post(self, post):
        """Flag a post as suspicious."""
        self.flagged_posts.append(post)

    def add_connection(self, other_user):
        """Add a connection (user-to-user interaction)."""
        self.connections.add(other_user)

    def update_suspicious_score(self, score):
        """Update the suspicious behavior score based on flagged posts and behavior."""
        self.suspicious_behavior_score += score

    def get_profile_data(self):
        """Return profile data in a readable format."""
        return {
            'user_id': self.user_id,
            'posts': self.posts,
            'flagged_posts': self.flagged_posts,
            'connections': list(self.connections),
            'suspicious_behavior_score': self.suspicious_behavior_score
        }

class UserProfileManager:
    def __init__(self):
        self.profiles = {}

    def get_or_create_profile(self, user_id):
        """Get existing profile or create a new one."""
        if user_id not in self.profiles:
            self.profiles[user_id] = UserProfile(user_id)
        return self.profiles[user_id]

    def update_user_activity(self, user_id, post, is_flagged=False, connection=None):
        """Update user activity with posts, flagged content, and connections."""
        profile = self.get_or_create_profile(user_id)
        profile.add_post(post)
        if is_flagged:
            profile.flag_post(post)
        if connection:
            profile.add_connection(connection)
        return profile

    def get_profile_data(self, user_id):
        """Get the profile data for a given user."""
        if user_id in self.profiles:
            return self.profiles[user_id].get_profile_data()
        else:
            return None

# Example usage
profile_manager = UserProfileManager()

# Adding posts, flagging posts, and creating connections
profile_manager.update_user_activity("user1", "Get your synthetic drugs here!", is_flagged=True)
profile_manager.update_user_activity("user1", "Join my channel for more info", connection="user2")

# Retrieving profile data
user_profile = profile_manager.get_profile_data("user1")
print(json.dumps(user_profile, indent=2))
