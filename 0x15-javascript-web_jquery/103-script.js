$(document).ready(function() {
  function fetchTranslation() {
    const languageCode = $("#language_code").val();
    const apiUrl = "https://www.fourtonfish.com/hellosalut/hello/";

    $.ajax({
      url: apiUrl + "?lang=" + languageCode,
      method: "GET",
      success: function(data) {
        $("#hello").text(data.hello);
      }
    });
  }

  $("#btn_translate").click(fetchTranslation);

  $("#language_code").keypress(function(event) {
    if (event.keyCode === 13) {
      fetchTranslation();
    }
  });
});
