// // import { defineSchema, defineTable } from "convex/server";
// // import { v } from "convex/values";

// // export default defineSchema({
// //   diseases: defineTable({
// //     name: v.string(),
// //     category: v.string(),
// //     description: v.string(),
// //     symptoms: v.array(v.string()),
// //     advice: v.string(),
// //     medicines: v.array(
// //       v.object({
// //         name: v.string(),
// //         dosage: v.string(),
// //         frequency: v.string(),
// //         duration: v.string(),
// //       })
// //     ),
// //   }).searchIndex("search_diseases", {
// //     searchField: "name",
// //   }),
// // });

// import { defineSchema, defineTable } from "convex/server";
// import { v } from "convex/values";

// export default defineSchema({
//   diseases: defineTable({
//     name: v.string(),
//     category: v.string(),
//     description: v.string(),
//     symptoms: v.array(v.string()),
//     symptomsText: v.string(), // 👈 NEW
//     advice: v.string(),
//     medicines: v.array(
//       v.object({
//         name: v.string(),
//         dosage: v.string(),
//         frequency: v.string(),
//         duration: v.string(),
//       })
//     ),
//   }).searchIndex("search_diseases", {
//     searchField: "name",
//     filterFields: ["symptomsText"],
//   }),
// });


import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  diseases: defineTable({
    name: v.string(),
    category: v.string(),
    description: v.string(),
    symptoms: v.array(v.string()),
    symptomsText: v.string(),
    advice: v.string(),
    medicines: v.array(
      v.object({
        name: v.string(),
        dosage: v.string(),
        frequency: v.string(),
        duration: v.string(),
      })
    ),
  }).searchIndex("search_diseases", {
    searchField: "symptomsText",
  }),
});
