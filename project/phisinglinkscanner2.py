import tldextract
import Levenshtein as lv  # Using Levenshtein library for string similarity

legitimate_domains = ['example.com', 'google.com', 'facebook.com', 'instagram.com']

test_urls = [
    'http://example.co',
    'http://example.com',
    'http://www.google.security-update.com',
    'http://facebook.com/login',
    'http://google.com'
]

def extract_domain_part(url):
    extracted = tldextract.extract(url)
    return extracted.subdomain, extracted.domain, extracted.suffix

def is_mispelled_domain(domain, legitimate_domains, threshold=0.9):
    for legit_domain in legitimate_domains:
        similarity = lv.ratio(domain, legit_domain)
        if similarity > threshold:
            return False  # It's a legitimate domain
    return True  # No close match found, possibly misspelled

def is_phishing_url(url, legitimate_domains):
    subdomain, domain, suffix = extract_domain_part(url)

    # Check if it's a known legitimate domain or very similar to one
    if is_mispelled_domain(domain, legitimate_domains):
        print(f"Potential phishing detected (suspected domain): {url}")
        return True

    # Check for suspicious subdomains (e.g., www.google.security-update.com)
    if subdomain and subdomain.lower() not in ['www', 'mail', 'secure']:
        print(f"Potential phishing detected (suspicious subdomain): {url}")
        return True

    # Check for uncommon TLDs or double extensions
    if '.' in suffix:
        main_suffix = suffix.split('.')[-1]
        if main_suffix not in ['com', 'net', 'org', 'gov', 'edu']:
            print(f"Potential phishing detected (uncommon TLD): {url}")
            return True

    # Add more sophisticated checks here if needed

    return False

if __name__ == '__main__':
    for url in test_urls:
        is_phishing_url(url, legitimate_domains)
