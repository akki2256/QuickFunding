# -*- coding: utf-8 -*-
"""Generate submenu pages from partials/header.html and partials/footer.html."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
HEAD = '''<!DOCTYPE html>
<html lang="en-AU">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Quick Funding</title>
  <link rel="stylesheet" href="css/styles.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
</head>
<body>
'''
MAIN_TPL = '''
  <main>
    <div class="page-header"><div class="container"><h1>{title}</h1></div></div>
    <div class="page-content">
      <p>Content for {title} will go here. Quick Funding helps Australian businesses access finance from 90+ lenders.</p>
      <p><a href="index.html" class="btn btn-primary">Back to Home</a></p>
    </div>
  </main>
'''
TAIL = '''
  <script src="js/main.js"></script>
</body>
</html>
'''

PAGES = [
    ("General Business Loan", "general-business-loan.html"),
    ("Business Term Loan", "business-term-loan.html"),
    ("Trade Finance", "trade-finance.html"),
    ("Invoice Finance", "invoice-finance.html"),
    ("Business Line of Credit", "business-line-of-credit.html"),
    ("Merchant Cash Advance", "merchant-cash-advance.html"),
    ("Business Overdrafts", "business-overdrafts.html"),
    ("Debt Consolidation", "debt-consolidation.html"),
    ("Secured Term Loan", "secured-term-loan.html"),
    ("Vehicle Finance (Cars, Vans, Trucks)", "vehicle-finance.html"),
    ("Equipment Finance", "equipment-finance.html"),
    ("Lease Agreement", "lease-agreement.html"),
    ("Heavy Machinery Loans", "heavy-machinery-loans.html"),
    ("Business Acquisition Loan", "business-acquisition-loan.html"),
    ("Construction Finance", "construction-finance.html"),
    ("Hospitality Finance", "hospitality-finance.html"),
    ("Healthcare Finance", "healthcare-finance.html"),
    ("Manufacturing Finance", "manufacturing-finance.html"),
    ("Fitness Finance", "fitness-finance.html"),
    ("Livestock Finance", "livestock-finance.html"),
    ("Professional Services Finance", "professional-services-finance.html"),
    ("Retail Finance", "retail-finance.html"),
    ("Agriculture Finance", "agriculture-finance.html"),
    ("Sole Trader Finance", "sole-trader-finance.html"),
    ("Veterinary Finance", "veterinary-finance.html"),
    ("Blog", "blog.html"),
    ("Media", "media.html"),
    ("Guides and Whitepapers", "guides-whitepapers.html"),
    ("Glossary", "glossary.html"),
    ("Business Loan Calculator", "calculator-business-loan.html"),
    ("Car Finance Calculator", "calculator-car.html"),
    ("Truck Loan Calculator", "calculator-truck.html"),
    ("EV Car Loan Calculator", "calculator-ev-car.html"),
    ("Premium Car Loan Calculator", "calculator-premium-car.html"),
    ("Refinance Calculator", "calculator-refinance.html"),
    ("About", "about.html"),
    ("Careers", "careers.html"),
    ("Our Difference", "our-difference.html"),
    ("Enterprise Solutions", "enterprise-solutions.html"),
    ("Enterprise Developers", "enterprise-developers.html"),
    ("Partners Overview", "partners-overview.html"),
    ("Partners Toolkit", "partners-toolkit.html"),
]

def main():
    with open(os.path.join(BASE, "partials", "header.html"), "r", encoding="utf-8") as f:
        header = f.read()
    with open(os.path.join(BASE, "partials", "footer.html"), "r", encoding="utf-8") as f:
        footer = f.read()
    for title, filename in PAGES:
        html = HEAD.format(title=title) + header + MAIN_TPL.format(title=title) + footer + TAIL
        path = os.path.join(BASE, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print("Wrote", filename)
    print("Done. Generated", len(PAGES), "pages.")

if __name__ == "__main__":
    main()
