//function toggle_button_deactivate(element){
//    console.log(element.options[element.selectedIndex].style.color)
//    return element.options[element.selectedIndex].value;
//
//}
function show_group_items(){
    const group_items = document.getElementById('group_items')
    const group_item_checkbox = document.getElementById('id_is_group_item')
    if (group_item_checkbox.checked) {
        group_items.className = '';
    }
    else{
        // Unselect all elements
        elements = document.getElementById('id_group_item_child_item').options
        for(var i = 0; i < elements.length; i++){
          elements[i].selected = false;
        }
        group_items.className = 'hidden';
    }
}