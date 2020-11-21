<?php require "header.php"; ?>

<div id="download_page_div">
  <h3>Modify Sensors</h3>
  <div id="modify_sensors_left_div">
    <table class="table table-sm" id="sensor_modify_table">
      <tbody>
        <tr>
          <td><b>Sensing Node</b></td>
          <td colspan="3">
            <select id="placement_select" class="form-control" onchange="updateSensorListForModificaiton();">
              <option value="">Please Select</option>
              <?php get_all_placements_as_option(); ?>
            </select>
          </td>
        </tr>

        <tr>
          <td>
            <input type="button" value="Back" class="btn btn-warning btn-block" onclick="goToDashboard();">
          </td>
          <td colspan="3">
            <input type="button" value="Add New Sensor" class="btn btn-light btn-block" data-toggle="modal" data-target="#add_sensor_modal">
          </td>
        </tr>
        <tr>
          <td id="sensor_modification_div" colspan="4"></td>
        </tr>
      </tbody>
    </table>
  </div>
  <div id="modify_sensors_right_div">
      <div id="sensor_details_title_div"><b>Sensor Types</b></div>
      <li>Type 1: Digital Sensor - this type of sensors are directly connected to the GPIO pins of the Raspberry Pi and can directly provide readings to the Raspberry Pi, for example: LDR.</li><br>
      <li>Type 2: Analog Sensor - this type of sensors are connected to the Raspberry Pi via the MCP3008 Analogue to Digital Converter and can provide continuous readings, for example: MQ2 Gas sensor</li><br>
      <li>Type 3: Special Sensor - this type of sensors provide a signal or beat when an event occurs and can be either digital or analog, for example: Motion sensor</li>
  </div>
</div>

<div id="sensor_modification_div_old">
</div>


<!-- Modal -->
<div class="modal fade" id="add_sensor_modal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">

      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Add New Sensor</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>

      <div class="modal-body">
        <table>
          <tbody>
            <tr>
              <td>Sensor Name</td>
              <td>
                <input type="text" id="sensor_name_input" class="form-control">
              </td>
            </tr>

            <tr>
              <td>Sensor Type</td>
              <td>
                <select class="form-control" id="sensor_type_select">
                  <option value="1">1</option>
                  <option value="2">2</option>
                  <option value="3">3</option>
                </select>
              </td>
            </tr>

            <tr>
              <td>Pin #</td>
              <td>
                <input type="text" id="pin_input" class="form-control">
              </td>
            </tr>

          </tbody>
        </table>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary" onclick="clickedAddSensorBtn();">Save changes</button>
      </div>
    </div>
  </div>
</div>

<?php require "footer.php"; ?>
