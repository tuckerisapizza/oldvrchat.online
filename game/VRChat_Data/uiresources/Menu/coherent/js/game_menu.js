/* jshint browser: true */
/* global engine */
/* exported GameMenu */
var GameMenu = (function () {

	function createMenu(options, buttons, parent) {
		var menu = document.createElement('div');
		menu.classList.add('cui-menu');
		if (!options.Visible) {
			menu.classList.add('cui-hidden');
		}

		for (var i=0; i < buttons.length; i++) {
			var buttonOption = buttons[i];
			var button = document.createElement('button');
			button.classList.add('btn', 'btn-large', 'btn-primary');
			button.type = 'button';
			button.innerHTML = buttonOption.label;
			button.addEventListener('click' , buttonOption.callback, false);
			button.disabled = buttonOption.disabled === true;
			menu.appendChild(button);
		}
		parent.appendChild(menu);
		return menu;
	}

	function GameMenu(id, parent, buttons, options) {
		this.id = id;
		this.menu = createMenu(options, buttons, parent);
	}

	GameMenu.prototype.show = function() {
		this.menu.classList.remove('cui-hidden');
	};

	GameMenu.prototype.hide = function() {
		this.menu.classList.add('cui-hidden');
	};

	function createButtonCallback(id, buttonName) {
		return function() {
			engine.trigger('cui.MenuButtonClicked', id, buttonName);
		};
	}

	var menus = {};
	var c = 0;
	engine.on('cui.CreateMenu', function (id, options) {
		c++;
		console.log('Create Menu:' + id + ' So far ' + c);
		var menu = [],
			buttons = options.Buttons,
			buttonsCount = buttons.length;

		for (var i = 0; i < buttonsCount; i++) {
			var button = buttons[i];

			menu.push({
				label: button.Label,
				callback: createButtonCallback(id, button.Label),
				disabled: button.Disabled,
			});
		}

		var parent = document.getElementById(options.Parent);
		if (parent === null) {
			parent = document.createElement('div');
			parent.classList.add('cui-default-menu');
			document.body.appendChild(parent);
		}
		var gameMenu = new GameMenu(id, parent, menu, options);
		menus[id] = gameMenu;
	});

	engine.on('cui.ShowMenu', function (id) {
		var menu = menus[id];
		if (menu !== undefined) {
			menu.show();
		}
	});

	engine.on('cui.HideMenu', function (id) {
		var menu = menus[id];
		if (menu !== undefined) {
			menu.hide();
		}
	});

	engine.trigger('cui.MenuReady');

	return GameMenu;
})();
