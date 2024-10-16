import hashlib
import time

# User class to manage user-specific URL shortening (Optional)
class User:
    def __init__(self, user_id, name, email):
        self.id = user_id
        self.name = name
        self.email = email
        self.urls = []  # List of URLs created by the user

    def shorten_url(self, long_url):
        url = URL.create(long_url, user=self)
        self.urls.append(url)
        return url.short_url


# URL class to handle the creation of short URLs and redirection
class URL:
    url_mapping = {}  # To simulate storage (use database in real scenario)

    def __init__(self, long_url, short_url, user=None, expiration=None):
        self.long_url = long_url
        self.short_url = short_url
        self.user = user
        self.created_at = time.time()
        self.expiration = expiration

    @classmethod
    def create(cls, long_url, user=None, expiration=None):
        # Generate a unique short URL using a hash function
        short_url = cls.generate_short_url(long_url)
        new_url = cls(long_url, short_url, user, expiration)
        cls.url_mapping[short_url] = new_url
        return new_url

    @staticmethod
    def generate_short_url(long_url):
        # Simple example using hashlib (for interview purposes)
        hash_object = hashlib.sha256(long_url.encode())
        short_hash = hash_object.hexdigest()[:6]  # Take the first 6 characters
        return f"http://short.ly/{short_hash}"

    @classmethod
    def redirect(cls, short_url):
        # Fetch the original URL and perform the redirection (mock)
        url_obj = cls.url_mapping.get(short_url)
        if url_obj:
            # Check for expiration
            if url_obj.expiration and time.time() > url_obj.expiration:
                return "Error: This short URL has expired."
            return url_obj.long_url
        return "Error: Short URL not found."

    def __repr__(self):
        return f"Short URL: {self.short_url}, Long URL: {self.long_url}"


# Example Flow
if __name__ == "__main__":
    # User (optional feature for interview)
    user1 = User(1, "Alice", "alice@example.com")

    # URL Shortening
    long_url = "https://www.example.com/this-is-a-very-long-url-for-a-specific-page"
    short_url = user1.shorten_url(long_url)
    print(f"Generated short URL: {short_url}")

    # URL Redirection
    original_url = URL.redirect(short_url)
    print(f"Redirected to: {original_url}")

    # Expiration handling
    short_url_with_expiration = URL.create(
        "https://www.expired-url.com", expiration=time.time() + 10  # 10 seconds expiration
    ).short_url
    print(f"Short URL with expiration: {short_url_with_expiration}")
    time.sleep(11)  # Wait for URL to expire
    print(URL.redirect(short_url_with_expiration))
