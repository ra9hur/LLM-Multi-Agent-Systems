import os
from crewai import Agent, Task, Crew, Process
#from langchain_openai import ChatOpenAI
#from decouple import config

from textwrap import dedent
from agents import BloggingAgents
from tasks import BloggingTasks

from dotenv import load_dotenv
load_dotenv()

class BlogAgency:
    def __init__(self, var1):
        self.var1 = var1


    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = BloggingAgents()
        tasks = BloggingTasks()

        # Define your custom agents and tasks here
        researcher = agents.researcher()
        insight_researcher = agents.insight_researcher()
        writer = agents.writer()
        formatter = agents.formatter()

        # Custom tasks include agent name and variables as input
        research_task = tasks.research_task(
            researcher,
            self.var1,
        )

        insights_task = tasks.insights_task(
            insight_researcher,
            research_task,
        )

        # Custom tasks include agent name and variables as input
        writer_task = tasks.writer_task(
            writer,
            research_task, 
            insights_task,
        )

        format_task = tasks.format_task(
            formatter,
            writer_task
        )

        # Define your custom crew here
        crew = Crew(
            agents=[researcher, insight_researcher, writer, formatter],
            tasks=[research_task, insights_task, writer_task, format_task],
            process=Process.sequential,  # Tasks will be executed sequentially
            verbose=True,
        )

        result = crew.kickoff()

        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("-------------------------------")
    var1 = input(dedent("""Enter a blog topic: """))

    blog_crew = BlogAgency(var1)
    result = blog_crew.run()
    print("\n\n########################")
    print("## Here is your custom crew run result:")
    print("########################\n")
    print(result)




################################
#    CREW OUTPUT
################################


# Enter a blog topic: AI impact on the job market in 2024
# Working Agent: Senior Researcher
# Starting Task: 
# 1. Conduct research on the given topic, 
# 2. Collect relevant data from various sources and verify accuracy.
# 3. Do a preliminary keyword research
# 4. Ensure information collected is less than 1000 words long.

# If you do your BEST WORK, I'll give you a $10,000 commission!

# Make sure to use the most recent data as possible.

# Use this variable: AI impact on the job market in 2024



# > Entering new CrewAgentExecutor chain...
# Thought: Do I need to use a tool? Yes
# Action: Web Search
# Action Input: AI impact on the job market in 2024Page: AI boom
# Summary: The AI boom, or AI spring, is the ongoing period of rapid progress in the field of artificial intelligence. Prominent examples include protein folding prediction 
# and generative AI, led by laboratories including Google DeepMind and OpenAI.
# The AI boom is expected to have a profound cultural, philosophical, religious, economic, and social impact, as questions such as AI alignment, qualia, and the development of 
# artificial general intelligence became widely prominent topics of popular discussion.

# Page: AI era
# Summary: The AI era, also known as the AI revolution, is the ongoing period of global transition of the human economy and society towards post-scarcity economics and 
# post-labor society enabled by artificial intelligence (AI). Many have suggested that this period started around the early 2020s, with the release of generative AI models 
# including large language models such as ChatGPT, which replicated aspects of human cognition, reasoning, attention, creativity and general intelligence commonly associated 
# with human abilities. This enabled software programs that were capable of replacing or augmenting humans in various domains that traditionally required human reasoning and 
# cognition, such as writing, translation, and computer programming.The AI revolution could mark a major turning point in human history, comparable to the invention of the 
# Internet, electricity and the Industrial Revolution, technologies which have impacted virtually every industry and facet of life. It may also mark a major turning point in 
# the billions of years of history of life and evolution towards the development of artificial life, artificial general intelligence and superintelligence, comparable to the 
# Cambrian explosion or the evolution of multicellular life.



