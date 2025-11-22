contents = ["All carrots are to be sliced longituduabally.",
            "The carrots were reporterdly sliced.",
            "The slicing process was well precented"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)
