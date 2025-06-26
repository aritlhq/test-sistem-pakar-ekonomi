// Wait for DOM to be fully loaded
let cart = [];

// Main function on DOM ready
document.addEventListener('DOMContentLoaded', function () {
    initCart();
    initCharts();
    animateCounters();
    validateForms();

    // Fixed header on scroll
    window.addEventListener('scroll', function () {
        document.querySelector('.navbar').classList.toggle('sticky-top', window.scrollY > 100);
    });
});

// Initialize Cart
function initCart() {
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    const cartBadge = document.querySelector('.cart-badge');
    const cartItemsContainer = document.querySelector('.cart-items');
    const cartFooter = document.querySelector('.cart-footer');
    const emptyCart = document.querySelector('.empty-cart');

    updateCartUI();

    addToCartButtons.forEach(button => {
        button.addEventListener('click', function () {
            const id = this.dataset.id;
            const name = this.dataset.name;
            const price = parseInt(this.dataset.price);

            const existing = cart.find(item => item.id === id);
            if (!existing) {
                cart.push({ id, name, price, quantity: 1 });
                updateCartUI();
                showToast(`${name} telah ditambahkan ke keranjang!`, 'success');
            } else {
                showToast(`${name} sudah ada di keranjang.`, 'warning');
            }
        });
    });

    function updateCartUI() {
        cartBadge.textContent = cart.length;

        cartItemsContainer.innerHTML = '';
        if (cart.length === 0) {
            emptyCart.classList.remove('d-none');
            cartFooter.classList.add('d-none');
            return;
        }

        emptyCart.classList.add('d-none');
        cartFooter.classList.remove('d-none');

        let total = 0;
        cart.forEach((item, index) => {
            total += item.price;
            const itemHTML = document.createElement('div');
            itemHTML.classList.add('cart-item');
            itemHTML.innerHTML = `
                <div class="cart-item-details">
                    <h6 class="cart-item-title">${item.name}</h6>
                    <div class="cart-item-price">Rp${formatNumber(item.price)}</div>
                </div>
                <div class="cart-item-remove" data-index="${index}">
                    <i class="fas fa-times-circle"></i>
                </div>`;

            itemHTML.querySelector('.cart-item-remove').addEventListener('click', () => {
                cart.splice(index, 1);
                updateCartUI();
            });

            cartItemsContainer.appendChild(itemHTML);
        });

        document.querySelector('.cart-total').textContent = `Rp${formatNumber(total)}`;
    }
}

function showToast(message, type = 'success') {
    const toast = document.createElement('div');
    toast.className = `alert alert-${type} alert-dismissible fade show position-fixed bottom-0 end-0 m-3`;
    toast.style.zIndex = 9999;
    toast.innerHTML = `${message}<button type="button" class="btn-close" data-bs-dismiss="alert"></button>`;
    document.body.appendChild(toast);
    setTimeout(() => {
        toast.remove();
    }, 3000);
}

function formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, '.');
}

// Dummy function for completeness
function initCharts() {}
function animateCounters() {}
function validateForms() {}
