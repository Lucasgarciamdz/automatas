import re


def validar_fecha(fecha):
    patron = re.compile(r'^\d{2}[-/]\d{2}[-/]\d{4}$')
    return patron.match(fecha)


def validar_numero_real(numero):
    patron = re.compile(r'^\d{1,3}(,\d{3})*(\.\d{2})?$')
    return patron.match(numero)


def validar_id_youtube(id):
    patron = re.compile(r'^[a-zA-Z0-9_-]{11}$')
    return patron.match(id)


def validar_cuenta_email_alumno_um(email):
    patron = re.compile(r'^[a-zA-Z0-9._%+-]+@[alumno]\.[um]\.[edu]\.[ar]$')
    return patron.match(email)


def validar_numero_tel_arg(telefono):
    patron = re.compile(r'^[15][0-9]{3}[0-9]{7}$')
    return patron.match(telefono)


def validar_cuil(cuil):
    patron = re.compile(r'^[0-9]{2}[0-9]{6,8}[0-9]$')
    return patron.match(cuil)


def validar_contrasena_segura(contrasena):
    patron = re.compile(
        r'^(?=.*\d)(?=.*[A-Z])(?=.*[!@#$%^&*()_+{}|:"<>?`~\-=[\]\\;,./])(?=.{8,16})\S+$')
    return patron.match(contrasena)
