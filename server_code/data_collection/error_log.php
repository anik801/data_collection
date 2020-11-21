<?php require "header.php"; ?>

<div id="download_page_div">
  <h3>Download Error Log</h3>
  <div id="sensor_download_table_div">
    <table class="table table-sm" id="sensor_download_table">
      <tbody>
        <tr>
          <td><b>Sensing Node</b></td>
          <td>
            <select id="placement_select" class="form-control" onchange="showRecentErrors();">
              <option value="">Please select</option>
              <?php get_all_placements_as_option(); ?>
            </select>
          </td>
        </tr>
        <tr>
          <td><b>Start Date</b></td>
          <td>
            <input type="datetime-local" class="form-control"  id="start_date_time" placeholder="From" onchange="showRecentErrors();">
          </td>
        </tr>
        <tr>
          <td><b>End Date</b></td>
          <td>
            <input type="datetime-local" class="form-control" id="end_date_time" placeholder="To" onchange="showRecentErrors();">
          </td>
        </tr>
        <tr>
          <td>
            <input type="button" value="Back" class="btn btn-warning btn-block" onclick="goToDashboard();">
          </td>
          <td>
            <input type="button" value="Download Error Log" class="btn btn-light btn-block" onclick="clickedDownloadErrorLogBtn();">
          </td>
        </tr>
      </tbody>
    </table>
  </div>

  <div id="recent_error_div">
    <!-- Data is dynamically generated from AJAX -->
  </div>
</div>

<?php require "footer.php"; ?>
