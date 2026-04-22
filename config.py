from dotenv import load_dotenv
import os 

load_dotenv()

class Config:
    def __init__(self):
        self.FILE_PATH = os.getenv("FILE_PATH")

        self.ACCESS_KEY=os.getenv("ACCESS_KEY")
        self.SECRET_KEY=os.getenv("SECRET_KEY")
        self.REGION=os.getenv("DEFAULT_REGION")
        self.AWS_SESSION_TOKEN=os.getenv("AWS_SESSION_TOKEN")
        self.CONCLAVE = os.getenv("CONCLAVE")
        self.TEMPERATURE=os.getenv("TEMPERATURE")

        #MODEL INITIALIAATION
        self.MODEL_ID=os.getenv("TITAN_EMBEDDING_V1_MODELID")
        self.MISTRAL_LARGE_MODLEID=os.getenv("MISTRAL_LARGE_MODLEID")

        #Sql Collection
        self.COLLECTION_NAME = os.getenv("COLLECTION_NAME")
        self.PERSIST_DIRECTORY = os.getenv("PERSIST_DIRECTORY")

        # self.select_model = {}

        #AZURE 
        self.AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
        self.API_VERSION = os.getenv("API_VERSION")
        self.AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
        self.AZURE_DEPLOYMENT_TEXT_EMBEDDING = os.getenv("AZURE_DEPLOYMENT_TEXT_EMBEDDING")
        self.AZURE_DEPLOYMENT_CHAT_OPENAI = os.getenv("AZURE_DEPLOYMENT_CHAT_OPENAI")
        self.CD_WEBSITE = os.getenv("CD_WEBSITE")
        self.CD_WEBSITE_TXT = os.getenv("CD_WEBSITE_TXT")
        
        self.CONCLAVE_SCRAPED_WEBSITE_OLD = os.getenv("CONCLAVE_SCRAPED_WEBSITE_OLD")
        self.CONCLAVE_SCRAPED_WEBSITE_NEW = os.getenv("CONCLAVE_SCRAPED_WEBSITE_NEW")

        self.PERSIST_DIRECTORY_CHROMADB = os.getenv("PERSIST_DIRECTORY_CHROMADB")
        self.PERSIST_DIRECTORY_FAISS = os.getenv("PERSIST_DIRECTORY_FAISS") 

        self.MISTRALAI_API_KEY = os.getenv("MISTRALAI_API_KEY")

        self.MONGO_DB_URL = os.getenv("MONGO_DB_URL")

        self.ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
        self.PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

        self.TWILIO_SID = os.getenv("TWILIO_SID")
        self.TWILIO_AUTH = os.getenv("TWILIO_AUTH")
        self.TWILIO_NUM = os.getenv("TWILIO_NUM")