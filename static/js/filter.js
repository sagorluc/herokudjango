$(document).ready(function(){
    // alert('done')
    $(".ajaxLoader").hide();
	$(".filter-checkbox").on('click', function(){
		var filter_object={};
		$(".filter-checkbox").each(function(index,ele){
			var filter_value=$(this).val();
			var filter_key=$(this).data('filter');
			// console.log(filter_key,filter_value);
			filter_object[filter_key]=Array.from(document.querySelectorAll('input[data-filter='+filter_key+']:checked')).map(function(el){
			 	return el.value;
			});
		});
        // console.log(filter_object)
		$.ajax({
			url: "/filter-data",
			data: filter_object,
			dataType:'json',
            beforeSend: function(){
                $(".ajaxLoader").show();
            },		
			success:function(res){
                console.log(res);				
				$("#filteredProducts").html(res.datas, res.page_products);				
				$(".ajaxLoader").hide();				
			}
		});
	});
});
