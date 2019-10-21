/*changes the form input based on chosen drop down value (makes handinling for django backend easier)*/
function changeForm(){
    var value = $("#task_select :selected").val();
    var company_or_name = document.getElementById('company_or_name')
    if (value=="Assignment"){
        company_or_name.name = "name";
    }
}

function changeForm2(){
    var delvalue = $("#del_select :selected").val();
    var company_or_name_del = document.getElementById('company_or_name_del')
    if (delvalue=="Assignment"){
        company_or_name_del.name = "name";
    }
}