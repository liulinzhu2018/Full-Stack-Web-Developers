$(function(){
    var catList = ['cat', 'cat1', 'cat2', 'cat3', 'cat4'];

    var model = {
        init: function() {
            if (!localStorage.notes) {
                localStorage.notes = JSON.stringify([]);
            }
        },
        add: function(obj) {
            var data = JSON.parse(localStorage.notes);
            data.push(obj);
            localStorage.notes = JSON.stringify(data);
        },
        getAllCats: function() {
            for (var i = 0; i < catList.length; ++i) {
                model.add({id: i,
                    name: catList[i],
                    clickCount: 0,
                    image: catList[i]});
                
                var num = i;
                var elem = document.createElement('note');
                elem.addEventListener('click', (function(numCopy) {
                    return function() {
                        alert(numCopy);
                    };
                })(num));
    
                document.body.appendChild(elem);
            }
            return JSON.parse(localStorage.notes);
        },

        getCat: function(num) {
            //if (num < catList.lenght) {
            //    return catList[num];
            //}
            return JSON.parse(localStorage.notes)[num]
        }
    };


    var octopus = {
        addNewCat: function(noteStr) {
            model.add({
                content: noteStr,
				dateSubmitted: Date.now()
            });
            view.render();
        },

        getCats: function() {
            // return model.getAllNotes();
			return model.getAllCats().reverse();
        },

        getCat: function(num) {
            return model.getCat(num);
        },

        init: function() {
            model.init();
            view.init();
        }
    };


    var view = {
        init: function() {
            this.noteList = $('#notes');
            var newNoteForm = $('#new-note-form');
            var newNoteContent = $('#new-note-content');
            newNoteForm.submit(function(e){
                // octopus.addNewNote(newNoteContent.val());
                // newNoteContent.val('');
                e.preventDefault();
            });
            view.allCats();
            view.oneCat(0);
        },
        allCats: function(){
            var htmlStr = '';
            octopus.getCats().forEach(function(cat){
                htmlStr += '<li class="note">'+ cat.name +
                    '</li>';
            });
            this.noteList.html(htmlStr);
        },
        oneCat: function(num) {
            var cat = octopus.getCat(num);
            console.log(cat);
            var htmlStr = this.noteList.html();
            htmlStr += '<p>' + cat.name + '</p>';
            htmlStr += '<p> click count: ' + cat.clickCount + '</p>';
            // htmlStr += '<img src=' + 'C:\full-stack\6\click_cat\static\\' + cat.image + '.jpg></img>';
            // htmlStr += '<img src = "C:\full-stack\6\click_cat\cat.jpg" id = "my-cat1"></img>';
            this.noteList.html(htmlStr);
        }
    };

    octopus.init();
});