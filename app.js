document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.getElementById('sidebar');
    const collapseBtn = document.getElementById('collapseBtn');
    
    // Sidebar toggle functionality
    if (collapseBtn) {
        collapseBtn.addEventListener('click', () => {
            if (sidebar) sidebar.classList.toggle('collapsed');
        });
    }

    const allNavItems = document.querySelectorAll('.nav-item');
    const submenuItems = document.querySelectorAll('.submenu-item');
    const dropdownTriggers = document.querySelectorAll('.dropdown-trigger');

    // Reset active highlights across all links and submenus
    function clearAllActive() {
        allNavItems.forEach(item => {
            item.classList.remove('active');
            item.classList.remove('active-header');
            const bar = item.querySelector('.active-bar');
            if (bar) bar.remove();
        });
        submenuItems.forEach(sub => {
            sub.classList.remove('active');
        });
    }

    // Handle dropdown header toggle (e.g. Pitch Perfector, Other Systems, My performance...)
    dropdownTriggers.forEach(trigger => {
        trigger.addEventListener('click', (e) => {
            const navGroup = trigger.closest('.nav-group');
            if (navGroup) {
                const isOpen = navGroup.classList.contains('open');
                navGroup.classList.toggle('open');
                
                if (!isOpen) {
                    clearAllActive();
                    trigger.classList.add('active-header');
                }
            }
        });
    });

    // Handle regular top-level nav links (e.g. Home, Tasks, AI Agents)
    allNavItems.forEach(item => {
        if (!item.classList.contains('dropdown-trigger')) {
            item.addEventListener('click', (e) => {
                const href = item.getAttribute('href');
                if (!href || href === '#') {
                    e.preventDefault();
                    clearAllActive();
                    item.classList.add('active');
                    
                    const activeBar = document.createElement('div');
                    activeBar.className = 'active-bar';
                    item.prepend(activeBar);
                }
            });
        }
    });

    // Handle click selection on dropdown sub-items
    submenuItems.forEach(sub => {
        sub.addEventListener('click', (e) => {
            if (sub.getAttribute('href') === '#') {
                e.preventDefault();
            }
            e.stopPropagation();
            
            clearAllActive();
            sub.classList.add('active');

            const parentTrigger = sub.closest('.nav-group')?.querySelector('.dropdown-trigger');
            if (parentTrigger) {
                parentTrigger.classList.add('active-header');
            }
        });
    });

    // Two-stage Customer Search & Profile Dashboard Logic
    const searchWrapper = document.getElementById('searchWrapper');
    const customerSearchInput = document.getElementById('customerSearchInput');
    const recentSearchesDropdown = document.getElementById('recentSearchesDropdown');
    const searchResultsPanel = document.getElementById('searchResultsPanel');
    const searchActionBtn = document.getElementById('searchActionBtn');
    const recentItems = document.querySelectorAll('.recent-item');
    const profileResultItems = document.querySelectorAll('.profile-result-item');

    const detailAvatar = document.getElementById('detailAvatar');
    const detailName = document.getElementById('detailName');
    const detailCrn = document.getElementById('detailCrn');
    const detailMobile = document.getElementById('detailMobile');
    const detailEmail = document.getElementById('detailEmail');
    const detailAddress = document.getElementById('detailAddress');

    const profItem1Name = document.getElementById('profItem1Name');
    const profItem1Phone = document.getElementById('profItem1Phone');
    const profItem1Crn = document.getElementById('profItem1Crn');
    const profItem1Avatar = document.getElementById('profItem1Avatar');

    if (customerSearchInput && searchWrapper) {
        // Stage 1: Show Recent Searches dropdown when clicking/focusing search bar
        customerSearchInput.addEventListener('focus', () => {
            searchWrapper.classList.add('open');
        });

        customerSearchInput.addEventListener('click', () => {
            searchWrapper.classList.add('open');
        });

        // Close dropdown when clicking outside
        document.addEventListener('click', (e) => {
            if (!searchWrapper.contains(e.target)) {
                searchWrapper.classList.remove('open');
            }
        });

        // Helper function to open Big Customer Search Dashboard Panel
        const openBigCustomerDashboard = (name, crn, phone, email) => {
            searchWrapper.classList.remove('open'); // Close floating dropdown
            if (searchResultsPanel) searchResultsPanel.style.display = 'block'; // Open big panel

            // Update Input Text
            customerSearchInput.value = phone || name;

            // Update Left Profiles List Item 1
            if (profItem1Name) profItem1Name.textContent = name.toUpperCase();
            if (profItem1Phone) profItem1Phone.textContent = phone;
            if (profItem1Crn) profItem1Crn.textContent = `CRN: ${crn}`;
            if (profItem1Avatar) profItem1Avatar.textContent = name.charAt(0).toUpperCase();

            // Update Right Detail Panel
            if (detailName) detailName.textContent = name;
            if (detailCrn) detailCrn.textContent = `CRN: ${crn}`;
            if (detailMobile) detailMobile.textContent = `91${phone}`;
            if (detailEmail) detailEmail.textContent = email;
            if (detailAvatar) detailAvatar.textContent = name.charAt(0).toUpperCase();

            // Make Item 1 Active
            profileResultItems.forEach(i => i.classList.remove('active'));
            const profItem1 = document.getElementById('profItem1');
            if (profItem1) profItem1.classList.add('active');
        };

        // Stage 2: When clicking ANY Recent Search Item, navigate to customer overview
        recentItems.forEach(item => {
            item.addEventListener('click', (e) => {
                e.stopPropagation();
                const type = item.getAttribute('data-type');
                if (type === 'ntb') {
                    window.location.href = 'experience_solitaire_dashboard_new.html';
                } else {
                    // For Solitaire, Privy, Privy+ (all ETB)
                    window.location.href = 'customer_overview_solitaire.html';
                }
            });
        });

        // Click search icon button also triggers default Solitaire dashboard
        if (searchActionBtn) {
            searchActionBtn.addEventListener('click', (e) => {
                e.preventDefault();
                window.location.href = 'customer_overview_solitaire.html';
            });
        }

        // Switch active customer inside Big Dashboard left list
        profileResultItems.forEach(item => {
            item.addEventListener('click', () => {
                profileResultItems.forEach(i => i.classList.remove('active'));
                item.classList.add('active');

                const name = item.getAttribute('data-name');
                const crn = item.getAttribute('data-crn');
                const phone = item.getAttribute('data-phone');
                const email = item.getAttribute('data-email');

                if (name && detailName) detailName.textContent = name;
                if (crn && detailCrn) detailCrn.textContent = `CRN: ${crn}`;
                if (phone && detailMobile) detailMobile.textContent = `91${phone}`;
                if (email && detailEmail) detailEmail.textContent = email;
                if (name && detailAvatar) detailAvatar.textContent = name.charAt(0).toUpperCase();
            });
        });
        // Assist Customer button navigation
        const assistCustomerBtns = document.querySelectorAll('.btn-action-solid');
        assistCustomerBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                window.location.href = 'customer_overview_solitaire.html';
            });
        });
    }

    // View all tasks button handler
    const viewTasksBtn = document.querySelector('.btn-primary');
    if (viewTasksBtn) {
        viewTasksBtn.addEventListener('click', () => {
            alert('Navigating to all tasks...');
        });
    }

    // Smooth scrolling for Top Summary Cards to corresponding sections
    const summaryCards = document.querySelectorAll('.summary-card[data-target]');
    summaryCards.forEach(card => {
        card.addEventListener('click', () => {
            const targetSelector = card.getAttribute('data-target');
            if (targetSelector) {
                const targetElement = document.querySelector(targetSelector);
                if (targetElement) {
                    targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            }
        });
    });

    // Bank Accounts card click -> Navigate to account_details.html
    const bankAccountCards = document.querySelectorAll('#section-bank-accounts .overview-card-box');
    bankAccountCards.forEach(card => {
        card.style.cursor = 'pointer';
        card.addEventListener('click', () => {
            window.location.href = 'account_details.html';
        });
    });

    // Email Statement Tab Switching (Monthly / Yearly / Custom Dates)
    const stmtTabs = document.querySelectorAll('.stmt-tab');
    const optionMonthly = document.getElementById('optionMonthly');
    const optionYearly = document.getElementById('optionYearly');
    const optionCustom = document.getElementById('optionCustom');

    if (stmtTabs.length > 0) {
        stmtTabs.forEach(tab => {
            tab.addEventListener('click', () => {
                stmtTabs.forEach(t => {
                    t.classList.remove('active');
                    t.style.background = 'transparent';
                    t.style.color = '#4b5563';
                    t.style.boxShadow = 'none';
                });
                tab.classList.add('active');
                tab.style.background = '#ffffff';
                tab.style.color = '#111827';
                tab.style.boxShadow = '0 1px 2px rgba(0,0,0,0.05)';

                const period = tab.getAttribute('data-period');
                if (optionMonthly) optionMonthly.style.display = (period === 'monthly') ? 'block' : 'none';
                if (optionYearly) optionYearly.style.display = (period === 'yearly') ? 'block' : 'none';
                if (optionCustom) optionCustom.style.display = (period === 'custom') ? 'block' : 'none';
            });
        });
    }

    // Send Statement Button click handler & feedback alert
    const btnSendStatement = document.getElementById('btnSendStatement');
    const stmtSuccessBanner = document.getElementById('stmtSuccessBanner');
    const stmtEmailInput = document.getElementById('stmtEmailInput');
    const sentEmailAddr = document.getElementById('sentEmailAddr');

    if (btnSendStatement && stmtSuccessBanner) {
        btnSendStatement.addEventListener('click', () => {
            const email = (stmtEmailInput && stmtEmailInput.value) ? stmtEmailInput.value : 'kashyap.patel@gmail.com';
            if (sentEmailAddr) sentEmailAddr.textContent = email;

            btnSendStatement.innerHTML = '<span>⏳ Sending...</span>';
            btnSendStatement.style.opacity = '0.7';

            setTimeout(() => {
                btnSendStatement.innerHTML = '<span>📨 Send Statement</span>';
                btnSendStatement.style.opacity = '1';
                stmtSuccessBanner.style.display = 'block';

                setTimeout(() => {
                    stmtSuccessBanner.style.display = 'none';
                }, 4000);
            }, 600);
        });
    }

    // All Transactions Page Filtering Logic
    const filterFromDate = document.getElementById('filterFromDate');
    const filterToDate = document.getElementById('filterToDate');
    const filterTxnType = document.getElementById('filterTxnType');
    const filterSearchInput = document.getElementById('filterSearchInput');
    const filterPresetPills = document.querySelectorAll('.filter-preset-pill');
    const btnClearFilters = document.getElementById('btnClearFilters');
    const txnRows = document.querySelectorAll('.txn-row-item');
    const filteredCountText = document.getElementById('filteredCountText');

    function applyTxnFilters() {
        if (!txnRows.length) return;

        const fromVal = filterFromDate ? filterFromDate.value : '';
        const toVal = filterToDate ? filterToDate.value : '';
        const typeVal = filterTxnType ? filterTxnType.value : 'all';
        const searchVal = filterSearchInput ? filterSearchInput.value.toLowerCase().trim() : '';

        let visibleCount = 0;

        txnRows.forEach(row => {
            const rowDate = row.getAttribute('data-date');
            const rowType = row.getAttribute('data-type');
            const rowText = row.getAttribute('data-text');

            let matchesDate = true;
            if (fromVal && rowDate < fromVal) matchesDate = false;
            if (toVal && rowDate > toVal) matchesDate = false;

            let matchesType = true;
            if (typeVal !== 'all' && rowType !== typeVal) matchesType = false;

            let matchesSearch = true;
            if (searchVal && !rowText.includes(searchVal)) matchesSearch = false;

            if (matchesDate && matchesType && matchesSearch) {
                row.style.display = 'flex';
                visibleCount++;
            } else {
                row.style.display = 'none';
            }
        });

        if (filteredCountText) {
            filteredCountText.textContent = `${visibleCount} Transaction${visibleCount !== 1 ? 's' : ''}`;
        }
    }

    if (txnRows.length > 0) {
        if (filterFromDate) filterFromDate.addEventListener('change', applyTxnFilters);
        if (filterToDate) filterToDate.addEventListener('change', applyTxnFilters);
        if (filterTxnType) filterTxnType.addEventListener('change', applyTxnFilters);
        if (filterSearchInput) filterSearchInput.addEventListener('input', applyTxnFilters);

        filterPresetPills.forEach(pill => {
            pill.addEventListener('click', () => {
                filterPresetPills.forEach(p => {
                    p.classList.remove('active');
                    p.style.background = '#ffffff';
                    p.style.color = '#374151';
                });
                pill.classList.add('active');
                pill.style.background = '#111827';
                pill.style.color = '#ffffff';

                const range = pill.getAttribute('data-range');

                if (range === 'all') {
                    if (filterFromDate) filterFromDate.value = '2026-01-01';
                    if (filterToDate) filterToDate.value = '2026-12-31';
                } else if (range === 'this_month') {
                    if (filterFromDate) filterFromDate.value = '2026-07-01';
                    if (filterToDate) filterToDate.value = '2026-07-29';
                } else if (range === 'last_30') {
                    if (filterFromDate) filterFromDate.value = '2026-06-29';
                    if (filterToDate) filterToDate.value = '2026-07-29';
                } else if (range === 'last_3_months') {
                    if (filterFromDate) filterFromDate.value = '2026-04-01';
                    if (filterToDate) filterToDate.value = '2026-07-29';
                }

                applyTxnFilters();
            });
        });

        if (btnClearFilters) {
            btnClearFilters.addEventListener('click', () => {
                if (filterFromDate) filterFromDate.value = '2026-07-01';
                if (filterToDate) filterToDate.value = '2026-07-29';
                if (filterTxnType) filterTxnType.value = 'all';
                if (filterSearchInput) filterSearchInput.value = '';

                filterPresetPills.forEach((p, idx) => {
                    if (idx === 0) {
                        p.classList.add('active');
                        p.style.background = '#111827';
                        p.style.color = '#ffffff';
                    } else {
                        p.classList.remove('active');
                        p.style.background = '#ffffff';
                        p.style.color = '#374151';
                    }
                });

                applyTxnFilters();
            });
        }
    }

    // EMI & Rewards Calculator Logic (credit_card_details.html)
    const calcAmount = document.getElementById('calcAmount');
    const emiTenurePills = document.querySelectorAll('.emi-tenure-pill');
    const calcEmiResult = document.getElementById('calcEmiResult');
    const calcRewardsResult = document.getElementById('calcRewardsResult');

    let selectedMonths = 3;

    function updateEmiCalculation() {
        if (!calcAmount || !calcEmiResult) return;

        const principal = parseFloat(calcAmount.value) || 0;
        if (principal <= 0) {
            calcEmiResult.textContent = '₹ 0 / mo';
            if (calcRewardsResult) calcRewardsResult.textContent = '0 Points';
            return;
        }

        const annualRate = 0.135;
        const monthlyRate = annualRate / 12;
        const n = selectedMonths;

        // EMI = [P x r x (1+r)^n]/[(1+r)^n-1]
        const emi = (principal * monthlyRate * Math.pow(1 + monthlyRate, n)) / (Math.pow(1 + monthlyRate, n) - 1);
        calcEmiResult.textContent = `₹ ${Math.round(emi).toLocaleString('en-IN')} / mo`;

        const rewards = Math.floor((principal / 100) * 2);
        if (calcRewardsResult) {
            calcRewardsResult.textContent = `${rewards.toLocaleString('en-IN')} Points`;
        }
    }

    if (calcAmount && emiTenurePills.length > 0) {
        calcAmount.addEventListener('input', updateEmiCalculation);

        emiTenurePills.forEach(pill => {
            pill.addEventListener('click', () => {
                emiTenurePills.forEach(p => {
                    p.classList.remove('active');
                    p.style.background = '#ffffff';
                    p.style.color = '#374151';
                });
                pill.classList.add('active');
                pill.style.background = '#111827';
                pill.style.color = '#ffffff';

                selectedMonths = parseInt(pill.getAttribute('data-months')) || 3;
                updateEmiCalculation();
            });
        });
    }
});
