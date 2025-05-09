
from openai import OpenAI
from dotenv import load_dotenv
import re

""" Design Doc

Class name: APITools

Class description: APITools is a utility class defined to house all utility functions for interacting with an LLM through various APIs. 
                   This will allow for clean reusable code, improve the readability of the program, and significantly help the writability of ASC.

Class data members: N/A

Class member functions: generateQuestion(), generateFlashcards(), solveMathEquation()
"""

load_dotenv()

class Chatbot:
    def __init__(self, subject=None):
        # Client between user and OpenAI
        self.client = OpenAI()
        # Messages to be used for creations
        self.context = [
            {"role": "system", "content": self.build_sys_prompt(subject)},
        ]
    def build_sys_prompt(self, subject=None):
        base_prompt = (
            "You are an educational assistant that provides multiple-choice questions "
            "to help users learn different subjects. Each question should have exactly four "
            "answer choices labeled A, B, C, and D. You may not provide any number of answer choices other than 4. Exactly one of these choices can be the correct answer. "
            "One choice MUST be the correct answer, and the other three MUST be incorrect."
            "NONE is not a valid answer. "
            "You must indicate the correct answer clearly "
            "and provide an explanation for why the answer is correct."
            "For this explanation, please surround the entire explanation in {}."
            "A format for your response will be described. Do not respond with anything other than the exact format."
            "The format of your response must be as follows:\n"
            "Question: <Insert question here>\n"
            "A) <Option A>\n"
            "B) <Option B>\n"
            "C) <Option C>\n"
            "D) <Option D>\n"
            "Answer: <Correct answer letter>\n"
            "Explanation: {<Detailed explanation of why the correct answer is correct and why the others are not>}"
        )
        if subject == "Math":
            return (
            f"{base_prompt}\n\n"
            "For Math questions, use the following additional rules:\n"
            "- Format every question as:\n"
            "  Question: Solve for $$<variable>$$\n"
            "  $$<expression>$$\n"
            "- Provide answer choices as single-line equations in the form:\n"
            "  A) $$<variable> = <value>$$\n"
            "  B) $$<variable> = <value>$$\n"
            "  C) $$<variable> = <value>$$\n"
            "  D) $$<variable> = <value>$$\n"
            "- Use only one of the following variables: a, b, c, x, y, z.\n"
            "- All expressions must be solvable with exactly one rational solution.\n"
            "- Do NOT use expressions with multiple valid solutions (e.g., sqrt(x^4)).\n"
            "- Do NOT use irrational or undefined solutions.\n"
            "- Ensure that the correct answer satisfies the given expression."        )
        else:
            return base_prompt
    
    # Send and receive messages to and from OpenAI
    def generateQuestion(self, message: str):
        self.context.append({"role": "user", "content": message})

        # Send the outgoing message, set model, store on OpenAI, and send messages in context
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=self.context
        )
        # Store response
        response_content = response.choices[0].message.content
        
        self.context.append({"role": "assistant", "content": response_content})

        return response_content

    def get_user_answer(self, choices):
        valid_responses = {"A", "B", "C", "D"}
        while True:
            print("\nPlease select an answer:")
            user_answer = input("A/B/C/D").strip().upper()

            if user_answer in valid_responses:
                return user_answer
            else:
                print("Invalid choice. Please choose A, B, C, or D.")
