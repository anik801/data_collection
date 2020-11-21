<?php require "header.php"; ?>

<div id="download_page_div">
  <h3>Add/Remove Raspberry Pi</h3>
  <div id="modify_sensors_left_div">
    <table class="table table-sm" id="sensor_modify_table">
      <tbody>
        <tr>
          <th>Raspberry Pi</th>
          <th>Position</th>
          <th>Action</th>
        </tr>
        <fieldset>
          <?php get_rpi_for_modification(); ?>
        </fieldset>
        <tr>
          <td>
            <input type="button" value="Back" class="btn btn-warning btn-block" onclick="goToDashboard();">
          </td>
          <td colspan="3">
            <input type="button" value="Add New Raspberry Pi" class="btn btn-light btn-block" data-toggle="modal" data-target="#add_rpi_modal">
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Modal -->
<div class="modal fade" id="add_rpi_modal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">

      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Add New Raspberry Pi</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>

      <div class="modal-body">
        <table>
          <tbody>
            <tr>
              <td>Raspberry Pi Position</td>
              <td>
                <input type="text" id="rpi_position_input" class="form-control">
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="modal-footer">
        <p>Please go to the "Modify Sensors" page to add sensors to the newly added Raspberry Pi.</p>
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary" onclick="clickedAddRpiBtn();">Save changes</button>
      </div>
    </div>
  </div>
</div>

<?php require "footer.php"; ?>
