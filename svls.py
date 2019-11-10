import os, sys

print ("\033[1;32mHORAS HITA SUDE!!")

print ("\033[1;32mSilahkan Masukkan Username & Password Anda")

print ("\033[1;32mChat saya langsung, Nicoleus Sitorus ")

username = 'nicoleus'      

password = 'nicoleus01'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")



		if pwd == password:

			print "\033[1;32mSyukurlah sudah masuk juga:D..", 

			sys.exit()



		else:

			print "\033[1;32mYaelah Maaf Masukkan password Anda salah... [?]\033[00m"

			print "Silahkan segera log-in kembali...!!\n"

			restart()



	else:

		print "\033[1;32mSorry Masukkan Username Anda salah... [?]\033[00m"

		print "Silahkan segera log-in kembali...!!\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()
