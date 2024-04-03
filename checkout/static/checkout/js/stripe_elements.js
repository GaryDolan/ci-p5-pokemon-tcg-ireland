/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/
// Get public id from checkout templates, removing quotation marks
const stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
const clientSecret = $("#id_client_secret").text().slice(1, -1);

// Set up stripe using public key 
const stripe = Stripe(stripePublicKey);

// Create instance of stripe elements
const elements = stripe.elements();

// Style for the element
const style = {
  base: {
    color: "#000",
    fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    fontSmoothing: "antialiased",
    fontSize: "16px",
    "::placeholder": {
      color: "#aab7c4",
    },
  },
  invalid: {
    color: "#075997",
    iconColor: "#dc3545",
  },
};
// Use instance of stripe elements and style to create a card element
const card = elements.create("card", { style: style, disableLink: true });

// Mount card element to target div
card.mount("#card-element");

// Handle realtime validation errors on the card element
card.addEventListener("change", function (event) {
  const errorDiv = document.getElementById("card-errors");
  if (event.error) {
    const html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
    $(errorDiv).html(html);
  } else {
    errorDiv.textContent = "";
  }
});

// Handle form submit
const form = document.getElementById("payment-form");

form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    //Disable before submitting data to prevent multiple submissions
    card.update({ disabled: true });
    $("#submit-button").attr("disabled", true);
    $("#payment-form").fadeToggle(100);
    $("#loading-overlay").fadeToggle(100);

    const saveInfo = Boolean($("#id-save-info").attr("checked"));
    // From using {% csrf_token %} in the form
    const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    const postData = {
        csrfmiddlewaretoken: csrfToken,
        client_secret: clientSecret,
        save_info: saveInfo,
    };
    const url = "/checkout/cache_checkout_data/";
    //Confirm the payment using given details
    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county.value),
                    },
                },
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.postcode.value),
                    state: $.trim(form.county.value),
                },
            },
        }).then(function (result) {
            // Put any errors into error div on checkout template 
            if (result.error) {
                const errorDiv = document.getElementById("card-errors");
                const html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $("#payment-form").fadeToggle(100);
                $("#loading-overlay").fadeToggle(100);
                // If error returned re-enable the stripe and submit so user can fix errors
                card.update({ disabled: false });
                $("#submit-button").attr("disabled", false);
            } else {
                if (result.paymentIntent.status === "succeeded") {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        location.reload();
    });
});