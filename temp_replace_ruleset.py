from pathlib import Path

path = Path('rulesSet.html')
text = path.read_text(encoding='utf-8')

start_marker = '<!--dashboard-start-->'
end_marker = '<!--dashboard-end-->'
script_marker = '<script src="assets/js/select2.min.js"></script>'
body_marker = '</body>'

if start_marker not in text or end_marker not in text or script_marker not in text or body_marker not in text:
    raise SystemExit('Missing required markers')

start_index = text.index(start_marker)
end_index = text.index(end_marker) + len(end_marker)

new_dashboard = '''<!--dashboard-start-->
      <div class="main p-4 container-fluid">
        <div class="row">
          <div class="col"><h1>Rule Engine</h1></div>
        </div>
        <hr>
        <div class="row mb-4">
          <div class="col-12">
            <div class="card">
              <div class="card-body">
                <h5 class="card-title">Advanced Rule Builder</h5>
                <p class="text-muted">Create advanced rules using lookup keys and lookup values. No dataset selection or add/edit tabs are required.</p>
                <form id="advancedRuleForm">
                  <div class="row g-3">
                    <div class="col-md-6">
                      <label for="ruleName" class="form-label">Rule Name</label>
                      <input type="text" class="form-control" id="ruleName" placeholder="Enter rule name">
                    </div>
                    <div class="col-md-6">
                      <label for="lookupKeySelect" class="form-label">Lookup Key</label>
                      <select id="lookupKeySelect" class="form-select">
                        <option value="">Select lookup key</option>
                        <option value="Forecasted IRR">Forecasted IRR</option>
                        <option value="Land Remaining">Land Remaining</option>
                        <option value="POD/MOD">POD/MOD</option>
                        <option value="Actual vs Sale">Actual vs Sale</option>
                        <option value="Actual vs Target">Actual vs Target</option>
                        <option value="Remaining Lease">Remaining Lease</option>
                        <option value="Growth Rate">Growth Rate</option>
                        <option value="YTM vs Benchmark">YTM vs Benchmark</option>
                      </select>
                    </div>
                    <div class="col-md-6">
                      <label for="lookupValueSelect" class="form-label">Lookup Value</label>
                      <select id="lookupValueSelect" class="form-select">
                        <option value="">Select lookup value</option>
                      </select>
                    </div>
                    <div class="col-md-6">
                      <label for="conditionSelect" class="form-label">Condition</label>
                      <select id="conditionSelect" class="form-select">
                        <option value=">">Greater than</option>
                        <option value="<">Less than</option>
                        <option value="=">Equals</option>
                        <option value=">=">Greater than or equal</option>
                        <option value="<=">Less than or equal</option>
                      </select>
                    </div>
                    <div class="col-md-6">
                      <label for="thresholdInput" class="form-label">Threshold / Value</label>
                      <input type="text" class="form-control" id="thresholdInput" placeholder="Type rule threshold or value">
                    </div>
                    <div class="col-md-6 d-flex align-items-end gap-2">
                      <button type="button" id="generateRule" class="btn btn-primary">Generate Rule</button>
                      <button type="button" id="clearRule" class="btn btn-outline-secondary">Clear</button>
                    </div>
                  </div>
                </form>
              </div>
            </div>
            <div class="card mt-4">
              <div class="card-body">
                <h5 class="card-title">Rule Preview</h5>
                <div class="mb-3">
                  <label for="rulePreview" class="form-label">Generated Rule</label>
                  <textarea id="rulePreview" class="form-control" rows="5" readonly></textarea>
                </div>
                <div class="table-responsive">
                  <table class="table table-bordered" id="advancedRuleTable">
                    <thead>
                      <tr>
                        <th>Rule Name</th>
                        <th>Lookup Key</th>
                        <th>Lookup Value</th>
                        <th>Condition</th>
                        <th>Status</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>Sample Forecast Rule</td>
                        <td>Forecasted IRR</td>
                        <td>Above SAIBOR + 2%</td>
                        <td>> 2.00%</td>
                        <td>Active</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!--dashboard-end-->'''

script_start = text.index(script_marker)
body_index = text.rfind(body_marker)

new_script = '''<script>
  $(document).ready(function () {
    const lookupValues = {
      "Forecasted IRR": ["Above SAIBOR + 2%", "Below Target IRR", "Between 10% and 15%"],
      "Land Remaining": ["Less than 10 acres", "Between 10 and 25 acres", "More than 25 acres"],
      "POD/MOD": ["POD", "MOD", "Other"],
      "Actual vs Sale": ["Above Sale Price", "Below Sale Price", "Equal to Sale Price"],
      "Actual vs Target": ["Above Target", "Below Target", "Meets Target"],
      "Remaining Lease": ["Less than 1 year", "1-5 years", "More than 5 years"],
      "Growth Rate": ["Higher than forecast", "Lower than forecast", "As expected"],
      "YTM vs Benchmark": ["Above benchmark", "Below benchmark", "At benchmark"]
    };

    function populateLookupValues(key) {
      const $valueSelect = $("#lookupValueSelect");
      $valueSelect.empty().append('<option value="">Select lookup value</option>');
      if (key && lookupValues[key]) {
        lookupValues[key].forEach(value => {
          $valueSelect.append(`<option value="${value}">${value}</option>`);
        });
      }
    }

    $("#lookupKeySelect").on("change", function () {
      populateLookupValues(this.value);
      $("#rulePreview").val("");
    });

    $("#generateRule").on("click", function () {
      const ruleName = $("#ruleName").val().trim();
      const lookupKey = $("#lookupKeySelect").val();
      const lookupValue = $("#lookupValueSelect").val();
      const condition = $("#conditionSelect").val();
      const threshold = $("#thresholdInput").val().trim();

      if (!ruleName || !lookupKey || !lookupValue || !threshold) {
        alert("Please complete rule name, lookup key, lookup value, and threshold/value.");
        return;
      }

      const ruleText = `${ruleName}: If ${lookupKey} (${lookupValue}) ${condition} ${threshold}`;
      $("#rulePreview").val(ruleText);

      const newRow = $("<tr></tr>");
      newRow.append(`<td>${ruleName}</td>`);
      newRow.append(`<td>${lookupKey}</td>`);
      newRow.append(`<td>${lookupValue}</td>`);
      newRow.append(`<td>${condition} ${threshold}</td>`);
      newRow.append('<td>Active</td>');
      $("#advancedRuleTable tbody").append(newRow);
    });

    $("#clearRule").on("click", function () {
      $("#advancedRuleForm")[0].reset();
      $("#lookupValueSelect").html('<option value="">Select lookup value</option>');
      $("#rulePreview").val("");
    });
  });
</script>'''

text = text[:start_index] + new_dashboard + text[end_index:script_start] + new_script + text[body_index+len(body_marker):]
path.write_text(text, encoding='utf-8')
print('Updated rulesSet.html')
