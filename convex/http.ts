// // // // // // // // // import { httpRouter } from "convex/server";
// // // // // // // // // import { httpAction } from "./_generated/server";
// // // // // // // // // import { api } from "./_generated/api";

// // // // // // // // // const http = httpRouter();

// // // // // // // // // http.route({
// // // // // // // // //   path: "/api/search_diseases",
// // // // // // // // //   method: "POST",
// // // // // // // // //   handler: httpAction(async (ctx, req) => {
// // // // // // // // //     const { query } = await req.json();

// // // // // // // // //     const results = await ctx.runQuery(
// // // // // // // // //       api.diseases.searchDiseases,
// // // // // // // // //       { query }
// // // // // // // // //     );

// // // // // // // // //     return new Response(JSON.stringify(results), {
// // // // // // // // //       status: 200,
// // // // // // // // //       headers: { 
// // // // // // // // //         "Content-Type": "application/json",
// // // // // // // // //         // Recommended for local development/Streamlit
// // // // // // // // //         "Access-Control-Allow-Origin": "*", 
// // // // // // // // //       },
// // // // // // // // //     });
// // // // // // // // //   }),
// // // // // // // // // });

// // // // // // // // // export default http;










// // // // // // // // import { httpRouter } from "convex/server";
// // // // // // // // import { httpAction } from "./_generated/server";
// // // // // // // // import { api } from "./_generated/api";

// // // // // // // // const http = httpRouter();

// // // // // // // // http.route({
// // // // // // // //   path: "/api/search_diseases",
// // // // // // // //   method: "POST",
// // // // // // // //   handler: httpAction(async (ctx, req) => {
// // // // // // // //     const { query } = await req.json();

// // // // // // // //     const results = await ctx.runQuery(
// // // // // // // //       api.diseases.searchDiseases,
// // // // // // // //       { query }
// // // // // // // //     );

// // // // // // // //     return new Response(JSON.stringify(results), {
// // // // // // // //       status: 200,
// // // // // // // //       headers: {
// // // // // // // //         "Content-Type": "application/json",
// // // // // // // //         "Access-Control-Allow-Origin": "*",
// // // // // // // //       },
// // // // // // // //     });
// // // // // // // //   }),
// // // // // // // // });

// // // // // // // // export default http;



// // // // // // // import { httpRouter } from "convex/server";
// // // // // // // import { httpAction } from "./_generated/server";
// // // // // // // import { api } from "./_generated/api";

// // // // // // // const http = httpRouter();

// // // // // // // http.route({
// // // // // // //   path: "/api/search_diseases",
// // // // // // //   method: "POST",
// // // // // // //   handler: httpAction(async (ctx, req) => {
// // // // // // //     const { query } = await req.json();

// // // // // // //     const results = await ctx.runQuery(
// // // // // // //       api.diseases.searchDiseases,
// // // // // // //       { query }
// // // // // // //     );

// // // // // // //     return new Response(JSON.stringify(results), {
// // // // // // //       status: 200,
// // // // // // //       headers: {
// // // // // // //         "Content-Type": "application/json",
// // // // // // //         "Access-Control-Allow-Origin": "*",
// // // // // // //       },
// // // // // // //     });
// // // // // // //   }),
// // // // // // // });

// // // // // // // export default http;




// // // // // // import { httpRouter } from "convex/server";
// // // // // // import { httpAction } from "./_generated/server";
// // // // // // import { api } from "./_generated/api";

// // // // // // const http = httpRouter();

// // // // // // http.route({
// // // // // //   path: "/api/search_diseases",
// // // // // //   method: "POST",
// // // // // //   handler: httpAction(async (ctx, req) => {
// // // // // //     const { query } = await req.json();

// // // // // //     const results = await ctx.runQuery(
// // // // // //       api.diseases.searchDiseases,
// // // // // //       { query }
// // // // // //     );

// // // // // //     return new Response(JSON.stringify(results), {
// // // // // //       status: 200,
// // // // // //       headers: {
// // // // // //         "Content-Type": "application/json",
// // // // // //         "Access-Control-Allow-Origin": "*",
// // // // // //       },
// // // // // //     });
// // // // // //   }),
// // // // // // });

// // // // // // export default http;




// // // // // import { httpRouter } from "convex/server";
// // // // // import { httpAction } from "./_generated/server";
// // // // // import { api } from "./_generated/api";

// // // // // const http = httpRouter();

