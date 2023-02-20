const varientButton = document.querySelectorAll(".var-btn");
const price = document.getElementById("price") 
const card = document.querySelectorAll(".imgButton")
const mainImage = document.getElementById("main-image")
const imgSrc = mainImage.src

console.log(imgSrc)

varientButton.forEach(function(button) {
  button.addEventListener('click', function(event) {
    const attributeValue = event.target.getAttribute('data');
    price.style.opacity="0";
    setTimeout(function(){
      price.innerHTML ="₹ " + attributeValue;
      price.style.opacity="1";
    },500)
  });
});

card.forEach(function(a) {
  a.addEventListener('mouseover', function(event) {
    const attributeValue = event.target.getAttribute('data');
    mainImage.style.opacity="0";
    setTimeout(function(){
      mainImage.src=attributeValue;
      mainImage.alt=attributeValue;
      mainImage.style.opacity="1";
    },500)
    
  });
  a.addEventListener('mouseout', function(event) {
    mainImage.style.opacity="0";
    setTimeout(function(){
      mainImage.src=imgSrc;
      mainImage.alt=imgSrc;
      mainImage.style.opacity="1";
    },500)
  });
});


function calculateMonthlyPayment() {
    // Get the user inputs
    const loanAmount = document.getElementById('loanAmount').value;
    const interestRate = document.getElementById('interestRate').value / 100 / 12;
    const loanTerm = document.getElementById('loanTerm').value;

    // Calculate the monthly payment
    const monthlyPayment = (loanAmount * interestRate * Math.pow(1 + interestRate, loanTerm)) / (Math.pow(1 + interestRate, loanTerm) - 1);

    // Display the monthly payment
    document.getElementById('monthlyPayment').textContent = `₹${monthlyPayment.toFixed(2)}`;
}

    // Add an event listener to the calculate button
document.getElementById('calculateBtn').addEventListener('click', calculateMonthlyPayment);

