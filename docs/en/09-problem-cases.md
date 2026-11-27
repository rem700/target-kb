---
description: "14 common Meta and TikTok ad problems with fixes: junk leads, disabled or hacked ad accounts, Learning Limited, high CPM and more."
---

# Problem cases

Real situations almost everyone who runs ads ends up in. Each one has: what you see, why it happens, what to do right now, and how to avoid it next time.

!!! tip "How to use this"
    Find your symptom in the headings on the right and start with "What to do". If that doesn't help, see [Tests and problems](05-testing.md) for the general first-aid kit.

---

## 1. "I pressed Boost — lots of likes, zero sales"
**What you see.** Anya boosted a post with the Boost button right in Instagram. Hundreds of likes and a couple of new followers came in, but the website is silent.

**Why.** Boost is a simplified version of ads. By default it looks for people who like and watch, not people who buy. There are almost no settings and no tracking.

**What to do.** Run ads through Ads Manager with the "Sales" or "Leads" objective and a connected pixel.

**How to avoid it.** Boost is fine only for reach: an announcement, an event, a nice post. For money — Ads Manager.

---

## 2. "Leads at 1 € each, but they're junk"
**What you see.** Lots of cheap leads. But half the phones don't answer, names look like "asdf", and some people swear they never filled anything in.

**Why.** Three common reasons:

- **Autofill.** The instant form fills in name and phone automatically, and people tap "Submit" almost by accident.
- **Bots and click farms.** Easy forms attract bots, and some junk comes from Meta's partner sites (Audience Network). The algorithm learns from every "conversion", so if bots get rewarded, it goes looking for more of them.
- **The "Leads" objective** asks the robot to find people who will fill in a form, not people who will buy.

**What to do.**

- Switch the form to "Higher intent" (with a review screen).
- Add 1–2 screening questions with answer options: "When are you planning?", "What's your budget?". Such a question discourages spam and clarifies intent.
- Check the breakdown by placement. If leads come from Audience Network, exclude it for lead campaigns.
- Mark junk leads in your CRM and connect the "Conversion Leads" goal (see [Non-obvious things](08-hidden.md)).

**How to avoid it.** Count the cost per **customer**, not per lead. A 1 € lead that never buys costs more than a 10 € lead that does.

---

## 3. "Leads come in, customers don't — and the leads look fine"
**What you see.** The people are real, but almost none of them buy.

**Why.** Often the problem isn't the ads but what happens afterwards. Lead quality is largely decided outside the ads: by how fast you reply, whether your emails land in spam, by your sales process and automation.

**What to do.**

- Reply within 5–15 minutes. A day later people no longer remember leaving a request.
- Set up automatic export of leads to a CRM, spreadsheet or email. Leads that just sit in Meta's interface are easy to miss, and they're only stored there for a limited time.
- Check that your emails aren't going to spam.

**How to avoid it.** Before launch, go through the customer journey yourself: leave a request and time when and how you get a reply.

---

## 4. "My ad account got disabled"
**What you see.** An email: "Your ad account has been disabled for violating our policies". Ads have stopped.

**Why.** Most often because of advertising policy violations (sometimes cumulative: several rejected ads in a row), payment issues or suspicious activity (a new account, sudden spending, logins from different countries).

**What to do.**

1. **Find out what exactly is blocked.** It can be the ad account, the business portfolio or your personal profile. The appeal must be filed on the level that was actually hit: if your profile is restricted, requesting a review of the ad account does nothing.
2. Open Account Quality in Business Support Home and read the reason.
3. Remove or fix violating ads before appealing.
4. Submit a calm, factual review request.
5. Don't wait: you only have 180 days to appeal, after which the block becomes permanent.

How to contact support and pass an identity check — see [Meta support and outages](support.md).

**How to avoid it.** Don't create a new ad account to get around a block: Meta links accounts, and the ban will spread. Verified business, two-factor authentication, no sudden budget jumps on a fresh account.

---

## 5. "My card was charged for ads I never ran"
**What you see.** Charges from Meta, campaigns you didn't create, sometimes new admins or a changed spending limit.

**Why.** The account was hacked. Often through phishing: an email or message "from Meta support" saying your page is about to be blocked, with an "appeal" link. Hackers change payment settings, raise the spending limit and run their own ads on your money.

**What to do (in order).**

1. Call your bank and report the unauthorized charges. Block the card if needed.
2. Change your Facebook and email passwords and turn on two-factor authentication.
3. In Business settings, check people, partners and payment methods. Remove unknown partners and business portfolios: they can keep access even after passwords change.
4. Stop the foreign campaigns.
5. Report the hack to Meta support.

**How to avoid it.** Never follow links in messages "from Meta" — always open Ads Manager yourself. Two-factor authentication for all admins. Give agencies and freelancers access as partners with minimal rights rather than making them admins. Set an account spending limit.

---

## 6. "Learning Limited that never goes away"
**What you see.** The ad set shows "Learning Limited" and it stays like that for weeks.

**Why.** The ad set doesn't reach about 50 target actions in 7 days. Every significant edit restarts the 7-day clock. A common story: the ad set "isn't learning", so it gets edited, and starts from zero again.

**What to do.**

- Don't panic. It isn't a penalty; the ads keep running, Meta just has less data to optimize with. If your cost per customer is fine, you can live with it.
- Merge small ad sets into one.
- Check tracking: some purchases may simply not be reaching Meta.
- If the budget really is too small, optimize for a more frequent action. But careful: switching to "add to cart" just to escape the status can lower customer quality.

**How to avoid it.** Fewer ad sets, more budget for each, and don't touch anything for 7 days.

