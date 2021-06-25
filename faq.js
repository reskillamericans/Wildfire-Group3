const buttons = document.querySelector('.images').querySelectorAll('a');
const paragraphs = document.querySelector('.questions').querySelectorAll('p');

const newDiv = document.createElement('div');
newDiv.textContent = '"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt."'


for( let i = 0; i < buttons.length; i++) {
buttons[i].addEventListener('click', () => {
   newDiv.classList.toggle('active');
   paragraphs[i].append(newDiv);
});
}