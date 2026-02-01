// import { mutation, query } from "./_generated/server";
// import { v } from "convex/values";

// export const addDisease = mutation({
//   args: {
//     name: v.string(),
//     category: v.string(),
//     description: v.string(),
//     symptoms: v.array(v.string()),
//     advice: v.string(),
//     medicines: v.array(
//       v.object({
//         name: v.string(),
//         dosage: v.string(),
//         frequency: v.string(),
//         duration: v.string(),
//       })
//     ),
//   },
//   handler: async (ctx, args) => {
//     const symptomsText = args.symptoms.join(" ");

//     await ctx.db.insert("diseases", {
//       ...args,
//       symptomsText, // 👈 auto-generated
//     });
//   },
// });

// export const updateDiseaseSymptoms = mutation({
//   args: {
//     id: v.id("diseases"),
//     symptoms: v.array(v.string()),
//   },
//   handler: async (ctx, { id, symptoms }) => {
//     await ctx.db.patch(id, {
//       symptoms,
//       symptomsText: symptoms.join(" "),
//     });
//   },
// });


// export const searchDiseases = query({
//   args: { query: v.string() },
//   handler: async (ctx, { query }) => {
//     const q = query.toLowerCase();

//     // 1️⃣ Search by name using index
//     const nameMatches = await ctx.db
//       .query("diseases")
//       .withSearchIndex("search_diseases", (idx) =>
//         idx.search("name", q)
//       )
//       .take(5);

//     // 2️⃣ Search symptoms array manually
//     const symptomMatches = await ctx.db
//       .query("diseases")
//       .collect();

//     const symptomFiltered = symptomMatches.filter(d =>
//       d.symptoms.some(s =>
//         s.toLowerCase().includes(q)
//       )
//     );

//     // 3️⃣ Merge + deduplicate
//     const combined = [
//       ...nameMatches,
//       ...symptomFiltered,
//     ];

//     const unique = Array.from(
//       new Map(combined.map(d => [d._id, d])).values()
//     );

//     return unique.slice(0, 5);
//   },
// });









import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

/* 🔍 MAIN SEARCH (used by chatbot) */
// export const searchDiseases = query({
//   args: { query: v.string() },
//   handler: async (ctx, { query }) => {
//     const q = query.toLowerCase();

//     // Indexed search (fast)
//     const indexed = await ctx.db
//       .query("diseases")
//       .withSearchIndex("search_diseases", (s) =>
//         s.search("name", query)
//          .or(s.search("symptomsText", query))
//       )
//       .take(10);

//     // Score matches
//     const scored = indexed.map(d => {
//       let score = 0;
//       d.symptoms.forEach(s => {
//         if (q.includes(s.toLowerCase())) score++;
//       });
//       return { ...d, score };
//     });

//     return scored
//       .filter(d => d.score > 0)
//       .sort((a, b) => b.score - a.score)
//       .slice(0, 5);
//   },
// });

export const searchDiseases = query({
  args: { query: v.string() },
  handler: async (ctx, { query }) => {

    const indexed = await ctx.db
      .query("diseases")
      .withSearchIndex("search_diseases", (s) =>
        s.search("symptomsText", query)
      )
      .take(10);

    // Optional scoring
    const q = query.toLowerCase();
    const scored = indexed.map(d => {
      let score = 0;
      d.symptoms.forEach(s => {
        if (q.includes(s.toLowerCase())) score++;
      });
      return { ...d, score };
    });

    return scored
      .filter(d => d.score > 0)
      .sort((a, b) => b.score - a.score)
      .slice(0, 5);
  },
});

/* ➕ ADD DISEASE */
export const addDisease = mutation({
  args: {
    name: v.string(),
    category: v.string(),
    description: v.string(),
    symptoms: v.array(v.string()),
    advice: v.string(),
    medicines: v.array(
      v.object({
        name: v.string(),
        dosage: v.string(),
        frequency: v.string(),
        duration: v.string(),
      })
    ),
  },
  handler: async (ctx, args) => {
    await ctx.db.insert("diseases", {
      ...args,
      symptomsText: args.symptoms.join(" "),
    });
  },
});
