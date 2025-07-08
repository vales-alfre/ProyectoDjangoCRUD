// JavaScript helpers for CRUD project

document.addEventListener('DOMContentLoaded', () => {
  const messagesElement = document.getElementById('django-messages');
  if (messagesElement) {
    try {
      const messages = JSON.parse(messagesElement.textContent);
      messages.forEach(msg => {
        Swal.fire({
          icon: 'success',
          title: msg,
          timer: 2000,
          showConfirmButton: false
        });
      });
    } catch (e) {
      console.error('Failed to parse messages', e);
    }
  }
});


window.confirmDelete = function(id) {
  Swal.fire({
    title: '¿Eliminar item?',
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#d33',
    confirmButtonText: 'Eliminar'
  }).then(result => {
    if (result.isConfirmed) {
      const form = document.getElementById('delete-form');
      form.action = `/items/delete/${id}/`;
      form.submit();
    }
  });
};
