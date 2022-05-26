console.log("hello");
let cart1 = document.getElementsByClassName("add-to-cart")
for (var i = 0; i < cart1.length; i++) {
    cart1[i].addEventListener('click', function (e) {
        e.preventDefault()
        productId = this.dataset.productid
        action = this.dataset.action
        console.log('clicked', productId, action);
        if (user == 'AnonymousUser') {
            AddCookie(productId, action)
        }
        else {
            if (confirm(" Confirm to modify  your order ") == true) {
                Add_to_cart(productId, action)
            }
        }
    })
}
function AddCookie(productId, action) {
    if (action == 'add') {
        if (cart[productId] == undefined) {
            cart[productId] = { 'quantity': 1 }
        } else {
            cart[productId]['quantity'] += 1
        }
    }
    if (action == 'remove') {
        cart[productId]['quantity'] -= 1
        if (cart[productId]['quantity'] <= 0) {
            delete cart[productId]
            alert('Product deleted')
        }
    }
    console.log(cart);
    document.cookie='cart='+JSON.stringify(cart)+";domain=;path=/"
    location.reload()

}





function Add_to_cart(productId, action) {
    var url = '/update_cart/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })
        .then((response) => {
            return response.json()
        }).then((data) => {
            console.log(data);
            location.reload()
        })

}