// // // // // /**
// // // // //  * Health check (for debugging)
// // // // //  * URL: https://<CONVEX_URL>/health
// // // // //  */
// // // // // http.route({
// // // // //   path: "/health",
// // // // //   method: "GET",
// // // // //   handler: httpAction(async () => {
// // // // //     return new Response("OK", { status: 200 });
// // // // //   }),
// // // // // });

// // // // // /**
// // // // //  * Main search endpoint
// // // // //  * URL: https://<CONVEX_URL>/api/search_diseases
// // // // //  */
// // // // // http.route({
// // // // //   path: "/api/search_diseases",
// // // // //   method: "POST",
// // // // //   handler: httpAction(async (ctx, req) => {
// // // // //     const { query } = await req.json();

// // // // //     const results = await ctx.runQuery(
// // // // //       api.diseases.searchDiseases,
// // // // //       { query }
// // // // //     );

// // // // //     return new Response(JSON.stringify(results), {
// // // // //       status: 200,
// // // // //       headers: {
// // // // //         "Content-Type": "application/json",
// // // // //         "Access-Control-Allow-Origin": "*",
// // // // //       },
// // // // //     });
// // // // //   }),
// // // // // });

// // // // // export default http;






// // // // import { httpRouter } from "convex/server";
// // // // import { httpAction } from "./_generated/server";
// // // // import { api } from "./_generated/api";

// // // // const http = httpRouter();

// // // // // Define the route exactly as you want to call it
// // // // http.route({
// // // //   path: "/api/search_diseases", // Try removing the 'api/' prefix for simplicity
// // // //   method: "POST",
// // // //   handler: httpAction(async (ctx, req) => {
// // // //     try {
// // // //       const { query } = await req.json();

// // // //       const results = await ctx.runQuery(
// // // //         api.diseases.searchDiseases,
// // // //         { query }
// // // //       );

// // // //       return new Response(JSON.stringify(results), {
// // // //         status: 200,
// // // //         headers: {
// // // //           "Content-Type": "application/json",
// // // //           "Access-Control-Allow-Origin": "*",
// // // //           "Access-Control-Allow-Methods": "POST, OPTIONS",
// // // //           "Access-Control-Allow-Headers": "Content-Type",
// // // //         },
// // // //       });
// // // //     } catch (e) {
// // // //       return new Response(JSON.stringify({ error: "Invalid JSON" }), { status: 400 });
// // // //     }
// // // //   }),
// // // // });

// // // // export default http;


// // // import { httpRouter } from "convex/server";
// // // import { httpAction } from "./_generated/server";
// // // import { api } from "./_generated/api";

// // // const http = httpRouter();

// // // http.route({
// // //   path: "/api/search_diseases",
// // //   method: "POST",
// // //   handler: httpAction(async (ctx, req) => {
// // //     const { query } = await req.json();

// // //     const results = await ctx.runQuery(
// // //       api.diseases.searchDiseases,
// // //       { query }
// // //     );

// // //     return new Response(JSON.stringify(results), {
// // //       status: 200,
// // //       headers: {
// // //         "Content-Type": "application/json",
// // //         "Access-Control-Allow-Origin": "*",
// // //       },
// // //     });
// // //   }),
// // // });

// // // export default http;




// // import { httpRouter } from "convex/server";
// // import { httpAction } from "./_generated/server";

// // const http = httpRouter();

// // http.route({
// //   path: "/health",
// //   method: "GET",
// //   handler: httpAction(async () => {
// //     return new Response("OK");
// //   }),
// // });

// // export default http;




// import { httpRouter } from "convex/server";
// import { httpAction } from "./_generated/server";

// const http = httpRouter();

// http.route({
//   path: "/health",
//   method: "GET",
//   handler: httpAction(async () => {
//     return new Response("OK");
//   }),
// });

// export default http;




import { httpRouter } from "convex/server";
import { httpAction } from "./_generated/server";
import { api } from "./_generated/api";

const http = httpRouter();

http.route({
  path: "/health",
  method: "GET",
  handler: httpAction(async () => {
    return new Response("OK");
  }),
});

http.route({
  path: "/api/search_diseases",
  method: "POST",
  handler: httpAction(async (ctx, req) => {
    const { query } = await req.json();

    const results = await ctx.runQuery(
      api.diseases.searchDiseases,
      { query }
    );

    return new Response(JSON.stringify(results), {
      status: 200,
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
      },
    });
  }),
});

export default http;