---

## 7. "Ads Manager shows sales, but the till is empty"
**What you see.** The report says 30 purchases, the shop has 15.

**Why.** Several possibilities:

- **Double counting.** The pixel and CAPI send the same purchase, and deduplication isn't set up.
- **View-through credit.** Someone saw the ad, didn't click, bought on their own — Meta still credited itself.
- **Existing customers.** Ads were shown to people who were going to buy anyway.

**What to do.**

- In Events Manager, check deduplication: the pixel and server must share one `event_id`.
- In the report, look at the attribution breakdown: how many purchases came "from clicks" and how many "after viewing".
- Set up audience segments and see what share of money goes to existing customers.

**How to avoid it.** Compare Ads Manager with real sales weekly. A gap above 30% means find the cause.

---

## 8. "The money went who knows where"
**What you see.** CTR is oddly high but there are no sales. Or the budget is spent in a couple of hours.

**Why.** Some impressions may have gone to Audience Network (third-party apps and sites) or other places where people click by accident. Another option: budget sharing or spend on excluded placements is switched on.

**What to do.**

- In the report: "Breakdown" → "By placement". See where money is spent and where people buy.
- If a placement spends but doesn't sell, lower its bid with value rules or exclude it. After excluding, remember to turn off "limited spend on excluded placements".

**How to avoid it.** In the first days after launch, check the placement breakdown.

---

## 9. "The ad shows in the wrong city"
**What you see.** Anya advertises candles for pickup in Budapest, but leads come from Debrecen and Vienna.

**Why.** "Location expansion" ("reach more people") is on. Also, Meta can include not only people who live in the city but also people who were there recently, such as tourists.

**What to do.** Untick location expansion. If you only want locals, say so in the copy ("pickup in Budapest only") and add a question to the form.

**How to avoid it.** Check location settings at every launch and look at the region breakdown in reports.

---

## 10. "Everything was fine, then in November ads doubled in price"
**What you see.** You changed nothing, but CPM and cost per customer shot up.

**Why.** Season. Before Black Friday and the holidays everyone advertises, and impressions get pricier. Your ads are fine.

**What to do.**

- Don't break working campaigns out of panic.
- Check whether the cost per customer still fits your limit. If yes — carry on.
- If not: a stronger offer (gift wrapping, a set, "get it before…"), fresh videos.

**How to avoid it.** Launch and train campaigns early, in October, and budget for the seasonal price rise.

---

## 11. "I tweaked one small thing and everything broke"
**What you see.** A campaign was steady, you changed the audience or sharply raised the budget, and results dropped.

**Why.** A big edit sends the ad set back into the learning phase.

**What to do.** If it's already broken, give the ad set 5–7 days to recover without new edits. If it doesn't recover, restore the old settings.

**How to avoid it.** Want to test a new idea? Make a **copy** of the ad set or a separate campaign and leave the working one alone. Raise budgets by 15–20% at a time.

---

## 12. "My ad was rejected, but I didn't write anything bad"
**What you see.** "Your ad doesn't comply with our Advertising Policies". Common for clinics, beauticians, trainers, financial services.

**Why.** Usually one of:

- addressing personal attributes: "Tired of back pain?";
- promising results: "Lose 5 kg in a month";
- before-and-after photos;
- the site doesn't match the ad;
- unlicensed music.

**What to do.** Rewrite from "you" to the service: not "Does your back hurt?" but "Rehabilitation after back injuries". Remove promises and before/after. Resubmit, or request another review if you're sure it's a mistake.

**How to avoid it.** Check copy against the [restrictions list](07-restrictions.md) before launch. Several rejections in a row raise the risk of the whole account being blocked.

---

## 13. "The pixel is installed, but Meta sees almost nothing"
**What you see.** Few events in Events Manager. More sales on the site than purchases in Ads Manager.

**Why.** Usually one of these:

- the cookie banner blocks the pixel until the person agrees, and many don't;
- no CAPI, so the browser loses part of the data;
- the pixel isn't on every page, or broke after a site or plugin update;
- the domain isn't on the allowed list.

**What to do.** Go through the buyer's path in "Test events", connect CAPI, check the allowed domains list, turn on advanced matching.

**How to avoid it.** After every site or plugin update, make a test purchase or request and check that the event arrived.

---

## 14. "My TikTok ad lost its sound"
**What you see.** The ad video plays without music, or it was rejected.

**Why.** You used a track that's allowed in regular videos but not in ads.

**What to do.** Replace the music with a track from the Commercial Music Library and relaunch.

**How to avoid it.** Edit ad versions of your videos with licensed music from the start. For Meta — Sound Collection or a purchased licence.

## Sources
- [Relevant Audience — ad account disabled: causes and appeals](https://www.relevantaudience.com/facebook-ads/facebook-ad-account-disabled/)
- [Cropink — disabled account appeal, 180 days](https://cropink.com/facebook-ad-account-disabled-appeal)
- [McAfee — recovering a hacked Facebook business account](https://www.mcafee.com/blogs/tips-tricks/facebook-hacked-how-to-recover-your-account-and-remove-rogue-page-admins/)
- [Jon Loomer — lead quality is controlled outside the ads](https://pubcast.jonloomer.com/you-can-control-lead-quality-from-meta-ads/)
- [Polygraph — why Advantage+ campaigns get fake leads](https://www.polygraph.net/articles/why-do-advantage-plus-campaigns-get-fake-leads)
- [Lebesgue — Learning Limited explained](https://lebesgue.io/blog/facebook-ads-learning-phase/)

Checked: November 2026.

--8<-- "abbr-en.md"
