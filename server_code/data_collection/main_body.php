<div id="placements_div" class="hidden_div">
  <?php get_placements(); ?>
</div>

<div id="sensors_div" class="hidden_div">
  <?php get_all_sensors(); ?>
</div>

<div id="form_div">
  <table class="table">
    <thead>
      <tr>
        <th>Raspberry Pi Device</th>
        <th>Time Range (Start)</th>
        <th>Time Range (End)</th>
        <th>Interval</th>
        <th>Select Sensor</th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          <select id="placement_select" class="form-control" onchange="rpiSelectedInIndex(this.value);">
            <option value="">Please select</option>
            <?php get_all_placements_as_option(); ?>
          </select>
        </td>
        <td>
          <input type="datetime-local" class="form-control" class="glyphicon glyphicon-calendar" id="start_date_time" placeholder="From" onchange="update_sensor_table();">
        </td>
        <td>
          <input type="datetime-local" class="form-control" id="end_date_time" placeholder="To" onchange="update_sensor_table();">
        </td>
        <td>
          <select id="interval_select" class="form-control">
            <option value="1">1 minute</option>
            <option value="5">5 minutes</option>
            <option value="10">10 minutes</option>
            <option value="30">30 minutes</option>
            <option value="60">1 hour</option>
          </select>
        </td>

        <td id="sensor_select_td">
          <!-- Data is dynamically generated from AJAX -->
        </td>

      </tr>

      <tr>
        <td>
          <input type="button" value="Download Data (CSV)" class="btn btn-light btn-block" onclick="clickedDataDownloadBtn();">
        </td>
        <td>
          <input type="button" value="See Error Log" class="btn btn-light btn-block" onclick="clickedErrorLogBtn();">
        </td>
        <td>
          <input type="button" id="modify_sensors_btn" value="Modify Sensors" class="btn btn-light btn-block" onclick="modifySensorsBtnClicked();">
        </td>
        <td colspan="2">
          <input type="button" id="modify_rpi_btn" value="Add/Remove Raspberry Pi Device" class="btn btn-light btn-block" onclick="modifyRpiBtnClicked();">
        </td>

      </tr>

    </tbody>
  </table>
</div>

<div id="logout_div">
  <input class='btn btn-danger' type='button' value='Log Out' onclick='logOutButtonPressed();'>
</div>

<div id="table_div">
  <!-- Left blank intentionally. AJAX response will be displayed here.  -->
</div>
