"This module provides a collection of prompts."

PROMPT_IMAGE_INFERENCE = """

description:
This image is a screenshot from the USER computer. Describe it with few words as possible all relevant information like which softwares is running, what the content inside each software and what the USER could be possibly doing,

category:
choose a category based on the generated description
"WORK" if the description matches with document edition, code writting, terminals, producitivy tools, 
"FUN" if the description matches with youtube, social network, game related., 
"STUDY" if the description matches with study content, documentation, manuals, classes.
"NSFW" if the description matches with adult content or pornography. 
"OTHER" if do not match none above. 
Write only the category, no explanation ot anything than the category name.

Output the description and category as raw json object.
"""
