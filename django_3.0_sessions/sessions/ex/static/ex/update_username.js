function updateUsername() {
	fetch(window.location.href, { headers: { 'X-Requested-With': 'XMLHttpRequest' } })
		.then(response => response.json())
		.then(data => {document.getElementById('username-display').innerText = `Hello, ${data.username}!`});
}

setInterval(updateUsername, 4200);