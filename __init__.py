# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

   sudo pip install <package> -t .

"""


# ignore the undefined functions and vars that come from Rocketbot Suite
GetParams = GetParams  # type: ignore
SetVar = SetVar  # type: ignore
PrintException = PrintException  # type: ignore
tmp_global_obj = tmp_global_obj  # type: ignore
alert = alert  # type: ignore

# ------------------------- libraries used by this __init__.py -------------------------
import os
import sys

# custom file imports
import rocketbot_funcs as rbfn  # type: ignore

# add libs to the path
folder_name = "template-rocketbot-module"
base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + folder_name + os.sep + "libs"

if cur_path not in sys.path:
    sys.path.append(cur_path)


# Globals declared here
global mod_my_sessions

# Default declared here
SESSION_DEFAULT = "default"

# Initialize settings for the module here
try:
    if mod_my_sessions is None:  # type: ignore
        mod_my_sessions = {SESSION_DEFAULT: {}}
except NameError:
    mod_my_sessions = {SESSION_DEFAULT: {}}

# get the running session, otherwise get the default session
session = GetParams("session")
if not session:
    session = SESSION_DEFAULT

# capture the name of the running command
module = GetParams("module")


# ------------------------------------ new command ------------------------------------
if module == "alerta":
    data = GetParams("identifier")
    option = GetParams("option")
    rbfn.func("hi")  # I call the func in rocketbot_func.py file

    alert("Hola " + str(data) + ", Opcion:" + str(option))

# ------------------------------------ new command ------------------------------------
if module == "example_view":
    textarea = GetParams("iframe")
    print(textarea["input"])

# ------------------------------------ new command ------------------------------------
if module == "example_html":
    textarea = GetParams("iframe")
    print(textarea["input"])
