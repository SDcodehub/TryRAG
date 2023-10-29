from dotenv import load_dotenv
from app.utils.api_key_check import check_api_key

load_dotenv()

check_api_key("OPENAI_API_KEY")

# Parse arguments

# Load arguments and config file for the all the settings

# Get the query and embed it using embedding model

# get retrived results using retriever

# makellm call using the retrieved results

# Return the output
