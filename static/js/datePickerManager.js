const DatePickerManager = (function() {

    function loadDatePickers() {
        try {
            $(function() {
                const dateRangePicker = {
                    minDate: getTodayDate(),
                    autoUpdateInput: false,
                    locale: {
                        cancelLabel: 'Cancel'
                    },
                    showCustomRangeLabel: false,
                    autoApply: false,
                    autoUpdateInput: false,
                    applyButtonClasses: "btn orange-eb text-white",
                }
                
                const dates = getPickerDates();
                if(dates) {
                    dateRangePicker["startDate"] = formatDate(dates.startDate, "-", "/");
                    dateRangePicker["endDate"] = formatDate(dates.endDate, "-", "/");
                }
    
                try {
                    $('input[name="datefilter"]').daterangepicker(dateRangePicker);
        
                    $('input[name="datefilter"]').on('apply.daterangepicker', function(ev, picker) {
                        const startDate = picker.startDate.format('YYYY-MM-DD');
                        const endDate = picker.endDate.format('YYYY-MM-DD');
                        const arrayDates = [startDate];
                        if(startDate !== endDate) arrayDates.push(endDate);
                        $(this).val(arrayDates.join(' to '));
                    });
                } catch(e) {}
            });
        } catch(e) {}
    }

    function getPickerDates() {
        try {
            const fullDates = document.getElementById('datefilter').value
            const dates = fullDates.split(' to ')
            if(dates && dates[0]) {
                return {
                    startDate: dates[0],
                    endDate: dates[dates.length - 1]
                }
            }
        } catch(e) {}
    }

    function formatDate(date, oldSeparator, newSeparator) {
        fields = date.split(oldSeparator);
        year = fields[0];
        month = fields[1];
        day = fields[2];
        return month + newSeparator + day + newSeparator + year;
    }

    function getTodayDate() {
        const today = new Date();
        const dd = String(today.getDate()).padStart(2, '0');
        const mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
        const yyyy = today.getFullYear();

        return mm + '/' + dd + '/' + yyyy;
    }

    return {
        loadDatePickers
    }
})()
