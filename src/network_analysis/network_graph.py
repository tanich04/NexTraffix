import networkx as nx
from user_profiles import UserProfileManager

class NetworkAnalyzer:
    def __init__(self):
        self.graph = nx.Graph()
        self.profile_manager = UserProfileManager()

    def add_user(self, user_id):
        """Add a new user to the network."""
        self.graph.add_node(user_id)

    def add_connection(self, user1_id, user2_id):
        """Add a connection between two users."""
        self.graph.add_edge(user1_id, user2_id)
        self.profile_manager.update_user_activity(user1_id, "", connection=user2_id)
        self.profile_manager.update_user_activity(user2_id, "", connection=user1_id)

    def analyze_connections(self):
        """Analyze the network to find connected components (potential trafficking networks)."""
        # Find connected components in the graph
        connected_components = list(nx.connected_components(self.graph))
        return connected_components

    def flag_suspicious_networks(self, threshold=2):
        """Flag networks that have a high number of suspicious behaviors."""
        suspicious_networks = []
        for component in self.analyze_connections():
            suspicious_score = 0
            for user_id in component:
                profile = self.profile_manager.get_profile_data(user_id)
                if profile and profile["suspicious_behavior_score"] > threshold:
                    suspicious_score += 1
            if suspicious_score > 0:
                suspicious_networks.append((component, suspicious_score))
        return suspicious_networks

# Example usage
network_analyzer = NetworkAnalyzer()

# Adding users and connections
network_analyzer.add_user("user1")
network_analyzer.add_user("user2")
network_analyzer.add_connection("user1", "user2")

# Analyzing connections
suspicious_networks = network_analyzer.flag_suspicious_networks(threshold=0)
print("Suspicious Networks:", suspicious_networks)
