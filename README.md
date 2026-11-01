# Moocar full-site redesign concept

A responsive, five-page design study for [Moocar](https://www.moocar.com.au/): **Home, Services, The Process, Deliveries, Contact**. This is an independent review site, not the business's live website.

The site uses plain static HTML/CSS/JavaScript. Run `python build_site.py` to regenerate the pages, then preview with `python -m http.server 8000`. The published `index.html` and other pages work without a build step.

- Navigation, gallery filtering and photo lightbox are interactive.
- The contact form is **a demo only**. It never stores or sends details, and displays that warning before and after submission. Phone and email links go to the business's published contact details.
- Content is adapted from the current public site; no prices or savings amounts are invented. Business terms and eligibility should be confirmed with Moocar.
- Photos, orange pattern and Moocar logo are sourced from Moocar's current public site for this design study. They are not licensed for third-party reuse; obtain the business owner's approval before using this concept as a production site.
- Barlow Condensed and DM Sans font files are distributed under the SIL Open Font License; notices are in `licenses/`.
- The site is public but uses `noindex` and `robots.txt` to discourage indexing. Those measures do **not** make it private.

The earlier contact-only explorations remain in the separate [contact concepts repository](https://github.com/j0nathontayl0r/moocar-contact-concepts).
