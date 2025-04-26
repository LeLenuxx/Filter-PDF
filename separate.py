import os
import re

def extract_articles(input_file):
    # Create output directory if it doesn't exist
    output_dir = "extracted_articles"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Read the entire file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract article index
    article_titles = []
    for line in content.split('\n'):
        match = re.match(r'^\d+\.\s+(.+)$', line)
        if match:
            article_titles.append(match.group(1).strip())