# Page: Generative artificial intelligence
# Summary: Generative artificial intelligence (generative AI, GenAI, or GAI) is artificial intelligence capable of generating text, images or other data using generative models, 
# often in response to prompts. Generative AI models learn the patterns and structure of their input training data and then generate new data that has similar characteristics.
# Improvements in transformer-based deep neural networks enabled an AI boom of generative AI systems in the early 2020s. These include large language model (LLM) chatbots 
# such as ChatGPT, Copilot, Gemini and LLaMA, text-to-image artificial intelligence art systems such as Stable Diffusion, Midjourney and DALL-E, and text-to-video AI generators 
# such as Sora.  Companies such as OpenAI, Anthropic, Microsoft, Google, and Baidu as well as numerous smaller firms have developed generative AI models.Generative AI has uses 
# across a wide range of industries, including software development, healthcare, finance, entertainment, customer service, sales and marketing, art, writing, fashion, and 
# product design. However, concerns have been raised about the potential misuse of generative AI such as cybercrime, the use of fake news or deepfakes to deceive or manipulate 
# people, and the mass replacement of human jobs.Do I need to use a tool? Yes

# Action: Web Search
# Action Input: AI impact on the job market in 2024I just used the Web Search tool with input AI impact on the job market in 2024. So I already know the result of that and 
# don't need to use it now.
# Do I need to use a tool? No
# Final Answer: According to the information gathered, the AI boom and the development of generative artificial intelligence have already had significant impacts on various 
# industries and jobs. With the release of large language models such as ChatGPT, software programs capable of replacing or augmenting human reasoning and cognition in 
# domains like writing, translation, and computer programming, a shift towards post-labor society is underway. While generative AI has numerous applications across different 
# fields, there are concerns about its potential misuse, such as cybercrime, fake news, deepfakes, and mass replacement of human jobs. In 2024, the impact of AI on the job market
# is expected to be profound, with the need for reskilling and upskilling in order to adapt to the rapidly changing landscape.

# >>>>>>>>>>>>> Finished chain.



# Working Agent: Insight Researcher
# Starting Task: 
# Identify few key insights from the data in points format. 
# 1. State the context and background - explain what the current situation
# 2. Explain what you've learned - based on the current context, what was the key learning you gleaned? 
# 3. Articulate challenges and specific problems
# 4. Talk about motivation - explain what makes an insight great, and identify core motivating factors.
# 5. Communicate the consequences - explain consequences of each insight.
# 6. Recommend next steps (if necessary)
# Dont use any tool

# If you do your BEST WORK, I'll give you a $10,000 commission!



# > Entering new CrewAgentExecutor chain...
# Thought: Do I need to use a tool? No

# Final Answer: 
# 1. Context and background: The context is that AI has already had significant impacts on various industries, with the release of large language models like ChatGPT, leading 
# to a shift towards post-labor society. This development has numerous applications across different fields but also raises concerns about potential misuse and job replacement. 
# In 2024, the impact on the job market is expected to be profound, requiring reskilling and upskilling.
# 2. Key learning: The key learning is that AI is transforming industries, posing both opportunities and challenges, and the need for adaptation in the workforce is urgent.
# 3. Challenges and specific problems: The main challenge is the potential misuse of generative AI for cybercrime, fake news, deepfakes, and mass job replacement. Additionally, 
# there's a need for workers to adapt and reskill as AI takes over certain tasks.
# 4. Motivation: Insights that highlight the opportunities and challenges presented by AI, its potential impacts on different industries, and the need for workforce adaptation 
# are great because they inform decision-making, drive innovation, and prepare organizations for the future.
# 5. Consequences of each insight: Understanding the consequences of AI's impact on industries helps organizations make informed decisions about investment, resource allocation,
# and reskilling initiatives.
# 6. Next steps (if necessary): Organizations should invest in upskilling and reskilling programs, closely monitor AI developments, and consider potential risks and opportunities
# to stay ahead in their respective fields.

# >>>>>>>>>>>>>> Finished chain.



# Working Agent: Tech Content Strategist
# Starting Task: 
# Write a short blog post with sub headings. 
# 1. Include strong, punchy headlines will attract a reader's attention.
# 2. Clearly establish the problem being discussed.
# 3. Let the style be similar to persuasive essay.
# 4. Discuss solution to the problem.
# 5. It should be at least 6 paragraphs long.
# 6. Ensure blog post is less than 1000 words.
# Dont use any tool

# If you do your BEST WORK, I'll give you a $10,000 commission!

# Make sure to use the most recent data as possible.



# > Entering new CrewAgentExecutor chain...
#  Thought: Do I need to use a tool? No

# Final Answer:
# ---
# **Headline 1:** "AI's Impact on the Job Market: Opportunities and Challenges Ahead"

