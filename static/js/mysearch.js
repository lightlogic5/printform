

//顶部搜索栏搜索方法
function search_click(){
    var keywords = $('#search_keywords').val(),
        request_url = '';
    if(keywords == ""){
        request_url = "/polls/list/"
    }
    else {
        request_url = "/polls/list?keywords="+keywords
    }
    window.location.href = request_url
}


    $('#jsSearchBtn').on('click',function(){
        search_click()
    });
    //搜索表单键盘事件
    $("#search_keywords").keydown(function(event){
        if(event.keyCode == 13){
             $('#jsSearchBtn').trigger('click');
        }
    });