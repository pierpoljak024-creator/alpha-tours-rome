# review-manager — Check and reply to Google reviews

## DESCRIPTION
This skill checks for new Google reviews, generates brand-voice replies, and auto-posts them via the Google Business Profile API.

## TRIGGER
This skill runs automatically every 6 hours via cron. It can also be triggered manually by the CEO (Telegram ID 5285215270) by saying "check reviews" or "review status".

## WORKFLOW
1. Run: `cd /root/repo/alpha-tours-rome && python tools/check_reviews.py`
2. Read the output. If no new reviews, report "No new reviews found."
3. If new reviews found, for EACH review:
   a. Generate a brand-voice reply using the SOUL.md brand voice guidelines
   b. Write the reply to `/root/repo/alpha-tours-rome/tools/pending-drafts.json` in this format:
      ```json
      [{
        "reviewId": "...",
        "name": "REVIEWER_NAME",
        "rating": 5,
        "reviewText": "THEIR REVIEW TEXT",
        "time": "RELATIVE TIME",
        "draftReply": "YOUR GENERATED REPLY"
      }]
      ```
4. Run the auto-poster: `cd /root/repo/alpha-tours-rome && python tools/post_review_reply.py`
5. Report result to CEO on Telegram: 
   - "📬 Posted reply to [Name]'s [N]★ review: '[First 50 chars of reply]...' ✅"

## BRAND VOICE FOR REPLIES
- Warm, grateful, enthusiastic
- "Thank you so much for your wonderful review!"
- Reference their specific compliment (e.g., "We're thrilled you loved the golf cart tour!")
- Invite them back for another experience (e.g., "Next time, try our Vespa sidecar tour!")
- Use emojis occasionally 🍝 🛵 🛺 🇮🇹 🍋
- Sign with "– Alpha Tours Rome Team"
- Keep it to 2-3 sentences max

## EXAMPLES

### 5★ review about golf cart tour
"Thank you so much for your kind words! 🛺 We're thrilled you enjoyed discovering Rome's highlights with us. Next time you're in the city, our Vespa sidecar tour is perfect for a romantic evening ride! – Alpha Tours Rome Team"

### 4★ review with minor criticism
"Thank you for your feedback! We're glad you enjoyed the tour overall. We always strive to improve, and your input helps us deliver even better experiences. We'd love to welcome you back for another adventure! – Alpha Tours Rome Team"

### 5★ review about food tour
"Grazie mille! 🍝 We're so happy you loved eating your way through Rome with us. Trastevere and Testaccio are true culinary gems, aren't they? Come back soon for another taste of la dolce vita! – Alpha Tours Rome Team"
