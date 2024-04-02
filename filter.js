function filterByBrand(brand) {
    const allProducts = getProductsData();
    const filteredProducts = allProducts.filter(product => product.brand === brand);
  
    // Update product list UI with filtered products
    updateProductList(filteredProducts);
  }
  
  // Add event listener to brand filter checkbox
  const brandCheckbox = document.getElementById("brandFilter");
  brandCheckbox.addEventListener("change", () => {
    if (brandCheckbox.checked) {
      filterByBrand(brandCheckbox.value);
    } else {
      // Uncheck - display all products
      updateProductList(getProductsData());
    }
  });
  