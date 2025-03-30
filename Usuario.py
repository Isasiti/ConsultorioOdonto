"Parte solo para comprobar el usuario"
class Usuario:
    _USUARIO_ESPERADO = "lacabramosquera"
    _CONTRASEÑA_ESPERADA = "NOPUEDOMASSSSSSSS"
    def __init__(self, usuario: str, contraseña: str):
        self.usuario = usuario
        self.contraseña = contraseña
    def verificar_credenciales(self) -> bool:
        """
        Verifica si las credenciales ingresadas son correctas.
        """
        return self.usuario == self._USUARIO_ESPERADO and self.contraseña == self._CONTRASEÑA_ESPERADA
     
