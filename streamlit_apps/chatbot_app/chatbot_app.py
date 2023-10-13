

class ChatBot():

    def __init__(self, message_history):
        self.message_history = []

    def append_messages(self, message: str) -> list:
        prompt = {"role": "user", "content": message}
        self.message_history.append(prompt)
        response = self.get_response()
        self.message_history.append(response)

        return self.message_history

    def get_response(self, prompt):

        # TODO: This is where an LLM call will happen
        response = {"role": "system", "content": f"You said {prompt}"}

        return response
