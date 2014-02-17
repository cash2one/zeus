function valid_form(memoryform){
	with(memoryform)
	{
		if(brand.value=="")
		{
			alert("内存厂商不能为空");
			brand.focus();
			return false;
		}
		else if((quantity.value=="")||isNaN(quantity.value))
		{
			alert("内存数量不能为空且是数字");
			quantity.focus();
			return false;
		}
        else if(category.value=="")
        {
            alert("内存类型不能为空");
            category.focus();
            return false;
        }
  	    else if(capacity.value=="")
        {
            alert("内存容量不能为空");
            capacity.focus();
            return false;
        }
	    else if(frequency.value=="")
        {
            alert("内存频率不能为空");
            frequency.focus();
            return false;
        }
    	else if(check.value=="")
        {
            alert("内存校验不能为空");
            check.focus();
            return false;
        }
	    else if(maintainer.value=="")
        {
            alert("维护人不能为空");
            maintainer.focus();
            return false;
        }
   	    else if((available.value=="")||isNaN(available.value))
        {
            alert("内存可用不能为空且为数字");
            available.focus();
            return false;
        }

	}


}
