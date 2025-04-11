// Called from products.html
function selectLaptop(model, price) {
    sessionStorage.setItem("laptopModel", model);
    sessionStorage.setItem("amount", price);
    window.location.href = "order.html";
}

// Called from order.html
function submitOrder() {
    const orderData = {
        customerId: "CUST" + Math.floor(1000 + Math.random() * 9000),
        name: document.getElementById("name").value,
        dob: document.getElementById("dob").value,
        mobile: document.getElementById("mobile").value,
        email: document.getElementById("email").value,
        address: document.getElementById("address").value,
        orderDate: new Date().toISOString().split("T")[0],
        laptopModel: document.getElementById("laptopModel").value,
        amount: document.getElementById("amount").value
    };

    fetch("http://127.0.0.1:5000/place_order", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(orderData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.orderId) {
            alert("✅ Order Placed! Order ID: " + data.orderId);
            window.location.href = "products.html";  // Redirect back to main page
        } else {
            alert("❌ Error placing order: " + JSON.stringify(data));
        }
    })
    .catch(error => alert("❌ Network Error: " + error.message));
}
