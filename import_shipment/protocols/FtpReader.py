import ftplib
import io


class FtpReader:

    # copy from gemini, not sure if it works
    def read_file_in_memory(self, ftp, filepath):
        """Reads a file from FTP directly into memory"""
        data = io.BytesIO()
        ftp.retrbinary('RETR ' + filepath, data.write)
        data.seek(0)  # Rewind to the beginning of the in-memory file
        return data

    def get_file_content(self, filepath, file_handler):
        # --- Main part of the script ---
        ftp = ftplib.FTP(filepath)
        ftp.login('your_username', 'your_password')

        remote_directory = '/path/to/remote/folder'
        ftp.cwd(remote_directory)

        for filename in ftp.nlst():  # Iterate over files in the directory
            file_in_memory = self.read_file_in_memory(ftp, filename)

            file_handler(file_in_memory, filename)
            # Process the file contents (now in file_in_memory)
            print("Contents of", filename)
            print(file_in_memory.read().decode())  # Example: Read and print as text

        ftp.quit()
