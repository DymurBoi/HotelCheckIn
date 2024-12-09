function openRoomDialog(roomId, catId, roomPhoto, roomPrice, roomDesc) {
    console.log("Room ID:", roomId, "Category ID:", catId); // Debugging line
    const dialog = document.getElementById('room_selection-dialog');
    const centerpoint = document.querySelector('.centerpoint');
    
    // Update dialog content
    document.getElementById('dialog-category-id').innerText = `${catId} Room`;
    document.getElementById('dialog-room-photo').src = roomPhoto;
    document.getElementById('dialog-room-price').innerText = `P${roomPrice}/night`;
    document.getElementById('dialog-room-desc').innerText = roomDesc;

    // Update the "Reserve" button to use the correct roomId
    const reserveButton = dialog.querySelector('#reserve-button');
    reserveButton.onclick = () => goToReserve(roomId); // Directly assign function

    // Show the dialog
    centerpoint.style.display = 'flex';
    dialog.showModal();
}

function closeRoomDialog() {
    const dialog = document.getElementById('room_selection-dialog');
    const centerpoint = document.querySelector('.centerpoint');

    dialog.close();
    centerpoint.style.display = 'none';
}

function goToReserve(roomId) {
    if (roomId) {
        console.log("Redirecting with roomId:", roomId);
        window.location.href = `reserve_room/${roomId}/`;
    } else {
        console.error("Category ID is missing. Cannot redirect.");
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const reservationForm = document.getElementById('reservationForm');

    reservationForm.addEventListener('submit', (event) => {
        // Get check-in and check-out dates
        const checkInInput = document.getElementById('id_check_in');
        const checkOutInput = document.getElementById('id_check_out');
        const checkInDate = new Date(checkInInput.value);
        const checkOutDate = new Date(checkOutInput.value);

        // Get today's date (without time for accurate comparison)
        const today = new Date();
        today.setHours(0, 0, 0, 0);

        // Check if check-in date is valid
        if (isNaN(checkInDate.getTime())) {
            event.preventDefault();
            alert('Please select a valid check-in date.');
            checkInInput.focus();
            return;
        }

        // Check if check-out date is valid
        if (isNaN(checkOutDate.getTime())) {
            event.preventDefault();
            alert('Please select a valid check-out date.');
            checkOutInput.focus();
            return;
        }

        // Check if check-in date is today or later
        if (checkInDate < today) {
            event.preventDefault();
            alert('Check-in date must be today or later.');
            checkInInput.focus();
            return;
        }

        // Check if check-in date is before check-out date
        if (checkInDate >= checkOutDate) {
            event.preventDefault();
            alert('Check-in date must be before the check-out date.');
            checkOutInput.focus();
            return;
        }
    });
});


function updatePaymentMessage(total_cost) {
    const paymentMethod = document.getElementById('payment-method').value;
    const totalAmount = total_cost; // Update this with the actual total amount dynamically if needed
    const messageElement1 = document.getElementById('payment-message1');
    const messageElement2 = document.getElementById('payment-message2');
    const paymentMessages = document.getElementById('payment-messages');

    if (paymentMethod) {
        paymentMessages.style.display = 'block';
        messageElement1.innerText = `You have chosen to pay by ${paymentMethod}. You will be forwarded to the ${paymentMethod} website to proceed with this transaction.`;
        messageElement2.innerText = `The total amount you will be charged is: ₱${totalAmount}.`;
    } else {
        messageElement.style.display = 'none'; // Hide the message if no method is selected
    }

// Custom alert handling (moved from HTML)
document.addEventListener("DOMContentLoaded", function () {
    const alert = document.getElementById('custom-alert');
    if (alert) {
        alert.style.display = 'flex';
        document.getElementById('ok-button').addEventListener('click', function () {
            window.location.href = "/room_list/"; // Update this to the actual room list URL
        });
    }
});
}
