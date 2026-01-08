$(document).ready(function() {
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = getCookie('csrftoken');

    $('#waitlist-form').on('submit', function(e) {
        e.preventDefault();

        const email = $('#waitlist-email').val();
        const $submitBtn = $('#waitlist-submit');
        const $emailInput = $('#waitlist-email');
        const $messageBox = $('#waitlist-message');

        $submitBtn.prop('disabled', true).text('Processing...');
        $emailInput.prop('readonly', true);
        $messageBox.addClass('d-none').removeClass('bg-success bg-danger text-white');

        $.ajax({
            url: '/api/v1/communication/waitlist/',
            type: 'POST',
            contentType: 'application/json',
            headers: { 'X-CSRFToken': csrftoken },
            data: JSON.stringify({ email: email }),
            success: function(data, textStatus, xhr) {
                if (xhr.status === 200 || xhr.status === 201) {
                    $messageBox
                        .text("You have successfully been added to the waitlist and will be notified on launch")
                        .addClass('bg-success text-white')
                        .removeClass('d-none');
                    $submitBtn.text('Signed Up');
                }
            },
            error: function(xhr) {

                let errorData = xhr.responseText;
                try {
                    const json = JSON.parse(xhr.responseText);
                    errorData = json.email ? `Email: ${json.email[0]}` : xhr.responseText;
                } catch(e) {}

                $messageBox
                    .text(errorData)
                    .addClass('bg-danger text-white')
                    .removeClass('d-none');

                $submitBtn.prop('disabled', false).text('Join Waitlist');
                $emailInput.prop('readonly', false);
            }
        });
    });


    $('#contact-form').on('submit', function(e) {
        e.preventDefault();

        const contact_name = $('#contact-name').val();
        const contact_email = $('#contact-email').val();
        const contact_subject = $('#contact-subject').val();
        const contact_message = $('.ql-editor').html();
        const $submitBtn = $('#contact-submit');
        const $contactNameInput = $('#contact-name');
        const $contactEmailInput = $('#contact-email');
        const $contactSubjectInput = $('#contact-subject');
        const $contactMessageInput = $('#contact-message');
        const $messageBox = $('#contact-response-message');

        $submitBtn.prop('disabled', true).text('Processing...');
        $contactNameInput.prop('readonly', true);
        $contactEmailInput.prop('readonly', true);
        $contactSubjectInput.prop('readonly', true);
        $contactMessageInput.prop('readonly', true);
        $messageBox.addClass('d-none').removeClass('bg-success bg-danger text-white');
        
        
        $.ajax({
            url: '/api/v1/communication/contact-form/',
            type: 'POST',
            contentType: 'application/json',
            headers: { 'X-CSRFToken': csrftoken },
            data: JSON.stringify({ 
                email: contact_email, 
                name: contact_name, 
                subject: contact_subject,
                message: contact_message }),
            success: function(data, textStatus, xhr) {
                if (xhr.status === 200 || xhr.status === 201) {
                    $messageBox
                        .text("Thank you for reaching out to us, we will respond as soon as possible.")
                        .addClass('bg-success text-white')
                        .removeClass('d-none');
                    $submitBtn.text('Sent');
                    $("#contact-form").hide()
                }
            },
            error: function(xhr) {

                let errorData = xhr.responseText;
                console.log(xhr)
                try {
                    const json = JSON.parse(xhr.responseText);
                    errorData = json.contact_email ? `Email: ${json.contact_email[0]}` : xhr.responseText;
                } catch(e) {}

                $messageBox
                    .text(errorData)
                    .addClass('bg-danger text-white')
                    .removeClass('d-none');

                $submitBtn.prop('disabled', false).text('Send Message');
                $contactNameInput.prop('readonly', false);
                $contactEmailInput.prop('readonly', false);
                $contactSubjectInput.prop('readonly', false);
                $contactMessageInput.prop('readonly', false);
            }
        });
    });

    // utils

// 1. Initialize Quill
const quill = new Quill('#editor-container', {
  theme: 'snow',
  placeholder: 'How can we help?',
  modules: {
    toolbar: [
      ['bold', 'italic', 'underline'],        // toggled buttons
      [{ 'list': 'ordered'}, { 'list': 'bullet' }],
      ['link', 'clean']                       // link and remove formatting
    ]
  }
});

// 2. Sync Quill content to the hidden textarea on form submission
const form = document.querySelector('#contact-form');
form.onsubmit = function() {
  const messageInput = document.querySelector('#contact-message');
  
  // Get the HTML content from Quill
  const html = quill.root.innerHTML;
  
  // Check if it's empty (Quill usually leaves a <p><br></p> when empty)
  if (html === '<p><br></p>') {
    messageInput.value = '';
  } else {
    messageInput.value = html;
  }
};

});