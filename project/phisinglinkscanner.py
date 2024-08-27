import tldextract 
import lavenshtein as lv

legitimate_domain = ['example.com','google.com','facebook.com','instagram.com']

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

def is_mispelled_domain(domain, legitimate_domain, threshold=0,9);
for legitimate_domain in legitimate_domains:
    similarity = lv.ratio(domain, legit_domain)
    if similarity > threshold:
        return False #its a legitimate domain
    return True # no close match found, possibly misspelled

def is_phishing_url(url, legitimate_domain):
    subdomain, domain, suffix = extract_domain_part(url)

# check if  it's a known legitimate domain
if is_mispelled_domain(domain,legitmate,domains):
    print("potential phishing detected: {url}")

return True

# you can add more checks here, like suspicious subdomains

return False

# press the green button in the qutter to run the script.
if __name__ == '__main__':
    for url in test_urls:
        if is_phishing_url(url, legitimate_domain):
