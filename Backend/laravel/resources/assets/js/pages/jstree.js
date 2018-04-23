"use strict";
$(document).ready(function () {
    $("#jstree1").jstree({
        "core" : { "check_callback" : true }, // so that operations work
        "plugins" : ["dnd"]
    });

//    Working with events
    $('#jstree2').jstree({
        'core' : {
            "check_callback" : true,
            'data' : [
                {"id" : 1, "text" : "Child node 1",  "children" : [
                    {"id" : 1.1, "text" : "Child node 1.1" },
                    {"id" : 1.2, "text" : "Child node 1.2" }
                ]
                },
                {"id" : 2, "text" : "Child node 2" },
                {"id" : 3, "text" : "Child node 3",  "children" : [
                    {"id" : 3.1, "text" : "Child node 3.1" },
                    {"id" : 3.2, "text" : "Child node 3.2" }
                ]
                },
                {"id" : 4, "text" : "Child node 4" }
            ]
        }
    });

    $('#jstree2').on("changed.jstree", function (e, data) {
        console.log(data.selected);
    });

    console = {
        log : function (m) {
            $("#jstree_events").empty();
            $("#jstree_events").append("event number: " + m.toString());
        }
    };


    //    Interacting with the tree using the API

    $('#jstree3').jstree({
        'core' : {
            "check_callback" : true,
            'data' : [
                {"id" : 1, "text" : "Child node 1",  "children" : [
                    {"id" : 1.1, "text" : "Child node 1.1" },
                    {"id" : 1.2, "text" : "Child node 1.2" }
                ]
                },
                {"id" : 2, "text" : "Child node 2" },
                {"id" : 3, "text" : "Child node 3",  "children" : [
                    {"id" : 3.1, "text" : "Child node 3.1" },
                    {"id" : 3.2, "text" : "Child node 3.2" }
                ]
                },
                {"id" : 4, "text" : "Child node 4" },
                {"id" : 5, "text" : "Child node 5" }
            ]
        }
    });
    $('.node1').on("click", function () {
        var instance = $('#jstree3').jstree(true);
        instance.deselect_all();
        instance.select_node('1');
    });
    $('.node2').on("click", function () {
        var instance = $('#jstree3').jstree(true);
        instance.deselect_all();
        instance.select_node('2');
    });
    $('.node1_1').on("click", function () {
        var instance = $('#jstree3').jstree(true);
        instance.deselect_all();
        instance.select_node('1.1');
    });
    $('.node1_2').on("click", function () {
        var instance = $('#jstree3').jstree(true);
        instance.deselect_all();
        instance.select_node('1.2');
    });
    $('.node3_1').on("click", function () {
        var instance = $('#jstree3').jstree(true);
        instance.deselect_all();
        instance.select_node('3.1');
    });
    $('.node3_2').on("click", function () {
        var instance = $('#jstree3').jstree(true);
        instance.deselect_all();
        instance.select_node('3.2');
    });

//     Create,rename and delete
    $('#jstree4').jstree({
        "core" : {
            "check_callback" : true, // enable all modifications
        },
        "plugins" : ["contextmenu"]
    });

    $('#jstree5').jstree({
        "plugins" : ["checkbox","state","contextmenu","dnd"]
    });
    $('#jstree6').jstree({
        "plugins" : ["search"]
    });
    $("#search").submit(function(e) {
        e.preventDefault();
        $("#jstree6").jstree(true).search($("#input_search").val());
    });
    $('#jstree7').jstree({
        "plugins" : ["sort"]
    });
    $('#jstree8').jstree({
        "types" : {
            "default" : {
                "icon" : "fa fa-file text-primary"
            },
            "demo" : {
                "icon" : "fa fa-check"
            }
        },
        "plugins" : ["types"]
    });
});