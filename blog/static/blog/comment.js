document.getElementById('commentForm').addEventListener('submit', function(event) {
    const element_error = document.getElementById('id_content_error');
        if (element_error) {
        const input = document.querySelector('textarea[name="content"]');
        const value = input.value.trim();

        const cleaned = value.replace(/\n/g, '').trim();

        if (!cleaned) {
            event.preventDefault();
        }
    }
});