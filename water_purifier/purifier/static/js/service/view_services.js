$(document).ready(function () {

    var deleteServiceLinks = document.querySelectorAll('.delete-service-btn');

    deleteServiceLinks.forEach(function(link) {
        link.addEventListener('click', function(event) {
            event.preventDefault();

            var service_id = link.getAttribute('data-bs-serviceId');
            var service_name = link.getAttribute('data-bs-serviceName');
            console.log(service_id);
            console.log(service_name);

            // Set the href attribute of the "Delete" link
            var confirmDeleteLink = document.getElementById('confirmServiceDelete');
            var deleteModalBody = document.getElementById('deleteServiceModalBody');
            deleteUrl = `/delete_service/${service_id}`;

            confirmDeleteLink.href = deleteUrl;
            deleteModalBody.innerHTML = 'you want to delete <b>' + service_name + '</b> from services list.';
        });
    });

});