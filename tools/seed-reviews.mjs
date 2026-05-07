#!/usr/bin/env node
/**
 * seed-reviews.mjs — Seed ALL known reviews into the cumulative archive
 *
 * This script populates tools/all-reviews.json with all 23 + 1 reviews
 * that were manually extracted from Google Business Profile data.
 *
 * Run ONCE to initialize, then use review-manager.mjs for daily operations.
 *
 * Usage:
 *   node tools/seed-reviews.mjs
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ALL_REVIEWS_FILE = path.join(__dirname, 'all-reviews.json');
const SEEN_FILE = path.join(__dirname, 'seen-reviews.json');
const NEW_REVIEWS_FILE = path.join(__dirname, 'new-reviews.json');

// ═══════════════════════════════════════════════════════════════════════
// ALL REVIEWS — Seeded from Google Business Profile (cumulative archive)
// ═══════════════════════════════════════════════════════════════════════

const ALL_REVIEWS = [
  // ── Places API reviews (with full metadata) ──
  {
    reviewId: "Ci9DQUlRQUNvZENodHljRjlvT25aMFNVOVpObms0UVVwc2JqQnpWRWhIVFhWTmFYYxAB",
    name: "Daniel Good",
    rating: 5,
    text: "Pierfilippo was a fantastic guide and shared lots of insightful information about the various sights we visited as well as many others along the route. A great way to see a lot in a relatively short space of time and gives your feet a day off! Thanks Pierfilippo. 👍",
    time: "in the last week",
    authorUri: "https://www.google.com/maps/contrib/104667675030982481626/reviews",
    authorPhoto: "https://lh3.googleusercontent.com/a/ACg8ocJoN31Q_EASUMxMfsNt8Dw9ck8E62GHj9jW8WCnZ828d91lAg=s128-c0x00000000-cc-rp-mo",
    archivedAt: "2026-05-06T17:56:47.143Z"
  },
  {
    reviewId: "Ci9DQUlRQUNvZENodHljRjlvT21sT2FGQklhR1p4WjBOVk5YSXlRV1JoYzFZMlpHYxAB",
    name: "Lucy Vanner",
    rating: 5,
    text: "Gabriele was an excellent tour guide taking us through an authentic Rome taste trail and making us feel warmly welcome! We were absolutely stuffed and satisfied by the end.",
    time: "in the last week",
    authorUri: "https://www.google.com/maps/contrib/110760004458098939928/reviews",
    authorPhoto: "https://lh3.googleusercontent.com/a-/ALV-UjUtMDZDpGtiUy7UzlEu6qNeh4Bxp-zgmSfo-aFR1o8f2P2P7rjDxw=s128-c0x00000000-cc-rp-mo",
    archivedAt: "2026-05-06T17:56:47.144Z"
  },
  {
    reviewId: "Ci9DQUlRQUNvZENodHljRjlvT2pkbk1XSjZabGhqTFhkaVlsTXdjRlpDV2t4MlFXYxAB",
    name: "Daniel Rishoff",
    rating: 5,
    text: "Pier was our tour guide.  He was extremely knowledgeable, accommodating and pleasant to spend an afternoon with.  I would highly recommend a golf cart tour to anyone visiting Rome.  It was a fantastic way to see many sights in just a couple hours.  Would do it again if we visit Rome in the future.",
    time: "in the last week",
    authorUri: "https://www.google.com/maps/contrib/103327265025204377720/reviews",
    authorPhoto: "https://lh3.googleusercontent.com/a/ACg8ocKHYvpvcBJ2rIg__TjWEw8pObibRkawRp_QTejEt6e7-QTcmQ=s128-c0x00000000-cc-rp-mo",
    archivedAt: "2026-05-06T17:56:47.144Z"
  },
  {
    reviewId: "Ci9DQUlRQUNvZENodHljRjlvT21vM1FtWkJaSEZDWlVwZlMxSjNXbDgwT1RsVU5VRRAB",
    name: "James Stephens",
    rating: 5,
    text: "Gabriele was a very charismatic host. We tried some incredible cuisine from multiple local stops in Rome. Great banter and great food, what else do you need!",
    time: "in the last week",
    authorUri: "https://www.google.com/maps/contrib/101965188057274073257/reviews",
    authorPhoto: "https://lh3.googleusercontent.com/a-/ALV-UjUqBJ6Tj-RP8l9DMk4XIywLe_90f7cr2ajeVv34VX4LHSfVLXlgOg=s128-c0x00000000-cc-rp-mo-ba3",
    archivedAt: "2026-05-06T17:56:47.144Z"
  },
  {
    reviewId: "Ci9DQUlRQUNvZENodHljRjlvT2tFMGQyMUdjbXgxWWxaU1JEbDBMVVpWYTI1T1JXYxAB",
    name: "LLOYD OSHIRO",
    rating: 5,
    text: "We had a fantastic tour with Paolo! He was friendly, knowledgeable and we had so much fun and learned so much!",
    time: "in the last week",
    authorUri: "https://www.google.com/maps/contrib/114561051239864198539/reviews",
    authorPhoto: "https://lh3.googleusercontent.com/a/ACg8ocLEN45uMOULpQfOEB-TwX_0FO0TVS6jShLujWVMYPbQABxwdQ=s128-c0x00000000-cc-rp-mo",
    archivedAt: "2026-05-06T17:56:47.144Z"
  },
  {
    reviewId: "Ci9DQUlRQUNvZENodHljRjlvT25oRmFHTkhOa0Y1TFd4VFV6ZFVPV2t4WjFFM1JGRRAB",
    name: "Danna Schwenk",
    rating: 5,
    text: "We loved our time with Gabriel and couldn't have asked for a better introduction to Rome! 100% recommend!!",
    time: "in the last week",
    authorUri: "https://www.google.com/maps/contrib/100528548088220694482/reviews",
    authorPhoto: "https://lh3.googleusercontent.com/a-/ALV-UjVDceq8Sp52g6QNiWmOsx30yVQunIhVcYi8fkPnyCGIeeWK03XmWQ=s128-c0x00000000-cc-rp-mo-ba3",
    archivedAt: "2026-05-06T19:16:09.794Z"
  },

  // ── Manually extracted reviews (from Google Business Profile) ──
  {
    reviewId: "ca4a0cec91ea972d819ee92dce8e2046",
    name: "Jamey Knight",
    rating: 5,
    text: "Gabriel was absolutely amazing!!! The tour was a perfect way to see the city and all the major attractions! Highly recommend this adventure.",
    time: "2 days ago",
    archivedAt: "2026-05-06T18:04:35.495Z"
  },
  {
    reviewId: "e782677af0bca99a800b65f03abf52cb",
    name: "Annalisa Narducci",
    rating: 5,
    text: "Very welcoming and joyful driver! Nice experience and easy way to see the must see in Rome!",
    time: "2 days ago",
    archivedAt: "2026-05-06T18:04:35.496Z"
  },
  {
    reviewId: "e2e7cc6f4c3bf26d06e09307f04d3b87",
    name: "Waleed Ismael",
    rating: 5,
    text: "We had a golf cart tour with Mahi and he was an amazing tour guide. Very knowledgeable, soo funny. We hit all of the major sites and he shared details about the city of Rome around every corner we went. So informative. We would do this golf cart tour over again every time",
    time: "2 days ago",
    archivedAt: "2026-05-06T18:04:35.496Z"
  },
  {
    reviewId: "feaaa281c2f578a3fad1aa45f4a6c452",
    name: "Layne Larson",
    rating: 5,
    text: "We had an incredible time on our golf cart tour with Alpha Tours. Our guide was knowledgeable and funny, and a great driver. Would recommend as a start to your trip or if you're only here for a short time!",
    time: "3 days ago",
    archivedAt: "2026-05-06T18:04:35.496Z"
  },
  {
    reviewId: "bbeb182b48234b505d197851cd237338",
    name: "laurence begg",
    rating: 5,
    text: "Outstanding tour guide, Claudio, gave a brief history with some amusing details. A thoroughly enjoyable experience. Recommend highly.",
    time: "3 days ago",
    archivedAt: "2026-05-06T18:04:35.496Z"
  },
  {
    reviewId: "d28d414b6961ea7be2d56c5dd7139213",
    name: "Adam Jefford",
    rating: 5,
    text: "Tour was excellent! Fun and knowledgeable guides who took us to the right spots around Rome. Would recommend and would take tour again!",
    time: "3 days ago",
    archivedAt: "2026-05-06T18:04:35.496Z"
  },
  {
    reviewId: "a7371ad915593fec953d21caada23e7f",
    name: "Myra Blackmon",
    rating: 5,
    text: "The tour was delightful! Pier is quite knowledgeable and has a great sense of humor! It was a crowded holiday weekend, and his ability to take alternative routes, back streets and get us where we wanted to be was especially helpful. I would highly recommend the tour as a quick overview of the highlights of Rome!",
    time: "3 days ago",
    archivedAt: "2026-05-06T18:04:35.496Z"
  },
  {
    reviewId: "ee45091bd388b0c4bcf2ac351a4c1f42",
    name: "Marta Starker",
    rating: 5,
    text: "We had the most amazing time with Gabrielle. He was so kind, informative and friendly. We highly recommend this tour. It's a wonderful way to see a bit of Rome.",
    time: "3 days ago",
    archivedAt: "2026-05-06T18:04:35.496Z"
  },
  {
    reviewId: "3b57310e5a65d2ee5b58c60d9f16026f",
    name: "Janice Huffman",
    rating: 5,
    text: "Pier was a great tour guide, full of personality and details about the history of Rome!",
    time: "3 days ago",
    archivedAt: "2026-05-06T18:04:35.496Z"
  },
  {
    reviewId: "6dbec24292c3ef8fa56a647bd320fe6a",
    name: "sylvia sims",
    rating: 5,
    text: "Really enjoyed the tour. Got to visit the most famous spots in Rome and didn't have to find them myself! I recommend, especially if traveling with kids or seniors.",
    time: "4 days ago",
    archivedAt: "2026-05-06T18:04:35.496Z"
  },
  {
    reviewId: "e30daab24648a3bd5061d1e93bc338da",
    name: "Yiannis Theodorakos",
    rating: 5,
    text: "Excellent experience and Gabriele is the best possible host for this!",
    time: "a week ago",
    archivedAt: "2026-05-06T18:04:35.496Z"
  },
  {
    reviewId: "dd999a29b20f7fca94bc652430dd5b52",
    name: "Richard Parisi",
    rating: 5,
    text: "Gabriel was our tour guide and he was great. We saw all the sites we wanted to see and a few we didn't know about in advance but were very glad we saw. Getting escorted through the small pedestrian streets and all around Rome was great fun for the kids (and a welcome break from all the walking for the adults)! Highly recommend!",
    time: "3 weeks ago",
    archivedAt: "2026-05-06T18:04:35.496Z"
  },
  {
    reviewId: "4cd7bd5adbdde64b0bb21f7ab84ac51c",
    name: "Pierfilippo Agati",
    rating: 5,
    text: "I can't recommend Alpha Tours enough! We did the private golf cart tour of Rome and it was honestly the highlight of our entire trip to Italy.",
    time: "a month ago",
    archivedAt: "2026-05-06T18:04:35.496Z"
  },
  {
    reviewId: "54dce55db83d592b14cf853c63048d9e",
    name: "ceren ercan",
    rating: 5,
    text: "Claudio was a fantastic person, a lot of fun.",
    time: "22 hours ago",
    archivedAt: "2026-05-06T18:04:35.496Z"
  },
  {
    reviewId: "6a3128cb9f77c53c2c5260d00c05b7e8",
    name: "Alison Maggioli",
    rating: 5,
    text: "Great experience!!! Thank you so much Gabriele, you are very nice and kind!",
    time: "4 days ago",
    archivedAt: "2026-05-06T18:04:35.496Z"
  },
  {
    reviewId: "d7265724da0a7a79fc1cf027bc68fe24",
    name: "Katarzyna Niedziela",
    rating: 5,
    text: "It was a truly successful and eventful trip. The guide was very dedicated, attentive to our needs and eager to accommodate our suggestions, creating a very friendly atmosphere. A huge plus was the short stops at the most beautiful spots where we could take photos and pause to fully appreciate our surroundings. During the tour, we saw many interesting sights and learned a lot of interesting facts, presented in an engaging way. The ride itself was comfortable, allowing us to fully focus on enjoying the entire trip. I highly recommend it!",
    time: "3 weeks ago",
    archivedAt: "2026-05-06T18:04:35.496Z"
  },
  {
    reviewId: "7a367d6c39a77c7e10b86670584cb57e",
    name: "Anna Niedziela",
    rating: 5,
    text: "I highly recommend a tour with these guides :) We saw all the main attractions, the guide explained everything to us and had answers to all our questions. We saw the Spanish Steps, Borghese Park, the Colosseum, and visited various spots.",
    time: "3 weeks ago",
    archivedAt: "2026-05-06T18:04:35.496Z"
  },
  {
    reviewId: "94233d15b8f0b053c233f61f5e53ff90",
    name: "Agnieszka Niedziela",
    rating: 5,
    text: "The tour and sightseeing were a great success and left us with many positive experiences. The stories told were incredibly interesting, and the way they was conveyed was full of passion, commitment, and humor! It was a true pleasure to listen to. The ride was very comfortable. We definitely recommend it! Thanks to you, our stay in Rome will remain in our memories for a long time",
    time: "3 weeks ago",
    archivedAt: "2026-05-06T18:04:35.496Z"
  },
];

// ═══════════════════════════════════════════════════════════════════════
// IDs that were seen by the old Places API (v3, short IDs)
// ═══════════════════════════════════════════════════════════════════════

const OLD_API_SEEN_IDS = [
  "1775128598",
  "1775675737",
  "1775675335",
  "1775674986",
];

// ═══════════════════════════════════════════════════════════════════════
// Main
// ═══════════════════════════════════════════════════════════════════════

function main() {
  console.log('🌱 Seeding review archive...\n');

  // Write cumulative archive
  fs.writeFileSync(ALL_REVIEWS_FILE, JSON.stringify(ALL_REVIEWS, null, 2), 'utf-8');
  console.log(`✅ Written ${ALL_REVIEWS.length} reviews to all-reviews.json`);

  // Build seen IDs: old API IDs + all review IDs from seed data
  const seenIds = new Set(OLD_API_SEEN_IDS);
  ALL_REVIEWS.forEach(r => seenIds.add(r.reviewId));
  fs.writeFileSync(SEEN_FILE, JSON.stringify([...seenIds], null, 2), 'utf-8');
  console.log(`✅ Written ${seenIds.size} seen IDs to seen-reviews.json`);

  // Clear new-reviews.json (all reviews are already seen)
  fs.writeFileSync(NEW_REVIEWS_FILE, '[]', 'utf-8');
  console.log('✅ Cleared new-reviews.json');

  console.log(`\n📊 Summary:`);
  console.log(`   Total reviews in archive: ${ALL_REVIEWS.length}`);
  console.log(`   Total seen IDs: ${seenIds.size}`);
  console.log(`   Old API IDs: ${OLD_API_SEEN_IDS.length}`);
  console.log(`   New reviews (pending): 0`);
  console.log(`\n🌱 Seed complete. You can now use:`);
  console.log(`   node tools/review-manager.mjs show`);
  console.log(`   node tools/review-manager.mjs list`);
}

main();
