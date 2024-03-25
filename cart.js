function addToCart(productId) {
    // Get product details from the DOM
    const product = getProductDetails(productId);
  
    // Access cart items from Local Storage (assuming it's an array)
    let cartItems = JSON.parse(localStorage.getItem("cartItems")) || [];
  
    // Check if product already exists in cart
    const existingItem = cartItems.find(item => item.id === productId);
  
    if (existingItem) {
      existingItem.quantity++;
    } else {
      cartItems.push({ ...product, quantity: 1 });
    }
  
    // Update Local Storage with updated cart items
    localStorage.setItem("cartItems", JSON.stringify(cartItems));
  
    // Update cart UI (item count, total price)
    updateCartUI();
  }
  