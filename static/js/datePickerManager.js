const DatePickerManager = (function() {

    function loadDatePickers() {
        $(function() {
            $('input[name="datefilter"]').daterangepicker({
                minDate: getTodayDate(),
                locale: {
                    cancelLabel: 'Clear'
                },
                applyButtonClasses: "btn orange-eb text-white"
            });
          
            $('input[name="datefilter"]').on('apply.daterangepicker', function(ev, picker) {
                const startDate = picker.startDate.format('YYYY-MM-DD');
                const endDate = picker.endDate.format('YYYY-MM-DD');
                const arrayDates = [startDate];
                if(startDate !== endDate) arrayDates.push(endDate);
                $(this).val(arrayDates.join(' to '));
            });
          
            $('input[name="datefilter"]').on('cancel.daterangepicker', function(ev, picker) {
                $(this).val('');
            });  
        });
    }

    function getTodayDate() {
        var today = new Date();
        var dd = String(today.getDate()).padStart(2, '0');
        var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
        var yyyy = today.getFullYear();

        today = mm + '/' + dd + '/' + yyyy;
        return today;
    }

    return {
        loadDatePickers,
        getTodayDate
    }
})()