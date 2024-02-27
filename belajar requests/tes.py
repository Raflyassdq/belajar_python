import json
data = [
    {
        "alpha_two_code": "US",
        "state-province": None,
        "country": "United States",
        "name": "Marywood University",
        "web_pages": [
            "http://www.marywood.edu", "http://www.google.com"
        ],
        "domains": [
            "marywood.edu"
        ]
    },
    {
        "alpha_two_code": "US",
        "state-province": None,
        "country": "United States",
        "name": "Lindenwood University",
        "web_pages": [
            "http://www.lindenwood.edu/"
        ],
        "domains": [
            "lindenwood.edu"
        ]
    }
]

for university in data:
    print("Name:", university["name"])
    print("Country:", university["country"])
    if university["web_pages"]:
        print("Web Pages:")
        for web_page in university["web_pages"]:
            print("\t", web_page)
    if university["domains"]:
        print("Domains:")
        for domain in university["domains"]:
            print("\t", domain)
    print()
