$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-event").modal("show");
      },
      success: function (data) {
        $("#modal-event .modal-content").html(data.html_form);
      }
    });
  };

  function loadCalendarForm (url) {

    var btn = $(this);
    $.ajax({
      url: url,
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-event").modal("show");
      },
      success: function (data) {
        $("#modal-event .modal-content").html(data.html_form);
      }
    });
    return false;

  };

  var saveForm = function () {

    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#event-table tbody").html(data.html_event_list);
          $('#calendar').fullCalendar( 'refetchEvents' );
          $("#modal-event").modal("hide");
        }
        else {
          $("#modal-event .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create event
  $(".js-create-event").click(loadForm);
  $("#modal-event").on("submit", ".js-event-create-form", saveForm);

  // Update event
  $(".js-update-event").click(loadCalendarForm);

  $("#event-table").on("click", ".js-update-event", loadForm);
  $("#modal-event").on("submit", ".js-event-update-form", saveForm);

  // Delete event
  $("#event-table").on("click", ".js-delete-event", loadForm);
  $("#modal-event").on("submit", ".js-event-delete-form", saveForm);

});