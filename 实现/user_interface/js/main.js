layui.use('element', function(){
    let element = layui.element;
});

let content = $('#content');
if (getCookie('frame_url'))
    content.attr('src', getCookie('frame_url'));

content.bind('load', change_url);

who_am_i();
