from flask import Flask, request, render_template
from datetime import datetime
import json

app = Flask(__name__)

try:
    with open('notes.json', 'r') as f:
        notes = json.load(f)
except FileNotFoundError:
    notes = []

def save_notes():
    with open('notes.json', 'w') as f:
        json.dump(notes, f, indent=4)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        note = request.form.get('note')
        index = request.form.get('index')
        index_del = request.form.get('index_del')
        editednote = request.form.get('editednote')
        editedtitle = request.form.get('editedtitle')
        search = request.form.get('search')

        searchednote = None

        if title and note:
            notes.append({'title':title,'note':note, 'time': datetime.now().strftime('%d %b %Y, %I:%M %p')
})
            save_notes()

        if index is not None and (editednote or editedtitle):
            if editednote:
               notes[int(index)]['note'] = editednote

            if editedtitle:
                notes[int(index)]['title'] = editedtitle

            notes[int(index)]['time'] = datetime.now().strftime('%d %b %Y, %I:%M %p')
            save_notes()

        # if index is not None and editednote != '':
            # notes[int(index)]['note'] = editednote
            # notes[int(index)]['title'] = editedtitle
            # notes[int(index)]['time'] = datetime.now().strftime('%d %b %Y, %I:%M %p')
            # save_notes()
        
        if index_del is not None and request.form.get('delete') == 'Delete':
            notes.pop(int(index_del))
            save_notes()

        if search:
            for note in notes:
                if search.lower().strip() == note['title'].lower().strip():
                    searchednote = note
                    break

        
        return render_template('index.html', notes = notes, searchednote = searchednote)

    return render_template('index.html', notes = notes)

if __name__ == '__main__':
    app.run(debug=True)

#CRUD operations for notes: Create, Read, Update, Delete    

#Clean UI                       {{ DONE }}
#Seaching options               {{ DONE }}
#Edit title of the note         {{ DONE }}
#Add timestamps to the notes   {{ DONE }}