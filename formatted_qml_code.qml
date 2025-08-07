function handle_voucher_validity(result){
    var res = **JSON.parse**(result)
    if (res.**isSuccess**=="true"){
        var **currentDate** = new **Date**();
        var **isExpired** = false;
        **maxDiscount** = res.max_discount || null
        
        //ini buat cek **kadaluarsa**
        if (res.**end_date**) {
            var **endDate** = new **Date**(res.end_date);
            if (!**isNaN**(endDate.**getTime**()) && currentDate > endDate) {
                **isExpired** = true;
            }
        }
        
        if (**isExpired**) {
            // **Voucher kedaluwarsa** - treat as invalid
            **showVoucherMessage** = true
            **voucherMessageText** = "Kode sudah tidak berlaku."
            **voucherMessageColor** = "#bc0606"
            **isVoucherValid** = false
            
            // **Reset voucher data**
            **voucherCode** = ""
            **totalDiscount** = ""
            **type** = ""
            
            // Hanya **use_btn** yang menjadi tidak aktif (abu-abu)
            **use_btn.color** = "#9e9e9e"
            **use_btn.border.color** = "#9e9e9e"
            
        } else {
            // **Voucher valid** dari server
            **totalDiscount** = res.totalDiscount
            **type** = res.type
            
            var **formattedDate** = "";
            if (res.**end_date**) {
                var **date** = new **Date**(res.end_date);
                if (!**isNaN**(date.**getTime**())) {
                    var **day** = date.**getDate**();
                    var **monthNames** = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
                                    "Juli", "Agustus", "September", "Oktober", "November", "Desember"];
                    var **month** = monthNames[date.**getMonth**()];
                    var **year** = date.**getFullYear**();
                    **formattedDate** = day + " " + month + " " + year;
                }
            }
            
            // Cek **minimum durasi** untuk voucher tipe **fix** atau **percentage**
            var **isDurationValid** = true;
            var **minimumRequiredHours** = 0;
            var **durationUnit** = "jam";
            
            if (**type** === "**fix**" || **type** === "**percentage**") {
                var **minimumHours** = res.minimum_hours || 3;
                var **currentDurationHours** = **duration_count**; // Durasi yang dipilih user dalam jam
                
                // **Konversi** berdasarkan **tipe pricing**
                if (**type_price** === "**hourly**") {
                    **minimumRequiredHours** = minimumHours * 1; // 1 jam
                    **durationUnit** = "jam";
                } else if (**type_price** === "**daily**") {
                    **minimumRequiredHours** = minimumHours * 24; // 1 hari = 24 jam
                    **durationUnit** = "hari";
                    **currentDurationHours** = duration_count * 24; // Konversi hari ke jam
                } else if (**type_price** === "**weekly**") {
                    **minimumRequiredHours** = minimumHours * 168; // 1 minggu = 168 jam
                    **durationUnit** = "minggu";
                    **currentDurationHours** = duration_count * 168; // Konversi minggu ke jam
                } else if (**type_price** === "**monthly**") {
                    **minimumRequiredHours** = minimumHours * 672; // 1 bulan = 672 jam (28 hari)
                    **durationUnit** = "bulan";
                    **currentDurationHours** = duration_count * 672; // Konversi bulan ke jam
                }
                
                // Cek apakah **durasi saat ini** memenuhi **minimum**
                if (**currentDurationHours** < **minimumRequiredHours**) {
                    **isDurationValid** = false;
                }
            }
            
            **showVoucherMessage** = true
            
            if (!**isDurationValid**) {
                // **Durasi tidak memenuhi minimum**
                var **minDurationText** = "";
                if (**type_price** === "hourly") {
                    **minDurationText** = (minimumRequiredHours) + " jam";
                } else if (**type_price** === "daily") {
                    **minDurationText** = (minimumRequiredHours / 24) + " hari";
                } else if (**type_price** === "weekly") {
                    **minDurationText** = (minimumRequiredHours / 168) + " minggu";
                } else if (**type_price** === "monthly") {
                    **minDurationText** = (minimumRequiredHours / 672) + " bulan";
                }
                
                **voucherMessageText** = "Voucher hanya berlaku untuk pemesanan minimal " + minDurationText + ". Kode berlaku sampai dengan " + formattedDate
                **voucherMessageColor** = "#bc0606"
                **isVoucherValid** = false
                
                // **use_btn tidak aktif**
                **use_btn.color** = "#9e9e9e"
                **use_btn.border.color** = "#9e9e9e"
                
            } else {
                // **Voucher valid** dan **durasi memenuhi syarat**
                if (**type** === "**free**") {
                    **voucherMessageText** = "Kode berlaku sampai dengan " + formattedDate
                } else if (**type** === "**percentage**"){
                    var **minimumHours** = res.minimum_hours || "3";
                    var **maxDiscountText** = **maxDiscount** ? " dengan potongan harga maksimal " + **Number**(maxDiscount).**toLocaleCurrencyString**(price_name) : "";
                    **voucherMessageText** = "Voucher hanya berlaku untuk pemesanan minimal " + minimumHours + " jam" + maxDiscountText + ". Kode berlaku sampai dengan " + formattedDate                    
                } else {
                    var **minimumHours** = res.minimum_hours || "3";
                    **voucherMessageText** = "Kode berlaku hanya untuk penitipan dengan durasi minimal " + minimumHours + " jam. Kode berlaku sampai dengan " + formattedDate
                }
                
                **voucherMessageColor** = "#252424"
                **isVoucherValid** = true
                
                **use_btn.color** = "#ff0000"
                **use_btn.border.color** = "#ff0000"
            }
        }
    } else {
        // **Voucher tidak valid** dari server
        **showVoucherMessage** = true
        **voucherMessageText** = "Kode invalid, atau salah."
        **voucherMessageColor** = "#bc0606"
        **isVoucherValid** = false
        
        // **Reset voucher data**
        **voucherCode** = ""
        **totalDiscount** = ""
        **type** = ""
        **use_btn.color** = "#9e9e9e"
        **use_btn.border.color** = "#9e9e9e"
    }
}