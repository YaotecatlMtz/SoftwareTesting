const { danger, warn, fail, message } = require("danger");

// ✅ 1️⃣ Verificar que DangerJS se esté ejecutando en un PR
if (!danger.github) {
  console.log("⚠️ DangerJS solo se ejecuta en Pull Requests.");
  process.exit(0);
}

// ✅ 2️⃣ Obtener archivos modificados y agregados
const modifiedFiles = danger.git.modified_files || [];
const createdFiles = danger.git.created_files || [];
const deletedFiles = danger.git.deleted_files || [];

console.log("📝 Archivos modificados:", modifiedFiles);
console.log("📂 Archivos nuevos:", createdFiles);
console.log("🗑️ Archivos eliminados:", deletedFiles);

// ✅ 3️⃣ Reglas de revisión

// ⚠️ Avisar si `package.json` o `package-lock.json` cambiaron sin cambios en `node_modules`
if (
  (modifiedFiles.includes("package.json") || modifiedFiles.includes("package-lock.json")) &&
  !modifiedFiles.some((file) => file.includes("node_modules"))
) {
  warn("📦 Cambiaste `package.json` o `package-lock.json`, asegúrate de actualizar dependencias.");
}

// ⚠️ Revisión de cambios en archivos críticos
const criticalFiles = ["src/index.js", "server.js", ".github/workflows/danger.yml"];
const modifiedCritical = modifiedFiles.filter((file) => criticalFiles.includes(file));

if (modifiedCritical.length > 0) {
  warn(`⚠️ Modificaste archivos críticos: ${modifiedCritical.join(", ")}`);
}

// ❌ Fallo si falta descripción en el PR
if (!danger.github.pr.body || danger.github.pr.body.length < 10) {
  fail("❌ Agrega una descripción al Pull Request.");
}

// ✅ 4️⃣ Convenciones de commits (Conventional Commits)
const prTitle = danger.github.pr.title;
const commitRegex = /^(feat|fix|docs|style|refactor|perf|test|chore|revert)(\(.+\))?:\s.+/;

if (!commitRegex.test(prTitle)) {
  fail("❌ El título del PR no sigue Conventional Commits. Ejemplo: `feat(auth): agregar login`");
}

// ✅ 5️⃣ Mensaje de éxito si todo está bien
message("🎉 ¡Revisión de PR activada! Todo se ve bien.");

