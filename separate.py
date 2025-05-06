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

# Split content by "End of Document" to get individual articles
    article_sections = content.split("End of Document")
    
    # Process each article
    for i, section in enumerate(article_sections):
        if i >= len(article_titles) or "Body" not in section:
            continue
        
        # Extract byline and length
        byline_match = re.search(r'Byline:.*', section)
        length_match = re.search(r'Length:.*', section)
        
        header = ""
        if byline_match:
            header += byline_match.group(0) + "\n"
        if length_match:
            header += length_match.group(0) + "\n"
        
        # Extract article body
        body_parts = section.split("Body")
        if len(body_parts) < 2:
            continue
        
        article_body = body_parts[1].strip()
        
        # Remove "Page X of X" lines
        cleaned_body = re.sub(r'Page \d+ of \d+\n?', '', article_body)
        
        # Create sanitized filename
        safe_title = re.sub(r'[\\/*?:"<>|]', '_', article_titles[i])
        filename = os.path.join(output_dir, f"{safe_title}.txt")
        
        # Write article to file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(header + "\n" + cleaned_body)
    
    return len(article_titles)

if __name__ == "__main__":
    count = extract_articles("./article data/text/Dateien (76).txt")
    print(f"Successfully extracted {count} articles to the 'extracted_articles' folder.")