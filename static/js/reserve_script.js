const dialog = document.getElementById('room_selection-dialog1');

dialog.addEventListener("click", (e) => {
    if (!dialog.contains(e.target)) {
        closeDialog(); // Call the closeDialog function here
    }
});

function openDialog(roomId, roomPhoto, roomType, roomPrice, roomDesc) {
    const centerpoint = document.querySelector('.centerpoint');

    document.getElementById('dialog-room-photo').src = roomPhoto;
    document.getElementById('dialog-room-type').innerText = `${roomType} Room`;
    document.getElementById('dialog-room-price').innerText = `$${roomPrice}/night`;
    document.getElementById('dialog-room-desc').innerText = roomDesc;

    const reserveButton = dialog.querySelector('button[onclick^="goToReserve"]');
    if (reserveButton) { // Check if reserveButton exists
        reserveButton.setAttribute('onclick', `goToReserve('${roomId}')`);
    }

    centerpoint.style.display = 'flex';
    dialog.showModal();
}

function closeDialog() {
    const centerpoint = document.querySelector('.centerpoint');

    dialog.close();
    centerpoint.style.display = 'none';
}

function viewRoom(userId) {
    if (userId) {
        window.location.href = `http://127.0.0.1:8000/profile/room/${userId}/`; // Updated to use the full URL
    } else {
        console.error("User ID is missing. Cannot redirect.");
    }
}
function viewReservations() {
        window.location.href = `http://127.0.0.1:8000/profile/reservation_list/`; // Updated to use the full URL
}
function checkInRoom(userId) {
    if (userId) {
        window.location.href = `http://127.0.0.1:8000/profile/room/${userId}/`; // Updated to use the full URL
    } else {
        console.error("User ID is missing. Cannot redirect.");
    }
}

function updatePaymentMessage(total_cost) {
    const paymentMethod = document.getElementById('payment-method').value;
    const totalAmount = total_cost; // Update this with the actual total amount dynamically if needed
    const messageElement1 = document.getElementById('payment-message1');
    const messageElement2 = document.getElementById('payment-message2');
    const paymentMessages = document.getElementById('payment-messages');

    if (paymentMethod) {
        paymentMessages.style.display = 'block';
        messageElement1.innerText = `You have chosen to pay by ${paymentMethod}. You will be forwarded to the ${paymentMethod} website to proceed with this transaction.`;
        messageElement2.innerText = `The total amount you will be charged is: $${totalAmount}.`;
    } else {
        paymentMessages.style.display = 'none'; // Hide the message if no method is selected
    }
}
