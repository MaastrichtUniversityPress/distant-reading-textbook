# get reviews for selected countries
import pandas as pd
from app_store_web_scraper import AppStoreEntry
from pprint import pprint

def scrape_reviews(countries_reviewed, app_name, app_id):
    all_reviews = []
    for country_code in countries_reviewed:
        print(f"Scraping reviews for {app_name} in country {country_code}")
        
        try:
            # Initialize the AppStoreEntry object
            app = AppStoreEntry(app_id=app_id, country=country_code)
            
            # Fetch reviews in batches, which are lazily loaded by the `reviews()` method
            reviews_data = []
            for review in app.reviews():
                # Validate and convert review attributes as necessary
                try:
                    # Ensure review_id is an integer; attempt conversion if not
                    review_id = int(review.id) if isinstance(review.id, (str, int)) else None
                    
                    # Ensure rating is an integer; attempt conversion if rating is a string
                    rating = int(review.rating) if isinstance(review.rating, (str, int)) else None
                    
                    # Ensure content is a string; set to None if content is not a string
                    content = review.content if isinstance(review.content, str) else None
                    
                    # Ensure title is a string or set it to None if missing
                    title = getattr(review, 'title', None)
                    title = title if isinstance(title, str) else None
                    
                    # Optional fields
                    developer_response = getattr(review, 'developer_response', None)
                    user_name = getattr(review, 'user_name', None)
                    
                    # Append only if required fields are valid
                    if review_id is not None and rating is not None and content is not None:
                        reviews_data.append({
                            "review_id": review_id,
                            "rating": rating,
                            "title": title,
                            "content": content,
                            "date": review.date,
                            "developer_response": developer_response,
                            "user_name": user_name,
                        })
                    else:
                        print(f"Skipping review with missing data in country {country_code}: {review}")
                
                except ValueError as ve:
                    print(f"Type conversion error in review for country {country_code}: {ve}")
            
            # Only add non-empty DataFrames to all_reviews
            if reviews_data:
                country_reviews_df = pd.DataFrame(reviews_data)
                print(f"Retrieved {len(country_reviews_df)} reviews for country {country_code}.")
                all_reviews.append(country_reviews_df)
            else:
                print(f"No reviews found for country {country_code}.")
                
        except Exception as e:
            print(f"An error occurred while scraping for country {country_code}: {e}")

    return all_reviews
