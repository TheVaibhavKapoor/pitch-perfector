        // Investment Calculator
        let invMode = 'sip';

        function switchInvCalc(mode) {
            invMode = mode;
            ['sip','swp','lump'].forEach(function(m) {
                var el = document.getElementById('inv-calc-' + m);
                if(el) el.style.display = m === mode ? 'block' : 'none';
                var btn = document.getElementById('inv-tab-' + m);
                if(btn) {
                    btn.style.background = m === mode ? '#1e3a8a' : 'transparent';
                    btn.style.color = m === mode ? 'white' : '#1e3a8a';
                }
            });
            calcInv();
        }

        function fmtRupee(n) {
            if(n >= 10000000) return '\u20b9' + (n/10000000).toFixed(2) + ' Cr';
            if(n >= 100000) return '\u20b9' + (n/100000).toFixed(2) + ' L';
            return '\u20b9' + Math.round(n).toLocaleString('en-IN');
        }

        function calcInv() {
            var invested = 0, total = 0, returns = 0;
            var yearData = [];

            if(invMode === 'sip') {
                var monthly = parseFloat(document.getElementById('sip-amount').value) || 10000;
                var rate = (parseFloat(document.getElementById('sip-rate').value) || 12) / 100 / 12;
                var yrs = parseInt(document.getElementById('sip-years').value) || 10;
                var months = yrs * 12;
                invested = monthly * months;
                total = monthly * ((Math.pow(1 + rate, months) - 1) / rate) * (1 + rate);
                returns = total - invested;
                for(var y = 1; y <= yrs; y++) {
                    var m = y * 12;
                    var tv = monthly * ((Math.pow(1+rate,m)-1)/rate)*(1+rate);
                    yearData.push({year: y, invested: monthly*m, total: tv});
                }
                setLabel('inv-lbl-invested','Total Invested');
                setLabel('inv-lbl-returns','Est. Returns');
                setLabel('inv-lbl-total','Maturity Value');
                setVal('inv-val-invested', fmtRupee(invested));
                setVal('inv-val-returns', fmtRupee(Math.max(0,returns)));
                setVal('inv-val-total', fmtRupee(total));

            } else if(invMode === 'swp') {
                var corpus = parseFloat(document.getElementById('swp-corpus').value) || 1000000;
                var mw = parseFloat(document.getElementById('swp-withdrawal').value) || 8000;
                var swpRate = (parseFloat(document.getElementById('swp-rate').value) || 8) / 100 / 12;
                invested = corpus;
                var bal = corpus;
                var withdrawn = 0;
                for(var y = 1; y <= 40; y++) {
                    for(var mo = 0; mo < 12; mo++) {
                        if(bal <= 0) break;
                        bal = bal * (1 + swpRate) - mw;
                        withdrawn += mw;
                        if(bal < 0) { withdrawn += bal; bal = 0; }
                    }
                    yearData.push({year: y, invested: corpus, total: Math.max(0, bal)});
                    if(bal <= 0) break;
                }
                total = Math.max(0, bal);
                setLabel('inv-lbl-invested','Initial Corpus');
                setLabel('inv-lbl-returns','Total Withdrawn');
                setLabel('inv-lbl-total','Remaining Value');
                setVal('inv-val-invested', fmtRupee(corpus));
                setVal('inv-val-returns', fmtRupee(Math.max(0,withdrawn)));
                setVal('inv-val-total', fmtRupee(total));

            } else { // lumpsum
                var principal = parseFloat(document.getElementById('lump-amount').value) || 500000;
                var lRate = (parseFloat(document.getElementById('lump-rate').value) || 12) / 100;
                var lYrs = parseInt(document.getElementById('lump-years').value) || 10;
                invested = principal;
                total = principal * Math.pow(1 + lRate, lYrs);
                returns = total - invested;
                for(var y = 1; y <= lYrs; y++) {
                    yearData.push({year: y, invested: principal, total: principal * Math.pow(1+lRate, y)});
                }
                setLabel('inv-lbl-invested','Invested Amount');
                setLabel('inv-lbl-returns','Est. Returns');
                setLabel('inv-lbl-total','Maturity Value');
                setVal('inv-val-invested', fmtRupee(invested));
                setVal('inv-val-returns', fmtRupee(Math.max(0,returns)));
                setVal('inv-val-total', fmtRupee(total));
            }

            drawInvChart(yearData);
        }

        function setLabel(id, txt) { var el = document.getElementById(id); if(el) el.textContent = txt; }
        function setVal(id, txt) { var el = document.getElementById(id); if(el) el.textContent = txt; }

        function drawInvChart(yearData) {
            var container = document.getElementById('inv-chart');
            if(!container || yearData.length === 0) return;
            var maxVal = 0;
            yearData.forEach(function(d){ if(d.total > maxVal) maxVal = d.total; if(d.invested > maxVal) maxVal = d.invested; });
            if(maxVal === 0) maxVal = 1;
            var n = yearData.length;
            var slotW = Math.min(56, Math.max(28, Math.floor(540 / n)));
            var w = slotW * n;
            var h = 160;
            var barW = Math.floor(slotW * 0.38);
            var gap = 3;
            var svg = '';
            yearData.forEach(function(d, i) {
                var x = i * slotW + Math.floor((slotW - barW*2 - gap) / 2);
                var investedH = Math.max(2, (d.invested / maxVal) * (h - 28));
                var totalH = Math.max(2, (d.total / maxVal) * (h - 28));
                var returnsH = Math.max(0, totalH - investedH);
                // Invested bar
                svg += '<rect x="' + x + '" y="' + (h - 20 - investedH) + '" width="' + barW + '" height="' + investedH + '" fill="#1e3a8a" rx="2" opacity="0.82"/>';
                // Total bar (invested part in lighter blue + returns in green stacked)
                svg += '<rect x="' + (x + barW + gap) + '" y="' + (h - 20 - investedH) + '" width="' + barW + '" height="' + investedH + '" fill="#3b82f6" rx="2" opacity="0.45"/>';
                if(returnsH > 0) {
                    svg += '<rect x="' + (x + barW + gap) + '" y="' + (h - 20 - totalH) + '" width="' + barW + '" height="' + returnsH + '" fill="#10b981" rx="2" opacity="0.88"/>';
                }
                // Year label
                svg += '<text x="' + (x + barW + gap/2) + '" y="' + (h - 5) + '" text-anchor="middle" font-size="9" fill="#9ca3af" font-family="sans-serif">Y' + d.year + '</text>';
            });
            container.innerHTML = '<svg width="100%" viewBox="0 0 ' + w + ' ' + h + '" style="min-height:' + h + 'px; overflow:visible;">' + svg + '</svg>';
        }

        // Init on DOM ready
        if(document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', function() { calcInv(); });
        } else {
            calcInv();
        }