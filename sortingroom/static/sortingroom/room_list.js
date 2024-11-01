dialog.addEventListener("click", (e) => {
    const dialog = document.getElementById('room_selection-dialog');
    if(!dialog.contains(e.target)){
        dialog.close()
    }
})

function openDialog(roomId, roomPhoto, roomType, roomPrice, roomDesc) {
    const dialog = document.getElementById('room_selection-dialog');
    const centerpoint = document.querySelector('.centerpoint');

    document.getElementById('dialog-room-photo').src = roomPhoto;
    document.getElementById('dialog-room-type').innerText = `${roomType} Room`;
    document.getElementById('dialog-room-price').innerText = `$${roomPrice}/night`;
    document.getElementById('dialog-room-desc').innerText = roomDesc;

    const reserveButton = dialog.querySelector('button[onclick^="goToReserve"]');
    reserveButton.setAttribute('onclick', `goToReserve('${roomId}')`);

    centerpoint.style.display = 'flex';
    dialog.showModal();
}


function closeDialog() {

    const dialog = document.getElementById('room_selection-dialog');
    const centerpoint = document.querySelector('.centerpoint');

    dialog.close();
    centerpoint.style.display = 'none';
}


function goToReserve(roomId) {
    if (roomId) {
        window.location.href = `/reserve_room/${roomId}/`;  // Update if route differs
    } else {
        console.error("Room ID is missing. Cannot redirect.");
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
        messageElement.style.display = 'none'; // Hide the message if no method is selected
    }
}


