import globals from "globals";
import pluginJs from "@eslint/js";

/** @type {import('eslint').Linter.FlatConfig[]} */
export default [
  {
    files: ["**/*.js"],
    languageOptions: {
      sourceType: "commonjs",
      globals: {
        ...globals.browser, // Agrega los globals del navegador
        danger: "readonly", // Indica que 'danger' es una variable global de solo lectura
        fail: "readonly",   // Indica que 'fail' es una variable global de solo lectura
        warn: "readonly",   // Indica que 'warn' es una variable global de solo lectura
        message: "readonly", // Indica que 'message' es una variable global de solo lectura
      },
    },
  },
  {
    rules: {
      // Tus reglas personalizadas
    },
  },
  pluginJs.configs.recommended,
];
