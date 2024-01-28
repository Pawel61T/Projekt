$(document).ready(function() {
    console.log("offert");
    //messages = document.getElementsByClassName("messages");
    //messages.fadeOut(5000); // 5 seconds x 1000 milisec = 5000 milise
    $('#id_offer_type').on('change', function() {
        console.log("change")
        if( this.value ==  "1"){
            console.log("1");
            $('#id_number_of_rooms').attr('value','');
            $('#id_number_of_rooms').hide()
            $('label[for="id_number_of_rooms"]').hide()
            $('#id_capacity').show()
            $('label[for="id_capacity"]').show()
        }
        else{
            console.log("2");
            $('#id_capacity').attr('value','');
            $('#id_number_of_rooms').show()
            $('label[for="id_number_of_rooms"]').show()
            $('#id_capacity').hide()
            $('label[for="id_capacity"]').hide()
        }
      });
      $('#id_offer_type').trigger('change');
});
