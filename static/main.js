// vars getting info from HTML
const openModalButton = document.getElementById('open-modal-button')
const modalContainer = document.getElementById('modal-container')
const modal = document.getElementById('modal')
const closeModalSymbol = document.getElementById('close-modal-symbol')


// adding visisbility to the modal when we click the modal button
openModalButton.addEventListener('click', () => {
    modalContainer.classList.add('visible')
})

// making the modal invisible when we click outside the modal
modalContainer.addEventListener('click', () => {
    modalContainer.classList.remove('visible')
})

// making the modal invisible when we click the 'x' button on the modal
closeModalSymbol.addEventListener('click', () => {
    modalContainer.classList.remove('visible')
})

modal.addEventListener('click', (e) => {
    e.stopPropagation()
})