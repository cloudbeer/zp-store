var sort_url;
var del_url;
var modi_url
var page_size = 20;

$(function () {
    $(".pagination li a").click(function () {
        if (sort_url === undefined) {
            alert("请指定 sort_url 参数。");
            return;
        }
        if (sort_url.indexOf("?") > 0)
            window.location = sort_url + "&size=" + page_size + "&page=" + $(this).attr("data-page");
        else
            window.location = sort_url + "?size=" + page_size + "&page=" + $(this).attr("data-page");
        return false;
    });
    $(".del").click(function () {
        if (del_url === undefined) {
            alert("请指定 del_url 参数。");
            return;
        }
        xthis = $(this);
        if (!confirm("是否确认删除")) return;
        $.post(del_url, { _id: $(this).attr("data-id") }, function (res) {
            if (res == "1") {
                xthis.parent().parent().remove();
            } else {
                alert("删除失败");
            }
        });
    });
    $(".modi").click(function () {
        if (modi_url === undefined) {
            alert("请指定 modi_url 参数。");
            return;
        }
        window.location = modi_url + $(this).attr("data-id");
    });
})