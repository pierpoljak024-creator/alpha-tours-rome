# review-manager — Check, draft, and show Google reviews (Copy/Paste Only)

## DESCRIPTION
This skill manages Google reviews for Alpha Tours Rome. It uses the **NEW Places API v1** (`places.googleapis.com`) — **no OAuth needed**, just a simple API key.

**⚠️ IMPORTANT:** This is a COPY/PASTE system. Hermes generates draft replies, but the CEO must copy them into business.google.com to post them. No automatic posting.

## IMPORTANT UPDATE (May 6, 2026)
**BREAKTHROUGH:** The NEW Places API v1 now works for Alpha Tours Rome! Previously we thought Places API didn't work because Alpha Tours is a service-area business. But the **New Places API** (with `AIzaSyBp0MQ_nXd6zhs6z9CU172Ua7q5FSzfBIg`) returns full review data including:
- ✅ 5 most recent reviews with full text
- ✅ Author names, ratings, timestamps
- ✅ Unique review IDs (for deduplication)
- ✅ Author profile photos and URIs
- ❌ Still only 5 reviews (Google limit), and still no API for POSTING replies
- ❌ No pagination support — cannot fetch all 23 via API in one go
- ❌ No `reply` field in API response data
- ❌ Old Places API (`maps.googleapis.com`) does NOT work (Place ID migrated)
- ❌ Text Search returns ZERO_RESULTS (service-area business)

**Key URL:** `https://places.googleapis.com/v1/places/ChIJHcAuWLqLJRMR-nD81t9OlAk`
**Headers:** `X-Goog-Api-Key`, `X-Goog-FieldMask`, `X-Goog-Language`

## WORKFLOW

### Step 1 — Fetch New Reviews
Run: `node tools/review-manager.mjs fetch`

This will:
1. Call NEW Places API v1
2. Compare review IDs with `tools/seen-reviews.json`
3. Show new (unseen) reviews
4. Save to `tools/new-reviews.json`
5. **Append to cumulative archive** (`tools/all-reviews.json`) — every fetch adds any new unique reviews

### Step 2 — Generate Draft Replies
Run: `node tools/review-manager.mjs draft`

This will:
1. Read `tools/new-reviews.json`
2. For each new review, generate a brand-voice draft reply
3. Save to `tools/pending-drafts.json`

### Step 3 — Show Pending Drafts (for CEO to copy/paste)
Run: `node tools/review-manager.mjs show`

This will display all pending drafts with the draft reply text ready for copying.

### Step 4 — CEO Posts on business.google.com
The CEO copies each draft reply and pastes it into the corresponding review on https://business.google.com.

### Step 5 — Track Replies (after CEO has posted)
After CEO has posted replies, run:
`node tools/review-manager.mjs replied --all`

This marks all reviews in the archive as replied (for tracking purposes).

## BRAND VOICE FOR REPLIES
- Warm, grateful, enthusiastic
- "Thank you so much for your wonderful review!"
- Reference their specific compliment
- Invite them back for another experience
- Use emojis occasionally 🍝 🛵 🛺 🇮🇹 🍋
- Sign with "– Alpha Tours Rome Team"
- Keep it to 2-3 sentences max

### Examples
**Golf cart review:** "Thank you so much for your kind words! 🛺 We're thrilled you enjoyed discovering Rome's highlights with us. Next time, our Vespa sidecar tour is perfect for a romantic evening ride! – Alpha Tours Rome Team"

**Food tour review:** "Grazie mille! 🍝 We're so happy you loved eating your way through Rome with us. Trastevere and Testaccio are true culinary gems! Next time, try our golf cart tour to see Rome's highlights! – Alpha Tours Rome Team"

**Generic tour review:** "Thank you so much for your wonderful feedback! 🇮🇹 We're thrilled you enjoyed the tour. We'd love to welcome you back for another Roman adventure! – Alpha Tours Rome Team"

## COMMANDS

| Command | Action |
|---------|--------|
| `node tools/review-manager.mjs fetch` | Fetch latest reviews from Google |
| `node tools/review-manager.mjs draft` | Generate brand-voice draft replies |
| `node tools/review-manager.mjs show` | Show current state (seen, new, drafts, archive) |
| `node tools/review-manager.mjs approve` | Mark drafts as approved, output for copying |
| `node tools/review-manager.mjs list` | Show ALL reviews ever fetched (cumulative archive) |
| `node tools/review-manager.mjs replied <id\|--all>` | Mark review(s) as replied (tracking only) |

**Note:** The `post` command exists in the script but is **DISABLED** — this system is copy/paste only.

## DATA FILES

| File | Purpose |
|------|---------|
| `tools/seen-reviews.json` | Set of review IDs already processed |
| `tools/new-reviews.json` | Newly fetched reviews not yet drafted |
| `tools/pending-drafts.json` | Draft replies ready for CEO to copy/paste |
| `tools/all-reviews.json` | **Cumulative archive** — all reviews ever seen (all 23 seeded) |
| `tools/replied-reviews.json` | Set of review IDs that have replies posted |
| `tools/seed-reviews.mjs` | One-time script that seeded all 23 reviews |

## TROUBLESHOOTING

| Problem | Cause | Fix |
|---------|-------|-----|
| `API Error: blocked` | Key1 doesn't have Places API enabled | Key2 (`AIzaSyBp0MQ_nXd6zhs6z9CU172Ua7q5FSzfBIg`) works |
| `No new reviews` | All API reviews already seen | Normal — means no recent new reviews |
| Draft wrong tour type | Text matching false-positive | Edit `draftReply` in `pending-drafts.json` before approve |
| API returns only 5 reviews | Google limit for non-OAuth | Acceptable — 5 is enough for weekly checks; cumulative archive builds over time |
| Can't see all 23 reviews | API pagination not available | Use `list` to see cumulative archive; run `fetch` regularly to accumulate |
