import os
aws_access_key = os.environ.get('ACCESS_KEY')
aws_secret_key = os.environ.get('SECRET_KEY')
aws_host = os.environ.get('HOST', default="s3.amazonaws.com")
aws_host_bucket = os.environ.get('HOST_BUCKET', default="%(bucket)s.s3.amazonaws.com")

cron_schedule_pull = os.environ.get('CRON_SCHEDULE_PULL', default="*/2 * * * *")
cron_schedule_push = os.environ.get('CRON_SCHEDULE_PUSH', default="*/5 * * * *")
s3_path = os.environ.get('S3_PATH')


# create dictionary of environment variables
cfg_dict = {}
cfg_dict['access_key'] = aws_access_key
cfg_dict['secret_key'] = aws_secret_key
cfg_dict['host_base'] = aws_host
cfg_dict['host_bucket'] = aws_host_bucket

env_dict = {}
env_dict['CRON_SCHEDULE_PULL'] = cron_schedule_pull
env_dict['CRON_SCHEDULE_PUSH'] = cron_schedule_push
env_dict['S3_PATH'] = s3_path


# function to add environment variables to file
def add_env_variables(file, env_dict):
    for key in env_dict:
        file = file.replace(key, env_dict[key])
    return file


# read file for crontabs
with open('/etc/crontabs/root', 'r') as in_file:
    text = in_file.read()

# write file for crontabs
with open('/etc/crontabs/root', 'w') as out_file:
    out_file.write(add_env_variables(text, env_dict))



# function to add config variables to file
def add_cfg_variables(file, cfg_dict):
    for key in cfg_dict:
        file = file.replace(f"{key} =", f"{key} = {cfg_dict[key]}")
    return file


# read file for crontabs
with open('/root/.s3cfg', 'r') as in_file:
    text = in_file.read()

# write file for crontabs
with open('/root/.s3cfg', 'w') as out_file:
    out_file.write(add_cfg_variables(text, cfg_dict))