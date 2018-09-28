$(document).ready(function(e){


var url_filename=   document.location.href;
var find_page =url_filename.search("/sub_project_form/");

if(find_page==25){
    $("#id_project_type").attr("disabled", "disabled");
    $("#id_project_code").attr("disabled", "disabled");
    $("#id_project_name").attr("disabled", "disabled");
    $("#id_subproject_code").attr("disabled", "disabled");
    $("#id_client").attr("disabled", "disabled");
    $("#id_enduser").attr("disabled", "disabled");
    $("#id_parent").hide();
    $('label[for="id_parent"]').hide();

}
});

$("#sub_project_form").on('submit',function(e) {
   e.preventDefault();

   $("#id_project_type").removeAttr("disabled");
    $("#id_project_code").attr("disabled", false);
    $("#id_project_name").attr("disabled", false);
    $("#id_subproject_code").attr("disabled", false);
    $("#id_client").attr("disabled", false);
    $("#id_enduser").attr("disabled", false);
    $("#id_parent").show();
    $('label[for="id_parent"]').show();




});

