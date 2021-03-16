import xml.etree.ElementTree as ET

data = """
<person>
    <users>
        <user x="2">
            <id>001</id>
            <name>Someone</name>
        </user>
        <user x="7">
            <id>002</id>
            <name>Someoneelse</name>
        </user>
    </users>
</person>"""

person = ET.fromstring(data)
listOfPerson = person.findall('users/user')

for person in listOfPerson:
    print('id', person.find('id').text)
    print('name', person.find('name').text)
    print('x', person.get('x'))



# print(type(listOfPerson))