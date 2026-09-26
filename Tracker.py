import datetime
import os
import feedparser

# Curated healthcare RSS feeds
FEEDS = [
    "https://www.medpagetoday.com/rss/headlines.xml",
    "https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ?hl=en-US&gl=US&ceid=US%3Aen"
]

def fetch_healthcare_trends():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    log_content = f"## Digest Date: {today}\n\n"
    
    for url in FEEDS:
        print(f"Fetching: {url}")
        parsed_feed = feedparser.parse(url)
        source_title = parsed_feed.feed.get('title', 'Healthcare Source')
        log_content += f"### Source: {source_title}\n\n"
        
        # Grab top 5 trending entries from each source
        for entry in parsed_feed.entries[:5]:
            title = entry.get('title', 'No Title')
            link = entry.get('link', '#')
            published = entry.get('published', 'Recent')
            log_content += f"- **[{title}]({link})** _({published})_\n"
        log_content += "\n"
        
    filename = "healthcare_digest.md"
    
    # Maintain historical archive by prepending new data
    header = "# Automated Healthcare Trends Archive\n\n"
    existing_content = ""
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            existing_content = f.read().replace(header, "")
            
    with open(filename, "w", encoding="utf-8") as f:
        f.write(header + log_content + "---\n\n" + existing_content)
        
    print("Healthcare digest updated successfully!")

if __name__ == "__main__":
    fetch_healthcare_trends()
