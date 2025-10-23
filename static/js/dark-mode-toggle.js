document.addEventListener('DOMContentLoaded', () => {
    // 1. Encontra o botão (que vamos criar no HTML)
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    // 2. Encontra o 'corpo' do HTML
    const body = document.body;
    // 3. Verifica se o usuário já tinha uma preferência salva
    const currentMode = localStorage.getItem('theme');

    // 4. Se já existia preferência 'dark', aplica o modo escuro ao carregar
    if (currentMode === 'dark') {
        body.classList.add('dark-mode');
    }

    // 5. O que fazer quando o botão for clicado:
    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', () => {
            // Adiciona/remove a classe 'dark-mode' do body
            body.classList.toggle('dark-mode');

            // Salva a nova preferência (ou remove se voltou para 'light')
            if (body.classList.contains('dark-mode')) {
                localStorage.setItem('theme', 'dark');
            } else {
                localStorage.removeItem('theme');
            }
        });
    }
});