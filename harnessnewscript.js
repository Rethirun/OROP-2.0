function populateRankDropdown() {
    var serviceType = document.getElementById("serviceType").value;
    var rankDropdown = document.getElementById("rank");

    // Clear existing options
    rankDropdown.innerHTML = '<option value="" selected disabled>Select rank</option>';

    // Populate rank options based on service type
    if (serviceType === 'Regular Commissioned Officers Excluding AMC/ADC/RVC/MNS/TA/EC/SSC') {
                addOption(rankDropdown, '2nd LIEUTENANT/LIEUTENANT', '2nd_LT_LT');
                addOption(rankDropdown, 'CAPTAIN', 'CAPT');
		addOption(rankDropdown, 'MAJOR', 'MAJOR');
                addOption(rankDropdown, 'LIEUTENANT COLONEL (TS)/LIEUTENANT COLONEL', 'LT_COL_TS_LT_COL');
		addOption(rankDropdown, 'COLONEL(TS)', 'COL_TS');
		addOption(rankDropdown, 'COLONEL', 'COL');
		addOption(rankDropdown, 'BRIGADIER', 'BRIG');
		addOption(rankDropdown, 'MAJOR GENERAL', 'MAJOR_GEN');
		addOption(rankDropdown, 'LIEUTENANT GENERAL', 'LT_GEN');
		addOption(rankDropdown, 'LIEUTENANT GENERAL HAG', 'LT_GEN_HAG');
		addOption(rankDropdown, 'ARMY CDR', 'ARMY_CDR');
		addOption(rankDropdown, 'VCOAS', 'VCOAS');
		addOption(rankDropdown, 'COAS', 'COAS');
                // Add other options as needed
            } else if (serviceType === 'Commissioned Officers of AMC/ADC/RVC') {
                addOption(rankDropdown, '2nd LIEUTENANT/LIEUTENANT', '2nd_LT_LT');
                addOption(rankDropdown, 'CAPTAIN', 'CAPT');
		addOption(rankDropdown, 'MAJOR', 'MAJOR');
                addOption(rankDropdown, 'LIEUTENANT COLONEL (TS)/LIEUTENANT COLONEL', 'LT_COL_TS_LT_COL');
		addOption(rankDropdown, 'COLONEL(TS)', 'COL_TS');
		addOption(rankDropdown, 'COLONEL', 'COL');
		addOption(rankDropdown, 'BRIGADIER', 'BRIG');
		addOption(rankDropdown, 'MAJOR GENERAL', 'MAJOR_GEN');
		addOption(rankDropdown, 'LIEUTENANT GENERAL', 'LT_GEN');
		addOption(rankDropdown, 'LIEUTENANT GENERAL HAG', 'LT_GEN_HAG');
		addOption(rankDropdown, 'DGAFMS', 'DGAFMS');
                // Add other options as needed
            } else if (serviceType === 'Commissioned Officers of Territorial Army') {
                addOption(rankDropdown, '2nd LIEUTENANT/LIEUTENANT', '2nd_LT_LT');
                addOption(rankDropdown, 'CAPTAIN', 'CAPT');
		addOption(rankDropdown, 'MAJOR', 'MAJOR');
                addOption(rankDropdown, 'LIEUTENANT COLONEL (TS)/LIEUTENANT COLONEL', 'LT_COL_TS_LT_COL');
		addOption(rankDropdown, 'COLONEL(TS)', 'COL_TS');
		addOption(rankDropdown, 'COLONEL', 'COL');
		addOption(rankDropdown, 'BRIGADIER', 'BRIG');
            }else if (serviceType === 'Commissioned Officers of Military Nursing Services') {
                addOption(rankDropdown, '2nd LIEUTENANT/LIEUTENANT', '2nd_LT_LT');
                addOption(rankDropdown, 'CAPTAIN', 'CAPT');
		addOption(rankDropdown, 'MAJOR', 'MAJOR');
                addOption(rankDropdown, 'LIEUTENANT COLONEL', 'LT_COL');
		addOption(rankDropdown, 'COLONEL', 'COL');
		addOption(rankDropdown, 'BRIGADIER', 'BRIG');
		addOption(rankDropdown, 'MAJOR GENERAL', 'MAJOR_GEN');
            }else if (serviceType === 'Regular EC/SSC Officers Other than AMC/ADC/RVC') {
                addOption(rankDropdown, '2nd LIEUTENANT/LIEUTENANT', '2nd_LT_LT');
                addOption(rankDropdown, 'CAPTAIN', 'CAPT');
		addOption(rankDropdown, 'MAJOR', 'MAJOR');
                addOption(rankDropdown, 'LIEUTENANT COLONEL', 'LT_COL');
            } else if (serviceType === 'EC/SSC Officers AMC/ADC/RVC doctors') {
                addOption(rankDropdown, '2nd LIEUTENANT/LIEUTENANT', '2nd_LT_LT');
                addOption(rankDropdown, 'CAPTAIN', 'CAPT');
		addOption(rankDropdown, 'MAJOR', 'MAJOR');
                addOption(rankDropdown, 'LIEUTENANT COLONEL', 'LT_COL');
            } else if (serviceType === 'JCOs/ORs including Honorary commisioned officers') {
                addOption(rankDropdown, 'SEPOY AND EQUIVALENT (GROUP:A/X)', 'SEPOY_A_X');
                addOption(rankDropdown, 'SEPOY AND EQUIVALENT (GROUP:B TO H/B TO E/Y/Z)', 'SEPOY_B_TO_Z');
		addOption(rankDropdown, 'HONY NAIK AND EQUIVALENT (GROUP:A/X)', 'HONY_NAIK_A_X');
                addOption(rankDropdown, 'HONY NAIK AND EQUIVALENT (GROUP:B TO H/B TO E/Y/Z)', 'HONY_NAIK_B_TO_Z');
		addOption(rankDropdown, 'NAIK/NAIK(TS) AND EQUIVALENT (GROUP:A/X)', 'NAIK_NAIK_TS_A_X');
		addOption(rankDropdown, 'NAIK/NAIK(TS) AND EQUIVALENT(GROUP: B TO H/B TO E/Y/Z)', 'NAIK_NAIK_TS_B_TO_Z');
		addOption(rankDropdown, 'HONY HAVILDAR AND EQUIVALENT (GROUP:A/X)', 'HONY_HAVILDAR_A_X');
		addOption(rankDropdown, 'HONY HAVILDAR AND EQUIVALENT(GROUP: B TO H/B TO E/Y/Z)', 'HONY_HAVILDAR_B_TO_Z');
		addOption(rankDropdown, 'HAVILDAR AND EQUIVALENT (GROUP:A/X)', 'HAVILDAR_A_X');
		addOption(rankDropdown, 'HAVILDAR AND EQUIVALENT(GROUP: B TO H/B TO E/Y/Z)', 'HAVILDAR_B_TO_Z');
		addOption(rankDropdown, 'HONY NAIB SUBEDAR AND EQUIVALENT (GROUP:A/X)', 'HONY_NAIB_SUBEDAR_A_X');
		addOption(rankDropdown, 'HONY NAIB SUBEDAR AND EQUIVALENT(GROUP: B TO H/B TO E/Y/Z)', 'HONY_NAIB_SUBEDAR_B_TO_Z');
		addOption(rankDropdown, 'ARTIFICER III-I(NAVY ONLY)', 'ARTIFICER_NAVY_A_X');
		addOption(rankDropdown, 'NAIB SUBEDAR AND EQUIVALENT (GROUP:A/X)', 'NAIB_SUBEDAR_A_X');
		addOption(rankDropdown, 'NAIB SUBEDAR AND EQUIVALENT(GROUP: B TO H/B TO E/Y/Z)', 'NAIB_SUBEDAR_B_TO_Z');
		addOption(rankDropdown, 'SUBEDAR AND EQUIVALENT (GROUP:A/X)', 'SUBEDAR_A_X');
		addOption(rankDropdown, 'SUBEDAR AND EQUIVALENT(GROUP: B TO H/B TO E/Y/Z)', 'SUBEDAR_B_TO_Z');
		addOption(rankDropdown, 'SUBEDAR MAJOR AND EQUIVALENT (GROUP:A/X)', 'SUBEDAR_MAJOR_A_X');
		addOption(rankDropdown, 'SUBEDAR MAJOR AND EQUIVALENT(GROUP: B TO H/B TO E/Y/Z)', 'SUBEDAR_MAJOR_B_TO_Z');
		addOption(rankDropdown, 'SUBEDAR MAJOR,SUBEDAR GRANTED ACP A/ACP B (GROUP:A/X)', 'SUBEDAR_MAJOR_SUBEDAR_GRANTEDACP_AACP_B_A_X');
		addOption(rankDropdown, 'SUBEDAR MAJOR,SUBEDAR GRANTED ACP A/ACP B(GROUP: B TO H/B TO E/Y/Z)', 'SUBEDAR_MAJOR_SUBEDAR_GRANTEDACP_AACP_B_TO_Z');
		addOption(rankDropdown, 'HONY LIEUTENANT', 'HONY_LIEUTENANT');
		addOption(rankDropdown, 'HONY CAPTAIN', 'HONY_CAPTAIN');
		addOption(rankDropdown, 'NCs ( E )', 'NCs_E');
                // Add other options as needed
            } else if (serviceType === 'JCOs/ORs of DSC in receipt of 2nd pension') {
                addOption(rankDropdown, 'SEPOY', 'SEPOY');
                addOption(rankDropdown, 'HONY NAIK', 'HONY_NAIK');
		addOption(rankDropdown, 'NAIK/NAIK(TS)', 'NAIK_NAIK_TS');
                addOption(rankDropdown, 'HONY HAVILDAR', 'HONY_HAVILDAR');
		addOption(rankDropdown, 'HAVILDAR', 'HAVILDAR');
		addOption(rankDropdown, 'HONY NAIB SUBEDAR', 'HONY_NAIB_SUBEDAR');
		addOption(rankDropdown, 'NAIB SUBEDAR', 'NAIB_SUBEDAR');
		addOption(rankDropdown, 'SUBEDAR', 'SUBEDAR');
		addOption(rankDropdown, 'SUBEDAR MAJOR', 'SUBEDAR_MAJOR');
            }else if (serviceType === 'JCOs/ORs of Territorial Army') {
                addOption(rankDropdown, 'SEPOY', 'SEPOY');
                addOption(rankDropdown, 'HONY NAIK', 'HONY_NAIK');
		addOption(rankDropdown, 'NAIK/NAIK(TS)', 'NAIK_NAIK_TS');
                addOption(rankDropdown, 'HONY HAVILDAR', 'HONY_HAVILDAR');
		addOption(rankDropdown, 'HAVILDAR', 'HAVILDAR');
		addOption(rankDropdown, 'HONY NAIB SUBEDAR', 'HONY_NAIB_SUBEDAR');
		addOption(rankDropdown, 'NAIB SUBEDAR', 'NAIB_SUBEDAR');
		addOption(rankDropdown, 'SUBEDAR', 'SUBEDAR');
		addOption(rankDropdown, 'SUBEDAR MAJOR', 'SUBEDAR_MAJOR');
		addOption(rankDropdown, 'HONY LIEUTENANT', 'HONY_LT');
		addOption(rankDropdown, 'HONY CAPTAIN', 'HONY_CAPT');

            }

// Add more conditions for other service types as needed}
}
function addOption(selectElement, text, value) {
    var option = document.createElement("option");
    option.text = text;
    option.value = value;
    selectElement.add(option);
}

