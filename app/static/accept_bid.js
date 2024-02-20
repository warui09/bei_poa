""" accept a bid """

$(document).ready(function() {
    // Set default headers for all AJAX requests
    $.ajaxSetup({
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token() }}'
        }
    });

    let acceptButtons = document.querySelectorAll('.accept-bid');
    acceptButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            let bidId = button.dataset.bidId;
            $.ajax('/user_products' + bidId, {
                method: 'POST',
                data: JSON.stringify({ bidId: bidId })
            })
            .then(response => {
                if (response.ok) {
                    button.closest('.list-group-item').classList.add('accepted');
                } else {
                    console.error('Failed to accept bid');
                }
            })
            .catch(error => {
                console.error('Error accepting bid:', error);
            });
        });
    });
});

