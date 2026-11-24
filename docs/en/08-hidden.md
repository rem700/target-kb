# Non-obvious things

Things beginner guides don't mention but that seriously affect your money. Many of them are on by default and quietly work against you.

## 1. Boxes Meta ticks for you
Ads Manager has lots of settings that switch themselves on. Each looks harmless alone, but together they can noticeably change your ads. What to check:

**Creative enhancements**
: Meta crops the image, adds overlays and music, rewrites the text. Sometimes it helps, sometimes it ruins things. Specialists' tip: turn everything on, then everything off, save, and make sure nothing switched itself back on.

**Testing new features at account level**
: the account's advertising settings have an option for testing new creative features. Test enhancements can apply even when enhancements are off in the ad. Better to untick it.

**"Reach more people likely to respond" (location expansion)**
: ads can leave the city or country you chose. If you only work in Budapest, untick it.

**Spend on excluded placements**
: even if you removed, say, Audience Network, by default Meta spends around 5% of budget on each excluded placement. Turn it off in "Manage excluded placements".

**Budget sharing between ad sets**
: Meta can move up to 20% of the daily budget between ad sets. If each ad set's spend matters, turn it off.

**Optimized destination**
: Meta can send people to your homepage or another page instead of the one you chose. Not what you want for a promo with a specific page.

**Related media**
: images from other ad sets, even old failed tests, can get pulled into the ad.

**Empty "Description" field**
: if you leave it blank, Meta can take your page's search-engine description. Sometimes that's something completely unsuitable.

**Site links, events, promo codes**
: Meta can add links to other pages or promo codes on its own. Check and remove what you don't need.

!!! tip "Make it a habit"
    Before launch, open the "Review defaults" tab next to the ad preview. It shows what Meta switched on by itself.

## 2. A "suggestion" and a "control" are different things
When you set up an audience, age, gender, interests and your own audiences are **suggestions** by default: the robot can go beyond them. If you need a hard limit (say, a service only for adults or only for women), set them as controls and untick "Use as a suggestion".

!!! example "Anya's example"
    Anya sets age 25–55 as a suggestion. A week later she sees 40% of the budget went to 18–24-year-olds, who rarely buy. Options: make age a hard control, or use value rules (see point 5).

## 3. Similar ads get merged
Andromeda groups ads that are similar in meaning and look into one "entity" (specialists call it an Entity ID). One such group gets one "seat" in the selection. So 30 nearly identical videos can act as one, and Meta will only spend on a few of them. (practice)

- Specialists observe that delivery gets limited once ads are more than about 60% similar. That's not an official Meta figure. (practice)
- Some accounts have a Creative Similarity report in the analytics section.

**Takeaway:** don't churn out versions with a different button colour. Make different ideas: problem, review, process, gift, humour.

## 4. Ads from a creator's account work better
**Partnership ads** run under two accounts at once: yours and a creator's (or another brand's). According to Meta, adding partnership ads to regular ones gives on average a 19% lower cost per action and 13% higher CTR. (official)

Why it works: the creator brings a new face, a new angle and a new audience — for Andromeda, a new "entity".

!!! example "Anya's example"
    A local creator films herself unboxing a candle and lighting it in the evening. Anya runs this video as a partnership ad: both accounts show in the header. It doesn't have to be expensive — sometimes a gift and an agreement are enough.

## 5. Value rules: "I'll pay more for these people"
**Value rules** let you tell Meta: "this group is worth more to me, bid higher for them" or "this one is worth less, bid lower". For example by age, gender, location or placement. They're set up in the account's Advertising settings. (official)

The big plus: you steer the budget without turning off the Advantage+ autopilot or hard-narrowing the audience. Lately Meta itself actively suggests value rules instead of restrictions. (practice)

## 6. Audience segments: how much goes to people who already know you
In Advertising settings you can define your **existing customers** and **engaged audience** (lists, site visitors, followers). Reports then show how much budget went to new people and how much to people who already know you.

Why: the algorithm likes showing ads to people who were about to buy anyway — cheap, easy results. The report looks great, but there are few new customers. Segments reveal this. (practice)

## 7. Leads: teach the robot to tell good from bad
A regular lead campaign looks for people who will **submit** a form. Not people who will **buy**. Hence lots of junk.

The fix is the **Conversion Leads** goal plus a CRM connection. You tell Meta which leads became customers, and the robot looks for similar people. According to Meta, this gives on average a 21% lower cost per quality lead for instant forms. (official)

Details:

- Works with Meta instant forms.
- Pick a CRM stage that predicts a sale and happens within 28 days of the lead. Roughly 1% to 40% of leads should reach that stage. (official)
- You can't change the optimization goal of a published campaign. Duplicate it and change it in the copy. (official)
- You can connect a CRM without a developer through Make or Zapier.

## 8. Long buying cycle — the report undercounts
By default Meta credits a purchase if it happens within 7 days of a click. If your customers take longer to decide (an expensive service, a wedding, a renovation), some ad-driven purchases won't appear in the report. Ads may work better than Ads Manager shows. Check against your CRM.

## 9. "Opportunity score" is advice, not orders
Ads Manager has an **Opportunity Score**: a score from 0 to 100 and a list of recommendations, each worth points. (official) Many are useful, but they don't know your economics or goals. Don't apply everything just to raise the score.

## 10. Small things that save your nerves
- **Automatic Advanced Matching** in pixel settings: turn it on. Meta recognises people better by hashed email and phone.
- **Allowed domains** for the pixel: add all your domains, otherwise some conversions may be ignored.
- **Ad scheduling** (daytime only, weekdays only) works only with a lifetime budget, not a daily one.
- **Spending limits** on the campaign and account: if ads suddenly stopped, check whether you hit an old limit.
- **Moving an ad by post ID** keeps likes and comments. The more real comments, the more trust — and, by many accounts, the better the ad performs.

## Sources
- [Anar Agency — Meta Ads settings to turn off](https://anaragency.com/blog/hidden-meta-ads-settings/)
- [AdsUploader — Andromeda and Entity IDs](https://adsuploader.com/blog/meta-andromeda)
- [eMarketer — Meta expands partnership ads](https://www.emarketer.com/content/meta-expands-partnership-ads-turn-creator-content-performance)
- [Jon Loomer — Value rules deep dive](https://www.jonloomer.com/value-rules/)
- [Jon Loomer — Opportunity Score explained](https://www.jonloomer.com/opportunity-score-campaign-score/)
- [Meta for Developers — Conversions API for CRM](https://developers.facebook.com/docs/marketing-api/conversions-api/conversion-leads-integration)
- [Zapier — Meta CAPI for CRM and lead quality](https://zapier.com/blog/meta-guide-to-better-lead-quality/)

Checked: November 2026.

--8<-- "abbr-en.md"
