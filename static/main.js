const openModalButton = document.getElementById('open-modal-button')
const modalContainer = document.getElementById('modal-container')
const modal = document.getElementById('modal')
const closeModalSymbol = document.getElementById('close-modal-symbol')

openModalButton.addEventListener('click', () => {
    modalContainer.classList.add('visible')
})

modalContainer.addEventListener('click', () => {
    modalContainer.classList.remove('visible')
})

closeModalSymbol.addEventListener('click', () => {
    modalContainer.classList.remove('visible')
})

modal.addEventListener('click', (e) => {
    e.stopPropagation()
})