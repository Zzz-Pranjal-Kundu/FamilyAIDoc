import { mutation } from "../_generated/server";

export const fixMedicines = mutation({
  args: {},
  handler: async (ctx) => {
    const diseases = await ctx.db.query("diseases").collect();

    let fixed = 0;

    for (const d of diseases) {
      // Runtime check for old string[] format
      if (
        Array.isArray(d.medicines) &&
        d.medicines.length > 0 &&
        typeof (d.medicines as any)[0] === "string"
      ) {
        const oldMedicines = d.medicines as unknown as string[];

        await ctx.db.patch(d._id, {
          medicines: oldMedicines.map((name) => ({
            name,
            dosage: "As directed",
            frequency: "As directed",
            duration: "As needed",
          })),
        });

        fixed++;
      }
    }

    return { fixed };
  },
});
