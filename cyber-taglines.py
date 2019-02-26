import random

s_nouns = ["Visibility", "Platform", "Solution", "Threat Hunting", "Machine Learning", "AI", "Insight", "Workflow", "Discovery", "Blockchain", "Intelligence", "Context", "Orchestration", "Runtime"]
p_nouns = ["Threats", "Anomalies", "Zero-Days", "IoT", "Containers", "Workflows", "Insights"]
adj = ["Cyber", "Automated", "Real-time", "Continuous", "Threat", "Advanced", "Automated", "Comprehensive", "Cyber", "Contextual", "Behavioral", "Scalable", "Seamless", "Simplified", "Unknown", "Orchestrated", "Actionable", "Deep", "Unified", "Proactive", "Adaptive", "Collaborative", "Intuitive", "Optimized", "Patented", "Cloud-based", "Cloud-native", "End-to-end", "Intelligent", "Next-gen", "Sophisticated", "Instant", "Real-world", "Customizable", "Holistic"]
s_verbs = ["Automates", "Automating", "Simplifies", "Empowers", "Orchestrates", "Discovers", "Prioritizes", "Optimizes", "Delivers", "Stops", "Detects", "Prevents"]

print (random.choice(adj),random.choice(adj),random.choice(s_nouns),random.choice(s_verbs),random.choice(adj),random.choice(p_nouns))
