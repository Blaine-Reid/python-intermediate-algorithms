# Intermediate Algorithm Scripting: Convert HTML Entities
# Convert the characters &, <, >, " (double quote), and ' (apostrophe), in a string to their corresponding HTML 
# entities.

def convertHTML(str):
  str = str.replace('&','&amp;')
  str = str.replace('<','&lt;')
  str = str.replace('>','&gt;')
  str = str.replace('"','&quot;')
  str = str.replace('\'','&apos;')
  return print(str)

convertHTML("Dolce & Gabbana") #should return Dolce &amp; Gabbana.
convertHTML("Hamburgers < Pizza < Tacos") #should return Hamburgers &lt; Pizza &lt; Tacos.
convertHTML("Sixty > twelve") #should return Sixty &gt; twelve.
convertHTML('Stuff in "quotation marks"') #should return Stuff in &quot;quotation marks&quot;.
convertHTML("Schindler's List") #should return Schindler&apos;s List.
convertHTML("<>") #should return &lt;&gt;.
convertHTML("abc") #should return abc.