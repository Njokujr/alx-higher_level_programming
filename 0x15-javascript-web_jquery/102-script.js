$(document).ready(function() {
      $('#btn_translate').click(function() {
        let languageCode = $('#language_code').val();
        $.ajax({
          url: 'https://www.fourtonfish.com/hellosalut/hello/' + languageCode,
          type: 'GET',
          success: function(result) {
            $('#hello').text(result.hello);
          },
          error: function(error) {
            console.log(error);
          }
        });
      });
    });
