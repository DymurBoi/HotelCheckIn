function openDialog(roomId, catId, roomPhoto, roomPrice, roomDesc) {
    console.log("Room ID:", roomId, "Category ID:", catId); // Debugging line
    const dialog = document.getElementById('room_selection-dialog');
    const centerpoint = document.querySelector('.centerpoint');
    
    document.getElementById('dialog-category-id').innerText = `${catId} Room`;
    document.getElementById('dialog-room-photo').src = roomPhoto;
    document.getElementById('dialog-room-price').innerText = `P${roomPrice}/night`;
    document.getElementById('dialog-room-desc').innerText = roomDesc;

    const reserveButton = dialog.querySelector('button[onclick^="goToReserve"]');
    reserveButton.setAttribute('onclick', goToReserve('${roomId}'));

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
        console.log("Redirecting with roomId:", roomId);
        window.location.href = 'reserve_room/${roomId}/';
    } else {
        console.error("Category ID is missing. Cannot redirect.");
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const reservationForm = document.getElementById('reservationForm');
    
    reservationForm.addEventListener('submit', (event) => {
        const checkInDate = new Date(document.getElementById('check_in').value);
        const checkOutDate = new Date(document.getElementById('check_out').value);
        const today = new Date();
        today.setHours(0, 0, 0, 0); // Remove time portion for comparison
        
        // Check if the check-in date is before today
        if (checkInDate < today) {
            event.preventDefault(); // Prevent form submission
            alert('Check-in date must be today or later.');
            return;
        }

        // Check if the check-in date is after or equal to the check-out date
        if (checkInDate >= checkOutDate) {
            event.preventDefault(); // Prevent form submission
            alert('Check-in date must be before the check-out date.');
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
        messageElement2.innerText = `The total amount you will be charged is: $${totalAmount}.`;
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
