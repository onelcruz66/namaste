// static/js/stripe.js
console.log("Hello World")
// new
// Get Stripe publishable key
fetch("/config/")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  console.log("Getting config stuff: ", data)
  const stripe = Stripe(data.publicKey);

  document.querySelector("#submitBtn").addEventListener("click", () => {
    // Get Checkout Session ID
    fetch("/create-checkout-session/")
    .then((result) => { return result.json(); })
    .then((data) => {
      console.log("Getting checkout stuff: ",data);
      // Redirect to Stripe Checkout
      return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
    .then((res) => {
      console.log(res);
    });
  });
});


// console.log("Stripe Public Key: ", stripePublicKey);
// var stripe = stripe(stripePublicKey);
// var elements = stripe.elements();
// var clientSecret = "{{ client_secret }}";
// var style = {
//     base: {
//         color: "#32325d",
//     }
// };

// var card = elements.create("card", { style: style });
// card.mount("#card-element");

// card.addEventListener('change', ({error}) => {
//     const displayError = document.getElementById('card-errors');
//     if (error) {
//         displayError.textContent = error.message;
//     } else {
//         displayError.textContent = '';
//     }
// });

// var form = document.getElementById('payment-form');
// form.addEventListener('submit', function(ev) {
//     ev.preventDefault();
//     stripe.confirmCardPayment(clientSecret, {
//         payment_method: {
//             card: card,
//             billing_details: {
//                 name: 'Jenny Rosen'
//             }
//         }
//     }).then(function(result) {
//         if (result.error) {
//             // Show error to your customer (e.g., insufficient funds)
//             console.log(result.error.message);
//         } else {
//             // The payment has been processed!
//             if (result.paymentIntent.status === 'succeeded') {
//                 console.log('Money is in the bank!');
//                 // Redirect or update UI
//             }
//         }
//     });
// });
