import { defineConfig } from "vite";
import path from "path";

// Configuration entry point
export default defineConfig({
  base: "/static/",
  build: {
    manifest: "manifest.json",
    emptyOutDir: true,
    outDir: path.resolve(__dirname, "static_compiled"),
    rollupOptions: {
      input: {
        main: path.resolve(__dirname, "static_src/javascript/main.js"),
      }
    },
  },
});
