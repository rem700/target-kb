---
description: "Meta ads tracking: pixel, Conversions API, deduplication, UTM parameters and 2026 attribution. Why Ads Manager and CRM numbers differ."
---

# Tracking: how to tell the ads are working

## Why bother
Imagine teaching a dog commands without being able to see whether it obeyed. You hand out treats at random. The dog learns nothing.

Same with the ad robot. If it can't see which of the people who saw the ad actually bought, it doesn't know who to look for next. **Tracking** is how you tell the robot: "this person bought — find more like them".

## Two must-haves
**Meta Pixel**
: a small piece of code on your site. It notices what people do: open a page, add to cart, buy.

**Conversions API (CAPI)**
: the same thing, but the data comes straight from your site's server instead of the browser.

Why both? Browsers lose some information: iPhones limit tracking, many people use ad blockers, and in Europe people can refuse cookies. Pixel and CAPI together see much more. WordPress sites have ready-made plugins (Meta's official one, Stape, PixelYourSite).

!!! warning "So nothing gets counted twice"
    If both the pixel and the server report a purchase, Meta needs to know it's one purchase. For that, both messages must carry the same event number (`event_id`). Plugins usually handle this, but it's worth checking.

## Which actions to track
Meta has a standard set of "events". The most useful ones:

- `PageView` — opened a page;
- `ViewContent` — viewed a product;
- `AddToCart` — added to cart;
- `InitiateCheckout` — started checkout;
- `Purchase` — bought (always with amount and currency);
- `Lead` — left a request;
- `Contact` — tapped the phone number or WhatsApp.

## UTM tags: a label on the link
UTM tags are a little tail on a link that says where the person came from. Thanks to them, Google Analytics and your CRM know that this particular ad brought the customer. The ad has a "URL parameters" field where you can paste a ready-made line:

```
utm_source={{site_source_name}}&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}
```

Meta replaces the curly brackets with the campaign and ad names automatically.

## Attribution: who gets credit for the sale
Someone saw the ad, remembered it three days later and bought. Was that the ad's doing? The rules that decide this are called **attribution**.

What to know about Meta in 2026:

- **A purchase is credited to the ad** if the person bought within 7 days of clicking a link, or within 1 day of seeing the ad.
- **Since March 2026 a "click" means only a link click.** If someone liked or saved the ad and then bought, it goes into a separate "engage-through" column and only counts within 1 day. (official)
- As a result, reports show fewer purchases "from clicks". That doesn't necessarily mean the ads got worse — the counting just got stricter.

## Why the numbers never match
Meta Ads Manager, Google Analytics and your CRM almost never agree. Each counts by its own rules, like three witnesses of the same event.

!!! tip "Who to believe"
    For decisions, trust **real sales**: your CRM, till, bookings. Ads Manager is good for comparing ads with each other: which is better, which is worse.

Simple ways to check whether ads work:

- ask customers "how did you hear about us?";
- use a separate promo code in ads;
- pause ads for a week and see whether sales drop (allowing for the season).

## A 10-minute check
- [ ] In Events Manager open "Test events", go through the buyer's path on your site and make sure every event shows up.
- [ ] Purchases aren't doubled.
- [ ] The event your ads optimize for is arriving and isn't marked as restricted.
- [ ] Once a week compare leads in Ads Manager and in your CRM. A gap above 30% is a reason to look for a problem.

## Sources
- [Search Engine Land — click and engage-through attribution](https://searchengineland.com/meta-introduces-click-and-engage-through-attribution-updates-470629)
- [Jon Loomer — How Meta Ads attribution works in 2026](https://www.jonloomer.com/meta-ads-attribution-2026/)
- [Dataslayer — attribution window changes, January 2026](https://www.dataslayer.ai/blog/meta-ads-attribution-window-removed-january-2026)
- [Digital Applied — click-through attribution change 2026](https://www.digitalapplied.com/blog/meta-ads-click-through-attribution-change-2026-what-changed)

Checked: November 2026.

--8<-- "abbr-en.md"
