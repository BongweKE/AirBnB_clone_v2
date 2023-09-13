#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
import os
from datetime import datetime
from fabric import task

@task
def do_pack(c):
    """Create a tar gzipped archive of the directory web_static."""
    source_dir = "web_static"
    destination_dir = "versions"

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    #generating archive filename
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{timestamp}.tgz"
    archive_path = os.path.join(destination_dir, archive_name)

    #create .tgz archieve
    with c.cd(source_dir):
        c.local(f"tar -czvf {archive_path} .")

    if os.path.exists(archive_path):
        return archive_path
    else:
        return None
