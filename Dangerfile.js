const commitMessages = danger.git.commits.map(commit => commit.message);
console.log("commitMessages ->",commitMessages)
// 1. Comprobar que el título del commit tenga un máximo de 50 caracteres
commitMessages.forEach(message => {
  const title = message.split('\n')[0]; // Primer línea (título)
  if (title.length > 50) {
    fail(`El título del commit no debe tener más de 50 caracteres. Título actual: "${title}"`);
  }
});

// 2. Comprobar que haya una línea vacía entre el título y la descripción
commitMessages.forEach(message => {
  const lines = message.split('\n');
  const title = lines[0]; 
  const description = lines.slice(1).join('\n'); // Todo el texto después del título

  if (description && lines[1] && lines[1].trim() !== '') {
    fail('Debe haber una línea vacía entre el título y la descripción del commit.');
  }
});

// 3. Comprobar que la descripción tenga al menos 5 caracteres
commitMessages.forEach(message => {
  if (description.length < 5) {
    fail('La descripción del commit debe tener al menos 5 caracteres.');
  }
});

// 4. Comprobar que cada línea de la descripción no tenga más de 72 caracteres
commitMessages.forEach(message => {
  const description = message.split('\n').slice(1).join('\n');
  const lines = description.split('\n');

  lines.forEach(line => {
    if (line.length > 72) {
      fail(`La línea de la descripción no debe tener más de 72 caracteres. Línea: "${line}"`);
    }
  });
});
