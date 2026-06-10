import os

class S3Sync:
    def sync_folder_to_s3(self, folder, aws_bucket_url):
        command = f'aws s3 sync "{folder}" "{aws_bucket_url}"'
        print("Running:", command)

        result = os.system(command)

        print("Exit code:", result)

    def sync_folder_from_s3(self, folder, aws_bucket_url):
        command = f'aws s3 sync "{aws_bucket_url}" "{folder}"'
        print("Running:", command)

        result = os.system(command)

        print("Exit code:", result)