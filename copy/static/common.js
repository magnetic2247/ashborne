function studpersubject() {
    swal({
        title:"Élèves d'une certaine matière",
        text:"Nom de la matière",
        content:"input",
        button: {
            text: "Recherche!",
            closeModal: false,
        },
    }).then(v =>{
        if (v!="" && v!=null) window.location.href = "/students/per_subject/"+v;
    });
}

function studperoption() {
    swal({
        title:"Élèves d'une certaine option",
        text:"Identifiant de l'option",
        content:"input",
        button: {
            text: "Recherche!",
            closeModal: false,
        },
    }).then(v =>{
        if (v!="" && v!=null) window.location.href = "/students/per_option/"+v;
    });
}

function teacherperstud() {
    swal({
        title:"Professeur d'un certain élève",
        text:"Identifiant de l'élève",
        content:"input",
        button: {
            text: "Recherche!",
            closeModal: false,
        },
    }).then(v =>{
        if (v!="" && v!=null) window.location.href = "/teachers/per_student/"+v;
    });
}