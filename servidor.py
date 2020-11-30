import socket

mi_socket = socket.socket()
mi_socket.bind( ('127.0.0.1', 9000) )
mi_socket.listen(5)


while True:
	conexion, addr = mi_socket.accept()
	print ("Cliente conectado!")
	print (addr)
	conexion.send("Hola, soy el servidor!")
	conexion.close()
	print (“cliente desconectado”)