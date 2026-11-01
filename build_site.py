#!/usr/bin/env python3
"""Generate the five static, responsive Moocar design-concept pages."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent
SITE = "Moocar — independent site redesign concept"
NAV = [("Home", "index.html"), ("Services", "services.html"), ("The process", "process.html"), ("Deliveries", "gallery.html"), ("Contact", "contact.html")]


def header(active):
    links = "".join(f'<a href="{href}"{(" aria-current=\"page\"" if href == active else "")}>{name}</a>' for name, href in NAV)
    mobile = "".join(f'<a href="{href}"{(" aria-current=\"page\"" if href == active else "")}>{name}</a>' for name, href in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<div class="concept">INDEPENDENT DESIGN CONCEPT · NOT THE LIVE MOOCAR SITE · FORMS DO NOT SEND</div>
<header class="site-header"><div class="wrap header-inner">
<a class="logo" href="index.html" aria-label="Moocar concept home"><img src="assets/logo.png" alt="Moocar" width="156" height="51"></a>
<nav class="desktop-nav" aria-label="Main navigation">{links}</nav>
<a class="btn header-cta" href="contact.html">Get in touch <span aria-hidden="true">↗</span></a>
<button class="menu-toggle" type="button" aria-label="Toggle menu" aria-controls="mobile-nav" aria-expanded="false"><span></span></button>
</div><nav class="mobile-nav" id="mobile-nav" aria-label="Mobile navigation" hidden>{mobile}<a class="btn" href="tel:1800950222">Call 1800 950 222</a></nav></header>'''


def footer():
    return '''<footer class="site-footer"><div class="wrap"><div class="footer-top">
<div><img class="footer-logo" src="assets/logo.png" alt="Moocar" width="190" height="62"><p>New car advice, sourcing and delivery — without doing all the searching yourself.</p><a class="btn" href="contact.html">Talk to Moocar <span aria-hidden="true">↗</span></a></div>
<div><h2>Explore</h2><a href="services.html">Services</a><a href="process.html">The process</a><a href="gallery.html">Deliveries</a><a href="contact.html">Contact</a></div>
<div><h2>Contact</h2><a href="tel:1800950222">1800 950 222</a><a href="mailto:info@moocar.com.au">info@moocar.com.au</a><p>526/368 Sussex St<br>Sydney NSW 2000<br>Monday–Friday · 8am–6pm</p></div>
</div><div class="footer-bottom"><span>Independent redesign concept for review · not operated by Moocar</span><span><a href="https://www.moocar.com.au/terms-and-conditions" target="_blank" rel="noopener">Live-site terms</a> · <a href="https://www.moocar.com.au/copy-of-terms-and-conditions" target="_blank" rel="noopener">Live-site privacy</a> · <a href="https://www.moocar.com.au/" target="_blank" rel="noopener">Current website ↗</a></span></div></div></footer>'''


def cta(title="READY TO GET MOOVING?", copy="Tell Moocar what you’re looking for, or just call and talk it through."):
    return f'''<section class="cta-band"><div class="wrap"><div><p class="eyebrow">Your next move</p><h2 class="section-heading">{title}</h2><p>{copy}</p></div><a class="btn btn-dark" href="contact.html">Start a conversation <span aria-hidden="true">↗</span></a></div></section>'''


def page(name, current, content, description):
    return f'''<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><meta name="theme-color" content="#161615"><meta name="description" content="{escape(description, quote=True)}"><title>{escape(name)} · Moocar redesign concept</title><link rel="preload" as="font" type="font/woff2" href="assets/barlow-condensed-700.woff2" crossorigin><link rel="stylesheet" href="styles.css"><script src="site.js" defer></script></head><body>{header(current)}<main id="main">{content}</main>{footer()}</body></html>'''

HOME = '''<section class="home-hero on-dark"><div class="wrap"><div class="hero-copy"><p class="eyebrow">New cars. Smarter buying.</p><h1 class="display">YOUR NEXT CAR.<br><em>LESS</em><br>RUNAROUND.</h1><p>Moocar sources brand-new cars through its dealer network, helping you compare availability and fleet pricing without chasing dealerships yourself.</p><div class="hero-actions"><a class="btn" href="contact.html">Find your next car <span aria-hidden="true">↗</span></a><a class="btn btn-outline" href="process.html">See how it works</a></div></div><div class="hero-image"><img src="assets/gallery-05.webp" alt="White new car with a large orange bow at a Moocar handover" width="1400" height="1050" fetchpriority="high"><span class="hero-label">From the Moocar delivery gallery</span></div></div></section>
<div class="statement"><div class="wrap"><span>YOU PICK THE CAR. WE DO THE LEGWORK.</span><span>NEW CAR ADVICE / DEALER SEARCH / DELIVERY</span></div></div>
<section class="home-intro"><div class="wrap intro-grid"><div><p class="eyebrow">What Moocar does</p><h2 class="section-heading">A BETTER ROUTE TO A NEW CAR.</h2></div><div><p>Whether you know the exact model or you’re still weighing options, Moocar helps you find the right new car and reaches out to dealers nationally for pricing and availability.</p><p>Ask about finance, a trade-in, or delivery to your home or workplace. Moocar also offers an employee benefit that passes on fleet discounts for a small fee.</p><a class="btn btn-dark" href="services.html">Explore the services <span aria-hidden="true">↗</span></a></div></div></section>
<section class="service-preview"><div class="wrap"><div class="section-bar"><div><p class="eyebrow">One place to start</p><h2 class="section-heading">MORE THAN THE PRICE TAG.</h2></div><p>The car is only part of the decision. Sort the details in one conversation.</p></div><div class="preview-row"><div class="preview-photo"><img src="assets/gallery-13.webp" loading="lazy" alt="New SUV ready for delivery with an orange bow" width="1400" height="1050"></div><div class="preview-copy"><div><p class="eyebrow">From search to handover</p><h3>THE WHOLE JOURNEY.</h3><p>Moocar can help source your new car, discuss finance and trade-in options, and arrange delivery.</p><ul><li>New car advice and sourcing</li><li>Finance options</li><li>Trade-ins</li><li>Delivery to home or work</li></ul></div><a class="btn btn-dark" href="services.html">See all services <span aria-hidden="true">↗</span></a></div></div></div></section>
<section class="process-strip on-dark"><div class="wrap"><div class="section-bar"><div><p class="eyebrow">The process</p><h2 class="section-heading">FOUR STEPS.<br>ONE NEW CAR.</h2></div><p>From choosing the vehicle to collecting the keys, here’s how Moocar describes the journey.</p></div><div class="mini-steps"><div class="mini-step"><span class="num">01</span><h3>Choose</h3><p>Know the model? Great. Need help deciding? Start there.</p></div><div class="mini-step"><span class="num">02</span><h3>Search</h3><p>Moocar asks its dealer network for pricing and availability.</p></div><div class="mini-step"><span class="num">03</span><h3>Finance</h3><p>Discuss a finance option suited to your needs if required.</p></div><div class="mini-step"><span class="num">04</span><h3>Deliver</h3><p>Collect at the dealer or arrange home or workplace delivery.</p></div></div><a class="btn" href="process.html">Walk through the process <span aria-hidden="true">↗</span></a></div></section>
<section class="proof"><div class="wrap"><div class="section-bar"><div><p class="eyebrow">Real deliveries</p><h2 class="section-heading">THE BEST PART? THE HANDOVER.</h2></div><a class="btn btn-dark" href="gallery.html">View the gallery <span aria-hidden="true">↗</span></a></div><div class="proof-grid"><figure><img src="assets/gallery-02.webp" loading="lazy" alt="New car handover at a dealership with an orange bow" width="1050" height="1400"><figcaption>Moocar deliveries</figcaption></figure><figure><img src="assets/gallery-03.webp" loading="lazy" alt="Black Porsche with a ribbon at delivery" width="480" height="640"><figcaption>New cars</figcaption></figure><figure><img src="assets/gallery-16.webp" loading="lazy" alt="A group of white vehicles sourced for a business" width="768" height="1024"><figcaption>Business vehicles</figcaption></figure></div></div></section>''' + cta()

SERVICES = '''<section class="page-head on-dark"><div class="wrap"><div><p class="eyebrow">What we do</p><h1 class="display-medium">ALL THE CAR.<br>LESS OF THE CHASE.</h1></div><p>From finding a brand-new car to working through the details around it, Moocar brings the search, the options and the handover together.</p></div></section>
<section class="services-list"><div class="wrap"><p class="eyebrow">The services</p>
<div class="service-entry"><span class="n">01</span><h2>New car sourcing</h2><p>Tell Moocar what you’re after. Its car experts can help with your decision, then contact a national dealer network to compare price and availability.</p></div>
<div class="service-entry"><span class="n">02</span><h2>Finance options</h2><p>Talk through a finance option that fits your situation. Ask for the full terms, costs and eligibility before deciding.</p></div>
<div class="service-entry"><span class="n">03</span><h2>Trade-ins</h2><p>Looking to move on your current car? Moocar can discuss a trade-in value and potentially arrange pickup when your new car arrives.</p></div>
<div class="service-entry"><span class="n">04</span><h2>Delivery</h2><p>Pick up your new car from the dealership, or discuss delivery to your home or workplace.</p></div>
<div class="service-entry"><span class="n">05</span><h2>Business vehicles</h2><p>Moocar also works with businesses looking for company vehicles and can explore manufacturer discounts where available.</p></div>
<div class="service-entry"><span class="n">06</span><h2>Servicing &amp; warranty</h2><p>Ask about applicable manufacturer warranties and servicing packages when comparing your options.</p></div>
</div></section>
<section class="service-feature on-dark"><img src="assets/corporate-event.webp" loading="lazy" alt="Vehicle showcased at a Moocar corporate event" width="1400" height="1050"><div class="service-feature-copy"><p class="eyebrow">For corporate partners</p><h2 class="section-heading">MAKE AN ENTRANCE.</h2><p>Moocar can arrange for a new vehicle to be showcased at a corporate event. Talk through the event and what would work for your audience.</p><a class="btn" href="contact.html">Enquire about events <span aria-hidden="true">↗</span></a></div></section>
<div class="wrap service-note">Finance, trade-in, delivery and any discount or fee are subject to the details of your enquiry. Confirm terms directly with Moocar.</div>''' + cta("WHAT ARE YOU LOOKING FOR?", "Whether you have a model in mind or need some advice, start with a conversation.")

PROCESS = '''<section class="page-head orange-head"><div class="wrap"><div><p class="eyebrow">The process</p><h1 class="display-medium">FROM "MAYBE"<br>TO "IT'S MINE."</h1></div><p>A straightforward four-step route from the first question to the new-car handover.</p></div></section>
<section class="process-main"><div class="wrap process-layout"><aside class="process-aside"><p class="eyebrow">How it works</p><h2 class="section-heading">LESS BACK<br>&amp; FORTH.</h2><p>Moocar does the dealer searching so you can focus on the car you want and the options that matter.</p><a class="btn btn-dark" href="contact.html">Talk through your options <span aria-hidden="true">↗</span></a></aside>
<div><div class="process-list"><article class="process-item"><span class="n">01</span><div><h2>Choose the car</h2><p>Know the exact new car you’re after? Tell Moocar. Still exploring? Its team can help narrow down the choice.</p></div></article>
<article class="process-item"><span class="n">02</span><div><h2>Search the dealers</h2><p>Moocar puts a quote request to its dealer network to compare pricing and availability for your chosen vehicle.</p></div></article>
<article class="process-item"><span class="n">03</span><div><h2>Discuss finance</h2><p>If finance is part of your plan, ask about options suited to your needs and review the terms before committing.</p></div></article>
<article class="process-item"><span class="n">04</span><div><h2>Take delivery</h2><p>Pick up from the dealership, or arrange delivery to your home or workplace where available.</p></div></article></div>
<img class="process-photo" src="assets/gallery-14.webp" loading="lazy" alt="Customer beside a new car with a blue delivery bow" width="960" height="1280"><p class="process-footnote">Manufacturer warranty and servicing arrangements vary by vehicle. Confirm the details of your quote directly with Moocar.</p></div></div></section>''' + cta("LET'S FIND YOUR CAR.", "Tell Moocar what you have in mind — even if you're still deciding.")

ALTS = [
("Two people beside a newly delivered dark SUV", "handover"),
("Two people with a black SUV wearing an orange bow", "handover"),
("Black Porsche with a ribbon at handover", "vehicle"),
("New ute with an orange delivery bow", "handover"),
("White car with a large orange bow beside a customer", "handover"),
("Two people beside a new ute at the dealership", "handover"),
("Customer beside a grey SUV with an orange bow", "handover"),
("White SUV ready for a new owner", "vehicle"),
("New white car with an orange bow and its owner", "handover"),
("Grey car at a dealership", "vehicle"),
("Blue convertible with a delivery bow and customer", "handover"),
("White performance car inside a dealership", "vehicle"),
("Grey SUV wearing a bow inside a dealership", "vehicle"),
("White Mercedes with a blue bow and customer", "handover"),
("Dark SUV with an orange delivery bow", "vehicle"),
("Line of white business vehicles", "fleet"),
("Business vehicle on a transport trailer", "fleet"),
("Line of white vehicles outside a workplace", "fleet"),
("Blue MG with a red bow and customer", "handover"),
("New black SUV with a red bow and customer", "handover"),
("Blue business truck", "fleet"),
]
assert len(ALTS) == 21
GALLERY_ITEMS = "\n".join(f'<button type="button" class="gallery-item" data-category="{cat}" aria-label="Open photo: {escape(alt, quote=True)}"><img src="assets/gallery-{i:02}.webp" loading="lazy" width="500" height="600" alt="{escape(alt, quote=True)}"></button>' for i,(alt,cat) in enumerate(ALTS,1))
GALLERY = '''<section class="page-head on-dark"><div class="wrap"><div><p class="eyebrow">The gallery</p><h1 class="display-medium">THE GOOD<br>PART.</h1></div><p>Real cars, real handovers and some of the business vehicles featured in Moocar’s current gallery.</p></div></section>
<section class="wrap"><div class="gallery-intro"><div><p class="eyebrow">Moocar deliveries</p><h2 class="section-heading">OUT THE DOOR.</h2></div><p>Browse the moments when the search is done and the keys are handed over.</p></div><div class="filters" role="group" aria-label="Filter photos"><button type="button" class="filter" data-filter="all" aria-pressed="true">All photos</button><button type="button" class="filter" data-filter="handover" aria-pressed="false">Handovers</button><button type="button" class="filter" data-filter="vehicle" aria-pressed="false">New cars</button><button type="button" class="filter" data-filter="fleet" aria-pressed="false">Business vehicles</button></div><div class="gallery-grid">''' + GALLERY_ITEMS + '''</div></section>
<dialog class="lightbox" aria-label="Gallery image"><div class="lightbox-head"><p></p><button type="button" class="lightbox-close" aria-label="Close image">×</button></div><img alt=""></dialog>''' + cta("YOUR TURN NEXT?", "Tell Moocar the kind of car you’d like to see in your driveway.")

CONTACT = '''<section class="page-head orange-head"><div class="wrap"><div><p class="eyebrow">Get in touch</p><h1 class="display-medium">LET'S TALK<br>NEW CARS.</h1></div><p>Know what you want? Have a quote already? Or just want someone to walk through the options with you? Start here.</p></div></section>
<section class="contact-main"><div class="wrap contact-layout"><div><p class="eyebrow">Direct to Moocar</p><h2 class="section-heading">A QUICK CHAT GOES A LONG WAY.</h2><div class="contact-methods">
<div class="contact-method"><small>Call</small><a href="tel:1800950222">1800 950 222 ↗</a><p>Monday to Friday, 8am–6pm Sydney time</p></div>
<div class="contact-method"><small>Email</small><a href="mailto:info@moocar.com.au?subject=New%20car%20enquiry">info@moocar.com.au ↗</a><p>Tell Moocar about the car you’re looking for.</p></div>
<div class="contact-method"><small>Visit</small><a href="https://maps.google.com/?q=368+Sussex+St+Sydney+NSW+2000" target="_blank" rel="noopener">Find the office ↗</a><p>526/368 Sussex St, Sydney NSW 2000</p></div></div></div>
<div><form class="contact-form" id="contact-form"><h2>TELL US WHAT YOU'RE AFTER.</h2><p>Explore how a simpler enquiry form could work. This is a concept: pressing the button does <strong>not</strong> send anything.</p>
<div class="field-row"><div class="field"><label for="name">Your name *</label><input id="name" name="name" autocomplete="name" required></div><div class="field"><label for="phone">Mobile *</label><input id="phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" required></div></div>
<div class="field"><label for="email">Email *</label><input id="email" name="email" type="email" autocomplete="email" required></div>
<div class="field"><label for="car">Car you have in mind</label><input id="car" name="car" placeholder="Make / model, or 'not sure yet'"></div>
<div class="field"><label for="quoted">Already received a quote?</label><select id="quoted" name="quoted"><option value="">Select an option</option><option>Yes — I'd like to compare it</option><option>No, not yet</option></select></div>
<div class="field"><label for="message">Anything else Moocar should know?</label><textarea id="message" name="message" placeholder="Trade-in, finance, timing, or any questions"></textarea></div>
<button class="btn btn-dark" type="submit">Preview enquiry <span aria-hidden="true">↗</span></button><p class="form-note">* Required for the demo. No data is stored or transmitted. To contact the real business, use the call or email links alongside.</p><div class="demo-result" role="status" tabindex="-1"><strong>Prototype only — no enquiry was sent.</strong><br>Use the phone or email links to reach Moocar directly.</div></form>
<div class="contact-map"><p><strong>Moocar · Sydney</strong><small>526/368 Sussex St, Sydney NSW 2000</small></p><a href="https://maps.google.com/?q=368+Sussex+St+Sydney+NSW+2000" target="_blank" rel="noopener">Open directions ↗</a></div></div></div></section>'''

PAGES = [
    ("index.html", "A better way to get mooving", HOME, "A responsive full-site redesign concept for Moocar's new-car sourcing service."),
    ("services.html", "Services", SERVICES, "Explore Moocar's new car sourcing, finance, trade-in, delivery, business and event services."),
    ("process.html", "The process", PROCESS, "How Moocar helps select, source, finance and deliver a new car."),
    ("gallery.html", "Deliveries", GALLERY, "Photos from the Moocar delivery gallery."),
    ("contact.html", "Contact", CONTACT, "Contact Moocar by phone or email; explore a contact form redesign concept."),
]
for filename, name, content, description in PAGES:
    destination = ROOT / filename
    destination.write_text(page(name, filename, content, description), encoding="utf-8")
    print(filename, destination.stat().st_size)
