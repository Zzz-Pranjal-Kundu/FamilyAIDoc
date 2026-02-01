import { mutation } from "../_generated/server";

export const backfillSymptomsText = mutation({
  args: {},
  handler: async (ctx) => {
    const diseases = await ctx.db.query("diseases").collect();

    for (const disease of diseases) {
      if (!disease.symptomsText) {
        const symptomsText = disease.symptoms.join(" ");

        await ctx.db.patch(disease._id, {
          symptomsText,
        });
      }
    }

    return { updated: diseases.length };
  },
});
