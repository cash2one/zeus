function tab1_form(tab1form){
    with(tab1form)
    {
        if(host.value=="")
        {
            alert("请填写主机");
            host.focus();
            return false;
        }
        else if(ip_list.value=="")
        {
            alert("IP不能为空");
            ip_list.focus();
            return false;
        }
        else if(idc.value=="idc_status")
        {
            alert("请选择机房");
            idc.focus();
            return false;
        }
        else if(disk.value=="")
        {
            alert("硬盘规格不能为空");
            disk.focus();
            return false;
        }
        else if(mem.value=="")
        {
            alert("内存不能为空");
            mem.focus();
            return false;
        }
        else if(os.value=="os_status")
        {
            alert("请选择是否重装系统");
            os.focus();
            return false;
        }
        else if(use.value=="")
        {
            alert("请填写用途");
            use.focus();
            return false;
        }
        else if(date.value=="")
        {
            alert("请选择期望完成时间");
            date.focus();
            return false;
        }
        else if(raid.value=="raid_status")
        {
            alert("请选择raid卡信息");
            raid.focus();
            return false;
        }
        else if(textarea.value=="")
        {
            alert("请认真填写需求详情");
            textarea.focus();
            return false;
        }

    }
} 
function tab2_form(tab2form){
    with(tab2form)
    {
        if(host.value=="")
        {
            alert("请填写主机");
            host.focus();
            return false;
        }
        else if(ip.value=="")
        {
            alert("IP不能为空");
            ip.focus();
            return false;
        }
        else if(idc.value=="idc_status")
        {
            alert("请选择机房");
            idc.focus();
            return false;
        }
        else if(location1.value=="")
        {
            alert("所属机柜不能为空");
            location1.focus();
            return false;
        }
        else if(sn.value=="")
        {
            alert("请核对SN");
            sn.focus();
            return false;
        }
        else if(variety.value=="host_status")
        {
            alert("请选择机器类型");
            variety.focus();
            return false;
        }
        else if(date.value=="")
        {
            alert("请选择期望完成时间");
            date.focus();
            return false;
        }
        else if(host_status.value=="host_status")
        {
            alert("请选择报修");
            host_status.focus();
            return false;
        }
        else if(textarea.value=="")
        {
            alert("请认真填写需求详情");
            textarea.focus();
            return false;
        }
    }
} 
function tab3_form(tab3form){
    with(tab3form)
    {
        if(host.value=="")
        {
            alert("请填写主机");
            host.focus();
            return false;
        }
        else if(ip.value=="")
        {
            alert("IP不能为空");
            ip.focus();
            return false;
        }
        else if(old_idc.value=="idc_status")
        {
            alert("请选择机房");
            old_idc.focus();
            return false;
        }
        else if(old_owner.value=="")
        {
            alert("请填写原机器owner");
            old_owner.focus();
            return false;
        }
        else if(now_owner.value=="")
        {
            alert("请填写当前机器owner");
            now_owner.focus();
            return false;
        }
        else if(now_idc.value=="idc_status")
        {
            alert("请选择搬至机房");
            now_idc.focus();
            return false;
        }
        else if(date.value=="")
        {
            alert("请选择期望完成时间");
            date.focus();
            return false;
        }
        else if(os.value=="choice")
        {
            alert("请选择是否重装系统");
            os.focus();
            return false;
        }
        else if(textarea.value=="")
        {
            alert("请认真填写需求详情");
            textarea.fmcus();
            return false;
        }
    }
} 
function tab4_form(tab4form){
    with(tab4form)
    {
        if(host.value=="")
        {
            alert("请填写主机");
            host.focus();
            return false;
        }
        else if(ip.value=="")
        {
            alert("IP不能为空");
            ip.focus();
            return false;
        }
        else if(os.value=="choice")
        {
            alert("请选择是否重装系统");
            os.focus();
            return false;
        }
        else if(owner.value=="")
        {
            alert("请填写机器owner");
            owner.focus();
            return false;
        }
        else if(date.value=="")
        {
            alert("请选择期望完成时间");
            date.focus();
            return false;
        }
        else if(resource.value=="resource_status")
        {
            alert("请选择升级硬件");
            resource.focus();
            return false;
        }
        else if(location1.value=="")
        {
            alert("请填写所属机柜");
            location1.focus();
            return false;
        }
        else if(idc.value=="choice")
        {
            alert("请选择机房");
            idc.focus();
            return false;
        }
        else if(textarea.value=="")
        {
            alert("请认真填写需求详情");
            textarea.focus();
            return false;
        }
    }
} 
function tab5_form(tab5form){
    with(tab5form)
    {
        if(host.value=="")
        {
            alert("请填写主机");
            host.focus();
            return false;
        }
        else if(ip.value=="")
        {
            alert("IP不能为空");
            ip.focus();
            return false;
        }
        else if(idc.value=="idc_status")
        {
            alert("请选择机房");
            idc.focus();
            return false;
        }
        else if(owner.value=="")
        {
            alert("请填写机器owner");
            owner.focus();
            return false;
        }
        else if(ra_ip.value=="")
        {
            alert("请填写远程控制卡IP/若没有请填“无”");
            ra_ip.focus();
            return false;
        }
        else if(raid.value=="raid_status")
        {
            alert("请选择RAID卡");
            raid.focus();
            return false;
        }
        else if(date.value=="")
        {
            alert("请选择期望完成时间");
            date.focus();
            return false;
        }
        else if(textarea.value=="")
        {
            alert("请认真填写需求详情");
            textarea.focus();
            return false;
        }
    }
} 
function tab6_form(tab6form){
    with(tab6form)
    {
        if(host.value=="")
        {
            alert("请填写主机");
            host.focus();
            return false;
        }
        else if(ip.value=="")
        {
            alert("IP不能为空");
            ip.focus();
            return false;
        }
        else if(monitor.value=="monitor_location")
        {
            alert("请选择监控系统");
            monitor.focus();
            return false;
        }
        else if(owner.value=="")
        {
            alert("请填写机器owner");
            owner.focus();
            return false;
        }
        else if(business.value=="")
        {
            alert("请填写业务owner");
            business.focus();
            return false;
        }
        else if(list.value=="mon_status")
        {
            alert("请选择监控需求");
            list.focus();
            return false;
        }
        else if(date.value=="")
        {
            alert("请选择期望完成时间");
            date.focus();
            return false;
        }
        else if(idc.value=="idc_status")
        {
            alert("请选择机房");
            idc.focus();
            return false;
        }
        else if(textarea=="")
        {
            alert("请认真填写需求详情");
            textarea.focus();
            return false;
        }
    }
}
function tab7_form(tab7form){
    with(tab7form)
    {
        if(textarea.value=="")
        {
            alert("理由不能为空");
            textarea.focus();
            return false;
        }
    }
}
