import { message, warn, fail } from "danger";

// Mensaje simple
message("⚡ ¡Revisión de PR activada!");

// Verificar si se modificaron archivos sensibles
const sensitiveFiles = ["package.json", "yarn.lock"];
const modifiedFiles = danger.git.modified_files;

sensitiveFiles.forEach((file) => {
  if (modifiedFiles.includes(file)) {
    warn(`⚠️ Se modificó ${file}, revisa que los cambios sean correctos.`);
  }
});

// Verificar que el PR tenga descripción
if (danger.github.pr.body.length < 10) {
  fail("❌ Agrega una descripción significativa al PR.");
}
