#!/usr/bin/python3
"""
bip
bip
complique
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8")
    return True


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionnary = {}
    for child in root:
        dictionnary[child.tag] = child.text
    return dictionnary
