import xml.etree.ElementTree as ET
import sys
import os
from datetime import datetime

def convert_datetime(sbest,s2):
    try:
        d = datetime.strptime(sbest,"%Y-%m-%d %H:%M:%S")
        return d.isoformat()
    except:
        try:
            d = datetime.strptime(s2,"%Y-%m-%d %H:%M:%S")
            return d.isoformat()
        except:
            print("NOPE")
            print(sbest)
            print(s2)

filename = sys.argv[1]
tree = ET.parse(filename)
root = tree.getroot()
items = [child for child in root[0] if child.tag=='item']
ns = {
    "wp":"http://wordpress.org/export/1.2/",
    "content":"http://purl.org/rss/1.0/modules/content/"
}
directory = filename+"-posts"
os.mkdir(directory)
for item in items:
    title=item.find("title").text
    link=item.find("link").text
    pub_date=item.find("pubDate").text
    content=getattr(item.find("content:encoded",ns),'text','nothing') or "empty"
    post_date=item.find("wp:post_date_gmt",ns).text
    post_modified_gmt=item.find("wp:post_modified_gmt",ns).text
    post_name=item.find("wp:post_name",ns).text
    post_id=item.find("wp:post_id",ns).text
    post_type=item.find("wp:post_type",ns).text
    status=item.find("wp:status",ns).text
    if not content:
        continue
    if not post_type=='post' and not post_type=='page':
        continue
    try:
        with open(directory+"/wp-es-"+status+"-"+post_id+".md","w") as output:
            output.write("---\n")
            if title: output.write("title: '"+title+"'\n")
            if post_type: output.write("post_type: '"+post_type+"'\n")
            if link: output.write("source: '"+link+"'\n")
            if pub_date: output.write("pub_date: '"+pub_date+"'\n")
            if post_date: output.write("post_date: '"+post_date+"'\n")
            if post_modified_gmt: output.write("post_modified_gmt: '"+post_modified_gmt+"'\n")
            if post_name: output.write("post_name: '"+post_name+"'\n")
            d = convert_datetime(post_modified_gmt, post_date)
            if d: 
                output.write("date: '"+d+"'\n")
            else:
                print(post_id+" has no date")
            if post_id: output.write("post_id: '"+post_id+"'\n")
            output.write("""tags:
    - pepenachohacejuegos
    - teenage
    - nerd
""")
            output.write("---\n")
            if content: output.write(content)
    except Exception as e:
        print("failed to export "+post_id)
        print(e)
    
    
