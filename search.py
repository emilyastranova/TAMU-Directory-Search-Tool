#!/usr/bin/env python3
from lxml import html
import requests
import sys


def search(search_term):
    search_term = search_term.lower()
    search_term = search_term.replace(" ", "+")
    url = "https://directory.tamu.edu/?branch=people&cn=" + search_term

    # Get HTML from URL
    page = requests.get(url)
    tree = html.fromstring(page.content)

    # Find all anchor links with the href containing /people/
    raw_links = tree.xpath('//a[contains(@href, "/people/")]/@href')
    links = set(raw_links)

    # Append https://directory.tamu.edu/ to the beginning of each link
    links = set()
    for link in raw_links:
        links.add("https://directory.tamu.edu" + link)

    # Get HTML from each link
    results = []
    if len(links) >= 50:
        print("More than the maximum number of results (50). This is a limitation of the TAMU Directory.")
    print(len(links), "results found")
    print("Checking for emails...\n")
    for link in links:
        page = requests.get(link)
        tree = html.fromstring(page.content)
        # Find email and add to list
        # Example: href="mailto:
        email = tree.xpath('//a[contains(@href, "mailto:")]/@href')
        # Find name and add to list
        # Example: <div class="result-listing">
        #          <h2>Harrison, Tyler</h2>
        name = tree.xpath('//div[@class="result-listing"]/h2/text()')
        result = {"name": "", "email": "", "link": link}
        if email:
            try:
                result["email"] = email[0].split(":")[1]
            except IndexError:
                result["email"] = email[0]
            except:
                result["email"] = "(No email found)"
        else:
            result["email"] = "(No email found)"
        if name:
            result["name"] = name[0]
        if result["name"] or result["email"]:
            results.append(result)
    return results


if __name__ == "__main__":
    search_term = ""
    if len(sys.argv) > 1:
        # Combine all arguments into one string
        for arg in sys.argv[1:]:
            search_term += arg + " "
        search_term = search_term.strip()
    else:
        search_term = input("Enter search term: ")

    results = search(search_term)
    # Print results as name: email
    for result in results:
        print("Name: " + result["name"] + "\n" + "Email: " +
              result["email"] + "\n" + "Link: " + result["link"] + "\n")

    # If no results, print error message
    if not results:
        print("No results found.")
        exit()
    # Ask user if they want to search the results for a specific email
    search_email = str(
        input("Search results for a specific email? (y/N): ")).lower()
    if search_email == "y":
        email = input("Enter email: ")
        for result in results:
            if email in result["email"]:
                print("Found!\n")
                print("Name: " + result["name"] + "\n" + "Email: " +
                      result["email"] + "\n" + "Link: " + result["link"] + "\n")
                exit()
        print("No results found.")
        exit()
