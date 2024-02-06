$(document).ready(function () {

    var formSelects = document.getElementById("serviceworkUpdateForm").getElementsByTagName("select");
    var formInputs = document.getElementById("serviceworkUpdateForm").getElementsByTagName("input");
    var formTextareas = document.getElementById("serviceworkUpdateForm").getElementsByTagName("textarea");

    for (var i = 0; i < formSelects.length; i++) {
        formSelects[i].setAttribute("disabled", "true");
    }

    for (var i = 0; i < formInputs.length; i++) {
        formInputs[i].setAttribute("readonly", "true");
    }

    for (var i = 0; i < formTextareas.length; i++) {
        formTextareas[i].setAttribute("readonly", "true");
    }

    $("#productServiceDiv").hide();

    $("#serviceworkSaveBtn").hide();


    $("#serviceworkEditBtn").click(function (event) {
        event.preventDefault();

        $("#serviceworkEditBtn").hide();
        $("#serviceworkDeleteBtn").hide();
        $("#serviceworkChangeStatus").hide();
        $("#servicesView").hide();
        $("#productServiceDiv").show();
        $("#serviceworkSaveBtn").show();

        for (var i = 0; i < formSelects.length; i++) {
            formSelects[i].removeAttribute("disabled");
        }
    
        for (var i = 0; i < formInputs.length; i++) {
            formInputs[i].removeAttribute("readonly");
        }
    
        for (var i = 0; i < formTextareas.length; i++) {
            formTextareas[i].removeAttribute("readonly");
        }

    });


    var selectedCustomer = $('#formServiceWorkCustomer').val();

    console.log(selectedCustomer);

    var productSelect = document.getElementById('formServiceWorkProduct');
    var productSelectLabel = document.getElementById('serviceWorkProductLabel');

    var serviceSelect = document.getElementById('formServiceWorkService');
    var serviceSelectLabel = document.getElementById('serviceWorkServiceLabel');

    $(serviceSelectLabel).show();
    $(serviceSelect).show();

    $(productSelectLabel).show();
    $(productSelect).show();


    function productChange() {

        console.log('in product');

        productSelect.innerHTML = '';

        var selectedCustomer = $('#formServiceWorkCustomer').val();

        console.log(selectedCustomer);

        if (selectedCustomer !== '') {
            
            $(productSelectLabel).show();
            $(productSelect).show();

            $.ajax({
                url: `/view_serviceworks/`,
                type: "GET",
                dataType: "json",
                data: {
                    'selectedCustomer': selectedCustomer,
                },
                success: function (data) {
                
                    console.log(data.products);

                    var option = document.createElement('option');
                        option.value = '';
                        option.text = '---------';
                        option.selected = true;
                        productSelect.add(option);

                    data.products.forEach(function (product) {
                        var option = document.createElement('option');
                        option.value = product.id;
                        option.text = product.name;
                        productSelect.add(option);
                    });


                },
                error: function (error) {
                    console.error(error);
                }
            });

        } else {
            $(productSelectLabel).hide();
            $(productSelect).hide();

            $(serviceSelectLabel).hide();
            $(serviceSelect).hide();
        }

    }


    function serviceChange() {

        console.log('in service');
        serviceSelect.innerHTML = '';

        var selectedProduct = $('#formServiceWorkProduct').val();

        console.log(selectedProduct);

        if (selectedProduct !== '') {
            
            $(serviceSelectLabel).show();
            $(serviceSelect).show();

            $.ajax({
                url: `/view_serviceworks/`,
                type: "GET",
                dataType: "json",
                data: {
                    'selectedProduct': selectedProduct,
                },
                success: function (data) {

                    console.log(data.products);

                    var option = document.createElement('option');
                        option.value = '';
                        option.text = '---------';
                        option.selected = true;
                        serviceSelect.add(option);

                    data.services.forEach(function (service) {
                        var option = document.createElement('option');
                        option.value = service.id;
                        option.text = service.name;
                        serviceSelect.add(option);
                    });


                },
                error: function (error) {
                    console.error(error);
                }
            });

        } else {
            $(serviceSelectLabel).hide();
            $(serviceSelect).hide();
        }
    }


    $("#formServiceWorkCustomer").change(function () {

        productChange();

    });


    $("#formServiceWorkProduct").change(function () {

        serviceChange();

    });


});