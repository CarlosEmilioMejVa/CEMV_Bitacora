import json
import PySimpleGUI as sg
import os

class User():
	"""docstring for User"""
	def __init__(self, ID_MAT, names, lnames, password, rol):
		self.ID_MAT = ID_MAT
		self.names = names
		self.lnames = lnames
		self.rol = rol
		self.password = password
		


	






def main():
	drive_letter = os.path.splitdrive(os.path.expanduser("~"))[0]
	rols = ["Admin", "User", "Viewer"]
	layout_users = [
		[sg.T("User ID: "), sg.I(default_text = "", k = "-USER_ID-")],
		[sg.T("User First Names: "), sg.I(default_text = "", k = "-USER_FNAMES-")],
		[sg.T("User Last Names: "), sg.I(default_text = "", k = "-USER_LNAMES-")],
		[sg.T("User password: "), sg.I(default_text="", k = "-USER_PASS-")],
		[sg.T("User Rol: "), sg.Combo(values = rols, default_value = rols[2])],
		[sg.B("Cancel", k = "-CANCEL-"), sg.B("Continuar >", k = "-CONTINUE-")]
	]
	layout_admin = [
		[sg.T("Admin ID: "), sg.I(default_text = "0000", k = "-ADMIN_ID-")],
		[sg.T("Admin First Names: "), sg.I(default_text = "admin admin", k = "-ADMIN_FNAMES-")],
		[sg.T("Admin Last Names: "), sg.I(default_text = "", k = "-ADMIN_LNAMES-")],
		[sg.T("Admin password: "), sg.I(default_text="admin", k = "-ADMIN_PASS-")],
		[sg.B("Cancel", k = "-CANCEL-"), sg.B("Continuar >", k = "-CONTINUE-")]

	]
	layout_location = [
		[sg.T("Selecciona donde se va a instalar el Software:")],
		[sg.I(default_text = drive_letter, k = "-INSTALATION_PATH-"), sg.FolderBrowse()],
		[sg.B("Cancel", k = "-CANCEL-"), sg.B("Continuar >", k = "-CONTINUE-")]
	]
	layout = [
		[sg.T("Instalador del Centro de Eventos y Monitoreo de Visualización\n\n\nDar click en Continuar para iniciar la instalación y configuración")],
		[sg.B("Cancel", k = "-CANCEL-"), sg.B("Continuar >", k = "-CONTINUE-")]
	]

	main_window = sg.Window("Installer CEMV", layout)
	location_window = sg.Window("Install location", layout_location)
	admin_window = sg.Window("Configure admin credentials", layout_admin)
	users_window = sg.Window("Add users", layout_users)

	confirmation = []

	location_bool = False
	admin_bool = False
	users_bool = False

	while True:
		event, values = main_window.read()

		if event == sg.WIN_CLOSED: break
		if event == "-CONTINUE-":
			location_bool = True
			main_window.close()
			
	while location_bool:
		event_location, values_location = location_window.read()
		if event_location == sg.WIN_CLOSED: break
		if event_location == "-CONTINUE-":
			path = values_location["-INSTALATION_PATH-"]
			if os.path.exists(path):
				admin_bool = True
				break
	location_window.close()

	while admin_bool:
		event_admin, values_admin = admin_window.read()
		print(event_admin)
		if event_admin in [sg.WIN_CLOSED, "-CANCEL-"]: break
		if event == "-CONTINUE-":
			print("event")
			admin_id = values_admin["-ADMIN_ID-"]
			admin_fnames = values_admin["-ADMIN_FNAMES-"]
			admin_lnames = values_admin["-ADMIN_LNAMES-"]
			admin_pass = values_admin["-ADMIN_PASS-"]
			user_admin = User(admin_id, admin_fnames, admin_lnames, admin_pass, "Admin")
			users_bool = True
			break
	admin_window.close()

	while users_bool and users_exit != False:
		event_users, values_users = users_window.read()
		if event in [sg.WIN_CLOSED, "-CANCEL-"]: break
		if event == "-CONTINUE-":
			pass





main()