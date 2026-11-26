import os
import re
import glob
import requests

ORCID_ID = "0000-0001-9927-3938"
ORCID_API = "https://" + "pub.orcid.org/v3.0/" + ORCID_ID + "/works"
HEADERS = {"Accept": "application/json"}

def get_crossref_authors(doi):
    """Fetch clean full author list from Crossref using DOI."""
    if not doi:
        return ""
    try:
        api_url = "https://" + "api.crossref.org/works/" + doi
        r = requests.get(api_url, timeout=10)
        if r.status_code == 200:
            authors = r.json().get("message", {}).get("author", [])
            names = []
            for a in authors:
                given = a.get("given", "")
                family = a.get("family", "")
                full = f"{given} {family}".strip()
                if "Caihao Qiu" in full or (family == "Qiu" and given.startswith("C")):
                    full = f"<b>{full}</b>"
                names.append(full)
            return ", ".join(names)
    except Exception:
        pass
    return ""

def main():
    resp = requests.get(ORCID_API, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    groups = resp.json().get("group", [])

    os.makedirs("_publications", exist_ok=True)
    for old_file in glob.glob("_publications/*.md"):
        os.remove(old_file)

    for group in groups:
        summaries = group.get("work-summary", [])
        if not summaries:
            continue
        work = summaries[0]

        # Title
        title_obj = work.get("title", {}).get("title", {})
        title = title_obj.get("value", "Untitled").replace('"', "'") if title_obj else "Untitled"

        # Venue / Journal
        journal_obj = work.get("journal-title")
        venue = journal_obj.get("value", "Preprint").replace("'", "&apos;") if journal_obj else "Preprint"

        # Date (Year-Month-Day)
        pub_date = work.get("publication-date") or {}
        year = (pub_date.get("year") or {}).get("value") or "2026"
        month = (pub_date.get("month") or {}).get("value") or "01"
        day = (pub_date.get("day") or {}).get("value") or "01"
        date_str = f"{year}-{month.zfill(2)}-{day.zfill(2)}"

        # DOI & URL
        doi = ""
        url = ""
        ext_ids = (work.get("external-ids") or {}).get("external-id", [])
        for eid in ext_ids:
            if eid.get("external-id-type") == "doi":
                doi = eid.get("external-id-value", "")
                url = "https://" + "doi.org/" + doi
                break
        if not url and work.get("url"):
            url = work["url"].get("value", "")

        # Category
        work_type = work.get("type", "")
        category = "conferences" if "conference" in work_type else "manuscripts"

        # Authors via Crossref DOI lookup
        authors = get_crossref_authors(doi) or "<b>Caihao Qiu</b>"

        # Build filename and citation
        slug = re.sub(r"[^a-zA-Z0-9_-]", "", title.replace(" ", "-"))
        slug = re.sub(r"-+", "-", slug).strip("-")[:65]
        filename = f"_publications/{date_str}-{slug}.md"

        citation = f'{authors}. ({year}). &quot;{title}.&quot; <i>{venue}</i>.'
        if doi:
            citation += f" DOI: {doi}"

        md_content = f"""---
title: "{title}"
authors: "{authors}"
collection: publications
category: {category}
permalink: /publication/{date_str}-{slug}
date: {date_str}
venue: '{venue}'
paperurl: '{url}'
citation: '{citation}'
---
"""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"Synced: {filename}")

if __name__ == "__main__":
    main()
