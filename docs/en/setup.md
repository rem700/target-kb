# Setting up from scratch

Before your first ad, you need to assemble the "kit": a business account, a Page, Instagram, an ad account, payment and a pixel. Order matters: skip a step and things start "not connecting" later. It takes 30–60 minutes.

!!! tip "Why so complicated"
    The Boost button in Instagram works without any of this. But without a business portfolio you get no proper Ads Manager, no pixel, no access for helpers and no protection against losing the account. Setting it up right once is cheaper than rescuing it later.

## What you'll need
- A personal Facebook profile (real, in your name, not brand new — fresh "empty" profiles get blocked more often).
- A work email you definitely have access to.
- Instagram switched to a professional account (Business or Creator).
- A website (if ads will lead there) and access to its settings.
- A bank card in the company's or your name.

## Step 1. Business portfolio
This is the "folder" that holds everything: Pages, Instagram, ad accounts, pixels, people with access.

1. Go to business.facebook.com and create a business portfolio.
2. Enter the business name, your name and work email.
3. Confirm the email via the link in the message — the portfolio isn't fully active until you do.

## Step 2. Facebook Page
Instagram ads are also shown "on behalf of" a Facebook Page, so you need one.

- Create the Page inside the portfolio (then it's owned by it from the start) or add an existing one.
- Make sure the Page is **owned** by your portfolio, not stuck on a personal profile or with a former contractor.

## Step 3. Instagram
1. In the Instagram app, switch to a professional account if you haven't yet.
2. Connect Instagram to the Facebook Page (Page settings → Linked accounts → Instagram).
3. Check that Instagram appears in the business portfolio under "Instagram accounts".

!!! warning "A common trap"
    Adding Instagram to the portfolio and connecting it to the Page are two different actions. You need both.

## Step 4. Ad account
1. In portfolio settings, create an ad account.
2. Choose the **currency and time zone** carefully: you can't change them later and would have to create a new account. For Hungary, euros or forints and the Budapest time zone make sense.
3. Make yourself the ad account admin.

## Step 5. Payment
Add a payment method to the ad account. How Meta charges, which options exist and how to get invoices for your company is covered in [Payment, invoices and taxes](billing.md).

## Step 6. Pixel and CAPI
1. In Events Manager, create a dataset (pixel).
2. Install it on your site: for WordPress the easiest way is a plugin (Meta's official one, PixelYourSite, Stape).
3. Connect the Conversions API (often with the same plugin).
4. Check in "Test events" that events arrive. More in [Tracking](04-tracking.md).

## Step 7. Domain verification
Verification tells Meta the site is yours. There are three methods: a DNS TXT record, a meta tag on the site, or uploading an HTML file to the site root. A DNS record or a meta tag via an SEO plugin is easiest.

## Step 8. Security and access
- Two-factor authentication for you and everyone with access.
- A **second portfolio admin** — someone you trust. If your profile is blocked or hacked, without a second admin you can lose everything.
- Give contractors access as **partners** with rights only to the ad account they need, rather than making them portfolio admins.
- Business verification isn't required to start, but may be needed for some features and higher limits.

## Final checklist
- [ ] Business portfolio created, email confirmed
- [ ] Facebook Page owned by the portfolio
- [ ] Instagram is professional, connected to the Page and to the portfolio
- [ ] Ad account created with the right currency and time zone
- [ ] Payment method added, company details and VAT number entered (if you have one)
- [ ] Pixel and CAPI working, events visible in "Test events"
- [ ] Domain verified
- [ ] Two-factor authentication on, second admin added

## Sources
- [Meta for Developers: domain verification](https://developers.facebook.com/documentation/sharing/domain-verification/verifying-your-domain)
- [Shopify: setting up a Meta business portfolio step by step](https://www.shopify.com/au/blog/business-manager-facebook)
- [Leadsie: what you need to run Meta ads](https://www.leadsie.com/blog/meta-ads-prerequisites)

Checked: November 2026.

--8<-- "abbr-en.md"
