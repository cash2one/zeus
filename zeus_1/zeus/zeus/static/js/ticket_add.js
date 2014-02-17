$('#sel_type_id').change(function() {
    $('#div_os, #div_hd').hide();
    var typeId = $(this).val();
    switch (typeId) {
    case '1':
        $('#div_os').show();
        break;

    case '2':
        $('#div_hd').show();
        break;
    }
}).change();

$('#btn_submit').click(function() {

    if (!$('#sel_type_id').val()) {
        alert('请选择需求类型');
        return false;
    }

});
