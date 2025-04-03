$(document).ready(function () {
	$("#login-form").on("submit", function (event) {
		event.preventDefault();
		
		$.post("/account/login/", $(this).serialize(), function (data) {
			if (data.success) {
				location.reload();
			} else {
				$("#error-messages").html("");
				$.each(data.errors, function (key, value) {
					$("#error-messages").append("<p>" + key + ": " + value + "</p>");
				});
			}
		});
	});

	$("#logout-btn").on("click", function () {
		$.post("/account/logout/", { csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val() }, function (data) {
			if (data.success) {
				location.reload();
			}
		});
	});
});
