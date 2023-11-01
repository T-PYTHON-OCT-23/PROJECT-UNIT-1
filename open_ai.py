import openai
import dotenv
import os


dotenv.load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY")

class OpenAi:

    def __init__(self,ask : str):
        self.ask = ask


    def ai_output(self) -> str:
            response = openai.Completion.create(
            model = "text-davinci-003",
            prompt = self.ask,
            temperature = 0.8,
            max_tokens = 1024,
            top_p = 1,
            frequency_penalty = 0.0,
            presence_penalty = 0.6
        )
            text = response['choices'][0]['text']
            return text




