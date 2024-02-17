from crewai import Task
from textwrap import dedent


class BloggingTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def research_task(self, agent, var1):
        return Task(
            description=dedent(
                f"""
            1. Conduct research on the given topic, 
            2. Collect relevant data from various sources and verify accuracy.
            3. Do a preliminary keyword research
            4. Ensure information collected is less than 1000 words long.
            
            {self.__tip_section()}
    
            Make sure to use the most recent data as possible.
    
            Use this variable: {var1}
        """
            ),
            agent=agent
        )

    def insights_task(self, agent, research_task):
        return Task(
            description=dedent(
                f"""
            Identify few key insights from the data in points format. 
            1. State the context and background - explain what the current situation
            2. Explain what you've learned - based on the current context, what was the key learning you gleaned? 
            3. Articulate challenges and specific problems
            4. Talk about motivation - explain what makes an insight great, and identify core motivating factors.
            5. Communicate the consequences - explain consequences of each insight.
            6. Recommend next steps (if necessary)
            Dont use any tool
                                       
            {self.__tip_section()}
        """
            ),
            agent=agent,
            context=[research_task]
        )

    def writer_task(self, agent, research_task, insights_task):
        return Task(
            description=dedent(
                f"""
            Write a short blog post with sub headings. 
            1. Include strong, punchy headlines will attract a reader's attention.
            2. Clearly establish the problem being discussed.
            3. Let the style be similar to persuasive essay.
            4. Discuss solution to the problem.
            5. It should be at least 6 paragraphs long.
            6. Ensure blog post is less than 1000 words.
            Dont use any tool
            
            {self.__tip_section()}
    
            Make sure to use the most recent data as possible.
        """
            ),
            agent=agent,
            context=[research_task, insights_task]
        )

    def format_task(self, agent, writer_task):
        return Task(
            description=dedent(
                f"""
            Convert the text into markdown format. 
            Dont use any tool
                                       
            {self.__tip_section()}

            Make sure to do something else.
        """
            ),
            agent=agent,
            context=[writer_task]
        )