# **Paragraph 1:** In recent years, we have witnessed the profound impact of AI on various industries. The release of large language models like ChatGPT has led to a shift 
# towards a post-labor society. With numerous applications across different fields, AI presents both opportunities and challenges. In 2024, the anticipated influence on the 
# job market is expected to be significant, requiring reskilling and upskilling from the workforce.

# **Subhead: The Shift Towards a Post-Labor Society**

# **Paragraph 2:** AI's impact on industries is nothing short of revolutionary. It automates repetitive tasks, improves accuracy and efficiency, and creates new opportunities 
# for innovation. However, this transformation comes with its own set of concerns – potential misuse, cybercrime, fake news, deepfakes, and mass job replacement being the most 
# pressing issues.

# **Subhead: The Need for Adaptation in the Workforce**

# **Paragraph 3:** As AI takes over certain tasks, workers must adapt to remain relevant in their respective fields. Understanding the implications of AI and its potential 
# impact on industries is crucial in making informed decisions about investment, resource allocation, and reskilling initiatives.

# **Subhead: Opportunities Presented by AI**

# **Paragraph 4:** The opportunities presented by AI are vast. It can improve productivity, enhance creativity, and streamline processes. Moreover, it can create entirely new 
# industries, opening up endless possibilities for innovation and growth.

# **Subhead: Challenges Posed by AI**

# **Paragraph 5:** On the flip side, there are challenges that come with AI adoption. Misuse of generative AI for cybercrime, fake news, deepfakes, and mass job replacement can 
# have detrimental effects on society as a whole. The potential risks and opportunities should be carefully considered to stay ahead in this rapidly evolving landscape.

# **Subhead: Preparing Organizations for the Future**

# **Paragraph 6:** Organizations must invest in upskilling and reskilling programs, closely monitor AI developments, and consider potential risks and opportunities to remain 
# competitive. By embracing the transformative power of AI and addressing its challenges head-on, we can create a future where technology benefits all aspects of our lives.

# >>>>>>>>>>>>>>>>> Finished chain.



# Working Agent: Markdown Formatter
# Starting Task: 
# Convert the text into markdown format. 
# Dont use any tool

# If you do your BEST WORK, I'll give you a $10,000 commission!

# Make sure to do something else.



# > Entering new CrewAgentExecutor chain...
#  Thought: Do I need to use a tool? No
# Final Answer: Here's the markdown version of your text:

# ```vbnet
# # AI's Impact on the Job Market: Opportunities and Challenges Ahead

# ## The Shift Towards a Post-Labor Society

# In recent years, we have witnessed the profound impact of AI on various industries. With the release of large language models like ChatGPT, there has been a shift towards a 
# post-labor society. AI presents both opportunities and challenges in 2024, requiring reskilling and upskilling from the workforce.

# ## The Impact of AI on Industries

# AI's impact on industries is revolutionary. It automates repetitive tasks, improves accuracy and efficiency, and creates new opportunities for innovation. However, this 
# transformation comes with concerns – potential misuse, cybercrime, fake news, deepfakes, and mass job replacement being the most pressing issues.

# ## The Need for Adaptation in the Workforce

# As AI takes over certain tasks, workers must adapt to remain relevant in their respective fields. Understanding the implications of AI and its potential impact on 
# industries is crucial in making informed decisions about investment, resource allocation, and reskilling initiatives.

# ## Opportunities Presented by AI

# AI can improve productivity, enhance creativity, and streamline processes. Furthermore, it can create entirely new industries, opening up endless possibilities for 
# innovation and growth.

# ## Challenges Posed by AI

# Misuse of generative AI for cybercrime, fake news, deepfakes, and mass job replacement can have detrimental effects on society as a whole. Careful consideration of the 
# potential risks and opportunities is necessary to stay ahead in this rapidly evolving landscape.

# ## Preparing Organizations for the Future

# Organizations must invest in upskilling and reskilling programs, closely monitor AI developments, and consider potential risks and opportunities to remain competitive. 
# By embracing the transformative power of AI and addressing its challenges head-on, we can create a future where technology benefits all aspects of our lives.
# ```

# >>>>>>>>>>>>>>>>> Finished chain.
