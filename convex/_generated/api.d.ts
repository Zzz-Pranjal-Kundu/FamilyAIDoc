/* eslint-disable */
/**
 * Generated `api` utility.
 *
 * THIS CODE IS AUTOMATICALLY GENERATED.
 *
 * To regenerate, run `npx convex dev`.
 * @module
 */

import type * as diseases from "../diseases.js";
import type * as http from "../http.js";
import type * as migrations_backfillSymptomsText from "../migrations/backfillSymptomsText.js";
import type * as migrations_fixMedicines from "../migrations/fixMedicines.js";

import type {
  ApiFromModules,
  FilterApi,
  FunctionReference,
} from "convex/server";

declare const fullApi: ApiFromModules<{
  diseases: typeof diseases;
  http: typeof http;
  "migrations/backfillSymptomsText": typeof migrations_backfillSymptomsText;
  "migrations/fixMedicines": typeof migrations_fixMedicines;
}>;

/**
 * A utility for referencing Convex functions in your app's public API.
 *
 * Usage:
 * ```js
 * const myFunctionReference = api.myModule.myFunction;
 * ```
 */
export declare const api: FilterApi<
  typeof fullApi,
  FunctionReference<any, "public">
>;

/**
 * A utility for referencing Convex functions in your app's internal API.
 *
 * Usage:
 * ```js
 * const myFunctionReference = internal.myModule.myFunction;
 * ```
 */
export declare const internal: FilterApi<
  typeof fullApi,
  FunctionReference<any, "internal">
>;

export declare const components: {};
