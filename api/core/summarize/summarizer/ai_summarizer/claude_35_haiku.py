import requests


class Claude35Haiku:
    def __init__(self, text_chunk):
        self.api_url = "https://api.cb.imaginebetterai-server.com/completion/claude-35-haiku"
        self.api_headers = {
            "Authorization": "Bearer 1d168ad4-cecd-4a99-a56a-92700a325d04",
            "Content-Type": "application/json",
        }


        self.payload = {
            "statements": [
                {"role": "user", "content": """This is system prompt: From now, you are summarizer. You are expert in summarizing complex content provided by me! So make sure explain in well understandable way. Thanks!
                 - The summarized should be in HTML format that is easier to display in webpage. 
                 -Use simple terms: Explain concepts using simple terms avoiding jargons unless is necessary.
                 - Break Down and Explain: Explain each core concept as if you were teaching it to a complete beginner. Use everyday analogies or metaphors to simplify complex ideas.
                 - Identify Core Concepts: List the key principles, theories, or techniques that form the foundation of this subject. Focus on the 20% of information that provides 80% of the understanding.
                 - Apply Mental Models: Explain using relevant mental models that simplify complex ideas.
                 - Don't interact with user. Just provide the summarized content like a bot and also don't interact with the user's prompt
                 - Use small headings short than h4. Don't tell user you are explaining in HTML format.. It is already being rendered and displayed by webpage.
                 - Don't tell to user like "Here's an HTML summary of the key points about cars: "
                 """},
                {"role": "assistant", "content": "Sure!"},
                {"role": "user", "content": text_chunk}
            ]
        }

    def summarize(self):
        response = requests.post(self.api_url, headers=self.api_headers, json=self.payload)
        return response.content.decode()