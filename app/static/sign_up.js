""" jquery to handle form submission """

$(document).ready(function() {
    $('#sign-up-form').submit(function(event) {
        event.preventDefault();
        let $form = $(this);
        let $submitButton = $form.find('button[type="submit"]');
        $.ajax({
            type: 'POST',
            url: '/sign_up',
            data: $form.serialize(),
            beforeSend: function() {
                $submitButton.prop('disabled', true);
            },
            success: function(response) {
                console.log(response);
                $form[0].reset();
            },
            error: function(error) {
                console.log(error);
                $submitButton.prop('disabled', false);
            },
            complete: function() {
                $submitButton.prop('disabled', false);
            }
        });
    });
});
