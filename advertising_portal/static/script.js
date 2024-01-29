let rating = 0

$(document).ready(function() {
    
    //messages = document.getElementsByClassName("messages");
    //messages.fadeOut(5000); // 5 seconds x 1000 milisec = 5000 milisec
    $('#message').fadeOut(5000);
    $('.save-opinion').on('click', function(){
        let _comment = $('.comment-text').val();
        let _offertid = $(this).data('offert');
        let _csrf = $(this).data('csrf');    
        // Ajax
        $.ajax({
            url:"/main/save_opinion",
            type:"post",
            data:{
                comment: _comment,
                rating: rating,
                offert_id: _offertid,
                csrfmiddlewaretoken: _csrf
            },
            dataType:'json',
            beforeSend:function(){
                $('.save-opinion').addClass('disabled').text('Saving...')
            },
            success:function(res){
                if(res.bool==true){
                    $('.comment-text').val('')
                    //Append element
                    let newDate = new Date();
                    let datetime = newDate.today() + ", " + newDate.timeNow();
                    let _html=   '<div class="card mb-2 mt-2 animate__animated animate__bounce">\
                    <div class="card-body">\
                        <p style="font-size: 1.3rem;">'+_comment+'</p>\
                        <p>\
                          <b>Added by:</b> '+res.user_name+' '+res.user_surname+' on '+datetime+'<br/>\
                          <b>Rating:</b> '+rating+'/5\
                        </p>\
                    </div>\
                    </div>';
                    $('.opinion-wrapper').prepend(_html)
                    let output = document.getElementById("output");
                    remove()
                    rating = 0;
                    output.innerText = "Rating is: 0/5"; 
                }
                else{
                    alert('Make sure you filled rating and comment inputs!')
                }
                $('.save-opinion').removeClass('disabled').text('Submit Comment')
            }
        })
    })
});
// To access the stars
let stars = 
    document.getElementsByClassName("star");
// Funtion to update rating
function gfg(n) {
    remove();
    let output = document.getElementById("output");
    for (let i = 0; i < n; i++) {
        if (n == 1) cls = "one";
        else if (n == 2) cls = "two";
        else if (n == 3) cls = "three";
        else if (n == 4) cls = "four";
        else if (n == 5) cls = "five";
        stars[i].className = "star " + cls;
    }
    output.innerText = "Rating is: " + n + "/5";
    rating = n;
}
 
// To remove the pre-applied styling
function remove() {
    let i = 0;
    while (i < 5) {
        stars[i].className = "star";
        i++;
    }
}

// For todays date;
Date.prototype.today = function () { 
    return ((this.getDate() < 10)?"0":"") + this.getDate() +"/"+(((this.getMonth()+1) < 10)?"0":"") + (this.getMonth()+1) +"/"+ this.getFullYear();
}

// For the time now
Date.prototype.timeNow = function () {
     return ((this.getHours() < 10)?"0":"") + this.getHours() +":"+ ((this.getMinutes() < 10)?"0":"") + this.getMinutes() +":"+ ((this.getSeconds() < 10)?"0":"") + this.getSeconds();
}