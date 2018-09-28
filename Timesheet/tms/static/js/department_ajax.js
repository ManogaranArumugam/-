//var formName = $(elem).closest('form').attr('name')
//  alert(formName);



  $(function () {
        $("#id_project_type").change(function () {
            var type_project = $(this).find("option:selected").val();

                 $.ajax({
//                            type: 'POST',
                            data: {'project_type': type_project},
                            url: '../../tms/project_list',
                            contentType: "application/json; charset=utf-8",
                            dataType: "json",
                            beforeSend: function() {
                                $('#id_project').find("option:gt(0)").remove();
                            },
                            success: function(data){
                             for(var i = 0; i<data.length ; i++){ //data[1] contains no of sem

                                     console.log(data[i][0])
//                              $('#id_project_name').children('option:not(:first)').remove();


                                $('#id_project').append('<option value="' + data[i][0] + '">' +data[i][2]+' - '+ data[i][1].toUpperCase() +'</option>');



                             }


//                              console.log(data[0][0])

//                            console.log(data)
                            },
                            error: function(data){

                            alert("something wrong with this page")

                            }
                        });


        });
    });



  $(function () {
        $("#id_project").change(function () {
            var id = $(this).find("option:selected").val();

                 $.ajax({
//                            type: 'POST',
                            data: {'project_id': id},
                            url: '../../tms/sub_project_list',
                            contentType: "application/json; charset=utf-8",
                            dataType: "json",
                            beforeSend: function() {
                                $('#id_subproject').find("option:gt(0)").remove();
                            },
                            success: function(data){
                             for(var i = 0; i<data.length ; i++){ //data[1] contains no of sem

                                     console.log(data[i][0])
//

                                $('#id_subproject').append('<option value="' + data[i][0] + '">' +data[i][2]+' - '+ data[i][1].toUpperCase() +'</option>');



                             }


//                              console.log(data[0][0])

//                            console.log(data)
                            },
                            error: function(data){

                            alert("something wrong with this page")

                            }
                        });


        });
    });