function populateYearsAndMonths() {
// Populate years dropdown (00 to 40)
var yearsDropdown = document.getElementById("yearsServed");
for (var i = 1; i <= 40; i++) {
    addOption(yearsDropdown, i.toString().padStart(2, '0'), i.toString().padStart(2, '0'));
}

// Set default value to "01"
yearsDropdown.value = "01";


// Populate months dropdown (00 to 12)
var monthsDropdown = document.getElementById("monthsServed");
for (var j = 0; j <= 12; j++) {
    addOption(monthsDropdown, j.toString().padStart(2, '0'), j.toString().padStart(2, '0'));
}
}

function toggleDateOfBirthAndDischarge() {
    var diedInHarness = document.querySelector('input[name="died-in-harness"]:checked').value;
    var dateOfBirthField = document.getElementById("date-of-birth-container");
    var dateOfDischargeField = document.getElementById("date-of-discharge-container");
    var dateOfBirthInput = document.getElementById("date-of-birth");
    var dateOfDischargeInput = document.getElementById("date-of-discharge");

    if (diedInHarness === 'no') {

        dateOfBirthInput.required = true;
        dateOfDischargeInput.required = true;

        dateOfBirthField.style.display = 'inline-block';
        dateOfBirthField.style.marginBottom = '20px';
        
        dateOfDischargeField.style.display = 'inline-block';
        dateOfDischargeField.style.marginBottom = '40px';
        dateOfDischargeField.style.marginRight = '40px';

    } else {
        dateOfBirthInput.required = false;
        dateOfDischargeInput.required = false;

        dateOfBirthField.style.display = 'none';
        dateOfDischargeField.style.display = 'none';
    }
}