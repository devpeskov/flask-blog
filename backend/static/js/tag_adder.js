// <!-- To use the script you need the following html-structure -->
//
// <label class="form-label" for="tags[]">Tags</label><br>
// <span class="btn btn-outline-primary" onclick="addTagInput()">Add new tag</span>
// <div id="tags">
//   <!-- Default tag-inputs -->
//   <div class="row">
//     <div class="col-md-6">
//       <input type="text" class="form-control" name="tags[]" maxlength="100">
//     </div>
//     <div class="col-md-2">
//       <span class="btn btn-outline-danger" onclick="removeTagInput(this)">-</span>
//     </div>
//   </div>
//
//   <!-- Here will be placed new tag-inputs generated by javascript -->
// </div>
//
//
// <script src="/static/js/tag_adder.js"></script>

function addTagInput(){
  // get main container
  let tag_container = document.getElementById('tags');

  // creating div containers.
  let row_div = document.createElement("div");
  row_div.setAttribute("class", "row");
  let col_6_div = document.createElement("div");
  col_6_div.setAttribute("class", "col-md-6");
  let col_2_div = document.createElement("div");
  col_2_div.setAttribute("class", "col-md-2");

  // Creating the input element.
  let field = document.createElement("input");
  field.setAttribute("type", "text");
  field.setAttribute("class", "form-control");
  field.setAttribute("name", "tags[]");
  field.setAttribute("maxlength", "100");

  // Creating the minus span element.
  let minus = document.createElement("span");
  minus.setAttribute("onclick", "removeTagInput(this)");
  minus.setAttribute("class", "btn btn-outline-danger");
  let minusText = document.createTextNode("-");
  minus.appendChild(minusText);

  // Adding the elements to the DOM.
  col_6_div.appendChild(field);
  col_2_div.appendChild(minus);
  row_div.appendChild(col_6_div);
  row_div.appendChild(col_2_div);
  tag_container.appendChild(row_div);
}

function removeTagInput(minusElement){
  // first parent is col_2_div container
  // second parent is row_div container
  minusElement.parentElement.parentElement.remove();
}
