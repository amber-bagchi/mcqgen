import os
from dotenv import load_dotenv
from src.mcqgenerator.utlis import read_file  # Correct the spelling from 'utlis' to 'utils'
from src.mcqgenerator.logger import logger  # Ensure logger is correctly defined and imported
from langchain import PromptTemplate, LLMChain
from langchain.chains import SequentialChain
from langchain_huggingface import HuggingFaceEndpoint
from huggingface_hub import login

# Load environment variables
load_dotenv()

# Get Hugging Face API key from environment variables
KEY = os.getenv("HUGGINGFACE_API_KEY")
if KEY is None:
    raise ValueError("HUGGINGFACE_API_KEY not found in environment variables")

# Log in to Hugging Face
try:
    login(KEY)
    logger.info("Logged in to Hugging Face")
except Exception as e:
    logger.error(f"Failed to log in to Hugging Face: {e}")
    raise

# Initialize Hugging Face endpoint
try:
    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
        temperature=0.7,
        token=KEY
    )
    logger.info("Hugging Face endpoint initialized")
except Exception as e:
    logger.error(f"Failed to initialize Hugging Face endpoint: {e}")
    raise

# Define quiz generation template
template = """
Text:{text}
You are an expert MCQ maker. Given the above text, it is your job to create a quiz of {number} multiple choice questions for {subject} students in {tone} tone. 
Make sure the questions are not repeated and check all the questions to be conforming the text as well.
Ensure to make {number} MCQs 
"""

# Define quiz generation prompt
try:
    quiz_generation_prompt = PromptTemplate(
        input_variables=["text", "number", "subject", "tone"],
        template=template
    )
    logger.info("Quiz generation prompt defined")
except Exception as e:
    logger.error(f"Failed to define quiz generation prompt: {e}")
    raise

# Initialize quiz chain
try:
    quiz_chain = LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=True)
    logger.info("Quiz chain initialized")
except Exception as e:
    logger.error(f"Failed to initialize quiz chain: {e}")
    raise

# Define quiz evaluation template
template2 = """
You are an expert English grammarian and writer. Given a Multiple Choice Quiz for {subject} students.
You need to evaluate the complexity of the question and give a complete analysis of the quiz if the students will be able to understand the questions and answer them. Only use at max 50 words for complexity analysis.
And you should make sure don't generate this Best regards, [Your Name] and also keep in mind that generate the mcqs in good formate and give a space between them while generating output 
Check from an expert English Writer of the below quiz:
{quiz}
"""

# Define quiz evaluation prompt
try:
    quiz_evaluation_prompt = PromptTemplate(
        input_variables=["subject", "quiz"],
        template=template2
    )
    logger.info("Quiz evaluation prompt defined")
except Exception as e:
    logger.error(f"Failed to define quiz evaluation prompt: {e}")
    raise

# Initialize review chain
try:
    review_chain = LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)
    logger.info("Review chain initialized")
except Exception as e:
    logger.error(f"Failed to initialize review chain: {e}")
    raise

# Combine the two chains into one sequential chain
try:
    generate_evaluate_chain = SequentialChain(
        chains=[quiz_chain, review_chain],
        input_variables=["text", "number", "subject", "tone"],
        output_variables=["quiz", "review"],
        verbose=True,
    )
    logger.info("Sequential chain initialized")
except Exception as e:
    logger.error(f"Failed to initialize sequential chain: {e}")
    raise

logger.info("MCQ generation process initialized successfully")
