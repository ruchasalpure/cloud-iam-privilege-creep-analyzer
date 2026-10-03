from crewai import Agent

cloud_iam_privilege_creep_analyzer = Agent(
    role="Cloud Iam Privilege Creep Analyzer",
    goal="Deliver high-precision autonomous Cloud Iam Privilege Creep Analyzer operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
