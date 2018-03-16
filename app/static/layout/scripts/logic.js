function highlightMe(id) {
  var highlightedElements = document.getElementsByClassName('highlighted')
  for (var i = 0; i < highlightedElements.length; i++) {
    highlightedElements[i].classList.remove('highlighted')
  }
  // document.getElementById(id).classname += "highlighted"
  document.getElementById(hash).style.backgroundColor="Yellow";

}
