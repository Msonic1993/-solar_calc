function GroundWorksFunction() {
  // Get the checkbox
  var checkBox = document.getElementById("GroundWorksCheck");
  var checkBox1 = document.getElementById("GroundWorksCheck1");
  // Get the output text
  var text = document.getElementById("textM2");

  // If the checkbox is checked, display the output text
  if (checkBox.checked == true){
    text.style.display = "block";
    document.getElementById("GroundWorksCheck1").disabled= true;
  } else {
    text.style.display = "none";
    document.getElementById("GroundWorksCheck1").disabled= false;

   if (checkBox1.checked == true){
    text.style.display = "none";
    document.getElementById("GroundWorksCheck").disabled= true;
    }else {
    text.style.display = "block";
    document.getElementById("GroundWorksCheck").disabled= false;
  }
}
}